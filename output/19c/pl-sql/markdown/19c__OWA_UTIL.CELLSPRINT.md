---
id: 19c__OWA_UTIL.CELLSPRINT
name: OWA_UTIL.CELLSPRINT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.CELLSPRINT

This procedure generates an HTML table from the output of a SQL query. SQL atomic data items are mapped to HTML cells and SQL rows to HTML rows. You must write the code to begin and end the HTML table.

## Syntax

```sql
OWA_UTIL.CELLSPRINT(
   p_colCnt          IN    INTEGER,
   p_resultTbl       IN    vc_arr,
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_query |  |  | A PL/SQL query. |
| p_colCnt | INTEGER | IN | The number of columns in the table. |
| p_theQuery |  |  | A SQL SELECT statement. |
| p_theCursor |  |  | A cursor ID. This can be the return value from the BIND_VARIABLES Function . |
| p_max_rows |  |  | The maximum number of rows to print. |
| p_format_numbers |  |  | If the value of this parameter is not NULL , number fields are right justified and rounded to two decimal places. |
| p_skip_rec |  |  | The number of rows to exclude from the HTML table. |
| p_more_data |  |  | TRUE if there are more rows in the query or cursor, FALSE otherwise. |
| p_reccnt |  |  | The number of rows that have been returned by the query. This value does not include skipped rows (if any). |
| p_resultTbl | vc_arr | IN | The index table which will contain the result of the query. Each entry in the query will correspond to one column value. |

## Usage Notes

There are nine versions of this procedure: The first version passes the results of a query into an index table. Perform the query and CELLSPRINT does the formatting. To have more control in generating an HTML table from the output of an SQL query, use the FORMAT_CELL Function in the " HTF " package. The second and third versions display rows (up to the specified maximum) returned by the query or cursor. The fourth and fifth versions exclude a specified number of rows from the HTML table. Use the fourth and fifth versions to scroll through result sets by saving the last row seen in a hidden form element. The sixth through ninth versions are the same as the first four versions, except that they return a row count output parameter. Syntax OWA_UTIL.CELLSPRINT( p_colCnt IN INTEGER, p_resultTbl IN vc_arr, p_format_numbers IN VARCHAR2 DEFAULT NULL); OWA_UTIL.CELLSPRINT( p_theQuery IN VARCHAR2, p_max_rows IN NUMBER DEFAULT 100, p_format_numbers IN VARCHAR2 DEFAULT NULL); OWA_UTIL.CELLSPRINT( p_theCursor IN INTEGER, p_max_rows IN NUMBER DEFAULT 100, p_format_numbers iN VARCHAR2 DEFAULT NULL); OWA_UTIL.CELLSPRINT( p_theQuery IN VARCHAR2, p_max_rows IN NUMBER DEFAULT 100, p_format_numbers IN VARCHAR2 DEFAULT NULL, p_skip_rec IN NUMBER DEFAULT 0, p_more_data OUT BOOLEAN); OWA_UTIL.CELLSPRINT( p_theCursor IN INTEGER, p_max_rows IN NUMBER DEFAULT 100, p_format_numbers IN VARCHAR2 DEFAULT NULL, p_skip_rec IN NUMBER DEFAULT 0, p_more_data OUT BOOLEAN); OWA_UTIL.CELLSPRINT( p_theQuery IN VARCHAR2, p_max_rows IN NUMBER DEFAULT 100, p_format_numbers IN VARCHAR2 DEFAULT NULL, p_reccnt OUT NUMBER); OWA_UTIL.CELLSPRINT( p_theCursor IN INTEGER, p_max_rows IN NUMBER DEFAULT 100, p_format_numbers IN VARCHAR2 DEFAULT NULL, p_reccnt OUT NUMBER); OWA_UTIL.CELLSPRINT( p_theQuery IN VARCHAR2, p_max_rows IN NUMBER DEFAULT 100, p_format_numbers IN VARCHAR2 DEFAULT NULL, p_skip_rec IN NUMBER DEFAULT 0, p_more_data OUT BOOLEAN p_reccnt OUT NUMBER); OWA_UTIL.CELLSPRINT( p_theCursor IN INTEGER, p_max_rows IN NUMBER DEFAULT 100, p_format_numbers IN VARCHAR2 DEFAULT NULL, p_skip_rec IN NUMBER DEFAULT 0, p_more_data OUT BOOLEAN, p_reccnt OUT NUMBER); Parameters Table 230-4 CELLSPRINT Procedure Parameters Parameter Description p_query A PL/SQL query. p_colCnt The number of columns in the table. p_theQuery A SQL SELECT statement. p_theCursor A cursor ID. This can be the return value from the BIND_VARIABLES Function . p_max_rows The maximum number of rows to print. p_format_numbers If the value of this parameter is not NULL , number fields are right justified and rounded to two decimal places. p_skip_rec The number of rows to exclude from the HTML table. p_more_data TRUE if there are more rows in the query or cursor, FALSE otherwise. p_reccnt The number of rows that have been returned by the query. This value does not include skipped rows (if any). p_resultTbl The index table which will contain the result of the query. Each entry in the query will correspond to one column value. Examples This procedure generates <tr><td> QueryResultItem </td><td> QueryResultItem </td></tr>...