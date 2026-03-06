---
id: 19c__DBMS_QOPATCH.GET_OPATCH_OLAYS
name: DBMS_QOPATCH.GET_OPATCH_OLAYS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_QOPATCH
tags: [dbms_qopatch]
source_file: DBMS_QOPATCH.html
---

# DBMS_QOPATCH.GET_OPATCH_OLAYS

This function provides overlay patches for a given patch as XML element.

## Syntax

```sql
DBMS_QOPATCH.GET_OPATCH_OLAYS (
   patchnum IN VARCHAR2);
 RETURN XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| patchnum | VARCHAR2) | IN | Patch number |

**Returns:** `XMLTYPE`

## Usage Notes

Syntax DBMS_QOPATCH.GET_OPATCH_OLAYS ( patchnum IN VARCHAR2); RETURN XMLTYPE; Parameters Table 135-8 GET_OPATCH_OLAYS Function Parameters Parameter Description patchnum Patch number