---
id: 19c__DBMS_XEVENT.ISNULL
name: DBMS_XEVENT.ISNULL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.ISNULL

This function returns TRUE if input argument is NULL .

## Syntax

```sql
DBMS_XEVENT.ISNULL (
    ev         IN   XDBEvent) 
  RETURN BOOLEAN;

DBMS_XEVENT.ISNULL (
    ev         IN   XDBRepositoryEvent) 
  RETURN BOOLEAN;

DBMS_XEVENT.ISNULL (
    hl         IN   XDBHandlerList) 
  RETURN BOOLEAN;

DBMS_XEVENT.ISNULL (
    handler    IN   XDBHandler) 
  RETURN BOOLEAN;
  RETURN BOOLEAN;

DBMS_XEVENT.ISNULL (
    path       IN   XDBPath) 
  RETURN BOOLEAN;

DBMS_XEVENT.ISNULL (
    link       IN   XDBLink) 
  RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBEvent) | IN | Event of specified type |
| hl | XDBHandlerList) | IN | Handler list |
| handler | XDBHandler) | IN | Handler |
| path | XDBPath) | IN | Path |

**Returns:** `BOOLEAN`

## Usage Notes

See Also: XDBEvent Type Subprograms for other subprograms in this group XDBRepositoryEvent Type Subprograms for other subprograms in this group XDBHandlerList Type Subprograms for other subprograms in this group XDBHandler Type Subprograms for other subprograms in this group XDBPath Type Subprograms for other subprograms in this group XDBLink Type Subprograms for other subprograms in this group See Also: XDBEvent Type Subprograms for other subprograms in this group XDBRepositoryEvent Type Subprograms for other subprograms in this group XDBHandlerList Type Subprograms for other subprograms in this group XDBHandler Type Subprograms for other subprograms in this group XDBPath Type Subprograms for other subprograms in this group XDBLink Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.ISNULL ( ev IN XDBEvent) RETURN BOOLEAN; DBMS_XEVENT.ISNULL ( ev IN XDBRepositoryEvent) RETURN BOOLEAN; DBMS_XEVENT.ISNULL ( hl IN XDBHandlerList) RETURN BOOLEAN; DBMS_XEVENT.ISNULL ( handler IN XDBHandler) RETURN BOOLEAN; RETURN BOOLEAN; DBMS_XEVENT.ISNULL ( path IN XDBPath) RETURN BOOLEAN; DBMS_XEVENT.ISNULL ( link IN XDBLink) RETURN BOOLEAN; Parameters Table 203-40 ISNULL Function Parameters Parameter Description ev Event of specified type hl Handler list handler Handler path Path