---
id: 19c__DBMS_MGD_ID_UTL.GET_JAVA_LOGGING_LEVEL
name: DBMS_MGD_ID_UTL.GET_JAVA_LOGGING_LEVEL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGD_ID_UTL
tags: [dbms_mgd_id_utl]
source_file: DBMS_MGD_ID_UTL.html
---

# DBMS_MGD_ID_UTL.GET_JAVA_LOGGING_LEVEL

This function returns an integer representing the current trace logging level.

## Syntax

```sql
DBMS_MGD_ID_UTL.GET_JAVA_LOGGING_LEVEL 
 RETURN INTEGER;
```

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_MGD_ID_UTL.GET_JAVA_LOGGING_LEVEL RETURN INTEGER; Usage Notes The return value is the integer value denoting the current Java logging level. Examples The following example gets the Java logging level. --Contents of getjavalogginglevel.sql DECLARE loglevel NUMBER; BEGIN DBMS_MGD_ID_UTL.set_java_logging_level(DBMS_MGD_ID_UTL.LOGGING_LEVEL_OFF); loglevel := DBMS_MGD_ID_UTL.get_java_logging_level(); dbms_output.put_line('Java logging level = ' ||loglevel); END; / SHOW ERRORS; SQL> @getjavalogginglevel.sql . . . Java logging level = 0 PL/SQL procedure successfully completed. . . .