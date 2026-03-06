---
id: 19c__DBMS_QOPATCH.GET_OPATCH_DATA
name: DBMS_QOPATCH.GET_OPATCH_DATA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_QOPATCH
tags: [dbms_qopatch]
source_file: DBMS_QOPATCH.html
---

# DBMS_QOPATCH.GET_OPATCH_DATA

This function provides top level patch information for the patch (such as Patch ID, patch creation time) in the XML element.

## Syntax

```sql
DBMS_QOPATCH.GET_OPATCH_DATA (
   patchnum IN VARCHAR2);
 RETURN XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| patchnum | VARCHAR2) | IN | Patch number |

**Returns:** `XMLTYPE`

## Usage Notes

Syntax DBMS_QOPATCH.GET_OPATCH_DATA ( patchnum IN VARCHAR2); RETURN XMLTYPE; Parameters Table 135-6 GET_OPATCH_DATA Function Parameters Parameter Description patchnum Patch number