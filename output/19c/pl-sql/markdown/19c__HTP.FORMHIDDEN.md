---
id: 19c__HTP.FORMHIDDEN
name: HTP.FORMHIDDEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.FORMHIDDEN

This procedure generates the <INPUT> tag with TYPE=" hidden ", which inserts a hidden form element.

## Syntax

```sql
HTP.FORMHIDDEN(
   cname          IN       VARCHAR2,
   cvalue         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cvalue | VARCHAR2 | IN | The value for the VALUE attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

This element is not seen by the user. It submits additional values to the script. Syntax HTP.FORMHIDDEN( cname IN VARCHAR2, cvalue IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-31 FORMHIDDEN Procedure Parameters Parameter Description cname The value for the NAME attribute. cvalue The value for the VALUE attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <INPUT TYPE="hidden" NAME=" cname " VALUE=" cvalue " cattributes >