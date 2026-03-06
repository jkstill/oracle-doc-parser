---
id: 19c__HTP.FORMPASSWORD
name: HTP.FORMPASSWORD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.FORMPASSWORD

This procedure generates the <INPUT> tag with TYPE="password" which creates a single-line text entry field. When the user enters text in the field, each character is represented by one asterisk. This is used for entering passwords.

## Syntax

```sql
HTP.FORMPASSWORD(
   cname          IN       VARCHAR2,
   csize          IN       VARCHAR2,
   cmaxlength     IN       VARCHAR2   DEFAULT NULL,
   cvalue         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| csize | VARCHAR2 | IN | The value for the SIZE attribute. |
| cmaxlength | VARCHAR2 | IN | The value for the MAXLENGTH attribute. |
| cvalue | VARCHAR2 | IN | The value for the VALUE attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.FORMPASSWORD( cname IN VARCHAR2, csize IN VARCHAR2, cmaxlength IN VARCHAR2 DEFAULT NULL, cvalue IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-33 FORMPASSWORD Procedure Parameters Parameter Description cname The value for the NAME attribute. csize The value for the SIZE attribute. cmaxlength The value for the MAXLENGTH attribute. cvalue The value for the VALUE attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <INPUT TYPE=" password " NAME=" cname " SIZE=" csize " MAXLENGTH=" cmaxlength " VALUE=" cvalue " cattributes >