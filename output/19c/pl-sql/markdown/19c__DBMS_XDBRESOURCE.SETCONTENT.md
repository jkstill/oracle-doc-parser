---
id: 19c__DBMS_XDBRESOURCE.SETCONTENT
name: DBMS_XDBRESOURCE.SETCONTENT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.SETCONTENT

This procedure replaces the contents of the given resource with the given datatype.

## Syntax

```sql
DBMS_XDBRESOURCE.SETCONTENT (
   res      IN OUT  XDBResource, 
   data     IN      BFILE,
   csid     IN      NUMBER);

DBMS_XDBRESOURCE.SETCONTENT (
   res      IN OUT  XDBResource, 
   data     IN      BLOB,
   csid     IN      PLS_INTEGER);

DBMS_XDBRESOURCE.SETCONTENT (
   res      IN OUT  XDBResource, 
   data     IN      CLOB);

DBMS_XDBRESOURCE.SETCONTENT (
   res      IN OUT  XDBResource, 
   data     IN      REF SYS.XMLType,
   sticky   IN      BOOLEAN := TRUE);

DBMS_XDBRESOURCE.SETCONTENT (
   res      IN OUT  XDBResource, 
   data     IN      VARCHAR2);

DBMS_XDBRESOURCE.SETCONTENT (
   res      IN OUT  XDBResource, 
   data     IN      SYS.XMLType);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource | IN OUT | XDBResource |
| data | BFILE | IN | Data input as BFILE , BLOB , CLOB , string, XMLType |
| csid | NUMBER) | IN | Character set ID of the BFILE , BLOB |
| sticky | BOOLEAN | IN | If TRUE creates a sticky REF , otherwise non-sticky |

## Usage Notes

Syntax DBMS_XDBRESOURCE.SETCONTENT ( res IN OUT XDBResource, data IN BFILE, csid IN NUMBER); DBMS_XDBRESOURCE.SETCONTENT ( res IN OUT XDBResource, data IN BLOB, csid IN PLS_INTEGER); DBMS_XDBRESOURCE.SETCONTENT ( res IN OUT XDBResource, data IN CLOB); DBMS_XDBRESOURCE.SETCONTENT ( res IN OUT XDBResource, data IN REF SYS.XMLType, sticky IN BOOLEAN := TRUE); DBMS_XDBRESOURCE.SETCONTENT ( res IN OUT XDBResource, data IN VARCHAR2); DBMS_XDBRESOURCE.SETCONTENT ( res IN OUT XDBResource, data IN SYS.XMLType); Parameters Table 200-49 SETCONTENT Procedure Parameters Parameter Description res XDBResource data Data input as BFILE , BLOB , CLOB , string, XMLType csid Character set ID of the BFILE , BLOB sticky If TRUE creates a sticky REF , otherwise non-sticky