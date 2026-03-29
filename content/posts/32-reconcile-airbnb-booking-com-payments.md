---
title: "How to Reconcile Airbnb and Booking.com Payments"
date: 2026-04-25
draft: false
description: "How to reconcile Airbnb and Booking.com payments. Covers data comparison, bank matching, discrepancy identification, and automated reconciliation."
tags: ["reconcile Airbnb Booking.com payments", "multi-platform payment reconciliation", "property income matching", "Airbnb Booking.com accounting"]
image: "/images/diagram-hmrc-workflow.svg"
slug: "reconcile-airbnb-booking-com-payments"
---

# How to Reconcile Airbnb and Booking.com Payments

*Last updated: March 2026*

If you list on both Airbnb and Booking.com, reconciling payments is one of the trickiest parts of property management. Different fee structures, different payout schedules, and different data formats make it hard to match your actual income to what each platform reports. Here's how to do it properly.

## Why Reconciliation Matters

Reconciliation means matching your records against platform statements to make sure everything adds up. It catches:

- **Missing bookings** — platforms occasionally omit transactions
- **Duplicate entries** — the same booking appearing twice
- **Fee miscalculations** — wrong commission rates applied
- **Refund errors** — incorrect refund amounts
- **Currency discrepancies** — conversion rate differences

For HMRC reporting, reconciliation ensures your figures are accurate — and match what platforms report about you.

## Airbnb vs Booking.com: Key Differences

| Feature | Airbnb | Booking.com |
|---|---|---|
| Host fee | ~3% | ~15% |
| Payout timing | 24hrs after check-in | Monthly (1st–15th of following month) |
| Data format | Transaction CSV | Reservation/statement CSV |
| Cleaning fees | Included in booking total | May be separate |
| Currency | Per transaction | Per reservation |

These differences mean you can't just add the two together without understanding each format.

## Step-by-Step Reconciliation

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

Both platforms export differently. Create a unified view:

| Field | Airbnb | Booking.com |
|---|---|---|
| Booking date | Transaction date | Reservation date |
| Guest | Guest name | Guest name |
| Property | Listing name | Property name |
| Gross amount | Booking total | Reservation value |
| Platform fee | Service fee | Commission |
| Net payout | Payout amount | Net amount |

Map each platform's columns to your standard format.

### Step 3: Match Against Bank Deposits

Check your bank account for deposits from each platform:

- **Airbnb:** Payouts per booking (24hrs after check-in)
- **Booking.com:** Monthly lump sum (1st–15th of following month)

Match each deposit to the corresponding transactions in your platform data.

### Step 4: Identify Discrepancies

Common issues:

**Missing deposits:**
- Booking completed but payout not received
- Check for pending payouts or hold periods

**Unmatched deposits:**
- Bank deposit doesn't match any booking
- Could be a refund reversal or adjustment

**Fee differences:**
- Expected fee doesn't match actual deduction
- Check for special promotions or rate changes

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

## Automating Reconciliation

Manual reconciliation works but takes hours. [HMRC Reporter](https://hmrcreporter.com/) automates it:

1. **Upload both CSVs** — Airbnb and Booking.com
2. **Automatic matching** — properties linked across platforms
3. **Gross income calculated** — handles different fee structures
4. **Discrepancies flagged** — missing or unusual entries highlighted
5. **Consolidated report** — combined figures ready for HMRC

[Learn more about HMRC Reporter →](https://hmrcreporter.com/)

## Reconciliation Frequency

### Monthly (Recommended)

- Easier to spot issues while recent
- Less data to process
- Builds consistent habit

### Quarterly (Minimum for MTD)

- Required if Making Tax Digital applies to you
- Aligns with MTD quarterly submissions

### Annually (Not Recommended)

- Harder to remember details
- Issues compound
- Stressful year-end scramble

## Common Reconciliation Problems

### Problem 1: Different Payout Schedules

Airbnb pays per booking. Booking.com pays monthly. Your bank shows deposits at different times.

**Solution:** Reconcile by booking date, not bank deposit date.

### Problem 2: Currency Conversion

Airbnb might pay in GBP. Booking.com might pay in EUR.

**Solution:** Convert to GBP using HMRC's rates. Track the conversion for each payment.

### Problem 3: Refunds and Adjustments

Guest cancels, you refund, platform adjusts fees.

**Solution:** Track refunds as negative income. Adjust platform fees accordingly.

### Problem 4: Cleaning Fees

Airbnb includes cleaning fees in the booking total. Booking.com might handle them separately.

**Solution:** Ensure cleaning fee income is captured consistently across both platforms.

## Frequently Asked Questions

**Q: How often should I reconcile?**
A: Monthly is ideal. Quarterly is the minimum if MTD applies.

**Q: What if the numbers don't match?**
A: Investigate. Common causes: missing transactions, duplicate entries, fee miscalculations, or pending payouts.

**Q: Do I need to reconcile if I use software?**
A: Yes, but software does most of the work. You review rather than calculate.

**Q: Can I reconcile across more than two platforms?**
A: Yes. [HMRC Reporter](https://hmrcreporter.com/) supports 27+ platforms and reconciles all of them together.

**Q: What if I find a discrepancy from a previous tax year?**
A: Correct it in your records. If it affects your Self Assessment, you may need to amend your return or contact HMRC.

---

*Reconcile automatically. [HMRC Reporter](https://hmrcreporter.com/) imports from Airbnb, Booking.com, and 25+ other platforms and reconciles payments in one view. [Get started →](https://hmrcreporter.com/)*

---
