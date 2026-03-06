---
id: 19c__DBMS_XEVENT.SETRENDERSTREAM
name: DBMS_XEVENT.SETRENDERSTREAM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.SETRENDERSTREAM

This procedure sets the BLOB from which the rendered contents can be read.

## Syntax

```sql
DBMS_XEVENT.SETRENDERSTREAM (
    ev    IN   XDBRepositoryEvent, 
    istr  IN   BLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent | IN | XDBRepositoryEvent object |
| istr | BLOB) | IN | Input stream from which to get the rendered contents |

## Usage Notes

This should not be called after the stream returned by GETOUTPUTSTREAM is written to or after SETRENDERPATH is called; doing so will result in an error. This is only valid for the render event. Syntax DBMS_XEVENT.SETRENDERSTREAM ( ev IN XDBRepositoryEvent, istr IN BLOB); Parameters Table 203-43 SETRENDERSTREAM Procedure Parameters Parameter Description ev XDBRepositoryEvent object istr Input stream from which to get the rendered contents