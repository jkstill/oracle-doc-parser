---
id: 19c__HTF.PARAGRAPH
name: HTF.PARAGRAPH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.PARAGRAPH

You can use this function to add attributes to the <P> tag created by the PARA Function.

## Syntax

```sql
HTF.PARAGRAPH(
   calign         IN       VARCHAR2   DEFAULT NULL,
   cnowrap        IN       VARCHAR2   DEFAULT NULL,
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| cnowrap | VARCHAR2 | IN | If the value for this parameter is not NULL , the NOWRAP attribute is added to the tag. |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.PARAGRAPH( calign IN VARCHAR2 DEFAULT NULL, cnowrap IN VARCHAR2 DEFAULT NULL, cclear IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-67 PARAGRAPH Function Parameters Parameter Description calign The value for the ALIGN attribute. cnowrap If the value for this parameter is not NULL , the NOWRAP attribute is added to the tag. cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <P ALIGN="calign" NOWRAP CLEAR="cclear" cattributes>