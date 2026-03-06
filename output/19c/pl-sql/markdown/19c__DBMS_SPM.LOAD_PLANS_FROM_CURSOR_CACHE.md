---
id: 19c__DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE
name: DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE

This function loads one or more plans present in the cursor cache for a SQL statement, or a set of SQL statements. It has four overloads: using SQL statement text, using SQL handle, using SQL ID, or using attribute_name and attribute_value pair.

## Syntax

```sql
DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE (
   sql_id            IN  VARCHAR2,
   plan_hash_value   IN  NUMBER   := NULL,
   sql_text          IN  CLOB,
   fixed             IN  VARCHAR2 := 'NO',
   enabled           IN  VARCHAR2 := 'YES')
 RETURN PLS_INTEGER;

DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE (
   sql_id            IN  VARCHAR2,
   plan_hash_value   IN  NUMBER   := NULL,
   sql_handle        IN  VARCHAR2,
   fixed             IN  VARCHAR2 := 'NO',
   enabled           IN  VARCHAR2 := 'YES')
 RETURN PLS_INTEGER;

DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE (
   sql_id            IN  VARCHAR2,
   plan_hash_value   IN  NUMBER   := NULL,
   fixed             IN  VARCHAR2 := 'NO',
   enabled           IN  VARCHAR2 := 'YES')
 RETURN PLS_INTEGER;

DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE (
   attribute_name   IN VARCHAR2,
   attribute_value  IN VARCHAR2,
   fixed            IN VARCHAR2 := 'NO',
   enabled          IN VARCHAR2 := 'YES')
  RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_id | VARCHAR2 | IN | SQL statement identifier. Identifies a SQL statement in the cursor cache. Note: In the third overload the text of identified SQL statement is extracted from cursor cache and is used to identify the SQL plan baseline into which the plan(s) are loaded. If the SQL plan baseline doesn't exist it is created. |
| plan_hash_value | NUMBER | IN | Plan identifier. Default NULL means capture all plans present in the cursor cache for the SQL statement identified by SQL_ID . |
| sql_text | CLOB | IN | SQL text to use in identifying the SQL plan baseline into which the plans are loaded. If the SQL plan baseline does not exist, it is created. The use of text is crucial when the user tunes a SQL statement by adding hints to its text and then wants to load the resulting plan(s) into the SQL plan baseline of the original SQL statement. |
| sql_handle | VARCHAR2 | IN | SQL handle to use in identifying the SQL plan baseline into which the plans are loaded. The sql_handle must denote an existing SQL plan baseline. The use of handle is crucial when the user tunes a SQL statement by adding hints to its text and then wants to load the resulting plan(s) into the SQL plan baseline of the original SQL statement. |
| fixed | VARCHAR2 | IN | Default 'NO' means the loaded plans are used as non-fixed plans. Value 'YES' means the loaded plans are used as fixed plans and the SQL plan baseline will not be evolved over time. |
| attribute_name | VARCHAR2 | IN | One of possible attribute names: SQL_TEXT '' ' PARSING_SCHEMA_NAME ' ' MODULE ' ' ACTION' |
| attribute_value | VARCHAR2 | IN | Attribute value is used as a search pattern of LIKE predicate if attribute name is 'SQL_TEXT' . Otherwise, it is used as an equality search value. (for example, for specifying attribute_name => 'SQL_TEXT' , and attribute_value => '% HR-123 %' means applying SQL_TEXT LIKE '% HR - 123 %' as a selection filter. Similarly, specifying attribute_name => 'MODULE' , and attribute_value => 'HR' means applying 'MODULE = ' HR' as a plan selection filter). The attribute value is upper-cased except when it is enclosed in double quotes or attribute name is 'SQL_TEXT' . |
| enabled | VARCHAR2 | IN | Default ' YES ' means the loaded plans are enabled for use by the optimizer |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE ( sql_id IN VARCHAR2, plan_hash_value IN NUMBER := NULL, sql_text IN CLOB, fixed IN VARCHAR2 := 'NO', enabled IN VARCHAR2 := 'YES') RETURN PLS_INTEGER; DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE ( sql_id IN VARCHAR2, plan_hash_value IN NUMBER := NULL, sql_handle IN VARCHAR2, fixed IN VARCHAR2 := 'NO', enabled IN VARCHAR2 := 'YES') RETURN PLS_INTEGER; DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE ( sql_id IN VARCHAR2, plan_hash_value IN NUMBER := NULL, fixed IN VARCHAR2 := 'NO', enabled IN VARCHAR2 := 'YES') RETURN PLS_INTEGER; DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE ( attribute_name IN VARCHAR2, attribute_value IN VARCHAR2, fixed IN VARCHAR2 := 'NO', enabled IN VARCHAR2 := 'YES') RETURN PLS_INTEGER; Parameters Table 161-19 LOAD_PLANS_FROM_CURSOR_CACHE Function Parameters Parameter Description sql_id SQL statement identifier. Identifies a SQL statement in the cursor cache. Note: In the third overload the text of identified SQL statement is extracted from cursor cache and is used to identify the SQL plan baseline into which the plan(s) are loaded. If the SQL plan baseline doesn't exist it is created. plan_hash_value Plan identifier. Default NULL means capture all plans present in the cursor cache for the SQL statement identified by SQL_ID . sql_text SQL text to use in identifying the SQL plan baseline into which the plans are loaded. If the SQL plan baseline does not exist, it is created. The use of text is crucial when the user tunes a SQL statement by adding hints to its text and then wants to load the resulting plan(s) into the SQL plan baseline of the original SQL statement. sql_handle SQL handle to use in identifying the SQL plan baseline into which the plans are loaded. The sql_handle must denote an existing SQL plan baseline. The use of handle is crucial when the user tunes a SQL statement by adding hints to its text and then wants to load the resulting plan(s) into the SQL plan baseline of the original SQL statement. fixed Default 'NO' means the loaded plans are used as non-fixed plans. Value 'YES' means the loaded plans are used as fixed plans and the SQL plan baseline will not be evolved over time. attribute_name One of possible attribute names: SQL_TEXT '' ' PARSING_SCHEMA_NAME ' ' MODULE ' ' ACTION' attribute_value Attribute value is used as a search pattern of LIKE predicate if attribute name is 'SQL_TEXT' . Otherwise, it is used as an equality search value. (for example, for specifying attribute_name => 'SQL_TEXT' , and attribute_value => '% HR-123 %' means applying SQL_TEXT LIKE '% HR - 123 %' as a selection filter. Similarly, specifying attribute_name => 'MODULE' , and attribute_value => 'HR' means applying 'MODULE = ' HR' as a plan selection filter). The attribute value is upper-cased except when it is enclosed in double quotes or attribute name is 'SQL_TEXT' . enabled Default ' YES ' means the loaded plans are enabled for use by the optimizer Return Values Number of plans loaded Usage Notes Invoking this subprogram requires the ADMINISTER SQL MANAGEMENT OBJECT privilege.