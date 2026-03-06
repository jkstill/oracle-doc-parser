---
id: 19c__DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT
name: DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PRIVILEGE_CAPTURE
tags: [dbms_privilege_capture]
source_file: DBMS_PRIVILEGE_CAPTURE.html
---

# DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT

This procedure populates the privilege analysis data dictionary views with data.

## Syntax

```sql
DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT (
   name        IN VARCHAR2,
   run_name    IN VARCHAR2 DEFAULT NULL,
   DEPENDENCY  IN BOOLEAN DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of the privilege analysis policy for which views are populated |
| run_name | VARCHAR2 | IN | Name of the capture run that is associated with the privilege analysis policy. If you omit this parameter, then the records of all created runs will be analyzed. When you specify the run_name parameter, only the records of that run are analyzed and all other runs are unaffected. |
| dependency | BOOLEAN | IN | Enter Y (yes) or N (no) to indicate if PL/SQL compilation privileges, set by the DBMS_PRIVILEGE_CAPTURE.CAPTURE_DEPENDENCY_PRIVS procedure, should be included in the report. |

## Usage Notes

See Also: Oracle® Database Security Guide for more information about privilege analysis views. See Also: Oracle® Database Security Guide for more information about privilege analysis views. Syntax DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT ( name IN VARCHAR2, run_name IN VARCHAR2 DEFAULT NULL, DEPENDENCY IN BOOLEAN DEFAULT NULL); Parameters Table 131-8 GENERATE_RESULT Procedure Parameters Parameter Description name Name of the privilege analysis policy for which views are populated run_name Name of the capture run that is associated with the privilege analysis policy. If you omit this parameter, then the records of all created runs will be analyzed. When you specify the run_name parameter, only the records of that run are analyzed and all other runs are unaffected. dependency Enter Y (yes) or N (no) to indicate if PL/SQL compilation privileges, set by the DBMS_PRIVILEGE_CAPTURE.CAPTURE_DEPENDENCY_PRIVS procedure, should be included in the report. Usage Notes You must disable a privilege analysis policy before populating the privilege analysis views for the policy. You cannot invoke this subprogram on an enabled privilege analysis policy.