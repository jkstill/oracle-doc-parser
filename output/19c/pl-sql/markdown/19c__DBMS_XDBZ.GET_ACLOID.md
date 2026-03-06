---
id: 19c__DBMS_XDBZ.GET_ACLOID
name: DBMS_XDBZ.GET_ACLOID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBZ
tags: [dbms_xdbz]
source_file: DBMS_XDBZ.html
---

# DBMS_XDBZ.GET_ACLOID

This function retrieves the ACL Object ID for the specified resource, if the repository path is known.

## Syntax

```sql
DBMS_XDBZ.GET_ACLOID(
   aclpath   IN   VARCHAR2,
   acloid    OUT  RAW)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| aclpath | VARCHAR2 | IN | ACL resource path for the repository |
| acloid | RAW) | OUT | Returned Object ID |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDBZ.GET_ACLOID( aclpath IN VARCHAR2, acloid OUT RAW) RETURN BOOLEAN; Parameters Table 202-7 GET_ACLOID Function Parameters Parameter Description aclpath ACL resource path for the repository acloid Returned Object ID Return Values Returns TRUE if successful.