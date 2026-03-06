---
id: 19c__DBMS_SQLDIAG.INCIDENTID_2_SQL
name: DBMS_SQLDIAG.INCIDENTID_2_SQL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.INCIDENTID_2_SQL

This procedure initializes a sql_setrow from an incident ID.

## Syntax

```sql
DBMS_SQLDIAG.INCIDENTID_2_SQL (
    incident_id   IN     VARCHAR2,
    sql_stmt      OUT    SQLSET_ROW,
    problem_type  OUT    NUMBER, 
    err_code      OUT    BINARY_INTEGER,
    err_mesg      OUT    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| incident_id | VARCHAR2 | IN | Identifier of the incident |
| sql_stmt | SQLSET_ROW | OUT | Resulting SQL |
| problem_type | NUMBER | OUT | Tentative type of SQL problem (currently among PROBLEM_TYPE_COMPILATION_ERROR and PROBLEM_TYPE_EXECUTION_ERROR ) |
| err_code | BINARY_INTEGER | OUT | Error code if any otherwise it is set to NULL |
| err_msg |  |  | Error message if any otherwise it is set to NULL |

## Usage Notes

Syntax DBMS_SQLDIAG.INCIDENTID_2_SQL ( incident_id IN VARCHAR2, sql_stmt OUT SQLSET_ROW, problem_type OUT NUMBER, err_code OUT BINARY_INTEGER, err_mesg OUT VARCHAR2); Parameters Table 165-26 INCIDENTID_2_SQL Procedure Parameters Parameter Description incident_id Identifier of the incident sql_stmt Resulting SQL problem_type Tentative type of SQL problem (currently among PROBLEM_TYPE_COMPILATION_ERROR and PROBLEM_TYPE_EXECUTION_ERROR ) err_code Error code if any otherwise it is set to NULL err_msg Error message if any otherwise it is set to NULL