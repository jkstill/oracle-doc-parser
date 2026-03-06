---
id: 19c__HTF.BLOCKQUOTEOPEN
name: HTF.BLOCKQUOTEOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.BLOCKQUOTEOPEN

This function generates the <BLOCKQUOTE> tag, which marks the beginning of a section of quoted text.

## Syntax

```sql
HTF.BLOCKQUOTEOPEN (
   cnowrap        IN       VARCHAR2   DEFAULT NULL,
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cnowrap | VARCHAR2 | IN | If the value for this parameter is not NULL , the NOWRAP attribute is added to the tag. |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

You mark the end of a section of text by means of the BLOCKQUOTECLOSE Function . Syntax HTF.BLOCKQUOTEOPEN ( cnowrap IN VARCHAR2 DEFAULT NULL, cclear IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-11 BLOCKQUOTEOPEN Function Parameters Parameter Description cnowrap If the value for this parameter is not NULL , the NOWRAP attribute is added to the tag. cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <BLOCKQUOTE CLEAR="cclear" NOWRAP cattributes>