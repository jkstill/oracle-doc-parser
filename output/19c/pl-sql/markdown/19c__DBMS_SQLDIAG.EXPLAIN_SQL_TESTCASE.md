---
id: 19c__DBMS_SQLDIAG.EXPLAIN_SQL_TESTCASE
name: DBMS_SQLDIAG.EXPLAIN_SQL_TESTCASE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.EXPLAIN_SQL_TESTCASE

This procedure explains a SQL test case.

## Syntax

```sql
DBMS_SQLDIAG.EXPLAIN_SQL_TESTCASE (
    sqlTestCase        IN   CLOB)
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sqlTestCase | CLOB) | IN | XML document describing the SQL test case |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_SQLDIAG.EXPLAIN_SQL_TESTCASE ( sqlTestCase IN CLOB) RETURN CLOB; Parameters Table 165-19 EXPLAIN_SQL_TESTCASE Function Parameters Parameter Description sqlTestCase XML document describing the SQL test case