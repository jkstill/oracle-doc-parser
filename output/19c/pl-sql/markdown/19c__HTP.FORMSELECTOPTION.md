---
id: 19c__HTP.FORMSELECTOPTION
name: HTP.FORMSELECTOPTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.FORMSELECTOPTION

This procedure generates the <OPTION> tag which represents one choice in a Select element.

## Syntax

```sql
HTP.FORMSELECTOPTION(
   cvalue         IN       VARCHAR2,
   cselected      IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cvalue | VARCHAR2 | IN | The text for the option. |
| cvalue | VARCHAR2 | IN | If the value for this parameter is not NULL , the SELECTED attribute is added to the tag. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.FORMSELECTOPTION( cvalue IN VARCHAR2, cselected IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-37 FORMSELECTOPTION Procedure Parameters Parameter Description cvalue The text for the option. cvalue If the value for this parameter is not NULL , the SELECTED attribute is added to the tag. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <OPTION SELECTED cattributes>cvalue as shown under Examples of the FORMSELECTOPEN Procedure .