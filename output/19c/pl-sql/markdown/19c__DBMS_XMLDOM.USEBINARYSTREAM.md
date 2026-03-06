---
id: 19c__DBMS_XMLDOM.USEBINARYSTREAM
name: DBMS_XMLDOM.USEBINARYSTREAM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.USEBINARYSTREAM

This function returns TRUE if the datatype of the node is RAW or BLOB , so that the node value may be read or written using an UTL_BINARYINPUTSTREAM or UTL_BINARYOUTPUTSTREAM .

## Syntax

```sql
DBMS_XMLDOM.USEBINARYSTREAM   (
   n        IN     DOMNODE)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE |

**Returns:** `BOOLEAN`

## Usage Notes

If a value of FALSE is returned, the node value may only be accessed through an UTL_CHARACTERINPUTSTREAM or UTL_CHARACTEROUTPUTSTREAM . See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.USEBINARYSTREAM ( n IN DOMNODE) RETURN BOOLEAN; Parameters Table 204-134 USEBINARYSTREAM Function Parameters Parameter Description n DOMNODE