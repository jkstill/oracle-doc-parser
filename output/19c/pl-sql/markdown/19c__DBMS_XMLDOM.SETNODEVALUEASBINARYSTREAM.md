---
id: 19c__DBMS_XMLDOM.SETNODEVALUEASBINARYSTREAM
name: DBMS_XMLDOM.SETNODEVALUEASBINARYSTREAM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SETNODEVALUEASBINARYSTREAM

The operation of these subprograms is described in the syntax section.

## Syntax

```sql
DBMS_XMLDOM.SETNODEVALUEASBINARYSTREAM (
   n      IN     DOMNODE)
 RETURN SYS.UTL_BINARYOUTPUTSTREAM;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE |
| value |  |  | BINARYINPUTSTREAM |

**Returns:** `SYS.UTL_BINARYOUTPUTSTREAM`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax This function returns an instance of the PL/SQL XMLBINARYOUTPUTSTREAM into which the caller can write the node value. The datatype of the node must be RAW or BLOB – if not, an exception is raised. DBMS_XMLDOM.SETNODEVALUEASBINARYSTREAM ( n IN DOMNODE) RETURN SYS.UTL_BINARYOUTPUTSTREAM; Using this procedure, the application passes in an implementation of sys . utl_BinaryInputStream from which XDB reads data to populate the node. The datatype of the node must be RAW or BLOB – if not an exception is raised. DBMS_XMLDOM.SETNODEVALUEASBINARYSTREAM ( n in DOMNODE, value in SYS.UTL_BINARYINPUTSTREAM); Parameters Table 204-126 SETNODEVALUEASBINARYSTREAM Function & Procedure Parameters Parameter Description n DOMNODE value BINARYINPUTSTREAM