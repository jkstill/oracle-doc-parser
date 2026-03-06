---
id: 19c__HTF.AREA
name: HTF.AREA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.AREA

This function generates the <AREA> tag, which defines a client-side image map. The <AREA> tag defines areas within the image and destinations for the areas.

## Syntax

```sql
HTF.AREA (
   ccoords        IN       VARCHAR2
   cshape         IN       VARCHAR2   DEFAULT NULL,
   chref          IN       VARCHAR2   DEFAULT NULL,
   cnohref        IN       VARCHAR2   DEFAULT NULL,
   ctarget        IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ccords |  |  | The value for the COORDS attribute. |
| cshape | VARCHAR2 | IN | The value for the SHAPE attribute. |
| chref | VARCHAR2 | IN | The value for the HREF attribute. |
| cnohref | VARCHAR2 | IN | If the value for this parameter is not NULL , the NOHREF attribute is added to the tag. |
| ctarget | VARCHAR2 | IN | The value for the TARGET attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.AREA ( ccoords IN VARCHAR2 cshape IN VARCHAR2 DEFAULT NULL, chref IN VARCHAR2 DEFAULT NULL, cnohref IN VARCHAR2 DEFAULT NULL, ctarget IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-6 AREA Function Parameters Parameter Description ccords The value for the COORDS attribute. cshape The value for the SHAPE attribute. chref The value for the HREF attribute. cnohref If the value for this parameter is not NULL , the NOHREF attribute is added to the tag. ctarget The value for the TARGET attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <AREA COORDS="ccoords" SHAPE="cshape" HREF="chref" NOHREF TARGET="ctarget" cattributes>