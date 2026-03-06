---
id: 19c__DBMS_METADATA.GET_XXX
name: DBMS_METADATA.GET_XXX
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_METADATA
tags: [dbms_metadata]
source_file: DBMS_METADATA.html
---

# DBMS_METADATA.GET_XXX

GET_xxx functions let you fetch metadata for objects with a single call.

## Syntax

```sql
DBMS_METADATA.GET_XML (
object_type     IN VARCHAR2,
name            IN VARCHAR2,
schema          IN VARCHAR2 DEFAULT NULL,
version         IN VARCHAR2 DEFAULT 'COMPATIBLE',
model           IN VARCHAR2 DEFAULT 'ORACLE',
transform       IN VARCHAR2 DEFAULT NULL)
RETURN CLOB;

DBMS_METADATA.GET_DDL (
object_type     IN VARCHAR2,
name            IN VARCHAR2,
schema          IN VARCHAR2 DEFAULT NULL,
version         IN VARCHAR2 DEFAULT 'COMPATIBLE',
model           IN VARCHAR2 DEFAULT 'ORACLE',
transform       IN VARCHAR2 DEFAULT 'DDL')
RETURN CLOB;

DBMS_METADATA.GET_SXML (
object_type     IN VARCHAR2,
name            IN VARCHAR2 DEFAULT NULL,
schema          IN VARCHAR2 DEFAULT NULL,
version         IN VARCHAR2 DEFAULT 'COMPATIBLE',
model           IN VARCHAR2 DEFAULT 'ORACLE',
transform       IN VARCHAR2 DEFAULT 'SXML')
RETURN CLOB;

DBMS_METADATA.GET_DEPENDENT_XML (
object_type        IN VARCHAR2,
base_object_name   IN VARCHAR2,
base_object_schema IN VARCHAR2 DEFAULT NULL,
version            IN VARCHAR2 DEFAULT 'COMPATIBLE',
model              IN VARCHAR2 DEFAULT 'ORACLE',
transform          IN VARCHAR2 DEFAULT NULL,
object_count       IN NUMBER   DEFAULT 10000)
RETURN CLOB;

DBMS_METADATA.GET_DEPENDENT_DDL (
object_type         IN VARCHAR2,
base_object_name    IN VARCHAR2,
base_object_schema  IN VARCHAR2 DEFAULT NULL,
version             IN VARCHAR2 DEFAULT 'COMPATIBLE',
model               IN VARCHAR2 DEFAULT 'ORACLE',
transform           IN VARCHAR2 DEFAULT 'DDL',
object_count        IN NUMBER   DEFAULT 10000)
RETURN CLOB;

DBMS_METADATA.GET_GRANTED_XML (
object_type     IN VARCHAR2,
grantee         IN VARCHAR2 DEFAULT NULL,
version         IN VARCHAR2 DEFAULT 'COMPATIBLE',
model           IN VARCHAR2 DEFAULT 'ORACLE',
transform       IN VARCHAR2 DEFAULT NULL,
object_count    IN NUMBER   DEFAULT 10000)
RETURN CLOB;

DBMS_METADATA.GET_GRANTED_DDL (
object_type     IN VARCHAR2,
grantee         IN VARCHAR2 DEFAULT NULL,
version         IN VARCHAR2 DEFAULT 'COMPATIBLE',
model           IN VARCHAR2 DEFAULT 'ORACLE',
transform       IN VARCHAR2 DEFAULT 'DDL',
object_count    IN NUMBER   DEFAULT 10000)
RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_type | VARCHAR2 | IN | The type of object to be retrieved. This parameter takes the same values as the OPEN object_type parameter, except that it cannot be a heterogeneous object type. The attributes of the object type must be appropriate to the function. That is, for GET_xxx it must be a named object. |
| name | VARCHAR2 | IN | The object name. It is used internally in a NAME filter. (If the name is longer than 30 characters, it will be used in a LONGNAME filter.) If this parameter is NULL, then no NAME or LONGNAME filter is specified. See Table 107-18 for a list of filters. |
| schema | VARCHAR2 | IN | The object schema. It is used internally in a SCHEMA filter. The default is the current user. |
| version | VARCHAR2 | IN | The version of metadata to be extracted. This parameter takes the same values as the OPEN version parameter. |
| model | VARCHAR2 | IN | The object model to use. This parameter takes the same values as the OPEN model parameter. |
| transform | VARCHAR2 | IN | The name of a transformation on the output. This parameter takes the same values as the ADD_TRANSFORM name parameter. For GET_XML this must not be DDL . |
| base_object_name | VARCHAR2 | IN | The base object name. It is used internally in a BASE_OBJECT_NAME filter. |
| base_object_schema | VARCHAR2 | IN | The base object schema. It is used internally in a BASE_OBJECT_SCHEMA filter. The default is the current user. |
| grantee | VARCHAR2 | IN | The grantee. It is used internally in a GRANTEE filter. The default is the current user. |
| object_count | NUMBER | IN | The maximum number of objects to return. See SET_COUNT Procedure . |

**Returns:** `CLOB`

## Usage Notes

These GET_xxx functions are: GET_XML GET_DDL GET_SXML GET_DEPENDENT_XML GET_DEPENDENT_DDL GET_GRANTED_XML GET_GRANTED_DDL See Also: For more information about related subprograms: Subprograms for Retrieving Multiple Objects From the Database See Also: For more information about related subprograms: Subprograms for Retrieving Multiple Objects From the Database Syntax DBMS_METADATA.GET_XML ( object_type IN VARCHAR2, name IN VARCHAR2, schema IN VARCHAR2 DEFAULT NULL, version IN VARCHAR2 DEFAULT 'COMPATIBLE', model IN VARCHAR2 DEFAULT 'ORACLE', transform IN VARCHAR2 DEFAULT NULL) RETURN CLOB; DBMS_METADATA.GET_DDL ( object_type IN VARCHAR2, name IN VARCHAR2, schema IN VARCHAR2 DEFAULT NULL, version IN VARCHAR2 DEFAULT 'COMPATIBLE', model IN VARCHAR2 DEFAULT 'ORACLE', transform IN VARCHAR2 DEFAULT 'DDL') RETURN CLOB; DBMS_METADATA.GET_SXML ( object_type IN VARCHAR2, name IN VARCHAR2 DEFAULT NULL, schema IN VARCHAR2 DEFAULT NULL, version IN VARCHAR2 DEFAULT 'COMPATIBLE', model IN VARCHAR2 DEFAULT 'ORACLE', transform IN VARCHAR2 DEFAULT 'SXML') RETURN CLOB; DBMS_METADATA.GET_DEPENDENT_XML ( object_type IN VARCHAR2, base_object_name IN VARCHAR2, base_object_schema IN VARCHAR2 DEFAULT NULL, version IN VARCHAR2 DEFAULT 'COMPATIBLE', model IN VARCHAR2 DEFAULT 'ORACLE', transform IN VARCHAR2 DEFAULT NULL, object_count IN NUMBER DEFAULT 10000) RETURN CLOB; DBMS_METADATA.GET_DEPENDENT_DDL ( object_type IN VARCHAR2, base_object_name IN VARCHAR2, base_object_schema IN VARCHAR2 DEFAULT NULL, version IN VARCHAR2 DEFAULT 'COMPATIBLE', model IN VARCHAR2 DEFAULT 'ORACLE', transform IN VARCHAR2 DEFAULT 'DDL', object_count IN NUMBER DEFAULT 10000) RETURN CLOB; DBMS_METADATA.GET_GRANTED_XML ( object_type IN VARCHAR2, grantee IN VARCHAR2 DEFAULT NULL, version IN VARCHAR2 DEFAULT 'COMPATIBLE', model IN VARCHAR2 DEFAULT 'ORACLE', transform IN VARCHAR2 DEFAULT NULL, object_count IN NUMBER DEFAULT 10000) RETURN CLOB; DBMS_METADATA.GET_GRANTED_DDL ( object_type IN VARCHAR2, grantee IN VARCHAR2 DEFAULT NULL, version IN VARCHAR2 DEFAULT 'COMPATIBLE', model IN VARCHAR2 DEFAULT 'ORACLE', transform IN VARCHAR2 DEFAULT 'DDL', object_count IN NUMBER DEFAULT 10000) RETURN CLOB; Parameters Table 107-9 GET_xxx Function Parameters Parameter Description object_type The type of object to be retrieved. This parameter takes the same values as the OPEN object_type parameter, except that it cannot be a heterogeneous object type. The attributes of the object type must be appropriate to the function. That is, for GET_xxx it must be a named object. name The object name. It is used internally in a NAME filter. (If the name is longer than 30 characters, it will be used in a LONGNAME filter.) If this parameter is NULL, then no NAME or LONGNAME filter is specified. See Table 107-18 for a list of filters. schema The object schema. It is used internally in a SCHEMA filter. The default is the current user. version The version of metadata to be extracted. This parameter takes the same values as the OPEN version parameter. model The object model to use. This parameter takes the same values as the OPEN model parameter. transform The name of a transformation on the output. This parameter takes the same values as the ADD_TRANSFORM name parameter. For GET_XML this must not be DDL . base_object_name The base object name. It is used internally in a BASE_OBJECT_NAME filter. base_object_schema The base object schema. It is used internally in a BASE_OBJECT_SCHEMA filter. The default is the current user. grantee The grantee. It is used internally in a GRANTEE filter. The default is the current user. object_count The maximum number of objects to return. See SET_COUNT Procedure . Return Values The metadata for the specified object as XML or DDL.