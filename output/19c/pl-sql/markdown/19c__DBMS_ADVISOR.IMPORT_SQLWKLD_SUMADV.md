---
id: 19c__DBMS_ADVISOR.IMPORT_SQLWKLD_SUMADV
name: DBMS_ADVISOR.IMPORT_SQLWKLD_SUMADV
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.IMPORT_SQLWKLD_SUMADV

This procedure collects a SQL workload from a Summary Advisor workload.

## Syntax

```sql
DBMS_ADVISOR.IMPORT_SQLWKLD_SUMADV (
   workload_name         IN VARCHAR2,
   import_mode           IN VARCHAR2 := 'NEW',
   priority              IN NUMBER := 2,
   sumadv_id             IN NUMBER,
   saved_rows            OUT NUMBER,
   failed_rows           OUT NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| workload_name | VARCHAR2 | IN | The workload object name that uniquely identifies an existing workload. |
| import_mode | VARCHAR2 | IN | Specifies the action to be taken when storing the workload. Possible values are: APPEND Indicates that the collected workload will be added to any existing workload in the task. NEW Indicates that the collected workload will be the exclusive workload for the task. If an existing workload is found, an exception will be thrown. REPLACE Indicates the collected workload will be the exclusive workload for the task. If an existing workload is found, it will be deleted prior to saving the new workload. The default value is NEW . |
| priority | NUMBER | IN | Specifies the default application priority for each statement that is saved in the workload object. If a Summary Advisor workload statement contains a priority of zero, the default priority will be applied. If the workload statement contains a valid priority, then the Summary Advisor priority will be converted to a comparable SQL Access Advisor priority. The value must be one of the following: 1- HIGH , 2- MEDIUM , or 3- LOW . |
| sumadv_id | NUMBER | IN | Specifies the Summary Advisor workload identifier number. |
| saved_rows | NUMBER | OUT | Returns the number of rows actually saved in the repository. |
| failed_rows | NUMBER) | OUT | Returns the number of rows that were not saved due to syntax or validation errors. |

## Usage Notes

This procedure is intended to assist Oracle9 i Database Summary Advisor users in the migration to SQL Access Advisor. Note: This procedure is deprecated starting in Oracle Database 11 g . Note: This procedure is deprecated starting in Oracle Database 11 g . Syntax DBMS_ADVISOR.IMPORT_SQLWKLD_SUMADV ( workload_name IN VARCHAR2, import_mode IN VARCHAR2 := 'NEW', priority IN NUMBER := 2, sumadv_id IN NUMBER, saved_rows OUT NUMBER, failed_rows OUT NUMBER); Parameters Table 16-24 IMPORT_SQLWKLD_SUMADV Procedure Parameters Parameter Description workload_name The workload object name that uniquely identifies an existing workload. import_mode Specifies the action to be taken when storing the workload. Possible values are: APPEND Indicates that the collected workload will be added to any existing workload in the task. NEW Indicates that the collected workload will be the exclusive workload for the task. If an existing workload is found, an exception will be thrown. REPLACE Indicates the collected workload will be the exclusive workload for the task. If an existing workload is found, it will be deleted prior to saving the new workload. The default value is NEW . priority Specifies the default application priority for each statement that is saved in the workload object. If a Summary Advisor workload statement contains a priority of zero, the default priority will be applied. If the workload statement contains a valid priority, then the Summary Advisor priority will be converted to a comparable SQL Access Advisor priority. The value must be one of the following: 1- HIGH , 2- MEDIUM , or 3- LOW . sumadv_id Specifies the Summary Advisor workload identifier number. saved_rows Returns the number of rows actually saved in the repository. failed_rows Returns the number of rows that were not saved due to syntax or validation errors. Return Values This call returns the number of rows saved and failed as output parameters.