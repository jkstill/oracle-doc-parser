---
id: 19c__HTP.ULISTOPEN
name: HTP.ULISTOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.ULISTOPEN

This procedure generates the <UL> tag which marks the beginning of an unordered list. An unordered list presents items with bullets.

## Syntax

```sql
HTP.ULISTOPEN(
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cwrap          IN       VARCHAR2   DEFAULT NULL,
   cdingbat       IN       VARCHAR2   DEFAULT NULL,
   csrc           IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cwrap | VARCHAR2 | IN | The value for the WRAP attribute. |
| cdingbat | VARCHAR2 | IN | The value for the DINGBAT attribute. |
| csrc | VARCHAR2 | IN | The value for the SRC attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

To mark the end of an unordered list, use the ULISTCLOSE Procedure . Add list items with LISTITEM Procedure . Syntax HTP.ULISTOPEN( cclear IN VARCHAR2 DEFAULT NULL, cwrap IN VARCHAR2 DEFAULT NULL, cdingbat IN VARCHAR2 DEFAULT NULL, csrc IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-89 ULISTOPEN Procedure Parameters Parameter Description cclear The value for the CLEAR attribute. cwrap The value for the WRAP attribute. cdingbat The value for the DINGBAT attribute. csrc The value for the SRC attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <UL CLEAR=" cclear " WRAP=" cwrap " DINGBAT=" cdingbat " SRC=" csrc " cattributes >