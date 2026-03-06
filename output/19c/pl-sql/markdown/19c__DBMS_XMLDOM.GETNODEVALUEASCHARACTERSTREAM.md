---
id: 19c__DBMS_XMLDOM.GETNODEVALUEASCHARACTERSTREAM
name: DBMS_XMLDOM.GETNODEVALUEASCHARACTERSTREAM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETNODEVALUEASCHARACTERSTREAM

The operation of these subprograms is described with each syntax implementation.

## Syntax

```sql
DBMS_XMLDOM.GETNODEVALUEASCHARACTERSTREAM  (
   n        IN     DOMNODE)
 RETURN SYS.UTL_CHARACTERINPUTSTREAM;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE |
| value |  |  | CHARACTEROUTPUTSTREAM |

**Returns:** `SYS.UTL_CHARACTERINPUTSTREAM`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax This function returns an instance of the PL/SQL XMLCharacterInputStream . If the node data is character it is converted to the current session character set. If the node data is not character data, it is first converted to character data. DBMS_XMLDOM.GETNODEVALUEASCHARACTERSTREAM ( n IN DOMNODE) RETURN SYS.UTL_CHARACTERINPUTSTREAM; Using this procedure, the node data is converted, as necessary, to the session character set and then "pushed" into the SYS . UTL_CHARACTEROUTPUTSTREAM . DBMS_XMLDOM.GETNODEVALUEASCHARACTERSTREAM ( n IN DOMNODE, value IN SYS.UTL_CHARACTEROUTPUTSTREAM); Parameters Table 204-68 GETNODEVALUEASCHARACTERSTREAM Function & Procedure Parameters Parameter Description n DOMNODE value CHARACTEROUTPUTSTREAM