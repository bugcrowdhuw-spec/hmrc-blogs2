# Skill: Expense Categorization

_Capability to categorize rental expenses and determine tax deductibility._

## Triggers

- "expenses", "deductions", "allowable costs", "what can I deduct"
- "expense category", "tax relief", "business expenses"

## Expense Categories

### Fully Allowable
- Agent fees (letting/management)
- Insurance (buildings, public liability)
- Professional fees (legal, accounting)
- Cleaning (between tenants)
- Utilities (if landlord pays)
- Repairs (not improvements - see HMRC distinction)
- Travel (wholly for rental purposes)
- Office costs (relevant portion)

### Partially Allowable
- Mortgage interest (basic rate tax relief)
- Property insurance (pro-rata if mixed use)
- Phone/internet (business portion only)

### Not Allowable
- Capital improvements (decorating, extensions)
- Personal expenses
- Pre-purchase costs
- Fines and penalties

## Actions

1. **Review User's Expense List**
   - Request expense breakdown
   - Categorize each item
   - Identify potential reclassification

2. **Apply HMRC Rules**
   - Check "wholly and exclusively" test
   - Verify timing (same tax year as income)
   - Ensure proper documentation

3. **Generate Expense Summary**
   - Total allowable expenses
   - Total disallowed expenses
   - Potential tax savings if reclassified

## Output Format

```
## Expense Analysis

### Allowable Expenses: £X
| Item | Amount | HMRC Reason |
|------|--------|--------------|
| ...  | ...    | ...          |

### Disallowed: £X
| Item | Amount | Reason |
|------|--------|--------|
| ...  | ...    | ...    |

### Tax Impact
- Deductible from rental profit: £X
- Potential adjustment: £X (if reclassify)
```

---

_Reference: HMRC Business Income Manual, Property Income Manual_