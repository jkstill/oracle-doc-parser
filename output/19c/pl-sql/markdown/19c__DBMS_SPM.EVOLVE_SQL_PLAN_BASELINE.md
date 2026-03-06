---
id: 19c__DBMS_SPM.EVOLVE_SQL_PLAN_BASELINE
name: DBMS_SPM.EVOLVE_SQL_PLAN_BASELINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.EVOLVE_SQL_PLAN_BASELINE

This function evolves SQL plan baselines associated with one or more SQL statements. A SQL plan baseline is evolved when one or more of its non-accepted plans is changed to an accepted plan or plans.

## Syntax

```sql
DBMS_SPM.EVOLVE_SQL_PLAN_BASELINE (
   sql_handle   IN VARCHAR2 := NULL,
   plan_name    IN VARCHAR2 := NULL,
   time_limit   IN INTEGER  := DBMS_SPM.AUTO_LIMIT,
   verify       IN VARCHAR2 := 'YES',
   commit       IN VARCHAR2 := 'YES')
  RETURN CLOB;

DBMS_SPM.EVOLVE_SQL_PLAN_BASELINE (
   plan_list    IN DBMS_SPM.NAME_LIST,
   time_limit   IN INTEGER  := DBMS_SPM.AUTO_LIMIT,
   verify       IN VARCHAR2 := 'YES',
   commit       IN VARCHAR2 := 'YES')
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_handle | VARCHAR2 | IN | SQL statement identifier. Unless plan_name is specified, NULL means to consider all statements with non-accepted plans in their SQL plan baselines. |
| plan_name | VARCHAR2 | IN | Plan identifier. Default NULL means to consider all non- accepted plans in the SQL plan baseline of either the identified SQL statement or all SQL statements if sql_handle is NULL . |
| plan_list | DBMS_SPM.NAME_LIST | IN | A list of plan names. Each plan in the list can belong to same or different SQL statement. |
| time_limit | INTEGER | IN | Time limit in number of minutes. This applies only if verify = ' YES '. The time limit is global and it is used as follows: The time limit for first non-accepted plan verification is set equal to the input value; the time limit for second non-accepted plan verification is set equal to (input value - time spent in first plan verification); and so on. DBMS_SPM . AUTO_LIMIT (Default) lets the system choose an appropriate time limit based on the number of plan verifications required to be done. DBMS_SPM . NO_LIMIT means there is no time limit. A positive integer value represents a user specified time limit. |
| verify | VARCHAR2 | IN | Specifies whether to execute the plans and compare the performance before changing non-accepted plans into accepted plans. A performance verification involves executing a non-accepted plan and a plan chosen from corresponding SQL plan baseline and comparing their performance statistics. If non-accepted plan shows performance improvement, it is changed to an accepted plan. ' YES ' (Default) - verifies that a non-accepted plan gives better performance before changing it to an accepted plan ' NO ' - directs not to execute plans but only to change non-accepted plans into accepted plans |
| commit | VARCHAR2 | IN | Specifies whether to update the ACCEPTED status of non-accepted plans from ' NO ' to ' YES '. ' YES ' (Default) - perform updates of qualifying non-accepted plans and generate a report that shows the updates and the result of performance verification when verify = ' YES '. ' NO ' - generate a report without any updates. Note that commit = ' NO ' together with verify = ' NO ' represents a no-op. |

**Returns:** `CLOB`

## Usage Notes

If interrogated by the user (parameter verify = ' YES '), the execution performance of each non-accepted plan is compared against the performance of a plan chosen from the associated SQL plan baseline. If the non-accepted plan performance is found to be better than SQL plan baseline performance, the non-accepted plan is changed to an accepted plan provided such action is permitted by the user (parameter commit = 'YES'). The second form of the function employs a plan list format. Syntax DBMS_SPM.EVOLVE_SQL_PLAN_BASELINE ( sql_handle IN VARCHAR2 := NULL, plan_name IN VARCHAR2 := NULL, time_limit IN INTEGER := DBMS_SPM.AUTO_LIMIT, verify IN VARCHAR2 := 'YES', commit IN VARCHAR2 := 'YES') RETURN CLOB; DBMS_SPM.EVOLVE_SQL_PLAN_BASELINE ( plan_list IN DBMS_SPM.NAME_LIST, time_limit IN INTEGER := DBMS_SPM.AUTO_LIMIT, verify IN VARCHAR2 := 'YES', commit IN VARCHAR2 := 'YES') RETURN CLOB; Parameters Table 161-14 EVOLVE_SQL_PLAN_BASELINE Function Parameters Parameter Description sql_handle SQL statement identifier. Unless plan_name is specified, NULL means to consider all statements with non-accepted plans in their SQL plan baselines. plan_name Plan identifier. Default NULL means to consider all non- accepted plans in the SQL plan baseline of either the identified SQL statement or all SQL statements if sql_handle is NULL . plan_list A list of plan names. Each plan in the list can belong to same or different SQL statement. time_limit Time limit in number of minutes. This applies only if verify = ' YES '. The time limit is global and it is used as follows: The time limit for first non-accepted plan verification is set equal to the input value; the time limit for second non-accepted plan verification is set equal to (input value - time spent in first plan verification); and so on. DBMS_SPM . AUTO_LIMIT (Default) lets the system choose an appropriate time limit based on the number of plan verifications required to be done. DBMS_SPM . NO_LIMIT means there is no time limit. A positive integer value represents a user specified time limit. verify Specifies whether to execute the plans and compare the performance before changing non-accepted plans into accepted plans. A performance verification involves executing a non-accepted plan and a plan chosen from corresponding SQL plan baseline and comparing their performance statistics. If non-accepted plan shows performance improvement, it is changed to an accepted plan. ' YES ' (Default) - verifies that a non-accepted plan gives better performance before changing it to an accepted plan ' NO ' - directs not to execute plans but only to change non-accepted plans into accepted plans commit Specifies whether to update the ACCEPTED status of non-accepted plans from ' NO ' to ' YES '. ' YES ' (Default) - perform updates of qualifying non-accepted plans and generate a report that shows the updates and the result of performance verification when verify = ' YES '. ' NO ' - generate a report without any updates. Note that commit = ' NO ' together with verify = ' NO ' represents a no-op. Return Values A CLOB containing a formatted text report showing non-accepted plans in sequence, each with a possible change of its ACCEPTED status, and if verify = ' YES ' the result of their performance verification. Usage Notes Invoking this subprogram requires the ADMINISTER SQL MANAGEMENT OBJECT privilege.