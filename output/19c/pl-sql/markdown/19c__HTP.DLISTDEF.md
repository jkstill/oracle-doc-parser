---
id: 19c__HTP.DLISTDEF
name: HTP.DLISTDEF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.DLISTDEF

This procedure generates the <DD> tag, which inserts definitions of terms. Use this tag for a definition list <DL> . Terms are tagged <DT> and definitions are tagged <DD> .

## Syntax

```sql
HTP.DLISTDEF (
   ctext          IN       VARCHAR2   DEFAULT NULL,
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The definition of the term. |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.DLISTDEF ( ctext IN VARCHAR2 DEFAULT NULL, cclear IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-21 DLISTDEF Procedure Parameters Parameter Description ctext The definition of the term. cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <DD CLEAR=" cclear " cattributes > ctext