---
id: 19c__DBMS_COMPARISON.PURGE_COMPARISON
name: DBMS_COMPARISON.PURGE_COMPARISON
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_COMPARISON
tags: [dbms_comparison]
source_file: DBMS_COMPARISON.html
---

# DBMS_COMPARISON.PURGE_COMPARISON

This procedure purges the comparison results, or a subset of the comparison results, for a comparison.

## Syntax

```sql
DBMS_COMPARISON.PURGE_COMPARISON(
   comparison_name  IN  VARCHAR2,
   scan_id          IN  NUMBER     DEFAULT NULL,
   purge_time       IN  TIMESTAMP  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| comparison_name | VARCHAR2 | IN | The name of the comparison. |
| scan_id | NUMBER | IN | The scan ID of the scan for which results are purged. The scan ID must identify a root scan. If the scan ID does not identify a root scan, then an error is raised. When a root scan ID is specified, it is purged, and all direct and indirect child scans of the specified root scan are purged. If NULL , then no scan ID is considered when purging comparison results for the comparison. See " Overview " for information about scans. |
| purge_time | TIMESTAMP | IN | The date before which results are purged. If NULL , then no date is considered when purging comparison results for the comparison. |

## Usage Notes

Note: At least one of the following parameters must be set to NULL : scan_id or purge_time . If both the scan_id and purge_time parameters are NULL , then this procedure purges all comparison results for the comparison. Note: At least one of the following parameters must be set to NULL : scan_id or purge_time . If both the scan_id and purge_time parameters are NULL , then this procedure purges all comparison results for the comparison. Syntax DBMS_COMPARISON.PURGE_COMPARISON( comparison_name IN VARCHAR2, scan_id IN NUMBER DEFAULT NULL, purge_time IN TIMESTAMP DEFAULT NULL); Parameters Table 37-8 PURGE_COMPARISON Procedure Parameters Parameter Description comparison_name The name of the comparison. scan_id The scan ID of the scan for which results are purged. The scan ID must identify a root scan. If the scan ID does not identify a root scan, then an error is raised. When a root scan ID is specified, it is purged, and all direct and indirect child scans of the specified root scan are purged. If NULL , then no scan ID is considered when purging comparison results for the comparison. See " Overview " for information about scans. purge_time The date before which results are purged. If NULL , then no date is considered when purging comparison results for the comparison.