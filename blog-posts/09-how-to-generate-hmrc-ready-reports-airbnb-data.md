# How to Generate HMRC-Ready Reports from Airbnb Data

*Last updated: March 2026*

You've got Airbnb income. You know you need to report it to HMRC. But turning a pile of CSV exports into something HMRC will actually accept? That's where most hosts and property managers get stuck. This guide walks you through how to generate HMRC-ready reports from your Airbnb data — step by step.

## What "HMRC-Ready" Actually Means

HMRC doesn't just want a number. They want structured data that matches what platforms report about you. Since January 2024, Airbnb reports your earnings directly to HMRC under OECD Digital Platform Reporting rules. Your tax return needs to match.

An HMRC-ready report includes:

- **Gross income** per property (before platform fees)
- **Allowable expenses** properly categorised
- **Rental days** and personal use days
- **Property details** (address, ownership)
- **Platform fees** listed separately as expenses

If you're filing Self Assessment, this goes on the SA105 property pages. If you're submitting Digital Platform Reporting data, it needs to be in OECD-compliant XML format.

## The Problem with Airbnb's Raw Data

Airbnb provides transaction exports, but they're not HMRC-ready. Issues include:

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
5. Save the file with a clear name (e.g. `airbnb-2025-26.csv`)

### Step 2: Export Data from Other Platforms

If you list on Booking.com, VRBO, or others, export their reports too. Each platform has a different export process, but they all provide transaction history.

Save each file separately with the platform name and date range.

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

If you have multiple properties, each needs its own record. Split income and expenses by property.

For jointly-owned properties, note the ownership split (e.g. 50/50).

### Step 6: Generate Your Report

You have two options:

**Option A: Manual (Self Assessment)**

Enter your totals into the SA105 property income pages on your Self Assessment. You'll need:

- Total income per property
- Total expenses per property
- Net profit or loss

**Option B: Automated (Software)**

Use a tool like [HMRC Reporter](https://hmrcreporter.com/) to:

1. Upload your platform CSVs
2. Automatically calculate gross income
3. Match properties across platforms
4. Generate HMRC-compliant output (SA105 figures or Digital Platform Reporting XML)

### Step 7: Check Against HMRC's Data

HMRC already has your income data from Airbnb. Before submitting, verify:

- Your gross income matches what platforms reported
- All platforms are included (not just Airbnb)
- Expenses are reasonable and supported by records

If your figures don't match HMRC's records, expect questions.

## Common Mistakes When Generating Reports

### 1. Reporting Net Income Instead of Gross

This is the most common error. HMRC wants gross income with fees claimed as expenses separately.

### 2. Forgetting Other Platforms

Airbnb isn't the only platform reporting to HMRC. Booking.com, VRBO, and others report too. Miss one and your numbers won't match.

### 3. Mixing Personal and Business Expenses

Only claim expenses related to rental periods. Personal use days don't qualify.

### 4. Incorrect Currency Conversion

If you receive bookings in other currencies, convert to GBP using the correct exchange rate (HMRC accepts average rates for the tax year or spot rates per transaction).

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

## What About Digital Platform Reporting XML?

If you're a platform operator or need to submit Digital Platform Reporting data, you need OECD-compliant XML. This is a specific format that includes:

- Property owner identification
- Gross income per property
- Number of transactions
- Property addresses

Most property managers don't need to generate this themselves — platforms submit it. But if you're managing properties at scale or running a platform, [HMRC Reporter](https://hmrcreporter.com/) generates this format automatically.

## Frequently Asked Questions

**Q: Do I need to generate a report if Airbnb already reports to HMRC?**
A: Yes. Airbnb reports your income to HMRC, but doesn't file your Self Assessment for you. You still need to submit your tax return with matching figures.

**Q: What format does HMRC accept?**
A: For Self Assessment, you enter figures online. For Digital Platform Reporting, HMRC accepts OECD-compliant XML files.

**Q: Can I use a spreadsheet to generate reports?**
A: You can, but you'll need to manually calculate gross income, track expenses, and format everything correctly. Software automates this.

**Q: How do I handle bookings from multiple platforms?**
A: Combine income from all platforms per property. Tools like HMRC Reporter do this automatically — you upload CSVs from each platform and it consolidates.

**Q: What if my numbers don't match what HMRC has?**
A: Investigate the difference. Common causes include reporting net instead of gross income, or missing a platform. Correct your return before submitting if possible.

---

*Generate HMRC-ready reports in minutes. [HMRC Reporter](https://hmrcreporter.com/) imports your booking data and produces compliant output automatically. [Get started →](https://hmrcreporter.com/)*

---

**Tags:** HMRC-ready reports, Airbnb data export, property income reporting, self assessment Airbnb, digital platform reporting

**Meta description:** Learn how to generate HMRC-ready reports from Airbnb data. Covers gross income calculation, expense tracking, and automated report generation.
