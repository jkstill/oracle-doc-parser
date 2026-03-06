---
id: 19c__DBMS_QOPATCH.GET_OPATCH_BUGS
name: DBMS_QOPATCH.GET_OPATCH_BUGS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_QOPATCH
tags: [dbms_qopatch]
source_file: DBMS_QOPATCH.html
---

# DBMS_QOPATCH.GET_OPATCH_BUGS

This function provides a bugs list in a patch if the patch number is given. If a patch number is not given, it lists all the bugs in the specified XML format.

## Syntax

```sql
DBMS_QOPATCH.GET_OPATCH_BUGS (
   patchnum IN VARCHAR2 DEFAULT NULL);
 RETURN XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| patchnum | VARCHAR2 | IN | Patch number |

**Returns:** `XMLTYPE`

## Usage Notes

Syntax DBMS_QOPATCH.GET_OPATCH_BUGS ( patchnum IN VARCHAR2 DEFAULT NULL); RETURN XMLTYPE; Parameters Table 135-4 GET_OPATCH_BUGS Function Parameters Parameter Description patchnum Patch number