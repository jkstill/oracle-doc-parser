---
id: 19c__DBMS_COMPARISON.COMPARE
name: DBMS_COMPARISON.COMPARE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_COMPARISON
tags: [dbms_comparison]
source_file: DBMS_COMPARISON.html
---

# DBMS_COMPARISON.COMPARE

This function performs the specified comparison.

## Syntax

```sql
DBMS_COMPARISON.COMPARE(
   comparison_name  IN   VARCHAR2,
   scan_info        OUT  COMPARISON_TYPE,
   min_value        IN   VARCHAR2   DEFAULT NULL,
   max_value        IN   VARCHAR2   DEFAULT NULL,
   perform_row_dif  IN   BOOLEAN    DEFAULT FALSE)
RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| comparison_name | VARCHAR2 | IN | The name of the comparison. |
| scan_info | COMPARISON_TYPE | OUT | Information about the compare operation returned in the COMPARISON_TYPE datatype. See COMPARISON_TYPE Record Type . |
| min_value | VARCHAR2 | IN | When the scan mode for the comparison is set to CMP_SCAN_MODE_CUSTOM , specify the minimum index column value for the range of rows that are being compared. To determine the index column for a comparison, query the DBA_COMPARISON_COLUMNS data dictionary view. For a composite index, specify a value for the column with column_position equal to 1 in the DBA_COMPARISON_COLUMNS view. See the index column requirements under DBMS_COMPARISON Operational Notes . If the scan mode is set to a value other than CMP_SCAN_MODE_CUSTOM , then this parameter must be set to NULL . If NULL and the scan_mode parameter is set to CMP_SCAN_MODE_CUSTOM , then an error is raised. To determine the scan mode for the comparison, query the DBA_COMPARISON data dictionary view. See DBMS_COMPARISON Constants for information about scan modes. |
| max_value | VARCHAR2 | IN | When the scan mode for the comparison is set to CMP_SCAN_MODE_CUSTOM , specify the maximum index column value for the range of rows that are being compared. To determine the index column for a comparison, query the DBA_COMPARISON_COLUMNS data dictionary view. For a composite index, specify a value for the column with column_position equal to 1 in the DBA_COMPARISON_COLUMNS view. See the index column requirements under DBMS_COMPARISON Operational Notes . If the scan mode is set to a value other than CMP_SCAN_MODE_CUSTOM , then this parameter must be set to NULL . If NULL and the scan_mode parameter is set to CMP_SCAN_MODE_CUSTOM , then an error is raised. To determine the scan mode for the comparison, query the DBA_COMPARISON data dictionary view. See DBMS_COMPARISON Constants for information about scan modes. |
| perform_row_dif | BOOLEAN | IN | If TRUE , then compares each row individually in the database object being compared after reaching the smallest possible bucket for the comparison. If FALSE , then compares buckets for differences but does not compare each row individually when differences are found in the smallest possible bucket. See DBMS_COMPARISON Overview for information about buckets. |

**Returns:** `BOOLEAN`

## Usage Notes

Each time a comparison is performed, it results in at least one new scan, and each scan has a unique scan ID. You can define and name a comparison using the CREATE_COMPARISON procedure. See Also: " Overview " CREATE_COMPARISON Procedure See Also: " Overview " CREATE_COMPARISON Procedure Syntax DBMS_COMPARISON.COMPARE( comparison_name IN VARCHAR2, scan_info OUT COMPARISON_TYPE, min_value IN VARCHAR2 DEFAULT NULL, max_value IN VARCHAR2 DEFAULT NULL, perform_row_dif IN BOOLEAN DEFAULT FALSE) RETURN BOOLEAN; Parameters Table 37-4 COMPARE Function Parameters Parameter Description comparison_name The name of the comparison. scan_info Information about the compare operation returned in the COMPARISON_TYPE datatype. See COMPARISON_TYPE Record Type . min_value When the scan mode for the comparison is set to CMP_SCAN_MODE_CUSTOM , specify the minimum index column value for the range of rows that are being compared. To determine the index column for a comparison, query the DBA_COMPARISON_COLUMNS data dictionary view. For a composite index, specify a value for the column with column_position equal to 1 in the DBA_COMPARISON_COLUMNS view. See the index column requirements under DBMS_COMPARISON Operational Notes . If the scan mode is set to a value other than CMP_SCAN_MODE_CUSTOM , then this parameter must be set to NULL . If NULL and the scan_mode parameter is set to CMP_SCAN_MODE_CUSTOM , then an error is raised. To determine the scan mode for the comparison, query the DBA_COMPARISON data dictionary view. See DBMS_COMPARISON Constants for information about scan modes. max_value When the scan mode for the comparison is set to CMP_SCAN_MODE_CUSTOM , specify the maximum index column value for the range of rows that are being compared. To determine the index column for a comparison, query the DBA_COMPARISON_COLUMNS data dictionary view. For a composite index, specify a value for the column with column_position equal to 1 in the DBA_COMPARISON_COLUMNS view. See the index column requirements under DBMS_COMPARISON Operational Notes . If the scan mode is set to a value other than CMP_SCAN_MODE_CUSTOM , then this parameter must be set to NULL . If NULL and the scan_mode parameter is set to CMP_SCAN_MODE_CUSTOM , then an error is raised. To determine the scan mode for the comparison, query the DBA_COMPARISON data dictionary view. See DBMS_COMPARISON Constants for information about scan modes. perform_row_dif If TRUE , then compares each row individually in the database object being compared after reaching the smallest possible bucket for the comparison. If FALSE , then compares buckets for differences but does not compare each row individually when differences are found in the smallest possible bucket. See DBMS_COMPARISON Overview for information about buckets. Return Values This function returns TRUE when no differences are found in the database objects being compared. This function returns FALSE when differences are found in the database objects being compared.