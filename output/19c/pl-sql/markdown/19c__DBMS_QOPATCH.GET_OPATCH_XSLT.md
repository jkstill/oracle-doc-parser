---
id: 19c__DBMS_QOPATCH.GET_OPATCH_XSLT
name: DBMS_QOPATCH.GET_OPATCH_XSLT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_QOPATCH
tags: [dbms_qopatch]
source_file: DBMS_QOPATCH.html
---

# DBMS_QOPATCH.GET_OPATCH_XSLT

This function returns the style-sheet for the opatch XML inventory presentation. You can use the return type of this subprogram to perform XMLTRANSFORM and the transformed result has the same appearance as opatch text output.

## Syntax

```sql
DBMS_QOPATCH.GET_OPATCH_XSLT
 RETURN XMLTYPE;
```

**Returns:** `XMLTYPE`

## Usage Notes

Syntax DBMS_QOPATCH.GET_OPATCH_XSLT RETURN XMLTYPE;