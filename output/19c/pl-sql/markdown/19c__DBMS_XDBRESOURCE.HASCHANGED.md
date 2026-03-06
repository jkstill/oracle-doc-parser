---
id: 19c__DBMS_XDBRESOURCE.HASCHANGED
name: DBMS_XDBRESOURCE.HASCHANGED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.HASCHANGED

Given an XPath, this function determines whether the element or attribute represented by the XPath has changed.

## Syntax

```sql
DBMS_XDBRESOURCE.HASCHANGED (
   res         IN    XDBResource, 
   xpath       IN    VARCHAR2,
   namespace   IN    VARCHAR2) 
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource | IN | XDBResource |
| xpath | VARCHAR2 | IN | XPath to check |
| bnamespace |  |  | Namespace to use |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDBRESOURCE.HASCHANGED ( res IN XDBResource, xpath IN VARCHAR2, namespace IN VARCHAR2) RETURN BOOLEAN; Parameters Table 200-26 HASCHANGED Function Parameters Parameter Description res XDBResource xpath XPath to check bnamespace Namespace to use