---
id: 19c__HTP.FORMSUBMIT
name: HTP.FORMSUBMIT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.FORMSUBMIT

This procedure generates the <INPUT> tag with TYPE="submit" which creates a button that, when clicked, submits the form. If the button has a NAME attribute, the button contributes a name/value pair to the submitted data.

## Syntax

```sql
HTP.FORMSUBMIT(
   cname          IN       VARCHAR2   DEFAULT NULL,
   cvalue        IN       VARCHAR2   DEFAULT 'Submit',
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cvalue | VARCHAR2 | IN | The value for the VALUE attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.FORMSUBMIT( cname IN VARCHAR2 DEFAULT NULL, cvalue IN VARCHAR2 DEFAULT 'Submit', cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-38 FORMSUBMIT Procedure Parameters Parameter Description cname The value for the NAME attribute. cvalue The value for the VALUE attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <INPUT TYPE="submit" NAME=" cname " VALUE=" cvalue " cattributes >