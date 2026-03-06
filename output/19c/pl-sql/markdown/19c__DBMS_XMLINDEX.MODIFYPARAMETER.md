---
id: 19c__DBMS_XMLINDEX.MODIFYPARAMETER
name: DBMS_XMLINDEX.MODIFYPARAMETER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLINDEX
tags: [dbms_xmlindex]
source_file: DBMS_XMLINDEX.html
---

# DBMS_XMLINDEX.MODIFYPARAMETER

This procedure modifies the XMLIndex parameter string that is associated with a given parameter identifier.

## Syntax

```sql
DBMS_XMLINDEX.MODIFYPARAMETER (
   name        IN      VARCHAR2, 
   parameter   IN      CLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Identifier for parameter string |
| parameter | CLOB) | IN | XMLIndex parameter clause that can appear in a CREATE INDEX or an ALTER INDEX statement |

## Usage Notes

Syntax DBMS_XMLINDEX.MODIFYPARAMETER ( name IN VARCHAR2, parameter IN CLOB); Parameters Table 206-5 MODIFYPARAMETER Procedure Parameters Parameter Description name Identifier for parameter string parameter XMLIndex parameter clause that can appear in a CREATE INDEX or an ALTER INDEX statement Examples DBMS_XMLINDEX.MODIFYPARAMETER ( 'myIndexParam', 'PATH TABLE po_ptab PATH ID INDEX po_pidx ORDER KEY INDEX po_oidx VALUE INDEX po_vidx');