---
id: 19c__OWA_UTIL.TABLEPRINT
name: OWA_UTIL.TABLEPRINT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.TABLEPRINT

This function generates either preformatted tables or HTML tables (depending on the capabilities of the user's browser) from database tables.

## Syntax

```sql
OWA_UTIL.TABLEPRINT(
   ctable         IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL,
   ntable_type    IN       INTEGER    DEFAULT HTML_TABLE,
   ccolumns       IN       VARCHAR2   DEFAULT '*',
   cclauses       IN    VARCHAR2   DEFAULT NULL,
   ccol_aliases   IN       VARCHAR2   DEFAULT NULL,
   nrow_min       IN       NUMBER     DEFAULT 0,
   nrow_max       IN       NUMBER     DEFAULT NULL)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctable | VARCHAR2 | IN | The database table. |
| cattributes | VARCHAR2 | IN | Other attributes to be included as-is in the tag. |
| ntable_type | INTEGER | IN | How to generate the table. Specify HTML_TABLE to generate the table using <TABLE> tags or PRE_TABLE to generate the table using the <PRE> tags. These are constants: HTML_TABLE CONSTANT INTEGER := 1; PRE_TABLE CONSTANT INTEGER := 2; |
| ccolumns | VARCHAR2 | IN | A comma-delimited list of columns from ctable to include in the generated table. |
| cclauses | VARCHAR2 | IN | WHERE or ORDER BY clauses, which specify which rows to retrieve from the database table, and how to order them. |
| ccol_aliases | VARCHAR2 | IN | A comma-delimited list of headings for the generated table. |
| nrow_min | NUMBER | IN | The first row, of those retrieved, to display. |
| nrow_max | NUMBER | IN | The last row, of those retrieved, to display. |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax OWA_UTIL.TABLEPRINT( ctable IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL, ntable_type IN INTEGER DEFAULT HTML_TABLE, ccolumns IN VARCHAR2 DEFAULT '*', cclauses IN VARCHAR2 DEFAULT NULL, ccol_aliases IN VARCHAR2 DEFAULT NULL, nrow_min IN NUMBER DEFAULT 0, nrow_max IN NUMBER DEFAULT NULL) RETURN BOOLEAN; Parameters Table 230-13 TABLEPRINT Function Parameters Parameter Description ctable The database table. cattributes Other attributes to be included as-is in the tag. ntable_type How to generate the table. Specify HTML_TABLE to generate the table using <TABLE> tags or PRE_TABLE to generate the table using the <PRE> tags. These are constants: HTML_TABLE CONSTANT INTEGER := 1; PRE_TABLE CONSTANT INTEGER := 2; ccolumns A comma-delimited list of columns from ctable to include in the generated table. cclauses WHERE or ORDER BY clauses, which specify which rows to retrieve from the database table, and how to order them. ccol_aliases A comma-delimited list of headings for the generated table. nrow_min The first row, of those retrieved, to display. nrow_max The last row, of those retrieved, to display. Return Values Returns TRUE if there are more rows beyond the nrow_max requested, FALSE otherwise. Usage Notes RAW columns are supported, but LONG RAW columns are not. References to LONG RAW columns will print the result 'Not Printable'. Note that in this function, cattributes is the second rather than the last parameter. Examples For browsers that do not support HTML tables, create the following procedure: CREATE OR REPLACE PROCEDURE showemps IS ignore_more BOOLEAN; BEGIN ignore_more := OWA_UTIL.TABLEPRINT('emp', 'BORDER', OWA_UTIL.PRE_TABLE); END; Requesting a URL such as http://myhost:7777/pls/hr/showemps returns to the following to the client: <PRE> ----------------------------------------------------------------- | EMPNO |ENAME |JOB |MGR |HIREDATE | SAL | COMM | DEPTNO | ----------------------------------------------------------------- | 7369| SMITH | CLERK | 7902 | 17-DEC-80 | 800 | | 20 | | 7499| ALLEN | SALESMAN| 7698 | 20-FEB-81 | 1600 | 300 | 30 | | 7521| WARD | SALESMAN| 7698 | 22-FEB-81 | 1250 | 500 | 30 | | 7566| JONES | MANAGER | 7839 | 02-APR-81 | 2975 | | 20 | | 7654| MARTIN | SALESMAN| 7698 | 28-SEP-81 | 1250 | 1400| 30 | | 7698| BLAKE | MANAGER | 7839 | 01-MAY-81 | 2850 | | 30 | | 7782| CLARK | MANAGER | 7839 | 09-JUN-81 | 2450 | | 10 | | 7788| SCOTT | ANALYST | 7566 | 09-DEC-82 | 3000 | | 20 | | 7839| KING | PRESIDENT | | 17-NOV-81 | 5000 | | 10 | | 7844| TURNER | SALESMAN| 7698 | 08-SEP-81 | 1500 | 0 | 30 | | 7876| ADAMS | CLERK | 7788 | 12-JAN-83 | 1100 | | 20 | | 7900| JAMES | CLERK | 7698 | 03-DEC-81 | 950 | | 30 | | 7902| FORD | ANALYST | 7566 | 03-DEC-81 | 3000 | | 20 | | 7934| MILLER | CLERK | 7782 | 23-JAN-82 | 1300 | | 10 | ------------------------------------------------------------------- </PRE> To view the employees in department 10, and only their employee ids, names, and salaries, create the following procedure: CREATE OR REPLACE PROCEDURE showemps_10 IS ignore_more BOOLEAN; begin ignore_more := OWA_UTIL.TABLEPRINT ('EMP', 'BORDER', OWA_UTIL.PRE_TABLE, 'empno, ename, sal', 'WHERE deptno=10 ORDER BY empno', 'Employee Number, Name, Salary'); END; A request for a URL like http://myhost:7777/pls/hr/showemps_10 would return the following to the client: <PRE> ------------------------------------- | Employee Number |Name | Salary | ------------------------------------- | 7782 | CLARK | 2450 | | 7839 | KING | 5000 | | 7934 | MILLER | 1300 | ------------------------------------- </PRE> For browsers that support HTML tables, to view the department table in an HTML table, create the following procedure: CREATE OR REPLACE PROCEDURE showdept IS ignore_more BOOLEAN; BEGIN ignore_more := oWA_UTIL.TABLEPRINT('dept', 'BORDER'); END; A request for a URL like http://myhost:7777/pls/hr/showdept would return the following to the client: <TABLE BORDER> <TR> <TH>DEPTNO</TH> <TH>DNAME</TH> <TH>LOC</TH> </TR> <TR> <TD ALIGN="LEFT">10</TD> <TD ALIGN="LEFT">ACCOUNTING</TD> <TD ALIGN="LEFT">NEW YORK</TD> </TR> <TR> <TD ALIGN="LEFT">20</TD> <TD ALIGN="LEFT">RESEARCH</TD> <TD ALIGN="LEFT">DALLAS</TD> </TR> <TR> <TD ALIGN="LEFT">30</TD> <TD ALIGN="LEFT">SALES</TD> <TD ALIGN="LEFT">CHICAGO</TD> </TR> <TR> <TD ALIGN="LEFT">40</TD> <TD ALIGN="LEFT">OPERATIONS</TD> <TD ALIGN="LEFT">BOSTON</TD> </TR> </TABLE> A Web browser would format this to look like the following table: DEPTNO DNAME LOC 10 ACCOUNTING NEW YORK 20 RESEARCH DALLAS 30 SALES CHICAGO