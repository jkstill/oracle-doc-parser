---
id: 19c__DBMS_DATAPUMP.METADATA_REMAP
name: DBMS_DATAPUMP.METADATA_REMAP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATAPUMP
tags: [dbms_datapump]
source_file: DBMS_DATAPUMP.html
---

# DBMS_DATAPUMP.METADATA_REMAP

This procedure specifies a remapping to be applied to objects as they are processed in the specified job.

## Syntax

```sql
DBMS_DATAPUMP.METADATA_REMAP (
   handle      IN NUMBER,
   name        IN VARCHAR2,
   old_value   IN VARCHAR2,
   value       IN VARCHAR2,
   object_type IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER | IN | The handle for the current job. The current session must have previously attached to the handle through a call to the OPEN function. |
| name | VARCHAR2 | IN | The name of the remap. See Table 49-17 for descriptions of the available remaps. |
| old_value | VARCHAR2 | IN | Specifies which value in the dump file set should be reset to value |
| value | VARCHAR2 | IN | The value of the parameter for the remap. This signifies the new value that old_value should be translated into. |
| object_type | VARCHAR2 | IN | Designates the object type to which the remap applies. The list of object types supported for each mode are contained in the DATABASE_EXPORT_OBJECTS , SCHEMA_EXPORT_OBJECTS , TABLE_EXPORT_OBJECTS , and TABLESPACE_EXPORT_OBJECTS catalog views. By default, the remap applies to all applicable objects within the job. The object_type parameter allows a caller to specify different parameters for different object types within a job. Remaps that explicitly specify an object type override remaps that apply to all object types. |

## Usage Notes

Syntax DBMS_DATAPUMP.METADATA_REMAP ( handle IN NUMBER, name IN VARCHAR2, old_value IN VARCHAR2, value IN VARCHAR2, object_type IN VARCHAR2 DEFAULT NULL); Parameters Table 49-16 METADATA_REMAP Procedure Parameters Parameter Description handle The handle for the current job. The current session must have previously attached to the handle through a call to the OPEN function. name The name of the remap. See Table 49-17 for descriptions of the available remaps. old_value Specifies which value in the dump file set should be reset to value value The value of the parameter for the remap. This signifies the new value that old_value should be translated into. object_type Designates the object type to which the remap applies. The list of object types supported for each mode are contained in the DATABASE_EXPORT_OBJECTS , SCHEMA_EXPORT_OBJECTS , TABLE_EXPORT_OBJECTS , and TABLESPACE_EXPORT_OBJECTS catalog views. By default, the remap applies to all applicable objects within the job. The object_type parameter allows a caller to specify different parameters for different object types within a job. Remaps that explicitly specify an object type override remaps that apply to all object types. Table 49-17 describes the remaps provided by the METADATA_REMAP procedure. Table 49-17 Remaps Provided by the METADATA_REMAP Procedure Name Datatype Object Type Meaning REMAP_SCHEMA TEXT Schema objects Any schema object in the job that matches the object_type parameter and was located in the old_value schema will be moved to the value schema. Privileged users can perform unrestricted schema remaps. Nonprivileged users can perform schema remaps only if their schema is the target schema of the remap. For example, SCOTT can remap his BLAKE's objects to SCOTT , but SCOTT cannot remap SCOTT's objects to BLAKE . REMAP_TABLESPACE TEXT TABLE, INDEX, ROLLBACK_SEGMENT, MATERIALIZED_VIEW, MATERIALIZED_VIEW_LOG,TABLE_SPACE Any storage segment in the job that matches the object_type parameter and was located in the old_value tablespace will be relocated to the value tablespace. REMAP_DATAFILE TEXT LIBRARY, TABLESPACE, DIRECTORY If old_value and value are both full file specifications, then any data file reference in the job that matches the object_type parameter and that referenced the old_value data file will be redefined to use the value data file. If old_value and value are both directory paths, then any data file reference whose object path matches old_value will have its path substituted with value . REMAP_TABLE TEXT TABLE Any reference to a table in the job that matches the old_value table name will be replaced with the value table name. The old_value parameter may refer to a partition such as employees.low . This allows names for tables constructed the by PARTITION_OPTIONS=DEPARTITION parameter to be specified by the user. Exceptions INVALID_HANDLE . The specified handle is not attached to a Data Pump job. INVALID_ARGVAL . This message can indicate any of the following: The job's mode does not include the specified object_type . The remap has already been specified for the specified old_value and object_type . INVALID_OPERATION . Remaps are only supported for SQL_FILE and Import operations. The job's operation was Export, which does not support the use of metadata remaps. INVALID_STATE . The user called METADATA_REMAP after the job had started (that is, the job was not in the defining state). INCONSISTENT_ARGS . There was no value supplied or it was of the wrong datatype for the remap. PRIVILEGE_ERROR . A nonprivileged user attempted to do a REMAP_SCHEMA to a different user's schema or a REMAP_DATAFILE . SUCCESS_WITH_INFO . The procedure succeeded, but further information is available through the GET_STATUS procedure. NO_SUCH_JOB . The specified job does not exist. Usage Notes The METADATA_REMAP procedure is only supported for Import and SQL_FILE operations. It enables you to apply commonly desired, predefined remappings to the definition of objects as part of the transfer. If you need remaps that are not supported within this procedure, you should do a preliminary SQL_FILE operation to produce a SQL script corresponding to the dump file set. By editing the DDL directly and then executing it, you can produce any remappings that you need. Transforms for the DataPump API are a subset of the remaps implemented by the DBMS_METADATA . SET_TRANSFORM_PARAMETER API. Multiple remaps can be defined for a single job. However, each remap defined must be unique according its parameters. That is, two remaps cannot specify conflicting or redundant remaps.