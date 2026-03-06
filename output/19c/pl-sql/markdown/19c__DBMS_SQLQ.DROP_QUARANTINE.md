---
id: 19c__DBMS_SQLQ.DROP_QUARANTINE
name: DBMS_SQLQ.DROP_QUARANTINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLQ
tags: [dbms_sqlq]
source_file: DBMS_SQLQ.html
---

# DBMS_SQLQ.DROP_QUARANTINE

This procedure deletes a quarantine configuration.

## Syntax

```sql
DBMS_SQLQ.DROP_QUARANTINE(quarantine_name IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| quarantine_name | VARCHAR2) | IN | Name of the quarantine configuration to delete. |

## Usage Notes

Syntax DBMS_SQLQ.DROP_QUARANTINE(quarantine_name IN VARCHAR2); Parameters Table 167-6 DROP_QUARANTINE Procedure Parameters Parameter Description quarantine_name Name of the quarantine configuration to delete. Examples The following example deletes the quarantine configuration having the name SQL_QUARANTINE_3z0mwuq3aqsm8cfe7a0e4 . BEGIN DBMS_SQLQ.DROP_QUARANTINE('SQL_QUARANTINE_3z0mwuq3aqsm8cfe7a0e4'); END; /