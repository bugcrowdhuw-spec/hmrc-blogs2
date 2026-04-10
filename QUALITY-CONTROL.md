# Quality Control Process for Product Builds

## Overview

This document defines the quality control process for verifying product builds before they are considered complete and ready for review.

## Current State (as of 2026-04-10)

- **Total Products:** 19
- **Products with CSVs:** 13
- **Total CSV Files:** 60
- **Target:** 100 products with formatted CSVs

---

## 1. Product Inventory Checklist

Each product must be tracked in the inventory using the following schema:

| Field | Description | Values |
|-------|-------------|--------|
| Product Name | Directory name | string |
| Directory | Path to product | string |
| CSV Count | Number of CSV files | integer |
| CSV Files | List of CSV filenames | array |
| Formula Validation | Formulas in CSVs validated | pass/fail |
| Documentation | README/guide present | pass/fail |
| Status | Current state | in_progress / ready_for_review / complete |

### Products with CSVs (13)

| Product | Directory | CSV Count |
|---------|-----------|-----------|
| airbnb-tax-toolkit | airbnb-tax-toolkit/ | 3 |
| crypto-tax-calculator | crypto-tax-calculator/ | 4 |
| director-salary-calculator | director-salary-calculator/ | 2 |
| inheritance-tax-planning | inheritance-tax-planning/ | 5 |
| investment-income-tracker | investment-income-tracker/ | 6 |
| landlord-expenses-tracker | landlord-expenses-tracker/ | 1 |
| online-seller-toolkit | online-seller-toolkit/ | 5 |
| pension-tax-relief-calculator | pension-tax-relief-calculator/ | 6 |
| property-cgt-calculator | property-cgt-calculator/ | 6 |
| self-assessment-tracker | self-assessment-tracker/ | 4 |
| side-hustle-calculator | side-hustle-calculator/ | 7 |
| student-tax-guide | student-tax-guide/ | 4 |
| vat-calculator | vat-calculator/ | 7 |

### Products without CSVs (6)

- dividend-tax-calculator
- marriage-allowance-tracker
- mileage-allowance-tracker
- pension-contribution-tracker
- rental-income-spreadsheet
- uk-tax-codes-guide

---

## 2. Pre-Merge Requirements

Before requesting review, all products must meet these requirements:

### Minimum CSV Count

- **Minimum:** 1 CSV file per product
- **Recommended:** 3+ CSV files for comprehensive tools

### Formula Validation

All CSV files containing formulas must pass validation:

1. No circular references
2. All cell references valid
3. No #REF!, #VALUE!, #DIV/0! errors
4. Headers present in all columns
5. Data types consistent (numbers as numbers, dates as dates)

### Documentation Requirements

Each product directory must contain:

- `README.md` - Product overview and usage instructions
- `guide.md` - Detailed guide (if applicable)

### Status Progression

```
in_progress -> ready_for_review -> complete
```

A product advances to `ready_for_review` only when:
- [ ] Minimum CSV count met
- [ ] All formulas validated
- [ ] README.md present
- [ ] Guide.md present (if applicable)

---

## 3. Weekly Audit Process

### Audit Script

Run the following to generate the weekly audit report:

```bash
# Count products and CSVs
find . -maxdepth 1 -type d ! -name '.' ! -name '.git' ! -name '.*' | while read dir; do
  csv_count=$(find "$dir" -name "*.csv" 2>/dev/null | wc -l)
  echo "$dir: $csv_count CSVs"
done
```

### Audit Checklist

1. **List all products and CSV counts**
   ```bash
   ls -d */ | xargs -I {} sh -c 'echo -n {}: ; find {} -name "*.csv" 2>/dev/null | wc -l'
   ```

2. **Identify gaps vs 100-product target**
   - Current: 13 products with CSVs
   - Target: 100 products
   - Gap: 87 products needed

3. **Identify products without CSVs**
   - dividend-tax-calculator
   - marriage-allowance-tracker
   - mileage-allowance-tracker
   - pension-contribution-tracker
   - rental-income-spreadsheet
   - uk-tax-codes-guide

4. **Report status to mayor**
   - Summary of products with/without CSVs
   - New products added this week
   - Products requiring attention

---

## 4. 100-Product Plan Reference

### Gap Analysis

- **Current products with CSVs:** 13
- **Products without CSVs:** 6
- **Target:** 100 products with formatted CSVs
- **Gap to target:** 87 products

### Priority Actions

1. **Immediate:** Add CSVs to the 6 products without CSVs
2. **Short-term:** Expand CSV offerings in existing products
3. **Medium-term:** Develop new product ideas to reach 100 target

### Plan Reference

No external 100-product plan document was found. Current focus should be:
- Convert 6 existing products without CSVs to meet minimum requirements
- Expand each existing product to 4+ CSVs
- Create 81 new products to reach 100 total

---

## 5. CSV Validation Commands

### Check for formula errors

```bash
grep -l "#REF!\|#VALUE!\|#DIV/0!\|#NAME?\|#NULL!" **/*.csv
```

### Validate CSV structure

```bash
# Check headers
head -1 *.csv

# Check for empty files
find . -name "*.csv" -empty
```

---

## 6. Pre-Review Checklist

Before calling `gt_done`, verify:

- [ ] At least 1 CSV file in product directory
- [ ] All CSVs have valid formulas (no errors)
- [ ] README.md present with product description
- [ ] guide.md present (if product has usage guide)
- [ ] Product status set to `ready_for_review`

---

*Last updated: 2026-04-10*