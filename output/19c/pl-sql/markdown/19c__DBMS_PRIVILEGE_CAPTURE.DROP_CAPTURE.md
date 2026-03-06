---
id: 19c__DBMS_PRIVILEGE_CAPTURE.DROP_CAPTURE
name: DBMS_PRIVILEGE_CAPTURE.DROP_CAPTURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PRIVILEGE_CAPTURE
tags: [dbms_privilege_capture]
source_file: DBMS_PRIVILEGE_CAPTURE.html
---

# DBMS_PRIVILEGE_CAPTURE.DROP_CAPTURE

This procedure removes a privilege analysis policy together with the data recorded. When a policy is removed, all previously recorded privilege use data associated with the policy is deleted.

## Syntax

```sql
DBMS_PRIVILEGE_CAPTURE.DROP_CAPTURE (
   name      IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2) | IN | Name of the privilege analysis policy to be removed |

## Usage Notes

Syntax DBMS_PRIVILEGE_CAPTURE.DROP_CAPTURE ( name IN VARCHAR2); Parameters Table 131-6 DROP_CAPTURE Procedure Parameters Parameter Description name Name of the privilege analysis policy to be removed Usage Notes You must disable a privilege analysis policy before removing it. An enabled policy cannot be removed. If there are capture runs associated with this policy, then they are automatically dropped when you drop the policy.