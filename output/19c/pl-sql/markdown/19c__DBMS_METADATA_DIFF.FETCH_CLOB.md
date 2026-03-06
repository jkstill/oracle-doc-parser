---
id: 19c__DBMS_METADATA_DIFF.FETCH_CLOB
name: DBMS_METADATA_DIFF.FETCH_CLOB
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_METADATA_DIFF
tags: [dbms_metadata_diff]
source_file: DBMS_METADATA_DIFF.html
---

# DBMS_METADATA_DIFF.FETCH_CLOB

The FETCH_CLOB functions and procedures return a CLOB showing the differences between the two documents specified by ADD_DOCUMENT .

## Syntax

```sql
DBMS_METADATA_DIFF.FETCH_CLOB(
handle IN NUMBER)
RETURN CLOB;

DBMS_METADATA_DIFF.FETCH_CLOB(
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER) | IN | The handle returned from OPENC . |
| doc |  |  | A CLOB containing the differences between documents 1 and 2. |
| diffs |  |  | TRUE if the documents are different or FALSE if they are identical. |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_METADATA_DIFF.FETCH_CLOB( handle IN NUMBER) RETURN CLOB; DBMS_METADATA_DIFF.FETCH_CLOB( handle IN NUMBER, doc IN OUT NOCOPY CLOB); DBMS_METADATA_DIFF.FETCH_CLOB( handle IN NUMBER, doc IN OUT NOCOPY CLOB diffs OUT BOOLEAN); Parameters Table 108-5 FETCH_CLOB Subprogram Parameters Parameter Description handle The handle returned from OPENC . doc A CLOB containing the differences between documents 1 and 2. diffs TRUE if the documents are different or FALSE if they are identical. Return Values The differences between documents 1 and 2. Exceptions INVALID_ARGVAL A NULL or invalid value was supplied for an input parameter. The error message text identifies the parameter.