---
id: 19c__HTP.DLISTTERM
name: HTP.DLISTTERM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.DLISTTERM

This procedure generates the <DT> tag which defines a term in a definition list <DL> .

## Syntax

```sql
HTP.DLISTTERM (
   ctext          IN       VARCHAR2   DEFAULT NULL,
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The term. |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.DLISTTERM ( ctext IN VARCHAR2 DEFAULT NULL, cclear IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-23 DLISTTERM Procedure Parameters Parameter Description ctext The term. cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <DT CLEAR=" cclear " cattributes > ctext