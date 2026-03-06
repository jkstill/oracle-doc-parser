---
id: 19c__DBMS_SQLTUNE.SELECT_WORKLOAD_REPOSITORY
name: DBMS_SQLTUNE.SELECT_WORKLOAD_REPOSITORY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.SELECT_WORKLOAD_REPOSITORY

This function collects SQL statements from the workload repository.

## Syntax

```sql
DBMS_SQLTUNE.SELECT_WORKLOAD_REPOSITORY (
  begin_snap        IN NUMBER,
  end_snap          IN NUMBER,
  basic_filter      IN VARCHAR2 := NULL,
  object_filter     IN VARCHAR2 := NULL,
  ranking_measure1  IN VARCHAR2 := NULL,
  ranking_measure2  IN VARCHAR2 := NULL,
  ranking_measure3  IN VARCHAR2 := NULL,
  result_percentage IN NUMBER   := 1,
  result_limit      IN NUMBER   := NULL,
  attribute_list    IN VARCHAR2 := NULL,
  recursive_sql     IN VARCHAR2 := HAS_RECURSIVE_SQL,
  dbid              IN NUMBER   := NULL)
 RETURN sys.sqlset PIPELINED;

DBMS_SQLTUNE.SELECT_WORKLOAD REPOSITORY (
  baseline_name     IN VARCHAR2,
  basic_filter      IN VARCHAR2 := NULL,
  object_filter     IN VARCHAR2 := NULL,
  ranking_measure1  IN VARCHAR2 := NULL,
  ranking_measure2  IN VARCHAR2 := NULL,
  ranking_measure3  IN VARCHAR2 := NULL,
  result_percentage IN NUMBER   := 1,
  result_limit      IN NUMBER   := NULL,
  attribute_list    IN VARCHAR2 := NULL,
  recursive_sql     IN VARCHAR2 := HAS_RECURSIVE_SQL,
  dbid              IN NUMBER   := NULL)
 RETURN sys.sqlset PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| begin_snap | NUMBER | IN | Defines the beginning AWR snapshot (non-inclusive). |
| end_snap | NUMBER | IN | Defines the ending AWR snapshot (inclusive). |
| baseline_name | VARCHAR2 | IN | Specifies the name of the AWR baseline period. |
| basic_filter | VARCHAR2 | IN | Specifies the SQL predicate to filter the SQL from the workload repository. The filter is defined on attributes of the SQLSET_ROW . If basic_filter is not set by the caller, then the subprogram captures only statements of type CREATE TABLE , INSERT , SELECT , UPDATE , DELETE , and MERGE . |
| object_filter | VARCHAR2 | IN | Currently not supported. |
| ranking_measure(n) |  |  | Defines an ORDER BY clause on the selected SQL. |
| result_percentage | NUMBER | IN | Specifies a filter that picks the top n % according to the supplied ranking measure. Note that this percentage applies only if one ranking measure is given. |
| result_limit | NUMBER | IN | Specifies the top limit SQL from the source according to the supplied ranking measure. |
| attribute_list | VARCHAR2 | IN | Specifies the SQL statement attributes to return in the result. The possible values are: TYPICAL — Returns BASIC plus SQL plan (without row source statistics) and without object reference list. This is the default. BASIC — Returns all attributes (such as execution statistics and binds) are returned except the plans. The execution context is always part of the result. ALL — Returns all attributes Comma-separated list of attribute names this allows to return only a subset of SQL attributes: EXECUTION_STATISTICS , SQL_BINDS , SQL_PLAN_STATISTICS (similar to SQL_PLAN plus row source statistics). |
| recursive_sql | VARCHAR2 | IN | Specifies the filter that includes recursive SQL in the SQL tuning set ( HAS_RECURSIVE_SQL ) or excludes it ( NO_RECURSIVE_SQL ). |
| dbid | NUMBER | IN | Specifies the DBID for imported or PDB-level AWR data. If NULL , then the function uses the current database DBID. |

**Returns:** `sys.sqlset`

## Usage Notes

The overloaded forms enable you to collect SQL statements from the following sources: Snapshots between begin_snap and end_snap A workload repository baseline Syntax DBMS_SQLTUNE.SELECT_WORKLOAD_REPOSITORY ( begin_snap IN NUMBER, end_snap IN NUMBER, basic_filter IN VARCHAR2 := NULL, object_filter IN VARCHAR2 := NULL, ranking_measure1 IN VARCHAR2 := NULL, ranking_measure2 IN VARCHAR2 := NULL, ranking_measure3 IN VARCHAR2 := NULL, result_percentage IN NUMBER := 1, result_limit IN NUMBER := NULL, attribute_list IN VARCHAR2 := NULL, recursive_sql IN VARCHAR2 := HAS_RECURSIVE_SQL, dbid IN NUMBER := NULL) RETURN sys.sqlset PIPELINED; DBMS_SQLTUNE.SELECT_WORKLOAD REPOSITORY ( baseline_name IN VARCHAR2, basic_filter IN VARCHAR2 := NULL, object_filter IN VARCHAR2 := NULL, ranking_measure1 IN VARCHAR2 := NULL, ranking_measure2 IN VARCHAR2 := NULL, ranking_measure3 IN VARCHAR2 := NULL, result_percentage IN NUMBER := 1, result_limit IN NUMBER := NULL, attribute_list IN VARCHAR2 := NULL, recursive_sql IN VARCHAR2 := HAS_RECURSIVE_SQL, dbid IN NUMBER := NULL) RETURN sys.sqlset PIPELINED; Parameters Table 169-45 SELECT_WORKLOAD_REPOSITORY Function Parameters Parameter Description begin_snap Defines the beginning AWR snapshot (non-inclusive). end_snap Defines the ending AWR snapshot (inclusive). baseline_name Specifies the name of the AWR baseline period. basic_filter Specifies the SQL predicate to filter the SQL from the workload repository. The filter is defined on attributes of the SQLSET_ROW . If basic_filter is not set by the caller, then the subprogram captures only statements of type CREATE TABLE , INSERT , SELECT , UPDATE , DELETE , and MERGE . object_filter Currently not supported. ranking_measure(n) Defines an ORDER BY clause on the selected SQL. result_percentage Specifies a filter that picks the top n % according to the supplied ranking measure. Note that this percentage applies only if one ranking measure is given. result_limit Specifies the top limit SQL from the source according to the supplied ranking measure. attribute_list Specifies the SQL statement attributes to return in the result. The possible values are: TYPICAL — Returns BASIC plus SQL plan (without row source statistics) and without object reference list. This is the default. BASIC — Returns all attributes (such as execution statistics and binds) are returned except the plans. The execution context is always part of the result. ALL — Returns all attributes Comma-separated list of attribute names this allows to return only a subset of SQL attributes: EXECUTION_STATISTICS , SQL_BINDS , SQL_PLAN_STATISTICS (similar to SQL_PLAN plus row source statistics). recursive_sql Specifies the filter that includes recursive SQL in the SQL tuning set ( HAS_RECURSIVE_SQL ) or excludes it ( NO_RECURSIVE_SQL ). dbid Specifies the DBID for imported or PDB-level AWR data. If NULL , then the function uses the current database DBID. Return Values This function returns one SQLSET_ROW per SQL_ID or PLAN_HASH_VALUE pair found in each data source. Usage Notes Filters provided to this function are evaluated as part of a SQL run by the current user. As such, they are executed with that user's security privileges and can contain any constructs and subqueries that user can access, but no more.