---
id: 19c__HTF.LISTITEM
name: HTF.LISTITEM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.LISTITEM

This function generates the <LI> tag, which indicates a list item.

## Syntax

```sql
HTF.LISTITEM(
   ctext          IN       VARCHAR2   DEFAULT NULL,
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cdingbat       IN       VARCHAR2   DEFAULT NULL,
   csrc           IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text for the list item. |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cdingbat | VARCHAR2 | IN | The value for the DINGBAT attribute. |
| csrc | VARCHAR2 | IN | The value for the SRC attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.LISTITEM( ctext IN VARCHAR2 DEFAULT NULL, cclear IN VARCHAR2 DEFAULT NULL, cdingbat IN VARCHAR2 DEFAULT NULL, csrc IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-60 LISTITEM Function Parameters Parameter Description ctext The text for the list item. cclear The value for the CLEAR attribute. cdingbat The value for the DINGBAT attribute. csrc The value for the SRC attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <LI CLEAR="cclear" DINGBAT="cdingbat" SRC="csrc" cattributes>ctext