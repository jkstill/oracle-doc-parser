---
id: 19c__DBMS_XEVENT.REMOVE
name: DBMS_XEVENT.REMOVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.REMOVE

This procedure removes the specified handler from the handler list.

## Syntax

```sql
DBMS_XEVENT.REMOVE (
    hl       IN OUT   XDBHandlerList, 
    handler  IN       XDBHandler);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| hl | XDBHandlerList | IN OUT | Handler list |
| handler | XDBHandler) | IN | Handler |

## Usage Notes

See Also: XDBHandlerList Type Subprograms for other subprograms in this group See Also: XDBHandlerList Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.REMOVE ( hl IN OUT XDBHandlerList, handler IN XDBHandler); Parameters Table 203-41 REMOVE Procedure Parameters Parameter Description hl Handler list handler Handler