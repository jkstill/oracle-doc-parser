---
id: 19c__HTP.OLISTOPEN
name: HTP.OLISTOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.OLISTOPEN

This procedure generates the <OL> tag which marks the beginning of an ordered list. An ordered list presents a list of numbered items.

## Syntax

```sql
HTP.OLISTOPEN(
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cwrap          IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cwrap | VARCHAR2 | IN | The value for the WRAP attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

To mark the end of a list of this kind, use the OLISTCLOSE Procedure . Numbered items are added using LISTITEM Procedure . Syntax HTP.OLISTOPEN( cclear IN VARCHAR2 DEFAULT NULL, cwrap IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-64 OLISTOPEN Procedure Parameters Parameter Description cclear The value for the CLEAR attribute. cwrap The value for the WRAP attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <OL CLEAR=" cclear " WRAP=" cwrap " cattributes >