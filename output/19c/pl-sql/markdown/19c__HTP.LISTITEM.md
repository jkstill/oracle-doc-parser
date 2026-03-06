---
id: 19c__HTP.LISTITEM
name: HTP.LISTITEM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.LISTITEM

This procedure generates the <LI> tag, which indicates a list item.

## Syntax

```sql
HTP.LISTITEM(
   ctext          IN       VARCHAR2   DEFAULT NULL,
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cdingbat       IN       VARCHAR2   DEFAULT NULL,
   csrc           IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text for the list item. |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cdingbat | VARCHAR2 | IN | The value for the DINGBAT attribute. |
| csrc | VARCHAR2 | IN | The value for the SRC attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.LISTITEM( ctext IN VARCHAR2 DEFAULT NULL, cclear IN VARCHAR2 DEFAULT NULL, cdingbat IN VARCHAR2 DEFAULT NULL, csrc IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-58 LISTITEM Procedure Parameters Parameter Description ctext The text for the list item. cclear The value for the CLEAR attribute. cdingbat The value for the DINGBAT attribute. csrc The value for the SRC attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <LI CLEAR=" cclear " DINGBAT=" cdingbat " SRC=" csrc " cattributes > ctext