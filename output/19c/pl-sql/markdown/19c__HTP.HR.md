---
id: 19c__HTP.HR
name: HTP.HR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.HR

This procedure generates the <HR> tag, which generates a line in the HTML document.

## Syntax

```sql
HTP.HR(
   cclear         IN       VARCHAR2   DEFAULT NULL,
   csrc           IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| csrc | VARCHAR2 | IN | The value for the SRC attribute which specifies a custom image as the source of the line. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

This subprogram performs the same operation as the LINE Procedure . Syntax HTP.HR( cclear IN VARCHAR2 DEFAULT NULL, csrc IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-47 HR Procedure Parameters Parameter Description cclear The value for the CLEAR attribute. csrc The value for the SRC attribute which specifies a custom image as the source of the line. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <HR CLEAR=" cclear " SRC=" csrc " cattributes >