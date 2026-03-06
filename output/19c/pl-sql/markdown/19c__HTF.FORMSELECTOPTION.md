---
id: 19c__HTF.FORMSELECTOPTION
name: HTF.FORMSELECTOPTION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FORMSELECTOPTION

This function generates the <OPTION> tag which represents one choice in a Select element.

## Syntax

```sql
HTF.FORMSELECTOPTION(
   cvalue           IN       VARCHAR2,
   cselected       IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cvalue | VARCHAR2 | IN | The text for the option |
| cvalue | VARCHAR2 | IN | If the value for this parameter is not NULL , the SELECTED attribute is added to the tag. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.FORMSELECTOPTION( cvalue IN VARCHAR2, cselected IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-39 FORMSELECTOPTION Function Parameters Parameter Description cvalue The text for the option cvalue If the value for this parameter is not NULL , the SELECTED attribute is added to the tag. cattributes The other attributes to be included as-is in the tag. Examples This function generates <OPTION SELECTED cattributes>cvalue as shown under the Examples section of the FORMSELECTOPEN Function .