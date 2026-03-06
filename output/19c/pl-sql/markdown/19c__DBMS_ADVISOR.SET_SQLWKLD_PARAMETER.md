---
id: 19c__DBMS_ADVISOR.SET_SQLWKLD_PARAMETER
name: DBMS_ADVISOR.SET_SQLWKLD_PARAMETER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.SET_SQLWKLD_PARAMETER

This procedure modifies a user parameter within a SQL Workload object or SQL Workload object template.

## Syntax

```sql
DBMS_ADVISOR.SET_SQLWKLD_PARAMETER (
   workload_name        IN VARCHAR2,
   parameter            IN VARCHAR2,
   value                IN VARCHAR2);

DBMS_ADVISOR.SET_SQLWKLD_PARAMETER (
   workload_name        IN VARCHAR2,
   parameter            IN VARCHAR2,
   value                IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| workload_name | VARCHAR2 | IN | The SQL Workload object name that uniquely identifies an existing workload. |
| parameter | VARCHAR2 | IN | The name of the data parameter to be modified. Parameter names are not case sensitive. |
| value | VARCHAR2) | IN | The value of the specified parameter. The value can be specified as a string or a number. If the value is DBMS_ADVISOR.DEFAULT , the value will be reset to the default value. |

## Usage Notes

A user parameter is a simple variable that stores various attributes that affect workload collection, tuning decisions and reporting. Note: This procedure is deprecated starting in Oracle Database 11 g . Note: This procedure is deprecated starting in Oracle Database 11 g . Syntax DBMS_ADVISOR.SET_SQLWKLD_PARAMETER ( workload_name IN VARCHAR2, parameter IN VARCHAR2, value IN VARCHAR2); DBMS_ADVISOR.SET_SQLWKLD_PARAMETER ( workload_name IN VARCHAR2, parameter IN VARCHAR2, value IN NUMBER); Parameters Table 16-33 SET_SQLWKLD_PARAMETER Procedure Parameters Parameter Description workload_name The SQL Workload object name that uniquely identifies an existing workload. parameter The name of the data parameter to be modified. Parameter names are not case sensitive. value The value of the specified parameter. The value can be specified as a string or a number. If the value is DBMS_ADVISOR.DEFAULT , the value will be reset to the default value. Usage Notes A parameter will only affect operations that modify the workload collection. Therefore, parameters should be set prior to importing or adding new SQL statements to a workload. If a parameter is set after data has been placed in a workload object, it will have no effect on the existing data.