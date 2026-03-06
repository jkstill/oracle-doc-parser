---
id: 19c__DBMS_METADATA.CLOSE
name: DBMS_METADATA.CLOSE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_METADATA
tags: [dbms_metadata]
source_file: DBMS_METADATA.html
---

# DBMS_METADATA.CLOSE

This procedure is used for both retrieval and submission. This procedure invalidates the handle returned by OPEN (or OPENW ) and cleans up the associated state.

## Syntax

```sql
DBMS_METADATA.CLOSE (
   handle  IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER) | IN | The handle returned from OPEN (or OPENW ). |

## Usage Notes

See Also: For more information about related subprograms: Subprograms for Retrieving Multiple Objects From the Database Subprograms for Submitting XML to the Database See Also: For more information about related subprograms: Subprograms for Retrieving Multiple Objects From the Database Subprograms for Submitting XML to the Database Syntax DBMS_METADATA.CLOSE ( handle IN NUMBER); Parameters Table 107-6 CLOSE Procedure Parameters Parameter Description handle The handle returned from OPEN (or OPENW ). Usage Notes Note: The following notes apply only to object retrieval You can prematurely terminate the stream of objects established by OPEN or ( OPENW) . If a call to FETCH_xxx returns NULL, indicating no more objects, a call to CLOSE is made transparently. In this case, you can still call CLOSE on the handle and not get an exception. (The call to CLOSE is not required.) If you know that only one specific object will be returned, you should explicitly call CLOSE after the single FETCH_xxx call to free resources held by the handle.