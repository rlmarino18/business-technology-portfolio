# Data Requirements

## Purpose

Define the minimum financial and operating data required to evaluate Toast's business performance, operating economics, and margin-improvement opportunities.

The objective is to avoid collecting data without a clear analytical use.

---

## 1. Financial Performance Data

Collect at least 3 years of annual data where available.

Required fields:

- total revenue
- subscription services revenue
- financial technology solutions revenue
- hardware and professional services revenue
- cost of revenue
- gross profit
- sales and marketing expense
- research and development expense
- general and administrative expense
- operating income or loss
- net income or loss
- cash and cash equivalents
- operating cash flow
- capital expenditures, if disclosed

---

## 2. Margin Metrics

These may be reported directly or calculated.

Required metrics:

- gross margin
- operating margin
- net margin
- subscription gross margin, if disclosed
- fintech gross margin, if disclosed
- operating expense as a percentage of revenue

Calculated metrics must be clearly labeled as calculated rather than reported.

---

## 3. Growth Metrics

Required metrics:

- year-over-year revenue growth
- subscription revenue growth
- fintech revenue growth
- gross profit growth
- operating expense growth

Where available:

- annualized recurring revenue
- location growth
- customer growth
- payment volume growth

---

## 4. Operating KPIs

Collect operating metrics that help explain financial performance.

Potential KPIs include:

- number of locations
- gross payment volume
- annualized recurring run-rate
- average revenue per location
- fintech revenue per location
- subscription revenue per location
- gross payment volume per location

Only include KPIs that Toast actually reports or that can be calculated from reported data.

---

## 5. Cost Structure

Identify the major categories driving cost.

Required areas:

- cost of subscription services
- cost of financial technology solutions
- hardware-related cost
- sales and marketing
- research and development
- general and administrative

Analytical questions:

- Which costs scale with revenue?
- Which costs appear to show operating leverage?
- Which costs are growing faster than revenue?
- Which expenses may offer realistic efficiency opportunities?

---

## 6. Business Model Drivers

Document the major economic drivers of the business.

Required areas:

- subscription monetization
- payment processing economics
- customer/location expansion
- cross-selling of additional products
- hardware economics
- customer acquisition
- operating leverage

Do not assume a driver is material until the company disclosures support it.

---

## 7. Historical Events and Management Commentary

Capture qualitative context that may explain changes in performance.

Examples:

- pricing changes
- product launches
- restructuring
- cost-reduction programs
- acquisitions
- changes in go-to-market strategy
- profitability targets
- margin guidance
- management commentary on operating leverage

These should be used to explain financial movements, not replace quantitative analysis.

---

## 8. Data Classification

Every data point used in the analysis must be classified as one of:

### Reported

Directly disclosed by Toast or another authoritative source.

### Calculated

Derived directly from reported figures.

### Assumption

Introduced for scenario modeling.

### Recommendation

Analytical conclusion based on evidence.

---

## 9. Initial Source Priority

Use sources in this order:

1. Toast annual reports / Form 10-K
2. Toast quarterly reports / Form 10-Q
3. Toast investor presentations
4. Toast earnings releases
5. Toast earnings-call commentary
6. SEC filings
7. Secondary financial sources only for cross-checking

Primary-source data should control when sources disagree.

---

## 10. Initial Dataset Structure

The first Pandas dataset should eventually contain one row per reporting period.

Example columns:

```text
period
revenue
subscription_revenue
fintech_revenue
hardware_services_revenue
cost_of_revenue
gross_profit
sales_marketing
research_development
general_administrative
operating_income
net_income
locations
gross_payment_volume
arr

