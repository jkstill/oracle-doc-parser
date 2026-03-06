---
id: 19c__HTP.FORMRADIO
name: HTP.FORMRADIO
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.FORMRADIO

This procedure generates the <INPUT> tag with TYPE="radio" , which creates a radio button on the HTML form. Within a set of radio buttons, the user selects only one. Each radio button in the same set has the same name, but different values. The selected radio button generates a name/value pair.

## Syntax

```sql
HTP.FORMRADIO(
   cname          IN       VARCHAR2,
   cvalue         IN       VARCHAR2,
   cchecked       IN       VARCHAR2   DEFAULT NULL,
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

Syntax HTP.FORMRADIO( cname IN VARCHAR2, cvalue IN VARCHAR2, cchecked IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-34 FORMRADIO Procedure Parameters Parameter Description cname The value for the NAME attribute. cvalue The value for the VALUE attribute. cchecked If the value for this parameter is not NULL , the CHECKED attribute is added to the tag. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <INPUT TYPE=" radio " NAME=" cname " VALUE=" cvalue " CHECKED cattributes >