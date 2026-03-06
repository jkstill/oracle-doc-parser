---
id: 19c__DBMS_METADATA.FETCH_XXX
name: DBMS_METADATA.FETCH_XXX
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_METADATA
tags: [dbms_metadata]
source_file: DBMS_METADATA.html
---

# DBMS_METADATA.FETCH_XXX

These functions and procedures return metadata for objects meeting the criteria established by OPEN , SET_FILTER , SET_COUNT , ADD_TRANSFORM , and so on.

## Syntax

```sql
DBMS_METADATA.FETCH_XML (
   handle  IN NUMBER) 
RETURN sys.XMLType;
```

**Returns:** `sys.XMLType`

## Usage Notes

See " Usage Notes " for the variants. See Also: For more information about related subprograms: Subprograms for Retrieving Multiple Objects From the Database See Also: For more information about related subprograms: Subprograms for Retrieving Multiple Objects From the Database Syntax The FETCH functions are as follows: DBMS_METADATA.FETCH_XML ( handle IN NUMBER) RETURN sys.XMLType; DBMS_METADATA.FETCH_DDL ( handle IN NUMBER) RETURN sys.ku$_ddls; DBMS_METADATA.FETCH_CLOB ( handle IN NUMBER, cache_lob IN BOOLEAN DEFAULT TRUE, lob_duration IN PLS INTEGER DEFAULT DBMS_LOB.SESSION) RETURN CLOB; The FETCH procedures are as follows: DBMS_METADATA.FETCH_CLOB ( handle IN NUMBER, doc IN OUT NOCOPY CLOB); DBMS_METADATA.FETCH_XML_CLOB ( handle IN NUMBER, doc IN OUT NOCOPY CLOB, parsed_items OUT sys.ku$_parsed_items, object_type_path OUT VARCHAR2); Parameters Table 107-8 FETCH_xxx Function Parameters Parameters Description handle The handle returned from OPEN . cache_lob TRUE =read LOB into buffer cache lob_duration The duration for the temporary LOB created by FETCH_CLOB , either DBMS_LOB.SESSION (the default) or DBMS_LOB.CALL . doc The metadata for the objects, or NULL if all objects have been returned. parsed_items A nested table containing the items specified by SET_PARSE_ITEM . If SET_PARSE_ITEM was not called, a NULL is returned. object_type_path For heterogeneous object types, this is the full path name of the object type for the objects returned by the call to FETCH_XXX . If handle designates a homogeneous object type, a NULL is returned. Return Values The metadata for the objects or NULL if all objects have been returned.