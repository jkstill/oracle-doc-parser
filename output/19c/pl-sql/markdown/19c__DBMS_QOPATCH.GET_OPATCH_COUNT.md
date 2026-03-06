---
id: 19c__DBMS_QOPATCH.GET_OPATCH_COUNT
name: DBMS_QOPATCH.GET_OPATCH_COUNT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_QOPATCH
tags: [dbms_qopatch]
source_file: DBMS_QOPATCH.html
---

# DBMS_QOPATCH.GET_OPATCH_COUNT

This function provides the total number of installed patches in XML format.

## Syntax

```sql
DBMS_QOPATCH.GET_OPATCH_COUNT (
   patchnum IN VARCHAR2);
 RETURN XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| patchnum | VARCHAR2) | IN | Patch number |

**Returns:** `XMLTYPE`

## Usage Notes

Syntax DBMS_QOPATCH.GET_OPATCH_COUNT ( patchnum IN VARCHAR2); RETURN XMLTYPE; Parameters Table 135-5 GET_OPATCH_COUNT Function Parameters Parameter Description patchnum Patch number