---
id: 19c__DBMS_CUBE.USING
name: DBMS_CUBE.USING
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE
tags: [dbms_cube]
source_file: DBMS_CUBE.html
---

# DBMS_CUBE.USING

SQL Aggregation Management is a group of PL/SQL subprograms in DBMS_CUBE that supports the rapid deployment of cube materialized views from existing relational materialized views.

## Syntax

```sql
SELECT query FROM user_mviews 
     WHERE mview_name='CAL_MONTH_SALES_MV';
 
QUERY
--------------------------------------------
SELECT   t.calendar_month_desc
  ,        sum(s.amount_sold) AS dollars
  FROM     sales s
  ,        times t
  WHERE    s.time_id = t.time_id
  GROUP BY t.calendar_month_desc
```

## Usage Notes

Cube materialized views are cubes that have been enhanced to use the automatic refresh and query rewrite features of Oracle Database. A single cube materialized view can replace many of the relational materialized views of summaries on a fact table, providing uniform response time to all summary data. Cube materialized views bring the fast update and fast query capabilities of the OLAP option to applications that query summaries of detail relational tables. The summary data is generated and stored in a cube, and query rewrite automatically redirects queries to the cube materialized views. Applications experience excellent querying performance. In the process of creating the cube materialized views, DBMS_CUBE also creates a fully functional analytic workspace including a cube and the cube dimensions. The cube stores the data for a cube materialized view instead of the table that stores the data for a relational materialized view. A cube can also support a wide range of analytic functions that enhance the database with information-rich content. Cube materialized views are registered in the data dictionary along with all other materialized views. A CB$ prefix identifies a cube materialized view. The DBMS_CUBE subprograms also support life-cycle management of cube materialized views. See Also: Adding Materialized View Capability to a Cube in Oracle OLAP User’s Guide for more information about cube materialized views and enhanced OLAP analytics. See Also: Adding Materialized View Capability to a Cube in Oracle OLAP User’s Guide for more information about cube materialized views and enhanced OLAP analytics. CREATE_MVIEW Function DERIVE_FROM_MVIEW Function DROP_MVIEW Procedure REFRESH_MVIEW Procedure The relational materialized view must conform to these requirements: Explicit GROUP BY clause for one or more columns. No expressions in the select list or GROUP BY clause. At least one of these numeric aggregation methods: SUM , MIN , MAX , or AVG . No outer joins. Summary keys with at least one simple column associated with a relational dimension. or Summary keys with at least one simple column and no hierarchies or levels. Numeric datatype of any type for the fact columns. All facts are converted to NUMBER . Eligible for rewrite. REWRITE_CAPABILITY should be GENERAL ; it cannot be NONE . Refer to the ALL_MVIEWS entry in the Oracle Database Reference . Cannot use the DISTINCT or UNIQUE keywords with an aggregate function in the defining query. For example, AVG(DISTINCT units) causes an error in STRICT mode and is ignored in LOOSE mode. You can choose between two modes when rendering the cube materialized view, LOOSE and STRICT . In STRICT mode, any deviation from the requirements raises an exception and prevents the materialized view from being created. In LOOSE mode (the default), some deviations are allowed, but they affect the content of the materialized view. These elements in the relational materialized view generate warning messages: Complex expressions in the defining query are ignored and do not appear in the cube materialized view. The AVG function is changed to SUM and COUNT . The COUNT function without a SUM , MIN , MAX , or AVG function is ignored. The STDDEV and VARIANCE functions are ignored. You can also choose how conditions in the WHERE clause are filtered. When filtering is turned off, the conditions are ignored. When turned on, valid conditions are rendered in the cube materialized view, but asymmetric conditions among dimension levels raise an exception. To create cube materialized views, you must have these privileges: CREATE [ANY] MATERIALIZED VIEW privilege CREATE [ANY] DIMENSION privilege ADVISOR privilege To access cube materialized views from another schema using query rewrite, you must have these privileges: GLOBAL QUERY REWRITE privilege SELECT or READ privilege on the relational source tables SELECT or READ privilege on the analytic workspace ( AW$ name ) that supports the cube materialized view SELECT or READ privilege on the cube SELECT or READ privilege on the dimensions of the cube Note that you need SELECT or READ privileges on the database objects that support the cube materialized views, but not on the cube materialized views.