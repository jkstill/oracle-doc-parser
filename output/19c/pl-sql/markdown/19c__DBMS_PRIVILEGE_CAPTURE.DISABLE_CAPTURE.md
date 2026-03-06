---
id: 19c__DBMS_PRIVILEGE_CAPTURE.DISABLE_CAPTURE
name: DBMS_PRIVILEGE_CAPTURE.DISABLE_CAPTURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PRIVILEGE_CAPTURE
tags: [dbms_privilege_capture]
source_file: DBMS_PRIVILEGE_CAPTURE.html
---

# DBMS_PRIVILEGE_CAPTURE.DISABLE_CAPTURE

This procedure stops the recording of privilege use for a specified privilege analysis policy. When a policy is disabled, privilege use meeting the policy condition is no longer recorded.

## Syntax

```sql
DBMS_PRIVILEGE_CAPTURE.DISABLE_CAPTURE (
   name        IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2) | IN | Name of the privilege analysis policy to be disabled |

## Usage Notes

Syntax DBMS_PRIVILEGE_CAPTURE.DISABLE_CAPTURE ( name IN VARCHAR2); Parameters Table 131-5 DISABLE_CAPTURE Procedure Parameters Parameter Description name Name of the privilege analysis policy to be disabled Usage Notes When a privilege analysis policy is first created, it is disabled by default.