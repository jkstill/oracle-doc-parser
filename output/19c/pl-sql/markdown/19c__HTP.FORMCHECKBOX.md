---
id: 19c__HTP.FORMCHECKBOX
name: HTP.FORMCHECKBOX
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.FORMCHECKBOX

This procedure generates the <INPUT> tag with TYPE="checkbox" which inserts a checkbox element in a form.

## Syntax

```sql
HTP.FORMCHECKBOX(
   cname          IN       VARCHAR2,
   cvalue         IN       VARCHAR2   DEFAULT 'ON',
   cchecked       IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cvalue | VARCHAR2 | IN | The value for the VALUE attribute. |
| cchecked | VARCHAR2 | IN | If the value for this parameter is not NULL , the CHECKED attribute is added to the tag. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

A checkbox element is a button that the user toggles on or off. Syntax HTP.FORMCHECKBOX( cname IN VARCHAR2, cvalue IN VARCHAR2 DEFAULT 'ON', cchecked IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-28 FORMCHECKBOX Procedure Parameters Parameter Description cname The value for the NAME attribute. cvalue The value for the VALUE attribute. cchecked If the value for this parameter is not NULL , the CHECKED attribute is added to the tag. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <INPUT TYPE=" checkbox " NAME=" cname " VALUE=" cvalue " CHECKED cattributes >