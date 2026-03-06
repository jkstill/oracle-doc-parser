---
id: 19c__DBMS_FGA.DISABLE_POLICY
name: DBMS_FGA.DISABLE_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FGA
tags: [dbms_fga]
source_file: DBMS_FGA.html
---

# DBMS_FGA.DISABLE_POLICY

This procedure disables an audit policy.

## Syntax

```sql
DBMS_FGA.DISABLE_POLICY(
   object_schema  IN  VARCHAR2, 
   object_name    IN  VARCHAR2, 
   policy_name    IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema of the object to be audited. If NULL , the current schema is assumed. |
| object_name | VARCHAR2 | IN | Name of the object to be audited |
| policy_name | VARCHAR2) | IN | Unique name of the policy |

## Usage Notes

Syntax DBMS_FGA.DISABLE_POLICY( object_schema IN VARCHAR2, object_name IN VARCHAR2, policy_name IN VARCHAR2); Parameters Table 69-3 DISABLE_POLICY Procedure Parameters Parameter Description object_schema Schema of the object to be audited. If NULL , the current schema is assumed. object_name Name of the object to be audited policy_name Unique name of the policy The default value for object_schema is NULL . If NULL , the current schema is assumed. Examples DBMS_FGA.DISABLE_POLICY ( object_schema => 'scott', object_name => 'emp', policy_name => 'mypolicy1');