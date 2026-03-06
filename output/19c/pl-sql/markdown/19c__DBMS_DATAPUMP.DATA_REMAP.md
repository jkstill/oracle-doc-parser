---
id: 19c__DBMS_DATAPUMP.DATA_REMAP
name: DBMS_DATAPUMP.DATA_REMAP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATAPUMP
tags: [dbms_datapump]
source_file: DBMS_DATAPUMP.html
---

# DBMS_DATAPUMP.DATA_REMAP

This procedure specifies transformations to be applied to column data as it is exported from, or imported into, a database.

## Syntax

```sql
DBMS_DATAPUMP.DATA_REMAP(
   handle          IN NUMBER,
   name            IN VARCHAR2,
   table_name      IN VARCHAR2,
   column          IN VARCHAR2,
   remap_function  IN VARCHAR2,
   schema          IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER | IN | The handle of the current job. The current session must have previously attached to the handle through a call to an OPEN function. |
| name | VARCHAR2 | IN | The name of the remap |
| table_name | VARCHAR2 | IN | The table containing the column to be remapped |
| column | VARCHAR2 | IN | The name of the column to be remapped |
| remap_function | VARCHAR2 | IN | The meaning of remap_function is dependent upon the value of name. See Table 49-8 for a list of possible names. |
| schema | VARCHAR2 | IN | The schema containing the column to be remapped. If NULL, the remapping applies to all schemas moved in the job that contain the specified table. |

## Usage Notes

Syntax DBMS_DATAPUMP.DATA_REMAP( handle IN NUMBER, name IN VARCHAR2, table_name IN VARCHAR2, column IN VARCHAR2, remap_function IN VARCHAR2, schema IN VARCHAR2 DEFAULT NULL); Parameters Table 49-7 DATA_REMAP Procedure Parameters Parameter Description handle The handle of the current job. The current session must have previously attached to the handle through a call to an OPEN function. name The name of the remap table_name The table containing the column to be remapped column The name of the column to be remapped remap_function The meaning of remap_function is dependent upon the value of name. See Table 49-8 for a list of possible names. schema The schema containing the column to be remapped. If NULL, the remapping applies to all schemas moved in the job that contain the specified table. Exceptions INVALID_ARGVAL . The mode is transportable (which does not support data modifications) or it has specified that no data to be included in the job. An invalid remap name was supplied. INVALID_OPERATION . Data remaps are only supported for Export and Import operations. INVALID_STATE . The DATA_REMAP procedure was called after the job started (that is, it was not in the defining state). NO_SUCH_JOB . The job handle is no longer valid. Usage Notes The DATA_REMAP procedure is only supported for Export and Import operations. It allows you to manipulate user data being exported or imported. The name of the remap determines the remap operation to be performed. For export operations, you might wish to define a data remap to obscure sensitive data such as credit card numbers from a dump file, but leave the remainder of the data so that it can be read. To accomplish this, the remapping should convert each unique source number into a distinct generated number. So that the mapping is consistent across the dump file set, the same function should be called for every column that contains the credit card number. For import operations, you might wish to define a data remap to reset the primary key when data is being merged into an existing table that contains colliding primary keys. A single remapping function should be provided for all columns defining or referencing the primary key to ensure that remapping is consistent. Note: If the called function uses package state variables, then to ensure that remapping is performed consistently across all tables, the job should be run with a SET_PARALLEL value of 1 and no restart operations should be performed. The Data Remap functions are listed in Table 49-8 . Table 49-8 Names of Data Remap Functions Name Meaning of remap_function Meaning COLUMN_FUNCTION String having the format: [schema.]package.function The name parameter references a PL/SQL package function which is called to modify the data for the specified column. The function accepts a single parameter, which has the same datatype as the remapped column, and returns a value having the same datatype as the remapped column. Note that the default for the schema is the schema of the user performing the export. Note: If the called function uses package state variables, then to ensure that remapping is performed consistently across all tables, the job should be run with a SET_PARALLEL value of 1 and no restart operations should be performed.