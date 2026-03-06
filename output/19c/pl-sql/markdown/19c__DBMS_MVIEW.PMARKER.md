---
id: 19c__DBMS_MVIEW.PMARKER
name: DBMS_MVIEW.PMARKER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MVIEW
tags: [dbms_mview]
source_file: DBMS_MVIEW.html
---

# DBMS_MVIEW.PMARKER

This function returns a partition marker from a rowid. It is used for Partition Change Tracking (PCT).

## Syntax

```sql
DBMS_MVIEW.PMARKER(
   rid IN ROWID)
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rid | ROWID) | IN | The rowid of a row entry in a master table |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_MVIEW.PMARKER( rid IN ROWID) RETURN NUMBER; Parameters Table 113-7 PMARKER Function Parameters Parameter Description rid The rowid of a row entry in a master table