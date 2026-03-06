---
id: 19c__DBMS_QOPATCH.IS_PATCH_INSTALLED
name: DBMS_QOPATCH.IS_PATCH_INSTALLED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_QOPATCH
tags: [dbms_qopatch]
source_file: DBMS_QOPATCH.html
---

# DBMS_QOPATCH.IS_PATCH_INSTALLED

This function provides information (such as patchID, application date, and SQL patch information) on the installed patch as XML node by querying the XML inventory.

## Syntax

```sql
DBMS_QOPATCH.IS_PATCH_INSTALLED (
   patchnum IN VARCHAR2);
 RETURN XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| patchnum | VARCHAR2) | IN | Patch number |

**Returns:** `XMLTYPE`

## Usage Notes

Syntax DBMS_QOPATCH.IS_PATCH_INSTALLED ( patchnum IN VARCHAR2); RETURN XMLTYPE; Parameters Table 135-12 IS_PATCH_INSTALLED Function Parameters Parameter Description patchnum Patch number