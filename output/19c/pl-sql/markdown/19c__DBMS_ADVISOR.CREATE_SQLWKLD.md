---
id: 19c__DBMS_ADVISOR.CREATE_SQLWKLD
name: DBMS_ADVISOR.CREATE_SQLWKLD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.CREATE_SQLWKLD

This procedure creates a new private SQL Workload object for the user.

## Syntax

```sql
DBMS_ADVISOR.CREATE_SQLWKLD (
   workload_name            IN OUT VARCHAR2,
   description              IN VARCHAR2 := NULL,
   template                 IN VARCHAR2 := NULL,
   is_template              IN VARCHAR2 := 'FALSE');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| workload_name | VARCHAR2 | IN OUT | A name that uniquely identifies the created workload. If not specified, the system will generate a unique name. Names can be up to 30 characters long. |
| description | VARCHAR2 | IN | Specifies an optional workload description. Descriptions can be up to 256 characters. |
| template | VARCHAR2 | IN | An optional SQL Workload name of an existing workload data object or data object template. |
| is_template | VARCHAR2 | IN | An optional value that enables you to set the newly created workload as a template. Valid values are TRUE and FALSE . |

## Usage Notes

A SQL Workload object manages a SQL workload on behalf of the SQL Access Advisor. A SQL Workload object must exist prior to performing any other SQL Workload operations, such as importing or updating SQL statements. Note: This procedure is deprecated starting in Oracle Database 11 g . Note: This procedure is deprecated starting in Oracle Database 11 g . Syntax DBMS_ADVISOR.CREATE_SQLWKLD ( workload_name IN OUT VARCHAR2, description IN VARCHAR2 := NULL, template IN VARCHAR2 := NULL, is_template IN VARCHAR2 := 'FALSE'); Parameters Table 16-9 CREATE_SQLWKLD Procedure Parameters Parameter Description workload_name A name that uniquely identifies the created workload. If not specified, the system will generate a unique name. Names can be up to 30 characters long. description Specifies an optional workload description. Descriptions can be up to 256 characters. template An optional SQL Workload name of an existing workload data object or data object template. is_template An optional value that enables you to set the newly created workload as a template. Valid values are TRUE and FALSE . Return Values The SQL Access Advisor returns a unique workload object identifier number that must be used for subsequent activities within the new SQL Workload object.