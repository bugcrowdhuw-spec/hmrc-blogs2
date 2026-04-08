# Skill: MTD Compliance Checker

_Capability to verify Making Tax Digital compliance status for property landlords._

## Triggers

- "mtd compliance", "making tax digital", "digital tax"
- "hmrc software", "vat registered", "income threshold"
- "compliance check", "mtd requirements"

## Actions

1. **Assess MTD Threshold**
   - Check if rental income exceeds £50,000 (mandatory MTD)
   - Check if income between £10,000-£50,000 (voluntary MTD)
   - Verify current enrollment status

2. **Validate Software Compatibility**
   - Confirm user has MTD-compatible software
   - Verify digital records maintained
   - Check quarterly submission capability

3. **Generate Compliance Report**
   - Current status: Compliant / Non-Compliant / Not Required
   - Action items if non-compliant
   - Deadline reminders

## Output Format

```
## MTD Compliance Status

### Your Situation
- Annual Rental Income: £X
- MTD Status: [Required/Voluntary/Exempt]
- Current Enrollment: [Yes/No]

### Requirements
- Software: [Compatible/Need to switch]
- Records: [Digital/Paper]
- Submissions: [Quarterly/Annual]

### Next Steps
1. [Action item]
2. [Action item]
```

## Key Thresholds (2025/26)

- **Mandatory MTD:** Income £50,000+
- **Voluntary MTD:** Income £10,000 - £50,000
- **Exempt:** Income under £10,000

---

_Reference: HMRC MTD for Income Tax guidance, Finance Act 2016_