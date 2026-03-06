---
id: 19c__DBMS_PIPE.NEXT_ITEM_TYPE
name: DBMS_PIPE.NEXT_ITEM_TYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PIPE
tags: [dbms_pipe]
source_file: DBMS_PIPE.html
---

# DBMS_PIPE.NEXT_ITEM_TYPE

This function determines the datatype of the next item in the local message buffer.

## Syntax

```sql
DBMS_PIPE.NEXT_ITEM_TYPE 
  RETURN INTEGER;
```

**Returns:** `INTEGER`

## Usage Notes

After you have called RECEIVE_MESSAGE to place pipe information in a local buffer, call NEXT_ITEM_TYPE. Syntax DBMS_PIPE.NEXT_ITEM_TYPE RETURN INTEGER; Pragmas pragma restrict_references(next_item_type,WNDS,RNDS); Return Values Table 127-6 NEXT_ITEM_TYPE Function Return Values Return Description 0 No more items 6 NUMBER 9 VARCHAR2 11 ROWID 12 DATE 23 RAW