---
id: 19c__DBMS_DBFS_HS.REGISTERSTORECOMMAND
name: DBMS_DBFS_HS.REGISTERSTORECOMMAND
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_HS
tags: [dbms_dbfs_hs]
source_file: DBMS_DBFS_HS.html
---

# DBMS_DBFS_HS.REGISTERSTORECOMMAND

This procedure registers commands for a store with the Hierarchical Store. These commands are sent to the Media Manager for the external storage device associated with the store.

## Syntax

```sql
DBMS_DBFS_HS.REGISTERSTORECOMMAND (
   store_name      IN     VARCHAR2,
   message         IN     VARCHAR2,
   flags           IN     NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| message | VARCHAR2 | IN | Message to be sent to the Media Manager of the external store |
| flags | NUMBER) | IN | Valid values: BEFORE_PUT CONSTANT NUMBER := 1 ; BEFORE_GET CONSTANT NUMBER := 2 ; |

## Usage Notes

Syntax DBMS_DBFS_HS.REGISTERSTORECOMMAND ( store_name IN VARCHAR2, message IN VARCHAR2, flags IN NUMBER); Parameters Table 54-14 REGISTERSTORECOMMAND Procedure Parameters Parameter Description store_name Name of store message Message to be sent to the Media Manager of the external store flags Valid values: BEFORE_PUT CONSTANT NUMBER := 1 ; BEFORE_GET CONSTANT NUMBER := 2 ; Usage Notes These commands are sent before the next read or write of content. When the Hierarchical Store wants to push (or get) data to (or from) the storage device, it begins a session (to communicate with the device). After beginning the session, it sends all registered commands for the to the relevant device before writing (or getting) any data. If this method successfully executes, its actions cannot be rolled back by the user. To restore the previous state the user must call the DEREGSTORECOMMAND Function .