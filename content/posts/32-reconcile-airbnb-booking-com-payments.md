---
title: "How to Reconcile Airbnb and Booking.com Payments"
date: 2026-03-30
description: "How to reconcile Airbnb and Booking.com payments for HMRC. Step-by-step guide to matching income, spotting errors, and reporting accurately."
---

# How to Reconcile Airbnb and Booking.com Payments

*Last updated: March 2026*

If you list on both Airbnb and Booking.com, reconciling payments is one of the trickiest parts of property management. Different fee structures, different payout schedules, and different data formats make it hard to match your actual income. Here's how to do it properly.

## The Problem: Why Reconciliation Matters

Reconciliation means matching your records against platform statements to make sure everything adds up. Without it, you risk:

- **Missing bookings** — platforms occasionally omit transactions
- **Duplicate entries** — the same booking appearing twice
- **Fee miscalculations** — wrong commission rates applied
- **Refund errors** — incorrect refund amounts
- **Currency discrepancies** — conversion rate differences

For HMRC reporting, reconciliation ensures your figures are accurate and match what platforms report about you.

## What HMRC Expects

HMRC requires you to report **gross income** — the full amount guests pay, before platform fees. If your records don't match platform reports, you could face enquiries or penalties.

Reconciling Airbnb and Booking.com payments properly means you can prove every figure on your return.

## Airbnb vs Booking.com: Key Differences

| Feature | Airbnb | Booking.com |
|---|---|---|
| Host fee | ~3% | ~15% |
| Payout timing | 24hrs after check-in | Monthly (1st–15th of following month) |
| Data format | Transaction CSV | Reservation/statement CSV |
| Cleaning fees | Included in booking total | May be separate |

These differences mean you can't just add the two together without understanding each format.

## How to Reconcile Airbnb and Booking.com Payments

### Step 1: Export Data from Both Platforms

**Airbnb:**
1. Go to Transactions
2. Set date range (tax year: 6 April – 5 April)
3. Export CSV

**Booking.com:**
1. Go to Finance → Statements
2. Set the same date range
3. Export CSV or download statements

### Step 2: Standardise the Data

Both platforms export differently. Map each column to a standard format:

| Field | Airbnb | Booking.com |
|---|---|---|
| Booking date | Transaction date | Reservation date |
| Guest | Guest name | Guest name |
| Property | Listing name | Property name |
| Gross amount | Booking total | Reservation value |
| Platform fee | Service fee | Commission |
| Net payout | Payout amount | Net amount |

### Step 3: Match Against Bank Deposits

Check your bank account for deposits from each platform:

- **Airbnb:** Payouts per booking (24hrs after check-in)
- **Booking.com:** Monthly lump sum (1st–15th of following month)

Match each deposit to the corresponding transactions in your platform data.

### Step 4: Identify Discrepancies

Common issues:

- **Missing deposits** — booking completed but payout not received. Check for pending payouts or hold periods.
- **Unmatched deposits** — bank deposit doesn't match any booking. Could be a refund reversal or adjustment.
- **Fee differences** — expected fee doesn't match actual deduction. Check for special promotions or rate changes.

### Step 5: Calculate Correct Gross Income

For each platform:

```
Gross income = Total payouts + Total platform fees
```

Combined:

```
Total gross income = Airbnb gross + Booking.com gross
```

### Step 6: Record Platform Fees Separately

| Platform | Gross income | Platform fees | Net received |
|---|---|---|---|
| Airbnb | £10,000 | £300 | £9,700 |
| Booking.com | £6,000 | £900 | £5,100 |
| **Total** | **£16,000** | **£1,200** | **£14,800** |

For HMRC: report £16,000 gross income, claim £1,200 as platform fee expenses.

## How Often Should You Reconcile Airbnb and Booking.com Payments?

### Monthly (Recommended)

- Easier to spot issues while recent
- Less data to process
- Builds a consistent habit

### Quarterly (Minimum for MTD)

- Required if Making Tax Digital applies
- Aligns with MTD quarterly submissions

### Annually (Not Recommended)

- Harder to remember details
- Issues compound
- Stressful year-end scramble

## Common Reconciliation Problems

### Different Payout Schedules

Airbnb pays per booking. Booking.com pays monthly. Your bank shows deposits at different times.

**Solution:** Reconcile by booking date, not bank deposit date.

### Currency Conversion

Airbnb might pay in GBP. Booking.com might pay in EUR.

**Solution:** Convert to GBP using HMRC's rates. Track the conversion for each payment.

### Refunds and Adjustments

Guest cancels, you refund, platform adjusts fees.

**Solution:** Track refunds as negative income. Adjust platform fees accordingly.

### Cleaning Fees

Airbnb includes cleaning fees in the booking total. Booking.com may handle them separately.

**Solution:** Ensure cleaning fee income is captured consistently across both platforms.

## Automating Reconciliation

Manual reconciliation works but takes hours. [HMRC Reporter](https://hmrcreporter.com/) automates it:

1. **Upload both CSVs** — Airbnb and Booking.com
2. **Automatic matching** — properties linked across platforms
3. **Gross income calculated** — handles different fee structures
4. **Discrepancies flagged** — missing or unusual entries highlighted
5. **Consolidated report** — combined figures ready for HMRC

[Learn more about HMRC Reporter →](https://hmrcreporter.com/)

## Frequently Asked Questions

### How often should I reconcile Airbnb and Booking.com payments?

Monthly is ideal. Quarterly is the minimum if MTD applies to you.

### What if the numbers don't match between Airbnb and Booking.com?

Investigate. Common causes: missing transactions, duplicate entries, fee miscalculations, or pending payouts.

### Do I need to reconcile if I use software?

Yes, but software does most of the work. You review rather than calculate.

### Can I reconcile across more than two platforms?

Yes. [HMRC Reporter](https://hmrcreporter.com/) supports 27+ platforms and reconciles all of them together.

### What if I find a discrepancy from a previous tax year?

Correct it in your records. If it affects your Self Assessment, you may need to amend your return or contact HMRC.

---

*Reconcile automatically. [HMRC Reporter](https://hmrcreporter.com/) imports from Airbnb, Booking.com, and 25+ other platforms and reconciles payments in one view. [Get started →](https://hmrcreporter.com/)*

## Related Posts

- [Booking.com and Airbnb Income: How to Combine for HMRC](./21-booking-com-airbnb-income-combine-hmrc.md) — combining multi-platform income for tax
- [How to Turn Airbnb Transactions Into HMRC-Ready Reports](./28-how-to-turn-airbnb-transactions-into-hmrc-ready-reports.md) — from raw data to compliant reports
- [Common HMRC Reporting Errors Airbnb Hosts Make](./25-common-hmrc-reporting-errors-airbnb-hosts-make.md) — mistakes to avoid
