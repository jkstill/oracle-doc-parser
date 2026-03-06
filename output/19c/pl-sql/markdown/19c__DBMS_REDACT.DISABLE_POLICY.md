---
id: 19c__DBMS_REDACT.DISABLE_POLICY
name: DBMS_REDACT.DISABLE_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDACT
tags: [dbms_redact]
source_file: DBMS_REDACT.html
---

# DBMS_REDACT.DISABLE_POLICY

This procedure disables a Data Redaction policy.

## Syntax

```sql
DBMS_REDACT.DISABLE_POLICY (
   object_schema                IN    VARCHAR2 := NULL,
   object_name                  IN    VARCHAR2,
   policy_name                  IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema owning the table or view, current user if NULL |
| object_name | VARCHAR2 | IN | Name of table or view for which to disable a Data Redaction policy |
| policy_name | VARCHAR2) | IN | Name of policy to be disabled |

## Usage Notes

Syntax DBMS_REDACT.DISABLE_POLICY ( object_schema IN VARCHAR2 := NULL, object_name IN VARCHAR2, policy_name IN VARCHAR2); Parameters Table 137-10 DISABLE_POLICY Procedure Parameters Parameter Description object_schema Schema owning the table or view, current user if NULL object_name Name of table or view for which to disable a Data Redaction policy policy_name Name of policy to be disabled Exceptions ORA-28068 - The object object does not have a Data Redaction policy. ORA-28072 - The specified policy name is incorrect. ORA-28080 - The policy was already disabled. Examples BEGIN DBMS_REDACT.DISABLE_POLICY ( object_schema => 'hr', object_name => 'employees', policy_name => 'mask_emp_ids'); END;