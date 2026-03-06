---
id: 19c__DBMS_QOPATCH.GET_SQLPATCH_STATUS
name: DBMS_QOPATCH.GET_SQLPATCH_STATUS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_QOPATCH
tags: [dbms_qopatch]
source_file: DBMS_QOPATCH.html
---

# DBMS_QOPATCH.GET_SQLPATCH_STATUS

This procedure displays the SQL patch status by querying from SQL patch registry to produce complete patch level information. If the patch number is given, it displays the information specific to the given SQL patch, otherwise information for all SQL patches.

## Syntax

```sql
DBMS_QOPATCH.GET_SQLPATCH_STATUS (
   patchnum IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| patchnum | VARCHAR2 | IN | Patch number |

## Usage Notes

Syntax DBMS_QOPATCH.GET_SQLPATCH_STATUS ( patchnum IN VARCHAR2 DEFAULT NULL); Parameters Table 135-11 GET_SQLPATCH_STATUS Procedure Parameters Parameter Description patchnum Patch number