---
id: 19c__DBMS_ADVISOR.IMPORT_SQLWKLD_SCHEMA
name: DBMS_ADVISOR.IMPORT_SQLWKLD_SCHEMA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.IMPORT_SQLWKLD_SCHEMA

This procedure constructs and loads a SQL workload based on schema evidence. The workload is also referred to as a hypothetical workload.

## Syntax

```sql
DBMS_ADVISOR.IMPORT_SQLWKLD_SCHEMA (
   workload_name         IN VARCHAR2,
   import_mode           IN VARCHAR2 := 'NEW',
   priority              IN NUMBER := 2,
   saved_rows            OUT NUMBER,
   failed_rows           OUT NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| workload_name | VARCHAR2 | IN | The workload object name that uniquely identifies an existing workload. |
| import_mode | VARCHAR2 | IN | Specifies the action to be taken when storing the workload. Possible values are: APPEND Indicates that the collected workload will be added to any existing workload in the task. NEW Indicates that the collected workload will be the exclusive workload for the task. If an existing workload is found, an exception will be thrown. REPLACE Indicates the collected workload will be the exclusive workload for the task. If an existing workload is found, it will be deleted prior to saving the new workload. The default value is NEW . |
| priority | NUMBER | IN | Specifies the application priority for each statement that is saved in the workload object. The value must be one of the following: 1- HIGH , 2- MEDIUM , or 3- LOW . |
| failed_rows | NUMBER) | OUT | Returns the number or rows that were not saved due to syntax or validation errors |
| saved_rows | NUMBER | OUT | Returns the number of rows actually saved in the repository. |

## Usage Notes

Note: This procedure is deprecated starting in Oracle Database 11 g . Note: This procedure is deprecated starting in Oracle Database 11 g . Syntax DBMS_ADVISOR.IMPORT_SQLWKLD_SCHEMA ( workload_name IN VARCHAR2, import_mode IN VARCHAR2 := 'NEW', priority IN NUMBER := 2, saved_rows OUT NUMBER, failed_rows OUT NUMBER); Parameters Table 16-21 IMPORT_SQLWKLD_SCHEMA Procedure Parameters Parameter Description workload_name The workload object name that uniquely identifies an existing workload. import_mode Specifies the action to be taken when storing the workload. Possible values are: APPEND Indicates that the collected workload will be added to any existing workload in the task. NEW Indicates that the collected workload will be the exclusive workload for the task. If an existing workload is found, an exception will be thrown. REPLACE Indicates the collected workload will be the exclusive workload for the task. If an existing workload is found, it will be deleted prior to saving the new workload. The default value is NEW . priority Specifies the application priority for each statement that is saved in the workload object. The value must be one of the following: 1- HIGH , 2- MEDIUM , or 3- LOW . failed_rows Returns the number or rows that were not saved due to syntax or validation errors saved_rows Returns the number of rows actually saved in the repository. Return Values This call returns the number of rows saved and failed as output parameters.