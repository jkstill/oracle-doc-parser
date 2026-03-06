---
id: 19c__DBMS_METADATA_DIFF
name: DBMS_METADATA_DIFF
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_METADATA_DIFF
tags: [dbms_metadata_diff]
source_file: DBMS_METADATA_DIFF.html
---

# DBMS_METADATA_DIFF

These functions allow you to compare the metadata for two objects with a single call.

## Syntax

```sql
DBMS_METADATA_DIFF.COMPARE_SXML(
object_type   IN VARCHAR2,
name1         IN VARCHAR2,
name2         IN VARCHAR2,
schema1       IN VARCHAR2 DEFAULT NULL,
schema2       IN VARCHAR2 DEFAULT NULL,
network_link1 IN VARCHAR2 DEFAULT NULL,
network_link2 IN VARCHAR2 DEFAULT NULL)
RETURN CLOB;

DBMS_METADATA_DIFF.COMPARE_ALTER(
object_type   IN VARCHAR2,
name1         IN VARCHAR2,
name2         IN VARCHAR2,
schema1       IN VARCHAR2 DEFAULT NULL,
schema2       IN VARCHAR2 DEFAULT NULL,
network_link1 IN VARCHAR2 DEFAULT NULL,
network_link2 IN VARCHAR2 DEFAULT NULL)
RETURN CLOB;

DBMS_METADATA_DIFF.COMPARE_ALTER_XML(
object_type   IN VARCHAR2,
name1         IN VARCHAR2,
name2         IN VARCHAR2,
schema1       IN VARCHAR2 DEFAULT NULL,
schema2       IN VARCHAR2 DEFAULT NULL,
network_link1 IN VARCHAR2 DEFAULT NULL,
network_link2 IN VARCHAR2 DEFAULT NULL)
RETURN CLOB;
```

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_METADATA_DIFF.COMPARE_SXML( object_type IN VARCHAR2, name1 IN VARCHAR2, name2 IN VARCHAR2, schema1 IN VARCHAR2 DEFAULT NULL, schema2 IN VARCHAR2 DEFAULT NULL, network_link1 IN VARCHAR2 DEFAULT NULL, network_link2 IN VARCHAR2 DEFAULT NULL) RETURN CLOB; DBMS_METADATA_DIFF.COMPARE_ALTER( object_type IN VARCHAR2, name1 IN VARCHAR2, name2 IN VARCHAR2, schema1 IN VARCHAR2 DEFAULT NULL, schema2 IN VARCHAR2 DEFAULT NULL, network_link1 IN VARCHAR2 DEFAULT NULL, network_link2 IN VARCHAR2 DEFAULT NULL) RETURN CLOB; DBMS_METADATA_DIFF.COMPARE_ALTER_XML( object_type IN VARCHAR2, name1 IN VARCHAR2, name2 IN VARCHAR2, schema1 IN VARCHAR2 DEFAULT NULL, schema2 IN VARCHAR2 DEFAULT NULL, network_link1 IN VARCHAR2 DEFAULT NULL, network_link2 IN VARCHAR2 DEFAULT NULL) RETURN CLOB; Parameters Table 108-1 COMPARE_xxx Function Parameters Parameters Description object_type The type of object to be compared. Valid type names are CLUSTER , CONTEXT , DB_LINK , FGA_POLICY , INDEX , MATERIALIZED_VIEW , MATERIALIZED_VIEW_LOG , QUEUE , QUEUE_TABLE , RLS_CONTEXT , RLS_GROUP , RLS_POLICY , ROLE , SEQUENCE , SYNONYM , TABLE , TABLESPACE , TRIGGER , TYPE , TYPE_SPEC , TYPE_BODY , USER , and VIEW . name1 The name of the first object in the comparison. name2 The name of the second object in the comparison. schema1 The schema of the first object in the comparison. The default is the current user. schema2 The schema of the second object in the comparison. The default is the value of schema1 . network_link1 The name of a database link to the database on which the first object resides. If NULL (the default), then the object is assumed to be in the database on which the caller is running. network_link2 The name of a database link to the database on which the second object resides. The default is the value of network_link1 . Return Values DBMS_METADATA_DIFF.COMPARE_xxx returns the differences between two objects. Exceptions INVALID_ARGVAL A NULL or invalid value was supplied for an input parameter. The error message text identifies the parameter. OBJECT_NOT_FOUND The specified object was not found in the database. Usage Notes These functions encapsulate calls to both DBMS_METADATA and DBMS_METADATA_DIFF functions and procedures to fetch the metadata for each of the two objects and compare them. Which function you use depends on the comparison format you want: COMPARE_SXML returns an SXML difference document. COMPARE_ALTER returns a set of ALTER statements for making the first object like the second object. COMPARE_ALTER_XML returns an ALTER_XML document.