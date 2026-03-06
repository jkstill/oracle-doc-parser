---
id: 19c__DBMS_PRIVILEGE_CAPTURE.ENABLE_CAPTURE
name: DBMS_PRIVILEGE_CAPTURE.ENABLE_CAPTURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PRIVILEGE_CAPTURE
tags: [dbms_privilege_capture]
source_file: DBMS_PRIVILEGE_CAPTURE.html
---

# DBMS_PRIVILEGE_CAPTURE.ENABLE_CAPTURE

This procedure starts the recording of privilege analysis for a specified privilege analysis policy and optionally provides a capture run for this policy. After a policy is enabled, all privilege use under the policy condition is recorded.

## Syntax

```sql
DBMS_PRIVILEGE_CAPTURE.ENABLE_CAPTURE (
   name      IN VARCHAR2,
   run_name  IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of the privilege analysis policy to be enabled |
| run_name | VARCHAR2 | IN | Name of the capture run to associate with this policy, less than 128 characters. Enclose exotic characters in double quotation marks. |

## Usage Notes

Syntax DBMS_PRIVILEGE_CAPTURE.ENABLE_CAPTURE ( name IN VARCHAR2, run_name IN VARCHAR2 DEFAULT NULL); Parameters Table 131-7 ENABLE_CAPTURE Procedure Parameters Parameter Description name Name of the privilege analysis policy to be enabled run_name Name of the capture run to associate with this policy, less than 128 characters. Enclose exotic characters in double quotation marks. Usage Notes The following usage notes apply: When a privilege analysis policy is first created, it is disabled by default. You must run ENABLE_CAPTURE to enable the privilege analysis policy. You can enable only one privilege analysis policy at a time. However, a database-wide privilege analysis of the G_DATABASE type can be enabled together with another non G_DATABASE privilege analysis. You cannot enable the same run multiple times. For example, run_01 cannot be used again if you want to re-enable the capture for run_01 . Instead, create a new run.