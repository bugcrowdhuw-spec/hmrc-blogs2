# How to Generate HMRC-Ready Reports from Airbnb Data

<meta_description>Learn how to generate HMRC-ready reports from Airbnb data. Step-by-step guide to gross income calculation, expenses, and automated reporting.</meta_description>

*Last updated: March 2026*

You've got Airbnb income. You know you need to report it to HMRC. But turning CSV exports into something HMRC will accept? That's where most hosts get stuck. This guide shows you how to generate HMRC-ready reports from your Airbnb data — step by step.

## What Does "HMRC-Ready" Actually Mean?

An HMRC-ready report contains structured data that matches what platforms report about you to HMRC. Since January 2024, Airbnb reports your earnings directly to HMRC under OECD Digital Platform Reporting rules. Your tax return must match.

An HMRC-ready report includes:

- **Gross income** per property (before platform fees)
- **Allowable expenses** properly categorised
- **Rental days** and personal use days
- **Property details** (address, ownership)
- **Platform fees** listed separately as expenses

If you're filing Self Assessment, this goes on the SA105 property pages. If you're submitting Digital Platform Reporting data, it needs OECD-compliant XML format.

## The Problem with Airbnb's Raw Data

Airbnb provides transaction exports, but they're not HMRC-ready.

### Format Mismatch

Airbnb's CSV exports use their own format. HMRC expects data structured differently — gross income separated from fees, property details in specific fields, and figures in GBP.

### Missing Information

Airbnb's exports don't include:

- Allowable expenses (cleaning, maintenance, insurance)
- Property addresses matched to listings
- Personal use days
- Ownership splits for jointly-owned properties

### Multi-Platform Complexity

If you also list on Booking.com or VRBO, you need to combine data from all platforms into one report. Each platform exports differently.

## How to Generate HMRC-Ready Reports: Step by Step

### Step 1: Export Your Airbnb Data

1. Log in to Airbnb
2. Go to **Transaction History**
3. Select your date range (full tax year: 6 April – 5 April)
4. Export as CSV
5. Save with a clear name (e.g. `airbnb-2025-26.csv`)

### Step 2: Export Data from Other Platforms

If you list on Booking.com, VRBO, or others, export their reports too. Save each file separately with the platform name and date range.

### Step 3: Calculate Gross Income

This is where most people go wrong. Airbnb's CSV shows:

- **Payout amount** — what you received (net of fees)
- **Service fee** — Airbnb's commission

Your gross income = Payout + Service fee

**Example:**

| Booking | Payout | Service Fee | Gross Income |
|---|---|---|---|
| Guest A | £450 | £50 | £500 |
| Guest B | £380 | £45 | £425 |
| **Total** | **£830** | **£95** | **£925** |

HMRC wants £925 (gross), not £830 (payout). The £95 in fees goes under expenses.

### Step 4: Add Allowable Expenses

Gather receipts and records for:

- **Cleaning** — between guests
- **Maintenance and repairs** — keeping the property in good condition
- **Insurance** — buildings, contents, landlord insurance
- **Mortgage interest** — tax credit at 20% for residential property
- **Utilities** — gas, electricity, water, broadband (if you pay them)
- **Council tax** — if you pay it
- **Platform fees** — Airbnb, Booking.com service charges
- **Agent fees** — if you use a management company

### Step 5: Organise by Property

If you have multiple properties, each needs its own record. Split income and expenses by property. For jointly-owned properties, note the ownership split (e.g. 50/50).

### Step 6: Generate Your Report

You have two options:

**Option A: Manual (Self Assessment)**

Enter your totals into the SA105 property income pages. You'll need total income per property, total expenses per property, and net profit or loss.

**Option B: Automated (Software)**

Use a tool like [HMRC Reporter](https://hmrcreporter.com/) to upload your platform CSVs, automatically calculate gross income, match properties across platforms, and generate HMRC-compliant output (SA105 figures or Digital Platform Reporting XML).

### Step 7: Check Against HMRC's Data

HMRC already has your income data from Airbnb. Before submitting, verify:

- Your gross income matches what platforms reported
- All platforms are included (not just Airbnb)
- Expenses are reasonable and supported by records

If your figures don't match HMRC's records, expect questions.

## Why Do My Reports Need to Match HMRC's Data?

HMRC receives income data directly from Airbnb and other platforms under OECD reporting rules. If the figures on your Self Assessment don't match what HMRC has on file, it triggers an inquiry. The most common cause is reporting net income instead of gross. Getting this right the first time saves you from penalties and investigations.

## Common Mistakes When Generating Reports

### 1. Reporting Net Income Instead of Gross

This is the most common error. HMRC wants gross income with fees claimed as expenses separately.

### 2. Forgetting Other Platforms

Airbnb isn't the only platform reporting to HMRC. Booking.com, VRBO, and others report too. Miss one and your numbers won't match.

### 3. Mixing Personal and Business Expenses

Only claim expenses related to rental periods. Personal use days don't qualify.

### 4. Incorrect Currency Conversion

If you receive bookings in other currencies, convert to GBP using the correct exchange rate. HMRC accepts average rates for the tax year or spot rates per transaction.

### 5. Missing the Property Income Allowance

If your gross income is under £1,000 per year, you don't need to report at all. Check this before going through the full process.

## Using HMRC Reporter to Automate the Process

Manual reporting works, but it's slow and error-prone. [HMRC Reporter](https://hmrcreporter.com/) automates the entire process:

1. **Upload your CSVs** — from Airbnb, Booking.com, VRBO, and 24+ other platforms
2. **Automatic gross income calculation** — handles the net-to-gross conversion
3. **Property matching** — links the same property across different platforms
4. **Expense tracking** — add expenses per property
5. **Generate output** — SA105 figures or Digital Platform Reporting XML

What takes hours manually takes minutes with automation.

[Learn more about HMRC Reporter →](https://hmrcreporter.com/)

## Frequently Asked Questions

### Do I need to generate a report if Airbnb already reports to HMRC?

Yes. Airbnb reports your income to HMRC, but doesn't file your Self Assessment for you. You still need to submit your tax return with matching figures.

### What format does HMRC accept for reports?

For Self Assessment, you enter figures online. For Digital Platform Reporting, HMRC accepts OECD-compliant XML files.

### Can I use a spreadsheet to generate HMRC-ready reports?

You can, but you'll need to manually calculate gross income, track expenses, and format everything correctly. Software automates this and reduces errors.

### How do I handle bookings from multiple platforms for HMRC?

Combine income from all platforms per property. Tools like HMRC Reporter do this automatically — you upload CSVs from each platform and it consolidates them.

### What if my numbers don't match what HMRC has on file?

Investigate the difference. Common causes include reporting net instead of gross income, or missing a platform. Correct your return before submitting if possible.

---

*Generate HMRC-ready reports in minutes. [HMRC Reporter](https://hmrcreporter.com/) imports your booking data and produces compliant output automatically. [Get started →](https://hmrcreporter.com/)*

---

**Tags:** HMRC-ready reports, Airbnb data export, property income reporting, self assessment Airbnb, digital platform reporting

## Related Posts

- [Best Software for Airbnb Tax Reporting in the UK](./05-best-software-airbnb-tax-reporting-uk.md) — compare tools that handle Airbnb data for HMRC
- [How to Automate HMRC Reporting for Property Income](./06-how-to-automate-hmrc-reporting-property-income.md) — save time by automating your reporting workflow
- [How to Turn Airbnb Transactions Into HMRC-Ready Reports](./28-how-to-turn-airbnb-transactions-hmrc-ready-reports.md) — a deeper dive on converting raw Airbnb data
- [Spreadsheet vs Automated HMRC Reporting: What's Better?](./29-spreadsheet-vs-automated-hmrc-reporting.md) — weigh up manual and automated approaches
