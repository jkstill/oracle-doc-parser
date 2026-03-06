---
id: 19c__DBMS_RLS.DROP_POLICY_CONTEXT
name: DBMS_RLS.DROP_POLICY_CONTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RLS
tags: [dbms_rls]
source_file: DBMS_RLS.html
---

# DBMS_RLS.DROP_POLICY_CONTEXT

This procedure drops a driving context from the object so that it will have one less driving context.

## Syntax

```sql
DBMS_RLS.DROP_POLICY_CONTEXT (
   object_schema   IN VARCHAR2 NULL,
   object_name     IN VARCHAR2,
   namespace       IN VARCHAR2,
   attribute       IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. |
| object_name | VARCHAR2 | IN | Name of the table, view, or synonym to which the policy is dropped |
| namespace | VARCHAR2 | IN | Namespace of the driving context |
| attribute | VARCHAR2) | IN | Attribute of the driving context |

## Usage Notes

Syntax DBMS_RLS.DROP_POLICY_CONTEXT ( object_schema IN VARCHAR2 NULL, object_name IN VARCHAR2, namespace IN VARCHAR2, attribute IN VARCHAR2); Parameters Table 146-14 DROP_POLICY_CONTEXT Procedure Parameters Parameter Description object_schema Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. object_name Name of the table, view, or synonym to which the policy is dropped namespace Namespace of the driving context attribute Attribute of the driving context