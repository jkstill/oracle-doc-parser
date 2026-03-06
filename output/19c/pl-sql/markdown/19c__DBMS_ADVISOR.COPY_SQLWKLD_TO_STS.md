---
id: 19c__DBMS_ADVISOR.COPY_SQLWKLD_TO_STS
name: DBMS_ADVISOR.COPY_SQLWKLD_TO_STS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.COPY_SQLWKLD_TO_STS

This procedure copies the contents of a SQL workload object to a SQL tuning set.

## Syntax

```sql
DBMS_ADVISOR.COPY_SQLWKLD_TO_STS (
   workload_name         IN VARCHAR2,
   sts_name              IN VARCHAR2,
   import_mode           IN VARCHAR2 := 'NEW');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| workload_name | VARCHAR2 | IN | The SQL Workload object name to copy. |
| sts_name | VARCHAR2 | IN | The SQL tuning set name into which the SQL Workload object will be copied. |
| import_mode | VARCHAR2 | IN | Specifies the handling of the target SQL tuning set. Possible values are: APPEND Causes SQL Workload data to be appended to the target SQL tuning set. NEW Indicates the SQL tuning set can only contain the copied contents. If the SQL tuning set exists and has data, an error will be reported. REPLACE Causes any existing data in the target SQL tuning set to be purged prior to the workload copy. In all cases, if the specified SQL tuning set does not exist, it will be created. |

## Usage Notes

Syntax To use this procedure, the caller must have privileges to create and modify a SQL tuning set. DBMS_ADVISOR.COPY_SQLWKLD_TO_STS ( workload_name IN VARCHAR2, sts_name IN VARCHAR2, import_mode IN VARCHAR2 := 'NEW'); Parameters Table 16-6 COPY_SQLWKLD_TO_STS Procedure Parameter Parameter Description workload_name The SQL Workload object name to copy. sts_name The SQL tuning set name into which the SQL Workload object will be copied. import_mode Specifies the handling of the target SQL tuning set. Possible values are: APPEND Causes SQL Workload data to be appended to the target SQL tuning set. NEW Indicates the SQL tuning set can only contain the copied contents. If the SQL tuning set exists and has data, an error will be reported. REPLACE Causes any existing data in the target SQL tuning set to be purged prior to the workload copy. In all cases, if the specified SQL tuning set does not exist, it will be created. Usage Notes To use this procedure, the caller must have privileges to create and modify a SQL tuning set. Examples BEGIN DBMS_ADVISOR.COPY_SQLWKLD_TO_STS('MY_OLD_WORKLOAD', 'MY_NEW_STS', 'NEW'); END; /