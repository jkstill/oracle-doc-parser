---
id: 19c__HTF.HEADER
name: HTF.HEADER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.HEADER

This function generates opening heading tags (<H1> to <H6>) and their corresponding closing tags ( </H1> to </H6>) .

## Syntax

```sql
HTF.HEADER(
   nsize          IN       INTEGER,
   cheader        IN       VARCHAR2,
   calign         IN       VARCHAR2   DEFAULT NULL,
   cnowrap        IN       VARCHAR2   DEFAULT NULL,
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| nsize | INTEGER | IN | The heading level. This is an integer between 1 and 6. |
| cheader | VARCHAR2 | IN | The text to display in the heading. |
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| cnowrap | VARCHAR2 | IN | The value for the NOWRAP attribute. |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.HEADER( nsize IN INTEGER, cheader IN VARCHAR2, calign IN VARCHAR2 DEFAULT NULL, cnowrap IN VARCHAR2 DEFAULT NULL, cclear IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-48 HEADER Function Parameters Parameter Description nsize The heading level. This is an integer between 1 and 6. cheader The text to display in the heading. calign The value for the ALIGN attribute. cnowrap The value for the NOWRAP attribute. cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag. Examples HTF.header (1,'Overview') RETURN VARCHAR2; produces: <H1>Overview</H1>