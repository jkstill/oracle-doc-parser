---
id: 19c__DBMS_DATAPUMP.METADATA_FILTER
name: DBMS_DATAPUMP.METADATA_FILTER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATAPUMP
tags: [dbms_datapump]
source_file: DBMS_DATAPUMP.html
---

# DBMS_DATAPUMP.METADATA_FILTER

This procedure provides filters that allow you to restrict the items that are included in a job.

## Syntax

```sql
DBMS_DATAPUMP.METADATA_FILTER(
   handle       IN NUMBER,
   name         IN VARCHAR2,
   value        IN VARCHAR2,
   object_path  IN VARCHAR2 DEFAULT NULL);

DBMS_DATAPUMP.METADATA_FILTER(
   handle       IN NUMBER,
   name         IN VARCHAR2,
   value        IN CLOB,
   object_path  IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER | IN | The handle returned from the OPEN function |
| name | VARCHAR2 | IN | The name of the filter. See Table 49-15 for descriptions of the available filters. |
| value | VARCHAR2 | IN | The value of the filter |
| object_path | VARCHAR2 | IN | The object path to which the filter applies. If the default is used, the filter applies to all applicable objects. Lists of the object paths supported for each mode are contained in the catalog views for DATABASE_EXPORT_OBJECTS , SCHEMA_EXPORT_OBJECTS , and TABLE_EXPORT_OBJECTS . (Note that the TABLE_EXPORT_OBJECTS view is applicable to both Table and Tablespace mode because their object paths are the same.) For an import operation, object paths reference the mode used to create the dump file rather than the mode being used for the import. |

## Usage Notes

Syntax DBMS_DATAPUMP.METADATA_FILTER( handle IN NUMBER, name IN VARCHAR2, value IN VARCHAR2, object_path IN VARCHAR2 DEFAULT NULL); DBMS_DATAPUMP.METADATA_FILTER( handle IN NUMBER, name IN VARCHAR2, value IN CLOB, object_path IN VARCHAR2 DEFAULT NULL); Parameters Table 49-14 METADATA_FILTER Procedure Parameters Parameter Description handle The handle returned from the OPEN function name The name of the filter. See Table 49-15 for descriptions of the available filters. value The value of the filter object_path The object path to which the filter applies. If the default is used, the filter applies to all applicable objects. Lists of the object paths supported for each mode are contained in the catalog views for DATABASE_EXPORT_OBJECTS , SCHEMA_EXPORT_OBJECTS , and TABLE_EXPORT_OBJECTS . (Note that the TABLE_EXPORT_OBJECTS view is applicable to both Table and Tablespace mode because their object paths are the same.) For an import operation, object paths reference the mode used to create the dump file rather than the mode being used for the import. Table 49-15 describes the name, the object type, and the meaning of the filters available with the METADATA_FILTER procedure. The datatype for all the filters is a text expression. All operations support all filters. Table 49-15 Filters Provided by METADATA_FILTER Procedure Name Object Type Meaning NAME_EXPR NAME_LIST Named objects Defines which object names are included in the job. You use the object type parameter to limit the filter to a particular object type. For Table mode, identifies which tables are to be processed. SCHEMA_EXPR SCHEMA_LIST Schema objects Restricts the job to objects whose owning schema name is satisfied by the expression. For Table mode, only a single SCHEMA_EXPR filter is supported. If specified, it must only specify a single schema (for example, 'IN (''SCOTT'')') . For Schema mode, identifies which users are to be processed. TABLESPACE_EXPR TABLESPACE_LIST TABLE, CLUSTER, INDEX, ROLLBACK_SEGMENT Restricts the job to objects stored in a tablespace whose name is satisfied by the expression. For Tablespace mode, identifies which tablespaces are to be processed. If a partition of an object is stored in the tablespace, the entire object is added to the job. For Transportable mode, identifies which tablespaces are to be processed. If a table has a single partition in the tablespace set, all partitions must be in the tablespace set. An index is not included within the tablespace set unless all of its partitions are in the tablespace set. A domain index is not included in the tablespace set unless all of its secondary objects are included in the tablespace set. INCLUDE_PATH_EXPR INCLUDE_PATH_LIST EXCLUDE_PATH_EXPR EXCLUDE_PATH_LIST All Defines which object paths are included in, or excluded from, the job. You use these filters to select only certain object types from the database or dump file set. Objects of paths satisfying the condition are included ( INCLUDE_PATH_* ) or excluded ( EXCLUDE_PATH_* ) from the operation. The object_path parameter is not supported for these filters. EXCLUDE_TABLES TABLE_EXPORT Specifies that no tables are to be exported. VIEWS_AS_TABLES TABLE_EXPORT A comma-separated list of views to be exported as tables: [schema_name.]view_name[:table_name] The filter can be called multiple times with multiple values and all values get added to a list. All views on the list are exported as tables. Exceptions INVALID_HANDLE . The specified handle is not attached to a Data Pump job. INVALID_ARGVAL . This exception can indicate any of the following conditions: An object_path was specified for an INCLUDE_PATH_EXPR or EXCLUDE_PATH_EXPR filter. The specified object_path is not supported for the current mode. The SCHEMA_EXPR filter specified multiple schemas for a Table mode job. INVALID_STATE . The user called the METADATA_FILTER procedure after the job left the defining state. INCONSISTENT_ARGS . The filter value is of the wrong datatype or is missing. SUCCESS_WITH_INFO . The procedure succeeded but further information is available through the GET_STATUS procedure. NO_SUCH_JOB . The specified job does not exist. Usage Notes Metadata filters identify a set of objects to be included or excluded from a Data Pump operation. Except for EXCLUDE_PATH_EXPR and INCLUDE_PATH_EXPR , dependent objects of an identified object will be processed along with the identified object. For example, if an index is identified for inclusion by a filter, grants upon that index will also be included by the filter. Likewise, if a table is excluded by a filter, then indexes, constraints, grants and triggers upon the table will also be excluded by the filter. Two versions of each filter are supported: SQL expression and List. The SQL expression version of the filters offer maximum flexibility for identifying objects (for example the use of LIKE to support use of wild cards). The names of the expression filters are as follows: NAME_EXPR SCHEMA_EXPR TABLESPACE_EXPR INCLUDE_PATH_EXPR EXCLUDE_PATH_EXPR The list version of the filters allow maximum validation of the filter. An error will be reported if one of the elements in the filter is not found within the source database (for Export and network-based jobs) or is not found within the dump file (for file-based Import and SQLFILE jobs). The names of the list filters are as follows: NAME_LIST SCHEMA_LIST TABLESPACE_LIST INCLUDE_PATH_LIST EXCLUDE_PATH_LIST Filters allow a user to restrict the items that are included in a job. For example, a user could request a full export, but without Package Specifications or Package Bodies. If multiple filters are specified for a object type, they are implicitly 'ANDed' together (that is, objects participating in the job must pass all of the filters applied to their object types). The same filter name can be specified multiple times within a job. For example, specifying NAME_EXPR as '!=''EMP''' and NAME_EXPR as '!=''DEPT''' on a Table mode export would produce a file set containing all of the tables except for EMP and DEPT .