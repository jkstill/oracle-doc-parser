---
id: 19c__HTP.BGSOUND
name: HTP.BGSOUND
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.BGSOUND

This procedure generates the <BGSOUND> tag which includes audio for a Web page.

## Syntax

```sql
HTP.BGSOUND (
   csrc           IN       VARCHAR2,
   cloop          IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| csrc | VARCHAR2 | IN | The value for the SRC attribute. |
| cloop | VARCHAR2 | IN | The value for the LOOP attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.BGSOUND ( csrc IN VARCHAR2, cloop IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-9 BGSOUND Procedure Parameters Parameter Description csrc The value for the SRC attribute. cloop The value for the LOOP attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <BGSOUND SRC=" csrc " LOOP=" cloop " cattributes >