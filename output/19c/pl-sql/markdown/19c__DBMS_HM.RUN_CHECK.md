---
id: 19c__DBMS_HM.RUN_CHECK
name: DBMS_HM.RUN_CHECK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HM
tags: [dbms_hm]
source_file: DBMS_HM.html
---

# DBMS_HM.RUN_CHECK

This procedure runs the specified checker with the specified arguments.

## Syntax

```sql
DBMS_HM.RUN_CHECK (
   check_name     IN  VARCHAR2,
   run_name       IN  VARCHAR2 := NULL,
   timeout        IN  NUMBER := NULL,
   input_params   IN  VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| check_name | VARCHAR2 | IN | Name of the check to be invoked. Check names and their parameters can be accessed from the V$HM_CHECK and V$HM_CHECK_PARAM views. Users can run all checks which are not internal in nature: SELECT name FROM V$HM_CHECK WHERE INTERNAL_CHECK = 'N' retrieves the list of checks that can be run manually by users. |
| run_name | VARCHAR2 | IN | Name with which external users can uniquely identify this check's run. If NULL value is passed, then HM creates a unique name and associates with this check's run. |
| timeout | NUMBER | IN | Maximum amount of time (in units of seconds), this checker run is allowed to run. HM will interrupt the run, if it the specified time elapses for the run. If NULL value is passed, HM doesn't impose any timeout limits on the run. |
| input_params | VARCHAR2 | IN | Input string: which consists of name, value pairs de-limited by a special character ';'. Example ('Data Block Integrity Check' invocation may take following type of input parameters. 'BLC_DF_NUM=1;BLC_BL_NUM=23456' Input parameters BLC_DF_NUM and BLC_BL_NUM have values '1' and '23456' respectively. Every check will have well defined set of inputs associated with it. These Input parameters, their types, default values and descriptions can be obtained using V$HM_CHECK_PARAM view. Example: The following query gets the list of parameters, their default values and descriptions for a 'Data Block Integrity Check' SELECT a.* FROM v$hm_check_param a, v$hm_check b WHERE a.check_id = b.id AND b.name = 'Data Block Integrity Check'; |

## Usage Notes

You can specify a name for the run, the inputs needed and maximum time-out for the run. The run report will be maintained persistently in the database. Syntax DBMS_HM.RUN_CHECK ( check_name IN VARCHAR2, run_name IN VARCHAR2 := NULL, timeout IN NUMBER := NULL, input_params IN VARCHAR2 := NULL); Parameters Table 82-3 RUN_CHECK Procedure Parameters Parameter Description check_name Name of the check to be invoked. Check names and their parameters can be accessed from the V$HM_CHECK and V$HM_CHECK_PARAM views. Users can run all checks which are not internal in nature: SELECT name FROM V$HM_CHECK WHERE INTERNAL_CHECK = 'N' retrieves the list of checks that can be run manually by users. run_name Name with which external users can uniquely identify this check's run. If NULL value is passed, then HM creates a unique name and associates with this check's run. timeout Maximum amount of time (in units of seconds), this checker run is allowed to run. HM will interrupt the run, if it the specified time elapses for the run. If NULL value is passed, HM doesn't impose any timeout limits on the run. input_params Input string: which consists of name, value pairs de-limited by a special character ';'. Example ('Data Block Integrity Check' invocation may take following type of input parameters. 'BLC_DF_NUM=1;BLC_BL_NUM=23456' Input parameters BLC_DF_NUM and BLC_BL_NUM have values '1' and '23456' respectively. Every check will have well defined set of inputs associated with it. These Input parameters, their types, default values and descriptions can be obtained using V$HM_CHECK_PARAM view. Example: The following query gets the list of parameters, their default values and descriptions for a 'Data Block Integrity Check' SELECT a.* FROM v$hm_check_param a, v$hm_check b WHERE a.check_id = b.id AND b.name = 'Data Block Integrity Check';