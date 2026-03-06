---
id: 19c__DBMS_ADVISOR.SET_DEFAULT_SQLWKLD_PARAMETER
name: DBMS_ADVISOR.SET_DEFAULT_SQLWKLD_PARAMETER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.SET_DEFAULT_SQLWKLD_PARAMETER

This procedure modifies the default value for a user parameter within a SQL Workload object or SQL Workload object template.

## Syntax

```sql
DBMS_ADVISOR.SET_DEFAULT_SQLWKLD_PARAMETER (
   parameter            IN VARCHAR2,
   value                IN VARCHAR2);

DBMS_ADVISOR.SET_DEFAULT_SQLWKLD_PARAMETER (
   parameter            IN VARCHAR2,
   value                IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| parameter | VARCHAR2 | IN | The name of the data parameter to be modified. Parameter names are not case sensitive. Parameter names are unique to the workload object type, but not necessarily unique to all workload object types. Various object types may use the same parameter name for different purposes. |
| value | VARCHAR2) | IN | The value of the specified parameter. The value can be specified as a string or a number. If the value is DBMS_ADVISOR.DEFAULT , the value will be reset to the default value. |

## Usage Notes

A user parameter is a simple variable that stores various attributes that affect workload collection, tuning decisions and reporting. When a default value is changed for a parameter, workload objects will inherit the new value when they are created. Note: This procedure is deprecated starting in Oracle Database 11 g . Note: This procedure is deprecated starting in Oracle Database 11 g . Syntax DBMS_ADVISOR.SET_DEFAULT_SQLWKLD_PARAMETER ( parameter IN VARCHAR2, value IN VARCHAR2); DBMS_ADVISOR.SET_DEFAULT_SQLWKLD_PARAMETER ( parameter IN VARCHAR2, value IN NUMBER); Parameters Table 16-31 SET_DEFAULT_SQLWKLD_PARAMETER Procedure Parameters Parameter Description parameter The name of the data parameter to be modified. Parameter names are not case sensitive. Parameter names are unique to the workload object type, but not necessarily unique to all workload object types. Various object types may use the same parameter name for different purposes. value The value of the specified parameter. The value can be specified as a string or a number. If the value is DBMS_ADVISOR.DEFAULT , the value will be reset to the default value. Usage Notes A parameter will only affect operations that modify the workload collection. Therefore, parameters should be set prior to importing or adding new SQL statements to a workload. If a parameter is set after data has been placed in a workload object, it will have no effect on the existing data.