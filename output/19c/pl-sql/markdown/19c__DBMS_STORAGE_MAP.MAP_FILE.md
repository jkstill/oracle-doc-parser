---
id: 19c__DBMS_STORAGE_MAP.MAP_FILE
name: DBMS_STORAGE_MAP.MAP_FILE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STORAGE_MAP
tags: [dbms_storage_map]
source_file: DBMS_STORAGE_MAP.html
---

# DBMS_STORAGE_MAP.MAP_FILE

This function builds mapping information for the file identified by filename . Use this function if the mapping of one particular file has changed. The Oracle database server does not have to rebuild the entire mapping.

## Syntax

```sql
DBMS_STORAGE_MAP.MAP_FILE(
   filename           IN VARCHAR2, 
   filetype           IN VARCHAR2,
   cascade            IN BOOLEAN,
   max_num_fileextent IN NUMBER DEFAULT 100,
   dictionary_update  IN BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| filename | VARCHAR2 | IN | The file for which mapping information is built. |
| filetype | VARCHAR2 | IN | Defines the type of the file to be mapped. It can be " DATAFILE", "SPFILE", "TEMPFILE", "CONTROLFILE", "LOGFILE", or "ARCHIVEFILE" . |
| cascade | BOOLEAN | IN | Should be TRUE only if a storage reconfiguration occurred. For all other instances, such as file resizing (either through an ALTER SYSTEM command or DML operations on extended files), cascade can be set to FALSE because the mapping changes are limited to the file extents only. If TRUE , mapping DAGs are also built for the elements where the file resides. |
| max_num_fileextent | NUMBER | IN | Defines the maximum number of file extents to be mapped. This limits the amount of memory used when mapping file extents. The default value is 100 ; max_num_fileextent is an overloaded argument. |
| dictionary_update | BOOLEAN | IN | If TRUE , mapping information in the data dictionary is updated to reflect the changes. The default value is TRUE ; dictionary_update is an overloaded argument. |

**Returns:** `UNKNOWN`

## Usage Notes

Syntax DBMS_STORAGE_MAP.MAP_FILE( filename IN VARCHAR2, filetype IN VARCHAR2, cascade IN BOOLEAN, max_num_fileextent IN NUMBER DEFAULT 100, dictionary_update IN BOOLEAN DEFAULT TRUE); Parameters Table 172-7 MAP_FILE Function Parameters Parameter Description filename The file for which mapping information is built. filetype Defines the type of the file to be mapped. It can be " DATAFILE", "SPFILE", "TEMPFILE", "CONTROLFILE", "LOGFILE", or "ARCHIVEFILE" . cascade Should be TRUE only if a storage reconfiguration occurred. For all other instances, such as file resizing (either through an ALTER SYSTEM command or DML operations on extended files), cascade can be set to FALSE because the mapping changes are limited to the file extents only. If TRUE , mapping DAGs are also built for the elements where the file resides. max_num_fileextent Defines the maximum number of file extents to be mapped. This limits the amount of memory used when mapping file extents. The default value is 100 ; max_num_fileextent is an overloaded argument. dictionary_update If TRUE , mapping information in the data dictionary is updated to reflect the changes. The default value is TRUE ; dictionary_update is an overloaded argument. Usage Notes This function may not obtain the latest mapping information if the file being mapped, or any one of the elements within its I/O stack (if cascade is TRUE ), is owned by a library that must be explicitly synchronized.