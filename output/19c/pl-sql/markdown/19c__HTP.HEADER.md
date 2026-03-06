---
id: 19c__HTP.HEADER
name: HTP.HEADER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.HEADER

This procedure generates opening heading tags (<H1> to <H6>) and their corresponding closing tags ( </H1> to </H6>) .

## Syntax

```sql
HTP.HEADER(
   nsize          IN       INTEGER,
   cheader        IN       VARCHAR2,
   calign         IN       VARCHAR2   DEFAULT NULL,
   cnowrap        IN       VARCHAR2   DEFAULT NULL,
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| nsize | INTEGER | IN | The the heading level. This is an integer between 1 and 6. |
| cheader | VARCHAR2 | IN | The text to display in the heading. |
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| cnowrap | VARCHAR2 | IN | The value for the NOWRAP attribute. |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.HEADER( nsize IN INTEGER, cheader IN VARCHAR2, calign IN VARCHAR2 DEFAULT NULL, cnowrap IN VARCHAR2 DEFAULT NULL, cclear IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-46 HEADER Procedure Parameters Parameter Description nsize The the heading level. This is an integer between 1 and 6. cheader The text to display in the heading. calign The value for the ALIGN attribute. cnowrap The value for the NOWRAP attribute. cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag. Examples HTP.header (1,'Overview'); produces: <H1>Overview</H1>