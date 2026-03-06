---
id: 19c__DBMS_XMLDOM.GETNODEVALUEASBINARYSTREAM
name: DBMS_XMLDOM.GETNODEVALUEASBINARYSTREAM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETNODEVALUEASBINARYSTREAM

The operation of these subprograms is described with each syntax implementation.

## Syntax

```sql
DBMS_XMLDOM.GETNODEVALUEASBINARYSTREAM (
   n      IN     DOMNODE)
 RETURN SYS.UTL_BINARYINPUTSTREAM;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE |
| value |  |  | BINARYOUTPUTSTREAM |

**Returns:** `SYS.UTL_BINARYINPUTSTREAM`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax This function returns an instance of the PL/SQL XMLBinaryInputStream . The node datatype must be RAW or BLOB – if not an exception is raised. DBMS_XMLDOM.GETNODEVALUEASBINARYSTREAM ( n IN DOMNODE) RETURN SYS.UTL_BINARYINPUTSTREAM; Using this procedure, the application passes an implementation of SYS . UTL_BINARYOUTPUTSTREAM into which XDB writes the contents of the node. The datatype of the node must be RAW or CLOB – if not an exception is raised. DBMS_XMLDOM.GETNODEVALUEASBINARYSTREAM ( n in DOMNODE, value in SYS.UTL_BINARYOUTPUTSTREAM); Parameters Table 204-67 GETNODEVALUEASBINARYSTREAM Function & Procedure Parameters Parameter Description n DOMNODE value BINARYOUTPUTSTREAM