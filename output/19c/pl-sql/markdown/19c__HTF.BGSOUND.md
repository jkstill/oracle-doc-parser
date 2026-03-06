---
id: 19c__HTF.BGSOUND
name: HTF.BGSOUND
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.BGSOUND

This function generates the <BGSOUND> tag which includes audio for a Web page.

## Syntax

```sql
HTF.BGSOUND (
   csrc           IN       VARCHAR2,
   cloop          IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| csrc | VARCHAR2 | IN | The value for the SRC attribute. |
| cloop | VARCHAR2 | IN | The value for the LOOP attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.BGSOUND ( csrc IN VARCHAR2, cloop IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-9 BGSOUND Function Parameters Parameter Description csrc The value for the SRC attribute. cloop The value for the LOOP attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <BGSOUND SRC="csrc" LOOP="cloop" cattributes>