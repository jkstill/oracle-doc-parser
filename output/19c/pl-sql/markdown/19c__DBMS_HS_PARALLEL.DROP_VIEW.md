---
id: 19c__DBMS_HS_PARALLEL.DROP_VIEW
name: DBMS_HS_PARALLEL.DROP_VIEW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HS_PARALLEL
tags: [dbms_hs_parallel]
source_file: DBMS_HS_PARALLEL.html
---

# DBMS_HS_PARALLEL.DROP_VIEW

This procedure drops the view and internal objects created by the CREATE_OR_REPLACE_VIEW procedure. If the view has not already been created by the CREATE_OR_REPLACE_VIEW procedure, an error message is returned.

## Syntax

```sql
DROP_VIEW (oracle_view)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| oracle_view |  |  | The name of the Oracle view created by the CREATE_OR_REPLACE_VIEW procedure. If the view has not been created by the CREATE_OR_REPLACE_VIEW procedure, an error is returned. |

## Usage Notes

Syntax DROP_VIEW (oracle_view) Parameters Table 84-4 DROP_VIEW Procedure Parameter Parameter Description oracle_view The name of the Oracle view created by the CREATE_OR_REPLACE_VIEW procedure. If the view has not been created by the CREATE_OR_REPLACE_VIEW procedure, an error is returned.