const appState = {
  status: "SOURCE_ENTERED",

  source: {
    title: "",
    content: ""
  },

  stage1: {
    output: "",
    approved: false,
    version: 1,
    approvedVersion: null,
    promptVersion: "structured-extractor-v0.8"
  },

  stage2: {
    output: "",
    approved: false,
    promptVersion: "executive-brief-generator-v1.4"
  }
};


// =========================================================
// DOM REFERENCES
// =========================================================

const sourceTitleInput = document.getElementById("source-title");
const sourceContentInput = document.getElementById("source-content");

const runStage1Button = document.getElementById("run-stage1-button");
const clearButton = document.getElementById("clear-button");

const sourceSection = document.getElementById("source-section");
const stage1Section = document.getElementById("stage1-section");
const stage2Section = document.getElementById("stage2-section");

const originalSourceDisplay = document.getElementById(
  "original-source-display"
);

const stage1Output = document.getElementById("stage1-output");

const rerunStage1Button = document.getElementById(
  "rerun-stage1-button"
);

const approveStage1Button = document.getElementById(
  "approve-stage1-button"
);

const stage1ApprovalStatus = document.getElementById(
  "stage1-approval-status"
);

const stage2GenerationArea = document.getElementById(
  "stage2-generation-area"
);

const runStage2Button = document.getElementById(
  "run-stage2-button"
);

const approvedStage1Display = document.getElementById(
  "approved-stage1-display"
);

const stage2Output = document.getElementById("stage2-output");

const regenerateStage2Button = document.getElementById(
  "regenerate-stage2-button"
);

const approveFinalButton = document.getElementById(
  "approve-final-button"
);

const stage2ApprovalStatus = document.getElementById(
  "stage2-approval-status"
);

const finalApprovedMessage = document.getElementById(
  "final-approved-message"
);

const statusMessage = document.getElementById("status-message");

const progressSource = document.getElementById("progress-source");
const progressStage1 = document.getElementById("progress-stage1");
const progressStage2 = document.getElementById("progress-stage2");


// =========================================================
// STATUS HELPERS
// =========================================================

function setStatus(message) {
  statusMessage.innerHTML = `
    <strong>Status:</strong>
    ${message}
  `;
}


function updateProgress(step) {
  progressSource.className = "workflow-step";
  progressStage1.className = "workflow-step";
  progressStage2.className = "workflow-step";

  if (step === 1) {
    progressSource.classList.add("active");
    progressStage1.classList.add("locked");
    progressStage2.classList.add("locked");
  }

  if (step === 2) {
    progressSource.classList.add("complete");
    progressStage1.classList.add("active");
    progressStage2.classList.add("locked");
  }

  if (step === 3) {
    progressSource.classList.add("complete");
    progressStage1.classList.add("complete");
    progressStage2.classList.add("active");
  }

  if (step === 4) {
    progressSource.classList.add("complete");
    progressStage1.classList.add("complete");
    progressStage2.classList.add("complete");
  }
}


// =========================================================
// VIEW HELPERS
// =========================================================

function showSourceSection() {
  sourceSection.classList.remove("hidden");

  stage1Section.classList.add("hidden");
  stage2Section.classList.add("hidden");

  updateProgress(1);
}


function showStage1Section() {
  sourceSection.classList.add("hidden");

  stage1Section.classList.remove("hidden");
  stage2Section.classList.add("hidden");

  updateProgress(2);
}


function showStage2Section() {
  sourceSection.classList.add("hidden");
  stage1Section.classList.add("hidden");

  stage2Section.classList.remove("hidden");

  updateProgress(3);
}


// =========================================================
// STAGE 1
// =========================================================

async function runStage1() {
  const title = sourceTitleInput.value.trim();
  const content = sourceContentInput.value.trim();

  if (!content) {
    setStatus(
      "Enter operating source information before running Stage 1."
    );

    sourceContentInput.focus();

    return;
  }

  appState.source.title =
    title || "Untitled Operating Source";

  appState.source.content = content;

  appState.status = "STAGE1_RUNNING";

  setStatus(
    "Stage 1 is processing the source through Structured Extractor V0.8."
  );

  runStage1Button.disabled = true;

  try {
    const response = await fetch("/api/stage1", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        source: appState.source.content
      })
    });

    if (!response.ok) {
      throw new Error(
        `Stage 1 request failed with status ${response.status}.`
      );
    }

    const data = await response.json();

    if (
      data.status !== "success" ||
      !data.output
    ) {
      throw new Error(
        "Stage 1 returned an invalid response."
      );
    }

    appState.stage1.output = data.output;
    appState.stage1.promptVersion =
      data.promptVersion || "structured-extractor-v0.8";

    appState.stage1.approved = false;
    appState.stage1.approvedVersion = null;

    appState.status = "STAGE1_REVIEW";

    originalSourceDisplay.textContent =
      appState.source.content;

    stage1Output.value =
      appState.stage1.output;

    stage1ApprovalStatus.innerHTML = `
      <strong>Approval:</strong>
      Human review required
    `;

    stage2GenerationArea.classList.add("hidden");

    showStage1Section();

    setStatus(
      `Stage 1 draft generated using ${appState.stage1.promptVersion}. Human review and approval are required before Stage 2.`
    );
  } catch (error) {
    console.error(
      "Stage 1 generation failed:",
      error
    );

    appState.status = "SOURCE_ENTERED";

    setStatus(
      "Stage 1 could not be generated. Confirm the backend is running and try again."
    );
  } finally {
    runStage1Button.disabled = false;
  }
}


// =========================================================
// STAGE 1 APPROVAL
// =========================================================

function approveStage1() {
  const reviewedOutput = stage1Output.value.trim();

  if (!reviewedOutput) {
    setStatus(
      "Stage-1 structured output cannot be empty."
    );

    return;
  }

  appState.stage1.output = reviewedOutput;
  appState.stage1.approved = true;

  appState.stage1.approvedVersion =
    appState.stage1.version;

  appState.status = "STAGE1_APPROVED";

  stage1ApprovalStatus.innerHTML = `
    <strong>Approval:</strong>
    Stage 1 approved
  `;

  stage2GenerationArea.classList.remove("hidden");

  setStatus(
    "Stage 1 approved. Executive brief generation is now available."
  );
}


// =========================================================
// INVALIDATE STAGE 1 APPROVAL AFTER EDIT
// =========================================================

function invalidateStage1Approval() {
  if (!appState.stage1.approved) {
    return;
  }

  appState.stage1.version += 1;
  appState.stage1.approved = false;
  appState.stage1.approvedVersion = null;

  appState.status = "STAGE1_REVIEW";

  stage1ApprovalStatus.innerHTML = `
    <strong>Approval:</strong>
    Human review required
  `;

  stage2GenerationArea.classList.add("hidden");

  setStatus(
    "Stage-1 approval was invalidated because the structured output changed. Reapprove Stage 1 before generating a new executive brief."
  );
}


// =========================================================
// STAGE 2
// =========================================================

async function runStage2() {
  if (!appState.stage1.approved) {
    setStatus(
      "Stage 1 must be approved before generating the executive brief."
    );

    return;
  }

  appState.status = "STAGE2_RUNNING";

  setStatus(
    "Stage 2 is generating the executive brief using the approved Stage-1 output."
  );

  runStage2Button.disabled = true;

  try {
    const response = await fetch("/api/stage2", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        stage1Output: appState.stage1.output
      })
    });

    if (!response.ok) {
      throw new Error(
        `Stage 2 request failed with status ${response.status}.`
      );
    }

    const data = await response.json();

    if (
      data.status !== "success" ||
      !data.output
    ) {
      throw new Error(
        "Stage 2 returned an invalid response."
      );
    }

    appState.stage2.output = data.output;
    appState.stage2.promptVersion =
      data.promptVersion ||
      "executive-brief-generator-v1.4";

    appState.stage2.approved = false;

    appState.status = "FINAL_REVIEW";

    approvedStage1Display.textContent =
      appState.stage1.output;

    stage2Output.value =
      appState.stage2.output;

    stage2ApprovalStatus.innerHTML = `
      <strong>Approval:</strong>
      Human approval required
    `;

    finalApprovedMessage.classList.add("hidden");

    showStage2Section();

    setStatus(
      `Executive brief draft generated using ${appState.stage2.promptVersion}. Human approval is required before the brief is final.`
    );
  } catch (error) {
    console.error(
      "Stage 2 generation failed:",
      error
    );

    appState.status = "STAGE1_APPROVED";

    setStatus(
      "Stage 2 could not be generated. Confirm the backend is running and try again."
    );
  } finally {
    runStage2Button.disabled = false;
  }
}


// =========================================================
// FINAL APPROVAL
// =========================================================

function approveFinalBrief() {
  const reviewedBrief = stage2Output.value.trim();

  if (!reviewedBrief) {
    setStatus(
      "Executive brief cannot be empty."
    );

    return;
  }

  appState.stage2.output = reviewedBrief;
  appState.stage2.approved = true;

  appState.status = "FINAL_APPROVED";

  stage2ApprovalStatus.innerHTML = `
    <strong>Approval:</strong>
    Final approved
  `;

  finalApprovedMessage.classList.remove("hidden");

  updateProgress(4);

  setStatus(
    "Final executive brief approved. The human-controlled workflow is complete."
  );
}


// =========================================================
// RESET
// =========================================================

function resetApplication() {
  appState.status = "SOURCE_ENTERED";

  appState.source.title = "";
  appState.source.content = "";

  appState.stage1.output = "";
  appState.stage1.approved = false;
  appState.stage1.version = 1;
  appState.stage1.approvedVersion = null;
  appState.stage1.promptVersion =
    "structured-extractor-v0.8";

  appState.stage2.output = "";
  appState.stage2.approved = false;
  appState.stage2.promptVersion =
    "executive-brief-generator-v1.4";

  sourceTitleInput.value = "";
  sourceContentInput.value = "";

  stage1Output.value = "";
  stage2Output.value = "";

  originalSourceDisplay.textContent = "";
  approvedStage1Display.textContent = "";

  stage2GenerationArea.classList.add("hidden");
  finalApprovedMessage.classList.add("hidden");

  stage1ApprovalStatus.innerHTML = `
    <strong>Approval:</strong>
    Human review required
  `;

  stage2ApprovalStatus.innerHTML = `
    <strong>Approval:</strong>
    Human approval required
  `;

  showSourceSection();

  setStatus(
    "Ready for source input."
  );
}


// =========================================================
// EVENT LISTENERS
// =========================================================

runStage1Button.addEventListener(
  "click",
  runStage1
);


clearButton.addEventListener(
  "click",
  resetApplication
);


rerunStage1Button.addEventListener(
  "click",
  () => {
    sourceTitleInput.value =
      appState.source.title;

    sourceContentInput.value =
      appState.source.content;

    showSourceSection();

    setStatus(
      "Source restored. Update it if needed, then rerun Stage 1."
    );
  }
);


approveStage1Button.addEventListener(
  "click",
  approveStage1
);


stage1Output.addEventListener(
  "input",
  invalidateStage1Approval
);


runStage2Button.addEventListener(
  "click",
  runStage2
);


regenerateStage2Button.addEventListener(
  "click",
  runStage2
);


approveFinalButton.addEventListener(
  "click",
  approveFinalBrief
);


// =========================================================
// INITIALIZE
// =========================================================

resetApplication();
