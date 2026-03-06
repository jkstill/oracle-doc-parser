---
id: 19c__DBMS_CUBE.REQUIREMENTS
name: DBMS_CUBE.REQUIREMENTS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE
tags: [dbms_cube]
source_file: DBMS_CUBE.html
---

# DBMS_CUBE.REQUIREMENTS

SQL Aggregation Management uses an existing relational materialized view to derive all the information needed to generate a cube materialized view. The relational materialized view determines the detail level of data that is stored in the cube materialized view. The related relational dimension objects determine the scope of the aggregates, from the lowest level specified in the GROUP BY clause of the materialized view subquery, to the highest level of the dimension hierarchy.

## Usage Notes

The relational materialized view must conform to these requirements: Explicit GROUP BY clause for one or more columns. No expressions in the select list or GROUP BY clause. At least one of these numeric aggregation methods: SUM , MIN , MAX , or AVG . No outer joins. Summary keys with at least one simple column associated with a relational dimension. or Summary keys with at least one simple column and no hierarchies or levels. Numeric datatype of any type for the fact columns. All facts are converted to NUMBER . Eligible for rewrite. REWRITE_CAPABILITY should be GENERAL ; it cannot be NONE . Refer to the ALL_MVIEWS entry in the Oracle Database Reference . Cannot use the DISTINCT or UNIQUE keywords with an aggregate function in the defining query. For example, AVG(DISTINCT units) causes an error in STRICT mode and is ignored in LOOSE mode. You can choose between two modes when rendering the cube materialized view, LOOSE and STRICT . In STRICT mode, any deviation from the requirements raises an exception and prevents the materialized view from being created. In LOOSE mode (the default), some deviations are allowed, but they affect the content of the materialized view. These elements in the relational materialized view generate warning messages: Complex expressions in the defining query are ignored and do not appear in the cube materialized view. The AVG function is changed to SUM and COUNT . The COUNT function without a SUM , MIN , MAX , or AVG function is ignored. The STDDEV and VARIANCE functions are ignored. You can also choose how conditions in the WHERE clause are filtered. When filtering is turned off, the conditions are ignored. When turned on, valid conditions are rendered in the cube materialized view, but asymmetric conditions among dimension levels raise an exception.