require("dotenv").config();

const http = require("http");
const fs = require("fs");
const path = require("path");
const OpenAI = require("openai");

const PORT = 3000;

const ROOT_DIR = path.join(__dirname, "..");

const STAGE1_PROMPT_PATH = path.join(
  ROOT_DIR,
  "prompts",
  "structured-extractor-v0.8.txt"
);

const STAGE2_PROMPT_PATH = path.join(
  ROOT_DIR,
  "prompts",
  "executive-brief-generator-v1.4.txt"
);

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

const MIME_TYPES = {
  ".html": "text/html",
  ".css": "text/css",
  ".js": "application/javascript",
  ".json": "application/json",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".svg": "image/svg+xml"
};


// =========================================================
// BASIC RESPONSE HELPERS
// =========================================================

function sendJson(res, statusCode, data) {
  res.writeHead(statusCode, {
    "Content-Type": "application/json"
  });

  res.end(JSON.stringify(data));
}


function serveStaticFile(req, res) {
  let requestedPath =
    req.url === "/"
      ? "/index.html"
      : req.url;

  const filePath = path.join(
    ROOT_DIR,
    requestedPath
  );

  if (!filePath.startsWith(ROOT_DIR)) {
    sendJson(res, 403, {
      error: "Forbidden"
    });

    return;
  }

  fs.readFile(filePath, (error, content) => {
    if (error) {
      sendJson(res, 404, {
        error: "File not found"
      });

      return;
    }

    const extension = path.extname(filePath);

    const contentType =
      MIME_TYPES[extension] ||
      "application/octet-stream";

    res.writeHead(200, {
      "Content-Type": contentType
    });

    res.end(content);
  });
}


// =========================================================
// REQUEST BODY HELPER
// =========================================================

function readRequestBody(req) {
  return new Promise((resolve, reject) => {
    let body = "";

    req.on("data", chunk => {
      body += chunk;

      if (body.length > 1_000_000) {
        reject(
          new Error("Request body too large")
        );

        req.destroy();
      }
    });

    req.on("end", () => {
      try {
        const parsed = JSON.parse(body || "{}");
        resolve(parsed);
      } catch (error) {
        reject(
          new Error("Invalid JSON request body")
        );
      }
    });

    req.on("error", reject);
  });
}


// =========================================================
// HEALTH CHECK
// =========================================================

function handleHealthCheck(res) {
  const apiKeyLoaded =
    Boolean(process.env.OPENAI_API_KEY);

  sendJson(res, 200, {
    status: "ok",
    service: "Executive Brief Generator Backend",
    openaiConfigured: apiKeyLoaded
  });
}


// =========================================================
// STAGE 1 PROMPT
// =========================================================

function loadStage1Prompt() {
  if (!fs.existsSync(STAGE1_PROMPT_PATH)) {
    throw new Error(
      `Stage-1 prompt not found at ${STAGE1_PROMPT_PATH}`
    );
  }

  return fs.readFileSync(
    STAGE1_PROMPT_PATH,
    "utf8"
  );
}

function loadStage2Prompt() {
  if (!fs.existsSync(STAGE2_PROMPT_PATH)) {
    throw new Error(
      `Stage-2 prompt not found at ${STAGE2_PROMPT_PATH}`
    );
  }

  return fs.readFileSync(
    STAGE2_PROMPT_PATH,
    "utf8"
  );
}

// =========================================================
// STAGE 1 API
// =========================================================

async function handleStage1(req, res) {
  try {
    if (!process.env.OPENAI_API_KEY) {
      sendJson(res, 500, {
        error:
          "OpenAI API key is not configured."
      });

      return;
    }

    const body =
      await readRequestBody(req);

    const source =
      typeof body.source === "string"
        ? body.source.trim()
        : "";

    if (!source) {
      sendJson(res, 400, {
        error:
          "Source content is required."
      });

      return;
    }

    const stage1Prompt =
      loadStage1Prompt();

    console.log(
      `Stage 1 request received — ${source.length} source characters`
    );

    const response =
      await client.responses.create({
        model: "gpt-5.6-luna",

        input: [
          {
            role: "system",
            content: stage1Prompt
          },
          {
            role: "user",
            content:
              `SOURCE MATERIAL:\n\n${source}`
          }
        ]
      });

    const output =
      response.output_text?.trim();

    if (!output) {
      throw new Error(
        "OpenAI returned no Stage-1 output."
      );
    }

    sendJson(res, 200, {
      status: "success",
      stage: "stage1",
      promptVersion:
        "structured-extractor-v0.8",
      model: "gpt-5.6-luna",
      output
    });

  } catch (error) {
    console.error(
      "Stage 1 generation failed:",
      error.message
    );

    sendJson(res, 500, {
      error:
        "Stage 1 generation failed.",
      detail: error.message
    });
  }
}

// =========================================================
// STAGE 2 API
// =========================================================

async function handleStage2(req, res) {
  try {
    if (!process.env.OPENAI_API_KEY) {
      sendJson(res, 500, {
        error:
          "OpenAI API key is not configured."
      });

      return;
    }

    const body =
      await readRequestBody(req);

    const stage1Output =
      typeof body.stage1Output === "string"
        ? body.stage1Output.trim()
        : "";

    if (!stage1Output) {
      sendJson(res, 400, {
        error:
          "Approved Stage-1 output is required."
      });

      return;
    }

    const stage2Prompt =
      loadStage2Prompt();

    console.log(
      `Stage 2 request received — ${stage1Output.length} Stage-1 characters`
    );

    const response =
      await client.responses.create({
        model: "gpt-5.6-luna",

        input: [
          {
            role: "system",
            content: stage2Prompt
          },
          {
            role: "user",
            content:
              `APPROVED STAGE-1 STRUCTURED OUTPUT:\n\n${stage1Output}`
          }
        ]
      });

    const output =
      response.output_text?.trim();

    if (!output) {
      throw new Error(
        "OpenAI returned no Stage-2 output."
      );
    }

    sendJson(res, 200, {
      status: "success",
      stage: "stage2",
      promptVersion:
        "executive-brief-generator-v1.4",
      model: "gpt-5.6-luna",
      output
    });

  } catch (error) {
    console.error(
      "Stage 2 generation failed:",
      error.message
    );

    sendJson(res, 500, {
      error:
        "Stage 2 generation failed.",
      detail: error.message
    });
  }
}

// =========================================================
// REQUEST ROUTING
// =========================================================

const server = http.createServer(
  async (req, res) => {

    if (
      req.method === "GET" &&
      req.url === "/api/health"
    ) {
      handleHealthCheck(res);
      return;
    }

    if (
      req.method === "POST" &&
      req.url === "/api/stage1"
    ) {
      await handleStage1(req, res);
      return;
    }

    if (
      req.method === "POST" &&
      req.url === "/api/stage2"
    )  {
      await handleStage2(req, res);
      return;
    }

    if (req.method === "GET") {
      serveStaticFile(req, res);
      return;
    }

    sendJson(res, 405, {
      error: "Method not allowed"
    });
  }
);


// =========================================================
// START SERVER
// =========================================================

server.listen(PORT, () => {
  console.log(
    `Executive Brief Generator server running at http://localhost:${PORT}`
  );

  console.log(
    process.env.OPENAI_API_KEY
      ? "OpenAI API key detected."
      : "WARNING: OpenAI API key is not loaded."
  );

  console.log(
    "Stage 1 endpoint available at POST /api/stage1"
  );

  console.log(
  "Stage 2 endpoint available at POST /api/stage2"
  );
});
