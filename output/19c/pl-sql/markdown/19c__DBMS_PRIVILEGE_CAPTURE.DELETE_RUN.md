---
id: 19c__DBMS_PRIVILEGE_CAPTURE.DELETE_RUN
name: DBMS_PRIVILEGE_CAPTURE.DELETE_RUN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PRIVILEGE_CAPTURE
tags: [dbms_privilege_capture]
source_file: DBMS_PRIVILEGE_CAPTURE.html
---

# DBMS_PRIVILEGE_CAPTURE.DELETE_RUN

This procedure deletes a privilege analysis capture run.

## Syntax

```sql
DBMS_PRIVILEGE_CAPTURE.DELETE_RUN (
   name      IN VARCHAR2,
   run_name  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of the privilege analysis policy with which the capture run is associated |
| run_name | VARCHAR2) | IN | Name of the capture run |

## Usage Notes

Syntax DBMS_PRIVILEGE_CAPTURE.DELETE_RUN ( name IN VARCHAR2, run_name IN VARCHAR2); Parameters Table 131-4 DELETE_RUN Procedure Parameters Parameter Description name Name of the privilege analysis policy with which the capture run is associated run_name Name of the capture run Usage Notes You can find the names of existing privilege capture policies by querying the DBA_PRIV_CAPTURES data dictionary view. Another way to delete a capture run is to drop the policy with which the capture run is associated. Dropping the policy automatically drops its associated capture runs. When you drop a capture run it is no longer accessible through the privilege capture data dictionary views.