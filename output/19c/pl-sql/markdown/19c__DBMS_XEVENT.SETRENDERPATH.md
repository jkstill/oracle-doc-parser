---
id: 19c__DBMS_XEVENT.SETRENDERPATH
name: DBMS_XEVENT.SETRENDERPATH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.SETRENDERPATH

This procedure specifies the path of the resource that contains the rendered contents.

## Syntax

```sql
DBMS_XEVENT.SETRENDERPATH (
    ev     IN   XDBRepositoryEvent, 
    path   IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent | IN | XDB Repository Event object |
| path | VARCHAR2) | IN | Path of the resource containing the rendered contents |

## Usage Notes

This should not be called after the stream returned by GETOUTPUTSTREAM Function is written to or after the SETRENDERSTREAM Procedure is called; doing so will result in an error. This is only valid for the render event. Syntax DBMS_XEVENT.SETRENDERPATH ( ev IN XDBRepositoryEvent, path IN VARCHAR2); Parameters Table 203-42 SETRENDERPATH Procedure Parameters Parameter Description ev XDB Repository Event object path Path of the resource containing the rendered contents