---
id: 19c__HTF.FORMAT_CELL
name: HTF.FORMAT_CELL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FORMAT_CELL

This function formats column values inside an HTML table using the TABLEDATA Function. It allows for better control over the HTML tables.

## Syntax

```sql
HTF.FORMAT_CELL(
   columnValue          IN       VARCHAR2
   format_numbers       IN       VARCHAR2   DEFAULT NULL 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| columnValue | VARCHAR2 | IN | The value that needs to be formatted in an HTML table. |
| format_numbers | VARCHAR2 | IN | The format that numeric data is displayed in. If the value of this parameter is not NULL , the number fields are right-justified and rounded to two decimal places. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.FORMAT_CELL( columnValue IN VARCHAR2 format_numbers IN VARCHAR2 DEFAULT NULL RETURN VARCHAR2; Parameters Table 220-29 FORMAT_CELL Function Parameters Parameter Description columnValue The value that needs to be formatted in an HTML table. format_numbers The format that numeric data is displayed in. If the value of this parameter is not NULL , the number fields are right-justified and rounded to two decimal places. Examples This function generates <TD >columnValue</TD>