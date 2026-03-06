---
id: 19c__XMLTYPE.EXTRACT
name: XMLTYPE.EXTRACT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.EXTRACT

This member function extracts an XMLType fragment and returns an XMLType instance containing the result nodes. If the XPath does not result in any nodes, it then returns NULL .

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xpath |  |  | The XPath expression to apply. |
| nsmap |  |  | Optional prefix to namespace mapping information. |

## Usage Notes

The options are described in the following table.