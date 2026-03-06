---
id: 19c__DBMS_COMPARISON.RECHECK
name: DBMS_COMPARISON.RECHECK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_COMPARISON
tags: [dbms_comparison]
source_file: DBMS_COMPARISON.html
---

# DBMS_COMPARISON.RECHECK

This function rechecks the differences in a specified scan for a comparison.

## Syntax

```sql
DBMS_COMPARISON.RECHECK(
   comparison_name  IN  VARCHAR2,
   scan_id          IN  NUMBER,
   perform_row_dif  IN  BOOLEAN  DEFAULT FALSE)
RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| comparison_name | VARCHAR2 | IN | The name of the comparison. |
| scan_id | NUMBER | IN | The scan ID of the scan to recheck. See " Overview " for more information about specifying a scan ID in this parameter. |
| perform_row_dif | BOOLEAN | IN | If TRUE , then compares each row individually in the database objects being compared after reaching the smallest possible bucket for the comparison. If FALSE , then compares buckets for differences but does not compare each row individually when differences are found in the smallest possible bucket. See " Overview " for information about buckets. |

**Returns:** `BOOLEAN`

## Usage Notes

This function performs one of the following actions: If the specified scan completed successfully the last time it ran, then this function checks the previously identified differences in the scan. If the specified scan completed partially, then this function continues to check the database object from the point where the previous scan ended. Note: This function does not compare the shared database object for differences that were not recorded in the specified comparison scan. To check for those differences, run the COMPARE function. See Also: COMPARE Function Note: This function does not compare the shared database object for differences that were not recorded in the specified comparison scan. To check for those differences, run the COMPARE function. See Also: COMPARE Function Syntax DBMS_COMPARISON.RECHECK( comparison_name IN VARCHAR2, scan_id IN NUMBER, perform_row_dif IN BOOLEAN DEFAULT FALSE) RETURN BOOLEAN; Parameters Table 37-9 RECHECK Function Parameters Parameter Description comparison_name The name of the comparison. scan_id The scan ID of the scan to recheck. See " Overview " for more information about specifying a scan ID in this parameter. perform_row_dif If TRUE , then compares each row individually in the database objects being compared after reaching the smallest possible bucket for the comparison. If FALSE , then compares buckets for differences but does not compare each row individually when differences are found in the smallest possible bucket. See " Overview " for information about buckets.