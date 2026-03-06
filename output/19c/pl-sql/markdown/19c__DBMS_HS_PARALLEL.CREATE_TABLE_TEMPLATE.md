---
id: 19c__DBMS_HS_PARALLEL.CREATE_TABLE_TEMPLATE
name: DBMS_HS_PARALLEL.CREATE_TABLE_TEMPLATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HS_PARALLEL
tags: [dbms_hs_parallel]
source_file: DBMS_HS_PARALLEL.html
---

# DBMS_HS_PARALLEL.CREATE_TABLE_TEMPLATE

This procedure writes out a CREATE TABLE template based on information gathered from the remote table. You can use the information to add any optimal Oracle CREATE TABLE clauses.

## Syntax

```sql
CREATE_TABLE_TEMPLATE (remote_table, database_link, oracle_table, create_table_template_string)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| remote_table |  |  | The name of the remote database table. It is specified as [remote_schema_name.]remote_table_name . |
| database_link |  |  | The remote database link name. The call can only be applied to a heterogeneous services database link. |
| oracle_table |  |  | The name of the local Oracle table the data will be loaded into. It is specified as [schema_name.]oracle_table_name . The default schema name is the current user. If the oracle_table parameter is not specified, the remote table name will be used as the local Oracle name. |
| create_table_template_string |  |  | Contains the Oracle CREATE TABLE SQL template when the procedure is returned. |

## Usage Notes

Syntax CREATE_TABLE_TEMPLATE (remote_table, database_link, oracle_table, create_table_template_string) Parameters Table 84-3 CREATE_TABLE_TEMPLATE Procedure Parameters Parameter Description remote_table The name of the remote database table. It is specified as [remote_schema_name.]remote_table_name . database_link The remote database link name. The call can only be applied to a heterogeneous services database link. oracle_table The name of the local Oracle table the data will be loaded into. It is specified as [schema_name.]oracle_table_name . The default schema name is the current user. If the oracle_table parameter is not specified, the remote table name will be used as the local Oracle name. create_table_template_string Contains the Oracle CREATE TABLE SQL template when the procedure is returned.