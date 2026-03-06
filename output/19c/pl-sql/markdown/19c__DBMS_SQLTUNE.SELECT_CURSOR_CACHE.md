---
id: 19c__DBMS_SQLTUNE.SELECT_CURSOR_CACHE
name: DBMS_SQLTUNE.SELECT_CURSOR_CACHE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.SELECT_CURSOR_CACHE

This function collects SQL statements from the shared SQL area.

## Syntax

```sql
DBMS_SQLTUNE.SELECT_CURSOR_CACHE (
  basic_filter        IN   VARCHAR2 := NULL,
  object_filter       IN   VARCHAR2 := NULL,
  ranking_measure1    IN   VARCHAR2 := NULL,
  ranking_measure2    IN   VARCHAR2 := NULL,
  ranking_measure3    IN   VARCHAR2 := NULL,
  result_percentage   IN   NUMBER   := 1,
  result_limit        IN   NUMBER   := NULL,
  attribute_list      IN   VARCHAR2 := NULL,
  recursive_sql       IN   VARCHAR2 := HAS_RECURSIVE_SQL)
 RETURN sys.sqlset PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| basic_filter | VARCHAR2 | IN | Specifies the SQL predicate that filters the SQL from the shared SQL area defined on attributes of the SQLSET_ROW . If basic_filter is not set by the caller, then the subprogram captures only statements of the type CREATE TABLE , INSERT , SELECT , UPDATE , DELETE , and MERGE . |
| object_filter | VARCHAR2 | IN | Currently not supported. |
| ranking_measure(n) |  |  | Defines an ORDER BY clause on the selected SQL. |
| result_percentage | NUMBER | IN | Specifies a filter that picks the top n % according to the supplied ranking measure. The value applies only if one ranking measure is supplied. |
| result_limit | NUMBER | IN | Defines the top limit SQL from the filtered source ranked by the ranking measure. |
| attribute_list | VARCHAR2 | IN | Specifies the list of SQL statement attributes to return in the result. Possible values are: TYPICAL — Specifies BASIC plus SQL plan (without row source statistics) and without object reference list (default). BASIC — Specifies all attributes (such as execution statistics and binds) except the plans. The execution context is always part of the result. ALL — Specifies all attributes. Comma-separated list of attribute names. This values returns only a subset of SQL attributes: EXECUTION_STATISTICS BIND_LIST OBJECT_LIST SQL_PLAN SQL_PLAN_STATISTICS — Similar to SQL_PLAN plus row source statistics |
| recursive_sql | VARCHAR2 | IN | Specifies that the filter must include recursive SQL in the SQL tuning set ( HAS_RECURSIVE_SQL , which is the default) or exclude it ( NO_RECURSIVE_SQL ). |

**Returns:** `sys.sqlset`

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.SELECT_CURSOR_CACHE ( basic_filter IN VARCHAR2 := NULL, object_filter IN VARCHAR2 := NULL, ranking_measure1 IN VARCHAR2 := NULL, ranking_measure2 IN VARCHAR2 := NULL, ranking_measure3 IN VARCHAR2 := NULL, result_percentage IN NUMBER := 1, result_limit IN NUMBER := NULL, attribute_list IN VARCHAR2 := NULL, recursive_sql IN VARCHAR2 := HAS_RECURSIVE_SQL) RETURN sys.sqlset PIPELINED; Parameters Table 169-41 SELECT_CURSOR_CACHE Function Parameters Parameter Description basic_filter Specifies the SQL predicate that filters the SQL from the shared SQL area defined on attributes of the SQLSET_ROW . If basic_filter is not set by the caller, then the subprogram captures only statements of the type CREATE TABLE , INSERT , SELECT , UPDATE , DELETE , and MERGE . object_filter Currently not supported. ranking_measure(n) Defines an ORDER BY clause on the selected SQL. result_percentage Specifies a filter that picks the top n % according to the supplied ranking measure. The value applies only if one ranking measure is supplied. result_limit Defines the top limit SQL from the filtered source ranked by the ranking measure. attribute_list Specifies the list of SQL statement attributes to return in the result. Possible values are: TYPICAL — Specifies BASIC plus SQL plan (without row source statistics) and without object reference list (default). BASIC — Specifies all attributes (such as execution statistics and binds) except the plans. The execution context is always part of the result. ALL — Specifies all attributes. Comma-separated list of attribute names. This values returns only a subset of SQL attributes: EXECUTION_STATISTICS BIND_LIST OBJECT_LIST SQL_PLAN SQL_PLAN_STATISTICS — Similar to SQL_PLAN plus row source statistics recursive_sql Specifies that the filter must include recursive SQL in the SQL tuning set ( HAS_RECURSIVE_SQL , which is the default) or exclude it ( NO_RECURSIVE_SQL ). Return Values This function returns a one SQLSET_ROW per SQL_ID or PLAN_HASH_VALUE pair found in each data source.