---
id: 19c__DBMS_SQLTUNE.SELECT_SQLSET
name: DBMS_SQLTUNE.SELECT_SQLSET
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.SELECT_SQLSET

This is a table function that reads the contents of a SQL tuning set.

## Syntax

```sql
DBMS_SQLTUNE.SELECT_SQLSET (
  sqlset_name         IN   VARCHAR2,
  basic_filter        IN   VARCHAR2 := NULL,
  object_filter       IN   VARCHAR2 := NULL,
  ranking_measure1    IN   VARCHAR2 := NULL,
  ranking_measure2    IN   VARCHAR2 := NULL,
  ranking_measure3    IN   VARCHAR2 := NULL,
  result_percentage   IN   NUMBER   := 1,
  result_limit        IN   NUMBER   := NULL)
  attribute_list      IN   VARCHAR2 := NULL,
  plan_filter         IN   VARCHAR2 := NULL,
  sqlset_owner        IN   VARCHAR2 := NULL,
  recursive_sql       IN   VARCHAR2 := HAS_RECURSIVE_SQL)
 RETURN sys.sqlset PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sqlset_name | VARCHAR2 | IN | Specifies the name of the SQL tuning set to query. |
| basic_filter | VARCHAR2 | IN | Specifies the SQL predicate to filter the SQL from the SQL tuning set defined on attributes of the SQLSET_ROW . |
| object_filter | VARCHAR2 | IN | Currently not supported. |
| ranking_measure(n) |  |  | Specifies an ORDER BY clause on the selected SQL. |
| result_percentage | NUMBER | IN | Specifies a filter that picks the top n % according to the supplied ranking measure. Note that this parameter applies only if one ranking measure is supplied. |
| result_limit | NUMBER | IN | The top limit SQL from the filtered source, ranked by the ranking measure. |
| attribute_list | VARCHAR2 | IN | Defines the SQL statement attributes to return in the result. The possible values are: BASIC — Returns all attributes (such as execution statistics and binds) except the plans. The execution context is included in the result. TYPICAL — Returns BASIC plus the SQL plan, but without row source statistics and without the object reference list. This is the default. ALL — Returns all attributes. Comma-separated list of attribute names. This value enables the function to return only a subset of SQL attributes: EXECUTION_STATISTICS SQL_BINDS SQL_PLAN_STATISTICS (similar to SQL_PLAN plus row source statistics) |
| plan_filter | VARCHAR2 | IN | Specifies the plan filter. This parameter enables you to select a single plan when a statement has multiple plans. Possible values are: LAST_GENERATED — Returns the plan with the most recent timestamp. FIRST_GENERATED — Returns the plan with the least recent timestamp. LAST_LOADED — Returns the plan with the most recent FIRST_LOAD_TIME statistical information. FIRST_LOADED — Returns the plan with the least recent FIRST_LOAD_TIME statistical information. MAX_ELAPSED TIME — Returns the plan with the maximum elapsed time. MAX_BUFFER_GETS — Returns the plan with the maximum buffer gets. MAX_DISK_READS — Returns the plan with the maximum disk reads. MAX_DIRECT_WRITES — Returns the plan with the maximum direct writes. MAX_OPTIMIZER_COST — Returns the plan with the maximum optimizer cost value. |
| sqlset_owner | VARCHAR2 | IN | Specifies the owner of the SQL tuning set, or NULL for the current schema owner. |
| recursive_sql | VARCHAR2 | IN | Specifies that the filter must include recursive SQL in the SQL tuning set ( HAS_RECURSIVE_SQL , which is the default) or exclude it ( NO_RECURSIVE_SQL ). |

**Returns:** `sys.sqlset`

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.SELECT_SQLSET ( sqlset_name IN VARCHAR2, basic_filter IN VARCHAR2 := NULL, object_filter IN VARCHAR2 := NULL, ranking_measure1 IN VARCHAR2 := NULL, ranking_measure2 IN VARCHAR2 := NULL, ranking_measure3 IN VARCHAR2 := NULL, result_percentage IN NUMBER := 1, result_limit IN NUMBER := NULL) attribute_list IN VARCHAR2 := NULL, plan_filter IN VARCHAR2 := NULL, sqlset_owner IN VARCHAR2 := NULL, recursive_sql IN VARCHAR2 := HAS_RECURSIVE_SQL) RETURN sys.sqlset PIPELINED; Parameters Table 169-44 SELECT_SQLSET Function Parameters Parameter Description sqlset_name Specifies the name of the SQL tuning set to query. basic_filter Specifies the SQL predicate to filter the SQL from the SQL tuning set defined on attributes of the SQLSET_ROW . object_filter Currently not supported. ranking_measure(n) Specifies an ORDER BY clause on the selected SQL. result_percentage Specifies a filter that picks the top n % according to the supplied ranking measure. Note that this parameter applies only if one ranking measure is supplied. result_limit The top limit SQL from the filtered source, ranked by the ranking measure. attribute_list Defines the SQL statement attributes to return in the result. The possible values are: BASIC — Returns all attributes (such as execution statistics and binds) except the plans. The execution context is included in the result. TYPICAL — Returns BASIC plus the SQL plan, but without row source statistics and without the object reference list. This is the default. ALL — Returns all attributes. Comma-separated list of attribute names. This value enables the function to return only a subset of SQL attributes: EXECUTION_STATISTICS SQL_BINDS SQL_PLAN_STATISTICS (similar to SQL_PLAN plus row source statistics) plan_filter Specifies the plan filter. This parameter enables you to select a single plan when a statement has multiple plans. Possible values are: LAST_GENERATED — Returns the plan with the most recent timestamp. FIRST_GENERATED — Returns the plan with the least recent timestamp. LAST_LOADED — Returns the plan with the most recent FIRST_LOAD_TIME statistical information. FIRST_LOADED — Returns the plan with the least recent FIRST_LOAD_TIME statistical information. MAX_ELAPSED TIME — Returns the plan with the maximum elapsed time. MAX_BUFFER_GETS — Returns the plan with the maximum buffer gets. MAX_DISK_READS — Returns the plan with the maximum disk reads. MAX_DIRECT_WRITES — Returns the plan with the maximum direct writes. MAX_OPTIMIZER_COST — Returns the plan with the maximum optimizer cost value. sqlset_owner Specifies the owner of the SQL tuning set, or NULL for the current schema owner. recursive_sql Specifies that the filter must include recursive SQL in the SQL tuning set ( HAS_RECURSIVE_SQL , which is the default) or exclude it ( NO_RECURSIVE_SQL ). Return Values This function returns one SQLSET_ROW per SQL_ID or PLAN_HASH_VALUE pair found in each data source.