---
id: 19c__DBMS_ADVISOR.IMPORT_SQLWKLD_STS
name: DBMS_ADVISOR.IMPORT_SQLWKLD_STS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.IMPORT_SQLWKLD_STS

This procedure loads a SQL workload from an existing SQL tuning set. A SQL tuning set is typically created from the server workload repository using various time and data filters.

## Syntax

```sql
DBMS_ADVISOR.IMPORT_SQLWKLD_STS (
   workload_name         IN VARCHAR2,
   sts_name              IN VARCHAR2,
   import_mode           IN VARCHAR2 := 'NEW',
   priority              IN NUMBER := 2,
   saved_rows            OUT NUMBER,
   failed_rows           OUT NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| workload_name | VARCHAR2 | IN | The workload object name that uniquely identifies an existing workload. |
| sts_owner |  |  | The optional owner of the SQL tuning set. |
| sts_name | VARCHAR2 | IN | The name of an existing SQL tuning set workload from which the data will be imported. If the sts_owner value is not provided, the owner will default to the current user. |
| import_mode | VARCHAR2 | IN | Specifies the action to be taken when storing the workload. Possible values are: APPEND Indicates that the collected workload will be added to any existing workload in the task. NEW Indicates that the collected workload will be the exclusive workload for the task. If an existing workload is found, an exception will be thrown. REPLACE Indicates the collected workload will be the exclusive workload for the task. If an existing workload is found, it will be deleted prior to saving the new workload. The default value is NEW . |
| priority | NUMBER | IN | Specifies the application priority for each statement that is saved in the workload object. The value must be one of the following: 1- HIGH , 2- MEDIUM , or 3- LOW . The default value is 2. |
| saved_rows | NUMBER | OUT | Returns the number of rows actually saved in the repository. |
| failed_rows | NUMBER) | OUT | Returns the number of rows that were not saved due to syntax or validation errors. |

## Usage Notes

Note: This procedure is deprecated starting in Oracle Database 11 g . Note: This procedure is deprecated starting in Oracle Database 11 g . Syntax DBMS_ADVISOR.IMPORT_SQLWKLD_STS ( workload_name IN VARCHAR2, sts_name IN VARCHAR2, import_mode IN VARCHAR2 := 'NEW', priority IN NUMBER := 2, saved_rows OUT NUMBER, failed_rows OUT NUMBER); DBMS_ADVISOR.IMPORT_SQLWKLD_STS ( workload_name IN VARCHAR2, sts_owner IN VARCHAR2, sts_name IN VARCHAR2, import_mode IN VARCHAR2 := 'NEW', priority IN NUMBER := 2, saved_rows OUT NUMBER, failed_rows OUT NUMBER); Parameters Table 16-23 IMPORT_SQLWKLD_STS Procedure Parameters Parameter Description workload_name The workload object name that uniquely identifies an existing workload. sts_owner The optional owner of the SQL tuning set. sts_name The name of an existing SQL tuning set workload from which the data will be imported. If the sts_owner value is not provided, the owner will default to the current user. import_mode Specifies the action to be taken when storing the workload. Possible values are: APPEND Indicates that the collected workload will be added to any existing workload in the task. NEW Indicates that the collected workload will be the exclusive workload for the task. If an existing workload is found, an exception will be thrown. REPLACE Indicates the collected workload will be the exclusive workload for the task. If an existing workload is found, it will be deleted prior to saving the new workload. The default value is NEW . priority Specifies the application priority for each statement that is saved in the workload object. The value must be one of the following: 1- HIGH , 2- MEDIUM , or 3- LOW . The default value is 2. saved_rows Returns the number of rows actually saved in the repository. failed_rows Returns the number of rows that were not saved due to syntax or validation errors. Return Values This call returns the number of rows saved and failed as output parameters.