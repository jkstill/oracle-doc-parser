---
id: 19c__DBMS_ADVISOR.RESET_SQLWKLD
name: DBMS_ADVISOR.RESET_SQLWKLD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.RESET_SQLWKLD

This procedure resets a workload to its initial starting point.

## Syntax

```sql
DBMS_ADVISOR.RESET_SQLWKLD (
   workload_name        IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| workload_name | VARCHAR2) | IN | The SQL Workload object name that uniquely identifies an existing workload. |

## Usage Notes

Resetting the workload has the effect of removing all journal and log messages, and recalculating necessary volatility and usage statistics. Note: This procedure is deprecated starting in Oracle Database 11 g . Note: This procedure is deprecated starting in Oracle Database 11 g . Syntax DBMS_ADVISOR.RESET_SQLWKLD ( workload_name IN VARCHAR2); Parameters Table 16-29 RESET_SQLWKLD Procedure Parameters Parameter Description workload_name The SQL Workload object name that uniquely identifies an existing workload. Usage Notes RESET_SQLWKLD should be executed after any workload adjustments such as adding or removing SQL statements.