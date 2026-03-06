---
id: 19c__DBMS_METADATA_DIFF.OPENC
name: DBMS_METADATA_DIFF.OPENC
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_METADATA_DIFF
tags: [dbms_metadata_diff]
source_file: DBMS_METADATA_DIFF.html
---

# DBMS_METADATA_DIFF.OPENC

This function specifies the type of objects to be compared. The return value is an opaque context handle.

## Syntax

```sql
DBMS_METADATA_DIFF.OPENC (
object_type  IN VARCHAR2)
RETURN NUMBER;
```

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_METADATA_DIFF.OPENC ( object_type IN VARCHAR2) RETURN NUMBER; Parameters Table 108-3 OPENC Function Parameters Parameters Description object_type The type of object to be compared. Valid type names are CLUSTER , CONTEXT , DB_LINK , FGA_POLICY , INDEX , MATERIALIZED_VIEW , MATERIALIZED_VIEW_LOG , QUEUE , QUEUE_TABLE , RLS_CONTEXT , RLS_GROUP , RLS_POLICY , ROLE , SEQUENCE , SYNONYM , TABLE , TABLESPACE , TRIGGER , TYPE , TYPE_SPEC , TYPE_BODY , USER , and VIEW . Return Values The opaque handle that is returned is used as input to ADD_DOCUMENT , FETCH_xxx and CLOSE . Exceptions INVALID_ARGVAL A NULL or invalid value was supplied for an input parameter. The error message text identifies the parameter.