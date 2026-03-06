---
id: 19c__DBMS_REDACT.ENABLE_POLICY
name: DBMS_REDACT.ENABLE_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDACT
tags: [dbms_redact]
source_file: DBMS_REDACT.html
---

# DBMS_REDACT.ENABLE_POLICY

This procedure re-enables a Data Redaction policy.

## Syntax

```sql
DBMS_REDACT.ENABLE_POLICY (
   object_schema                IN    VARCHAR2 := NULL,
   object_name                  IN    VARCHAR2,
   policy_name                  IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema owning the table or view, current user if NULL |
| object_name | VARCHAR2 | IN | Name of table or view to which to enable a Data Redaction policy |
| policy_name | VARCHAR2) | IN | Name of policy to be enabled |

## Usage Notes

Syntax DBMS_REDACT.ENABLE_POLICY ( object_schema IN VARCHAR2 := NULL, object_name IN VARCHAR2, policy_name IN VARCHAR2); Parameters Table 137-13 ENABLE_POLICY Procedure Parameters Parameter Description object_schema Schema owning the table or view, current user if NULL object_name Name of table or view to which to enable a Data Redaction policy policy_name Name of policy to be enabled Exceptions ORA-28068 - The object object does not have a Data Redaction policy. ORA-28071 - The action is not valid. ORA-28072 - The specified policy name is incorrect. ORA-28079 - The policy was already enabled. Examples BEGIN DBMS_REDACT.ENABLE_POLICY ( object_schema => 'hr', object_name => 'employees', policy_name => 'mask_emp_ids'); END;