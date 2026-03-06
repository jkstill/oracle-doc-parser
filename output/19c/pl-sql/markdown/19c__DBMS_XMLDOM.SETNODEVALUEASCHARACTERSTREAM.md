---
id: 19c__DBMS_XMLDOM.SETNODEVALUEASCHARACTERSTREAM
name: DBMS_XMLDOM.SETNODEVALUEASCHARACTERSTREAM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SETNODEVALUEASCHARACTERSTREAM

The operation of these subprograms is described in the syntax section.

## Syntax

```sql
DBMS_XMLDOM.SETNODEVALUEASCHARACTERSTREAM  (
   n        IN     DOMNODE)
 RETURN SYS.UTL_CHARACTEROUTPUTSTREAM;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE |
| value |  |  | CHARACTERINPUTSTREAM |

**Returns:** `SYS.UTL_CHARACTEROUTPUTSTREAM`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax This function returns an instance of the PL/SQL XMLCHARACTEROUTPUTSTREAM type into which the caller can write the node value. The datatype of the node can be any valid XDB datatype. If the type is not character or CLOB , the character data written to the stream is converted to the node datatype. If the datatype of the node is character or CLOB , then the character data written to the stream is converted from PL/SQL session character set to the character set of the node. DBMS_XMLDOM.SETNODEVALUEASCHARACTERSTREAM ( n IN DOMNODE) RETURN SYS.UTL_CHARACTEROUTPUTSTREAM; Using this procedure, the application passes in an implementation of SYS . UTL_CHARACTERINPUTSTREAM from which XDB reads to populate the node. The datatype of the node may be any valid type supported by XDB. If a non-character datatype, the character data read from the stream is converted to the datatype of the node. If the datatype of the node is either character or CLOB , then no conversion occurs and the character set of the node becomes the character set of the PL/SQL session. DBMS_XMLDOM.SETNODEVALUEASCHARACTERSTREAM ( n IN DOMNODE, value IN SYS.UTL_CHARACTERINPUTSTREAM); Parameters Table 204-127 SETNODEVALUEASCHARACTERSTREAM Function & Procedure Parameters Parameter Description n DOMNODE value CHARACTERINPUTSTREAM