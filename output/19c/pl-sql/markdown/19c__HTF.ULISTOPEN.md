---
id: 19c__HTF.ULISTOPEN
name: HTF.ULISTOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.ULISTOPEN

This function generates the <UL> tag which marks the beginning of an unordered list. An unordered list presents items with bullets.

## Syntax

```sql
HTF.ULISTOPEN(
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cwrap          IN       VARCHAR2   DEFAULT NULL,
   cdingbat       IN       VARCHAR2   DEFAULT NULL,
   csrc           IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cwrap | VARCHAR2 | IN | The value for the WRAP attribute. |
| cdingbat | VARCHAR2 | IN | The value for the DINGBAT attribute. |
| csrc | VARCHAR2 | IN | The value for the SRC attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

To mark the end of an unordered list, use the ULISTCLOSE Function . Add list items with LISTITEM Function . Syntax HTF.ULISTOPEN( cclear IN VARCHAR2 DEFAULT NULL, cwrap IN VARCHAR2 DEFAULT NULL, cdingbat IN VARCHAR2 DEFAULT NULL, csrc IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-89 ULISTOPEN Function Parameters Parameter Description cclear The value for the CLEAR attribute. cwrap The value for the WRAP attribute. cdingbat The value for the DINGBAT attribute. csrc The value for the SRC attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <UL CLEAR="cclear" WRAP="cwrap" DINGBAT="cdingbat" SRC="csrc" cattributes>