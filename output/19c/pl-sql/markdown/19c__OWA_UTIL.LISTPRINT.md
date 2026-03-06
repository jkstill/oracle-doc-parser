---
id: 19c__OWA_UTIL.LISTPRINT
name: OWA_UTIL.LISTPRINT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.LISTPRINT

This procedure generates an HTML selection list form element from the output of a SQL query.

## Syntax

```sql
OWA_UTIL.LISTPRINT(
   p_theQuery     IN       VARCHAR2,
   p_cname        IN       VARCHAR2,
   p_nsize        IN       NUMBER,
   p_multiple     IN       BOOLEAN   DEFAULT FALSE);

OWA_UTIL.LISTPRINT(
   p_theCursor    IN    INTEGER,
   p_cname        IN       VARCHAR2,
   p_nsize        IN       NUMBER,
   p_multiple     IN       BOOLEAN   DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_theQuery | VARCHAR2 | IN | The SQL query. |
| p_theCursor | INTEGER | IN | The cursor ID. This can be the return value from the BIND_VARIABLES Function . |
| p_cname | VARCHAR2 | IN | The name of the HTML form element. |
| p_nsize | NUMBER | IN | The size of the form element (this controls how many items the user can see without scrolling). |
| p_multiple | BOOLEAN | IN | Whether multiple selection is permitted. |

## Usage Notes

There are two versions of this procedure. The first version contains a hard-coded SQL query. The second version uses a dynamic query prepared with the BIND_VARIABLES Function . Syntax OWA_UTIL.LISTPRINT( p_theQuery IN VARCHAR2, p_cname IN VARCHAR2, p_nsize IN NUMBER, p_multiple IN BOOLEAN DEFAULT FALSE); OWA_UTIL.LISTPRINT( p_theCursor IN INTEGER, p_cname IN VARCHAR2, p_nsize IN NUMBER, p_multiple IN BOOLEAN DEFAULT FALSE); Parameters Table 230-7 LISTPRINT Procedure Parameters Parameter Description p_theQuery The SQL query. p_theCursor The cursor ID. This can be the return value from the BIND_VARIABLES Function . p_cname The name of the HTML form element. p_nsize The size of the form element (this controls how many items the user can see without scrolling). p_multiple Whether multiple selection is permitted. Usage Notes The columns in the output of the query are handled in the following manner: The first column specifies the values that are sent back. These values are for the VALUE attribute of the OPTION tag. The second column specifies the values that the user sees. The third column specifies whether or not the row is marked as SELECTED in the OPTION tag. If the value is not NULL , the row is selected. Examples <SELECT NAME=" p_cname " SIZE=" p_nsize "> <OPTION SELECTED value='value_from_the_first_column'>value_from_the_second_column <OPTION SELECTED value='value_from_the_first_column'>value_from_the_second_column ... </SELECT>