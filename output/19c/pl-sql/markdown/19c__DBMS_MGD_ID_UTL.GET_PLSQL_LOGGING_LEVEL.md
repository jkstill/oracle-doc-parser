---
id: 19c__DBMS_MGD_ID_UTL.GET_PLSQL_LOGGING_LEVEL
name: DBMS_MGD_ID_UTL.GET_PLSQL_LOGGING_LEVEL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGD_ID_UTL
tags: [dbms_mgd_id_utl]
source_file: DBMS_MGD_ID_UTL.html
---

# DBMS_MGD_ID_UTL.GET_PLSQL_LOGGING_LEVEL

This function returns an integer representing the current PL/SQL trace logging level.

## Syntax

```sql
DBMS_MGD_ID_UTL.GET_PLSQL_LOGGING_LEVEL 
 RETURN INTEGER;

PRAGMA restrict_references(get_plsql_logging_level, WNDS);
```

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_MGD_ID_UTL.GET_PLSQL_LOGGING_LEVEL RETURN INTEGER; PRAGMA restrict_references(get_plsql_logging_level, WNDS); Usage Notes The return value is the integer value denoting the current PL/SQL logging level. Examples The following example gets the PL/SQL logging level. --Contents of getplsqllogginglevel.sql DECLARE loglevel NUMBER; BEGIN DBMS_MGD_ID_UTL.set_plsql_logging_level(0); loglevel := DBMS_MGD_ID_UTL.get_plsql_logging_level(); dbms_output.put_line('PL/SQL logging level = ' ||loglevel); END; / SHOW ERRORS; SQL> @getplsqllogginglevel.sql . . . PL/SQL logging level = 0 PL/SQL procedure successfully completed. . . .