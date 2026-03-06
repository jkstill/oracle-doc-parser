---
id: 19c__DBMS_METADATA.SET_COUNT
name: DBMS_METADATA.SET_COUNT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_METADATA
tags: [dbms_metadata]
source_file: DBMS_METADATA.html
---

# DBMS_METADATA.SET_COUNT

This procedure specifies the maximum number of objects to be retrieved in a single FETCH_xxx call.

## Syntax

```sql
DBMS_METADATA.SET_COUNT (
   handle           IN NUMBER,
   value            IN NUMBER,
   object_type_path IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER | IN | The handle returned from OPEN . |
| value | NUMBER | IN | The maximum number of objects to retrieve. |
| object_type_path | VARCHAR2 | IN | A path name designating the object types to which the count value applies. By default, the count value applies to the object type of the OPEN handle. When the OPEN handle designates a heterogeneous object type, behavior can be either of the following: If object_type_path is omitted, then the count applies to all object types within the heterogeneous collection. If object_type_path is specified, then the count only applies to the specific node (or set of nodes) within the tree of object types forming the heterogeneous collection. |

## Usage Notes

By default, each call to FETCH_xxx returns one object. You can use the SET_COUNT procedure to override this default. If FETCH_xxx is called from a client, specifying a count value greater than 1 can result in fewer server round trips and, therefore, improved performance. For heterogeneous object types, a single FETCH_xxx operation only returns objects of a single object type. See Also: For more information about related subprograms: Subprograms for Retrieving Multiple Objects From the Database See Also: For more information about related subprograms: Subprograms for Retrieving Multiple Objects From the Database Syntax DBMS_METADATA.SET_COUNT ( handle IN NUMBER, value IN NUMBER, object_type_path IN VARCHAR2 DEFAULT NULL); Parameters Table 107-16 SET_COUNT Procedure Parameters Parameter Description handle The handle returned from OPEN . value The maximum number of objects to retrieve. object_type_path A path name designating the object types to which the count value applies. By default, the count value applies to the object type of the OPEN handle. When the OPEN handle designates a heterogeneous object type, behavior can be either of the following: If object_type_path is omitted, then the count applies to all object types within the heterogeneous collection. If object_type_path is specified, then the count only applies to the specific node (or set of nodes) within the tree of object types forming the heterogeneous collection. Exceptions INVALID_ARGVAL . A NULL or invalid value was supplied for an input parameter. The error message text identifies the parameter. INVALID_OPERATION . SET_COUNT was called after the first call to FETCH_xxx for the OPEN context. After the first call to FETCH_xxx is made, no further calls to SET_COUNT for the current OPEN context are permitted. INCONSISTENT_ARGS . object_type parameter is not consistent with handle.