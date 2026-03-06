---
id: 19c__OWA_UTIL.CHOOSE_DATE
name: OWA_UTIL.CHOOSE_DATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.CHOOSE_DATE

This procedure generates three HTML form elements that allow the user to select the day, the month, and the year.

## Syntax

```sql
OWA_UTIL.CHOOSE_DATE(
   p_name         IN       VARCHAR2,
   p_date         IN       DATE       DEFAULT SYSDATE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_name | VARCHAR2 | IN | The name of the form elements. |
| p_date | DATE | IN | The initial date that is selected when the HTML page is displayed. |

## Usage Notes

Syntax OWA_UTIL.CHOOSE_DATE( p_name IN VARCHAR2, p_date IN DATE DEFAULT SYSDATE); Parameters Table 230-5 CHOOSE_DATE Procedure Parameters Parameter Description p_name The name of the form elements. p_date The initial date that is selected when the HTML page is displayed. Usage Notes The parameter in the procedure that receives the data from these elements must be a GET_CGI_ENV Function . Use the TODATE Function to convert the GET_CGI_ENV Function value to the standard Oracle DATE datatype. Examples <SELECT NAME="p_name" SIZE="1"> <OPTION value="01">1 ... <OPTION value="31">31 </SELECT> - <SELECT NAME="p_name" SIZE="1"> <OPTION value="01">JAN ... <OPTION value="12">DEC </SELECT> - <SELECT NAME="p_name" SIZE="1"> <OPTION value="1992">1992 ... <OPTION value="2002">2002 </SELECT>