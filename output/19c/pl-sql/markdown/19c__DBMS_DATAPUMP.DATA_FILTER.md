---
id: 19c__DBMS_DATAPUMP.DATA_FILTER
name: DBMS_DATAPUMP.DATA_FILTER
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATAPUMP
tags: [dbms_datapump]
source_file: DBMS_DATAPUMP.html
---

# DBMS_DATAPUMP.DATA_FILTER

This procedure specifies restrictions on the rows that are to be retrieved.

## Syntax

```sql
DBMS_DATAPUMP.DATA_FILTER (
   handle      IN NUMBER,
   name        IN VARCHAR2,
   value       IN NUMBER,
   table_name  IN VARCHAR2 DEFAULT NULL,
   schema_name IN VARCHAR2 DEFAULT NULL);

DBMS_DATAPUMP.DATA_FILTER(
   handle      IN NUMBER,
   name        IN VARCHAR2,
   value       IN VARCHAR2,
   table_name  IN VARCHAR2 DEFAULT NULL,
   schema_name IN VARCHAR2 DEFAULT NULL);

DBMS_DATAPUMP.DATA_FILTER(
   handle      IN NUMBER,
   name        IN VARCHAR2,
   value       IN CLOB,
   table_name  IN VARCHAR2 DEFAULT NULL,
   schema_name IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER | IN | The handle that is returned from the OPEN function |
| name | VARCHAR2 | IN | The name of the filter |
| value | NUMBER | IN | The value of the filter |
| table_name | VARCHAR2 | IN | The name of the table on which the data filter is applied. If no table name is supplied, the filter applies to all tables in the job. |
| schema_name | VARCHAR2 | IN | The name of the schema that owns the table on which the filter is applied. If no schema name is specified, the filter applies to all schemas in the job. If you supply a schema name you must also supply a table name. |

## Usage Notes

Syntax DBMS_DATAPUMP.DATA_FILTER ( handle IN NUMBER, name IN VARCHAR2, value IN NUMBER, table_name IN VARCHAR2 DEFAULT NULL, schema_name IN VARCHAR2 DEFAULT NULL); DBMS_DATAPUMP.DATA_FILTER( handle IN NUMBER, name IN VARCHAR2, value IN VARCHAR2, table_name IN VARCHAR2 DEFAULT NULL, schema_name IN VARCHAR2 DEFAULT NULL); DBMS_DATAPUMP.DATA_FILTER( handle IN NUMBER, name IN VARCHAR2, value IN CLOB, table_name IN VARCHAR2 DEFAULT NULL, schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 49-5 DATA_FILTER Procedure Parameters Parameter Description handle The handle that is returned from the OPEN function name The name of the filter value The value of the filter table_name The name of the table on which the data filter is applied. If no table name is supplied, the filter applies to all tables in the job. schema_name The name of the schema that owns the table on which the filter is applied. If no schema name is specified, the filter applies to all schemas in the job. If you supply a schema name you must also supply a table name. Exceptions INVALID_ARGVAL . There can be several reasons for this message: A bad filter name is specified The mode is TRANSPORTABLE , which does not support data filters The specified table does not exist The filter has already been set for the specified values of schema_name and table_name INVALID_STATE . The user called DATA_FILTER when the job was not in the Defining state. INCONSISTENT_ARGS . The value parameter is missing or its datatype does not match the filter name. Or a schema name was supplied, but not a table name. PRIVILEGE_ERROR . A schema name was supplied, but the user did not have the DATAPUMP_EXP_FULL_DATABASE or DATAPUMP_IMP_FULL_DATABASE role. SUCCESS_WITH_INFO . The procedure succeeded, but further information is available through the GET_STATUS procedure. NO_SUCH_JOB . The specified job does not exist. Usage Notes Each data filter can only appear once in each table (for example, you cannot supply multiple SUBQUERY filters to a table) or once in each job. If different filters using the same name are applied to both a particular table and to the whole job, the filter parameter supplied for the specific table will take precedence. With the exception of the INCLUDE_ROWS filter, data filters are not supported on tables having nested tables or domain indexes defined upon them. Data filters are not supported in jobs performed in Transportable Tablespace mode. The available data filters are described in Table 49-6 . Table 49-6 Data Filters Name Datatype Operations that Support Filter Description INCLUDE_ROWS NUMBER EXPORT, IMPORT If nonzero, this filter specifies that user data for the specified table should be included in the job. The default is 1. PARTITION_EXPR PARTITION_LIST TEXT EXPORT, IMPORT Note: In this description, the information about partitions also applies to subpartions. For Export jobs, these filters specify which partitions are unloaded from the database. For Import jobs, they specify which table partitions are loaded into the database. Partition names are included in the job if their names satisfy the specified expression (for PARTITION_EXPR ) or are included in the list (for PARTITION_LIST ). Whereas the expression version of the filter offers more flexibility, the list version provides for full validation of the partition names. Double quotation marks around partition names are required only if the partition names contain special characters. PARTITION_EXPR is not supported on jobs across a network link. Default=All partitions are processed SAMPLE NUMBER EXPORT, IMPORT For Export jobs, specifies a percentage for sampling the data blocks to be moved. This filter allows subsets of large tables to be extracted for testing purposes. SUBQUERY TEXT EXPORT, IMPORT Specifies a subquery that is added to the end of the SELECT statement for the table. If you specify a WHERE clause in the subquery, you can restrict the rows that are selected. Specifying an ORDER BY clause orders the rows dumped in the export which improves performance when migrating from heap-organized tables to index-organized tables. Note: In this description, the information about partitions also applies to subpartions.