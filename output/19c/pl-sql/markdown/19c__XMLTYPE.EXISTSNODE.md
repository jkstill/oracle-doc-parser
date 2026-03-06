---
id: 19c__XMLTYPE.EXISTSNODE
name: XMLTYPE.EXISTSNODE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.EXISTSNODE

This member function checks if the node exists.

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xpath |  |  | The XPath expression to test. |
| nsmap |  |  | Optional namespace mapping. |

## Usage Notes

If the XPath string is NULL or the document is empty, then a value of 0 is returned, otherwise returns 1. The options are described in the following table.