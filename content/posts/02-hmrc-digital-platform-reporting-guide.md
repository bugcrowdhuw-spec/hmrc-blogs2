# HMRC Digital Platform Reporting: What UK Holiday Let Owners Need to Know

*Last updated: March 2026*

If you let property through Airbnb, Booking.com, VRBO, or any other online platform, there's a new reporting requirement you need to understand. HMRC's **Digital Platform Reporting** rules mean your income is now automatically shared with the tax authorities. Here's what it means for you.

## What Is Digital Platform Reporting?

Digital Platform Reporting (DPR) is part of the OECD's Model Reporting Rules for Digital Platforms. The UK adopted these rules in January 2024, requiring platforms like Airbnb to report sellers' income to HMRC annually.

In plain English: **the platform you use to rent your property now tells HMRC exactly how much you've earned.**

## How It Works

```
┌─────────────────┐      ┌──────────────────┐      ┌─────────────┐
│  Your bookings  │ ───► │  Platform (e.g.  │ ───► │    HMRC     │
│  on Airbnb,     │      │  Airbnb) reports │      │  receives   │
│  Booking.com    │      │  your income as  │      │  XML data   │
│  VRBO, etc.     │      │  OECD DPI XML    │      │             │
└─────────────────┘      └──────────────────┘      └─────────────┘
```

The report includes:

| Data reported | Example |
|---|---|
| Property owner identity | Your name, address, tax ID |
| Property details | Address of each rental property |
| Gross income | Total earnings before fees |
| Number of transactions | Total bookings in the tax year |
| Platform fees | What the platform deducted |
| Currency | Original booking currency |

## Which Platforms Must Report?

Under the OECD rules, **all digital platforms** facilitating property rentals must report. This includes:

- Airbnb
- Booking.com
- VRBO (HomeAway)
- Vrbo
- TripAdvisor/Holiday Lettings
- Plum Guide
- Host & Stay
- Sykes Cottages
- And 20+ others

If a platform operates in the UK and facilitates short-term property rentals, they must comply.

## What Does This Mean for You?

### 1. HMRC Already Knows Your Income

There's no more "hoping they won't find out." The platform reports your gross earnings directly. If your Self Assessment doesn't match, HMRC will notice.

### 2. You Still Need to File Your Own Tax Return

The platform reports income, but **you** are responsible for:
- Filing your Self Assessment
- Claiming allowable expenses
- Reporting on the correct tax year
- Paying any tax due

### 3. Accuracy Matters More Than Ever

With HMRC receiving standardised data, discrepancies are easy to spot. Common issues:
- Reporting net income instead of gross
- Missing bookings from a platform
- Incorrect property matching
- Currency conversion errors

## What Is the OECD DPI XML Format?

The XML report follows the OECD's **Digital Platform Reporting Information** standard (version 2.0). It's a structured data format that includes:

- **ResoldFileInfo** — reporting period, platform details
- **Seller** — your identity and tax information
- **Property** — details of each rental property
- **Transaction** — individual booking data with amounts and dates
- **GrossAmounts** — income broken down by currency

This isn't something most property owners will generate themselves — platforms do it. But understanding the format helps you know what data is being shared.

## If You Use Multiple Platforms

Here's where it gets complicated. If you list the same property on Airbnb *and* Booking.com:

- **Each platform reports separately** to HMRC
- HMRC sees the **combined total** across all platforms
- You need to **deduplicate and consolidate** in your Self Assessment
- Property details must match across platforms

For property owners with multiple listings across platforms, manually tracking this is a nightmare. This is where automated tools can help — pulling data from all your platforms and generating a single consolidated report.

## Penalties for Non-Compliance

If HMRC's records don't match your Self Assessment:

| Issue | Potential penalty |
|---|---|
| Careless error | Up to 30% of the tax due |
| Deliberate error | Up to 70% of the tax due |
| Deliberate + concealed | Up to 100% of the tax due |
| Late filing | £100 initial, then £10/day up to £900 |

Given that HMRC now has your exact income figures from the platforms, claiming ignorance is not a defence.

## How to Stay Compliant

1. **Keep accurate records** of all platform income
2. **File on time** — don't wait until January
3. **Report gross income** (before platform fees)
4. **Cross-check** platform statements against your Self Assessment
5. **Use automation** — tools like [HMRC Reporter](/) handle the consolidation and accuracy for you

---

*HMRC Reporter automatically imports booking data from 27+ platforms, matches properties, handles currency conversion, and generates HMRC-compliant XML reports. [Try it free →](/)*

---

**Tags:** digital platform reporting, HMRC OECD, Airbnb HMRC reporting, holiday let compliance, OECD DPI XML

**Meta description:** Understand HMRC Digital Platform Reporting rules introduced in January 2024. Learn how platforms report your rental income and what you need to do to stay compliant.
