---
id: 19c__DBMS_QOPATCH.GET_OPATCH_PREQS
name: DBMS_QOPATCH.GET_OPATCH_PREQS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_QOPATCH
tags: [dbms_qopatch]
source_file: DBMS_QOPATCH.html
---

# DBMS_QOPATCH.GET_OPATCH_PREQS

This function provides prerequisite patches for a given patch as XML element.

## Syntax

```sql
DBMS_QOPATCH.GET_OPATCH_PREQS (
   patchnum IN VARCHAR2);
 RETURN XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| patchnum | VARCHAR2) | IN | Patch number |

**Returns:** `XMLTYPE`

## Usage Notes

Syntax DBMS_QOPATCH.GET_OPATCH_PREQS ( patchnum IN VARCHAR2); RETURN XMLTYPE; Parameters Table 135-9 GET_OPATCH_PREQS Function Parameters Parameter Description patchnum Patch number