# Skill: Tax Reporting

_Capability to generate and validate HMRC-compliant tax reports for property income._

## Triggers

- "generate report", "create tax report", "hmrc report"
- "prepare return", "tax calculation", "income summary"
- "sa100", "sa105", "property income"

## Actions

1. **Gather Income Data**
   - Collect rental income figures from user's records
   - Identify property type (Furnished Holiday Let vs Standard Rental)
   - Verify tax year applicability

2. **Calculate Taxable Income**
   - Total rental income - allowable expenses = taxable profit
   - Apply appropriate deductions (capital allowances, wear & tear)
   - Consider MTD digital record requirements

3. **Generate Report Summary**
   - Property income breakdown by address
   - Expense categorization (allowed vs disallowed)
   - Estimated tax liability
   - Recommended next steps

## Output Format

```
## Tax Report: [Tax Year]

### Income Summary
- Total Rental Income: £X
- Allowable Expenses: £X
- Taxable Profit: £X

### Property Details
| Property | Income | Expenses | Profit |
|----------|--------|----------|--------|
| ...     | ...    | ...      | ...    |

### Estimated Tax
- Income Tax: £X
- National Insurance: £X
- Total: £X

### HMRC Compliance Notes
- [Action items]
```

## Constraints

- Always include disclaimer to verify with accountant
- Flag MTD compliance requirements
- Note any deadlines approaching

---

_Reference: HMRC Property Income Manual, SA100 Notes, MTD for Income Tax_