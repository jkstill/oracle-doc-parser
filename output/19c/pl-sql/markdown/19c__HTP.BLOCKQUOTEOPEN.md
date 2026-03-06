---
id: 19c__HTP.BLOCKQUOTEOPEN
name: HTP.BLOCKQUOTEOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.BLOCKQUOTEOPEN

This procedure generates the <BLOCKQUOTE> tag, which marks the beginning of a section of quoted text.

## Syntax

```sql
HTP.BLOCKQUOTEOPEN (
   cnowrap        IN       VARCHAR2   DEFAULT NULL,
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cnowrap | VARCHAR2 | IN | If the value for this parameter is not NULL , the NOWRAP attribute is added to the tag. |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

You mark the end of a section of text by means of the BLOCKQUOTECLOSE Procedure . Syntax HTP.BLOCKQUOTEOPEN ( cnowrap IN VARCHAR2 DEFAULT NULL, cclear IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-11 BLOCKQUOTEOPEN Procedure Parameters Parameter Description cnowrap If the value for this parameter is not NULL , the NOWRAP attribute is added to the tag. cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <BLOCKQUOTE CLEAR=" cclear " NOWRAP cattributes >