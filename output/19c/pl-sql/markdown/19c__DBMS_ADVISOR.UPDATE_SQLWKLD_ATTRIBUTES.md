---
id: 19c__DBMS_ADVISOR.UPDATE_SQLWKLD_ATTRIBUTES
name: DBMS_ADVISOR.UPDATE_SQLWKLD_ATTRIBUTES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.UPDATE_SQLWKLD_ATTRIBUTES

This procedure changes various attributes of a SQL Workload object or template.

## Syntax

```sql
DBMS_ADVISOR.UPDATE_SQLWKLD_ATTRIBUTES (
   workload_name        IN VARCHAR2,
   new_name             IN VARCHAR2 := NULL,
   description          IN VARCHAR2 := NULL,
   read_only            IN VARCHAR2 := NULL,
   is_template          IN VARCHAR2 := NULL,
   how_created          IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| workload_name | VARCHAR2 | IN | The workload object name that uniquely identifies an existing workload. |
| new_name | VARCHAR2 | IN | The new workload object name. If the value is NULL or contains the value ADVISOR_UNUSED , the workload will not be renamed. A task name can be up to 30 characters long. |
| description | VARCHAR2 | IN | A new workload description. If the value is NULL or contains the value ADVISOR_UNUSED , the description will not be changed. Names can be up to 256 characters long. |
| read_only | VARCHAR2 | IN | Set to TRUE so it cannot be changed. |
| is_template | VARCHAR2 | IN | TRUE if workload is to be used as a template. |
| how_created | VARCHAR2 | IN | Indicates a source application name that initiated the workload creation. If the value is NULL or contains the value ADVISOR_UNUSED , the source will not be changed. |

## Usage Notes

Note: This procedure is deprecated starting in Oracle Database 11 g . Note: This procedure is deprecated starting in Oracle Database 11 g . Syntax DBMS_ADVISOR.UPDATE_SQLWKLD_ATTRIBUTES ( workload_name IN VARCHAR2, new_name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, read_only IN VARCHAR2 := NULL, is_template IN VARCHAR2 := NULL, how_created IN VARCHAR2 := NULL); Parameters Table 16-43 UPDATE_SQLWKLD_ATTRIBUTES Procedure Parameters Parameter Description workload_name The workload object name that uniquely identifies an existing workload. new_name The new workload object name. If the value is NULL or contains the value ADVISOR_UNUSED , the workload will not be renamed. A task name can be up to 30 characters long. description A new workload description. If the value is NULL or contains the value ADVISOR_UNUSED , the description will not be changed. Names can be up to 256 characters long. read_only Set to TRUE so it cannot be changed. is_template TRUE if workload is to be used as a template. how_created Indicates a source application name that initiated the workload creation. If the value is NULL or contains the value ADVISOR_UNUSED , the source will not be changed. Examples DECLARE workload_name VARCHAR2(30); BEGIN workload_name := 'My Workload'; DBMS_ADVISOR.CREATE_SQLWKLD(workload_name, 'My Workload'); DBMS_ADVISOR.ADD_SQLWKLD_STATEMENT(workload_name, 'MONTHLY', 'ROLLUP', 100,400,5041,103,640445,680000,2, 1,SYSDATE,1,'SH','SELECT AVG(amount_sold) FROM sh.sales WHERE promo_id = 10'); DBMS_ADVISOR.UPDATE_SQLWKLD_ATTRIBUTES(workload_name,'New workload name'); END; /