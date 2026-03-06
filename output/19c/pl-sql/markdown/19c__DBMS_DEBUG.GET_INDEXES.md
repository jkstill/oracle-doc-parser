---
id: 19c__DBMS_DEBUG.GET_INDEXES
name: DBMS_DEBUG.GET_INDEXES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.GET_INDEXES

Given a name of a variable or parameter, this function returns the set of its indexes, if it is an indexed table. An error is returned if it is not an indexed table.

## Syntax

```sql
DBMS_DEBUG.GET_INDEXES (
   varname   IN  VARCHAR2,
   frame#    IN  BINARY_INTEGER,
   handle    IN  program_info,
   entries   OUT index_table) 
RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| varname | VARCHAR2 | IN | Name of the variable to get index information about |
| frame# | BINARY_INTEGER | IN | Number of frame in which the variable or parameter resides; NULL for a package variable |
| handle | program_info | IN | Package description, if object is a package variable |
| entries | index_table) | OUT | 1-based table of the indexes: if non- NULL , then entries (1) contains the first index of the table, entries (2) contains the second index, and so on. |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_DEBUG.GET_INDEXES ( varname IN VARCHAR2, frame# IN BINARY_INTEGER, handle IN program_info, entries OUT index_table) RETURN BINARY_INTEGER; Parameters Table 57-25 GET_INDEXES Function Parameters Parameter Description varname Name of the variable to get index information about frame# Number of frame in which the variable or parameter resides; NULL for a package variable handle Package description, if object is a package variable entries 1-based table of the indexes: if non- NULL , then entries (1) contains the first index of the table, entries (2) contains the second index, and so on. Return Values Table 57-26 GET_INDEXES Function Return Values Return Description error_no_such_object One of the following: - The package does not exist - The package is not instantiated - The user does not have privileges to debug the package - The object does not exist in the package