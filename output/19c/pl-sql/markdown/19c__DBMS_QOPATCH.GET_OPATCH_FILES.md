---
id: 19c__DBMS_QOPATCH.GET_OPATCH_FILES
name: DBMS_QOPATCH.GET_OPATCH_FILES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_QOPATCH
tags: [dbms_qopatch]
source_file: DBMS_QOPATCH.html
---

# DBMS_QOPATCH.GET_OPATCH_FILES

This function provides the list of files modified in the given patch number in XML format.

## Syntax

```sql
DBMS_QOPATCH.GET_OPATCH_FILES (
   patchnum IN VARCHAR2);
 RETURN XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| patchnum | VARCHAR2) | IN | Patch number |

**Returns:** `XMLTYPE`

## Usage Notes

Syntax DBMS_QOPATCH.GET_OPATCH_FILES ( patchnum IN VARCHAR2); RETURN XMLTYPE; Parameters Table 135-7 GET_OPATCH_FILES Function Parameters Parameter Description patchnum Patch number