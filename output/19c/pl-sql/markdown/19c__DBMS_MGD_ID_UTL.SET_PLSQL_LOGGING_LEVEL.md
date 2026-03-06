---
id: 19c__DBMS_MGD_ID_UTL.SET_PLSQL_LOGGING_LEVEL
name: DBMS_MGD_ID_UTL.SET_PLSQL_LOGGING_LEVEL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGD_ID_UTL
tags: [dbms_mgd_id_utl]
source_file: DBMS_MGD_ID_UTL.html
---

# DBMS_MGD_ID_UTL.SET_PLSQL_LOGGING_LEVEL

This procedure sets the PL/SQL trace logging level.

## Syntax

```sql
DBMS_MGD_ID_UTL.SET_PLSQL_LOGGING_LEVEL (
   level IN INTEGER);

PRAGMA restrict_references(set_plsql_logging_level, WNDS);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| level | INTEGER) | IN | Logging level. The PL/SQL logging level can be one of the following values in descending order: LOGGING_LEVEL_OFF CONSTANT INTEGER := 0 LOGGING_LEVEL_SEVERE CONSTANT INTEGER := 1 LOGGING_LEVEL_WARNING CONSTANT INTEGER := 2 LOGGING_LEVEL_INFO CONSTANT INTEGER := 3 LOGGING_LEVEL_FINE CONSTANT INTEGER := 4 LOGGING_LEVEL_FINER CONSTANT INTEGER := 5 LOGGING_LEVEL_FINEST CONSTANT INTEGER := 6 LOGGING_LEVEL_ALL CONSTANT INTEGER := 7 |

## Usage Notes

Syntax DBMS_MGD_ID_UTL.SET_PLSQL_LOGGING_LEVEL ( level IN INTEGER); PRAGMA restrict_references(set_plsql_logging_level, WNDS); Parameters Table 109-17 SET_PLSQL_LOGGING_LEVEL Procedure Parameters Parameter Description level Logging level. The PL/SQL logging level can be one of the following values in descending order: LOGGING_LEVEL_OFF CONSTANT INTEGER := 0 LOGGING_LEVEL_SEVERE CONSTANT INTEGER := 1 LOGGING_LEVEL_WARNING CONSTANT INTEGER := 2 LOGGING_LEVEL_INFO CONSTANT INTEGER := 3 LOGGING_LEVEL_FINE CONSTANT INTEGER := 4 LOGGING_LEVEL_FINER CONSTANT INTEGER := 5 LOGGING_LEVEL_FINEST CONSTANT INTEGER := 6 LOGGING_LEVEL_ALL CONSTANT INTEGER := 7 Examples See the GET_PLSQL_LOGGING_LEVEL Function for an example.