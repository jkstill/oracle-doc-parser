---
id: 19c__DBMS_XMLINDEX.REGISTERPARAMETER
name: DBMS_XMLINDEX.REGISTERPARAMETER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLINDEX
tags: [dbms_xmlindex]
source_file: DBMS_XMLINDEX.html
---

# DBMS_XMLINDEX.REGISTERPARAMETER

This procedure registers a parameter identifier and XMLIndex parameter string pair in XDB.

## Syntax

```sql
DBMS_XMLINDEX.REGISTERPARAMETER (
   name        IN      VARCHAR2, 
   parameter   IN      CLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Identifier for parameter string |
| parameter | CLOB) | IN | XMLIndex parameter clause that can appear in a CREATE INDEX or an ALTER INDEX statement |

## Usage Notes

Syntax DBMS_XMLINDEX.REGISTERPARAMETER ( name IN VARCHAR2, parameter IN CLOB); Parameters Table 206-7 REGISTERPARAMETER Procedure Parameters Parameter Description name Identifier for parameter string parameter XMLIndex parameter clause that can appear in a CREATE INDEX or an ALTER INDEX statement Examples DBMS_XMLINDEX.REGISTERPARAMETER ( 'myIndexParam', 'PATH TABLE po_ptab PATH ID INDEX po_pidx ORDER KEY INDEX po_oidx VALUE INDEX po_vidx PATHS(NAMESPACE MAPPING(xmlns:p="http://www.example.com/IPO")) GROUP MASTERGROUP XMLTABLE PO_TAB (''/p:PurchaseOrder'' COLUMNS REFERENCE VARCHAR2(30) PATH ''p:Reference'', REQUESTOR VARCHAR2(30) PATH ''p:Requestor'' ) GROUP ITEMGROUP XMLTABLE ITEMGROUP_TAB (''/p:PurchaseOrder/p:LineItems/p:LineItem'' COLUMNS LINENUMBER NUMBER(38) PATH ''@p:ItemNumber'', QUANTITY NUMBER(38) PATH ''@p:Quantity'', DESCRIPTION VARCHAR2(256) PATH ''p:Description'''));