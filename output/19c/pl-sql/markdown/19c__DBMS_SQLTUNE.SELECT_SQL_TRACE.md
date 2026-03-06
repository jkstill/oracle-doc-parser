---
id: 19c__DBMS_SQLTUNE.SELECT_SQL_TRACE
name: DBMS_SQLTUNE.SELECT_SQL_TRACE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.SELECT_SQL_TRACE

This table function reads the content of one or more trace files and returns the SQL statements it finds in the format of sqlset_row .

## Syntax

```sql
DBMS_SQLTUNE.SELECT_SQL_TRACE (
  directory              IN VARCHAR2,
  file_name              IN VARCHAR2 := NULL,
  mapping_table_name     IN VARCHAR2 := NULL,
  mapping_table_owner    IN VARCHAR2 := NULL,,
  select_mode            IN POSITIVE := SINGLE_EXECUTION,
  options                IN BINARY_INTEGER := LIMITED_COMMAND_TYPE,
  pattern_start          IN VARCHAR2 := NULL,
  pattern_end            IN VARCHAR2 := NULL,
  result_limit           IN POSITIVE := NULL)
 RETURN sys.sqlset PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| directory | VARCHAR2 | IN | Defines the directory object containing the trace files. This field is mandatory. |
| file_name | VARCHAR2 | IN | Specifies all or part of the name of the trace files. If NULL , then the function uses the current or most recent file in the specified location or path. '%' wildcards are supported for matching trace file names. |
| mapping_table_name | VARCHAR2 | IN | Specifies the mapping table name. Note that the mapping table name is case insensitive. If the mapping table name is NULL , then the function uses the mappings in the current database. |
| mapping_table_owner | VARCHAR2 | IN | Specifies the mapping table owner. If it is NULL , then the function uses the current user. |
| select_mode | POSITIVE | IN | Specifies the mode for selecting SQL from the trace. Possible values are: SINGLE_EXECUTION — Returns one execution of a SQL. This is the default. ALL_EXECUTIONS — Returns all executions. |
| options | BINARY_INTEGER | IN | Specifies which types of SQL statements are returned. LIMITED_COMMAND_TYPE — Returns the SQL statements with the command types CREATE , INSERT , SELECT , UPDATE , DELETE , and MERGE . This value is the default. ALL_COMMAND_TYPE — Returns the SQL statements with all command types. |
| pattern_start | VARCHAR2 | IN | Specifies the delimiting pattern of the trace file sections to consider. CURRENTLY INOPERABLE. |
| pattern_end | VARCHAR2 | IN | Specifies the closing delimiting pattern of the trace file sections to process. CURRENTLY INOPERABLE. |
| result_limit | POSITIVE | IN | Specifies the top SQL from the filtered source. Default to MAXSB4 if NULL . |

**Returns:** `sys.sqlset`

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.SELECT_SQL_TRACE ( directory IN VARCHAR2, file_name IN VARCHAR2 := NULL, mapping_table_name IN VARCHAR2 := NULL, mapping_table_owner IN VARCHAR2 := NULL,, select_mode IN POSITIVE := SINGLE_EXECUTION, options IN BINARY_INTEGER := LIMITED_COMMAND_TYPE, pattern_start IN VARCHAR2 := NULL, pattern_end IN VARCHAR2 := NULL, result_limit IN POSITIVE := NULL) RETURN sys.sqlset PIPELINED; Parameters Table 169-42 SELECT_SQL_TRACE Function Parameters Parameter Description directory Defines the directory object containing the trace files. This field is mandatory. file_name Specifies all or part of the name of the trace files. If NULL , then the function uses the current or most recent file in the specified location or path. '%' wildcards are supported for matching trace file names. mapping_table_name Specifies the mapping table name. Note that the mapping table name is case insensitive. If the mapping table name is NULL , then the function uses the mappings in the current database. mapping_table_owner Specifies the mapping table owner. If it is NULL , then the function uses the current user. select_mode Specifies the mode for selecting SQL from the trace. Possible values are: SINGLE_EXECUTION — Returns one execution of a SQL. This is the default. ALL_EXECUTIONS — Returns all executions. options Specifies which types of SQL statements are returned. LIMITED_COMMAND_TYPE — Returns the SQL statements with the command types CREATE , INSERT , SELECT , UPDATE , DELETE , and MERGE . This value is the default. ALL_COMMAND_TYPE — Returns the SQL statements with all command types. pattern_start Specifies the delimiting pattern of the trace file sections to consider. CURRENTLY INOPERABLE. pattern_end Specifies the closing delimiting pattern of the trace file sections to process. CURRENTLY INOPERABLE. result_limit Specifies the top SQL from the filtered source. Default to MAXSB4 if NULL . Return Values This function returns a SQLSET_ROW object.