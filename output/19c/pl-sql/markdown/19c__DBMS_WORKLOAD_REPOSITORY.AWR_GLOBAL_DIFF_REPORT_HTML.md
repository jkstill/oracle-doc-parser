---
id: 19c__DBMS_WORKLOAD_REPOSITORY.AWR_GLOBAL_DIFF_REPORT_HTML
name: DBMS_WORKLOAD_REPOSITORY.AWR_GLOBAL_DIFF_REPORT_HTML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.AWR_GLOBAL_DIFF_REPORT_HTML

This table function displays Global AWR Compare Periods Report in HTML format.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.AWR_GLOBAL_DIFF_REPORT_HTML (
   dbid1        IN    NUMBER,
   inst_num1    IN    AWRRPT_INSTANCE_LIST_TYPE,
   bid1         IN    NUMBER,
   eid1         IN    NUMBER,
   dbid2        IN    NUMBER,
   inst_num2    IN    AWRRPT_INSTANCE_LIST_TYPE,
   bid2         IN    NUMBER,
   eid2         IN    NUMBER)
  RETURN awrrpt_html_type_table PIPELINED;

DBMS_WORKLOAD_REPOSITORY.AWR_GLOBAL_DIFF_REPORT_HTML (
   dbid1        IN    NUMBER,
   inst_num1    IN    VARCHAR2,
   bid1         IN    NUMBER,
   eid1         IN    NUMBER,
   dbid2        IN    NUMBER,
   inst_num2    IN    VARCHAR2,
   bid2         IN    NUMBER,
   eid2         IN    NUMBER)
  RETURN awrrpt_html_type_table PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dbid 1 |  |  | 1st database identifier |
| inst_num 1 |  |  | 1st list of instance numbers. If set to NULL , all instances for which begin and end snapshots are available, and which have not been restarted between snapshots, will be included in the report. |
| bid1 | NUMBER | IN | 1st beginning snapshot ID |
| eid 1 |  |  | 1st ending snapshot ID |
| dbid 2 |  |  | 2nd database identifier |
| inst_num 2 |  |  | 2nd list of instance numbers to be included in report. If set to NULL , all instances for which begin and end snapshots are available, and which have not been restarted between snapshots, will be included in the report. |
| bid2 | NUMBER | IN | 2nd beginning snapshot ID |
| eid 2 |  |  | 2nd ending snapshot ID |

**Returns:** `awrrpt_html_type_table`

## Usage Notes

The first overload accepts comma-separated lists of instance numbers for inst_num1 and inst_num2 . No leading zeroes are allowed and there is a limit of 1023 characters. Syntax DBMS_WORKLOAD_REPOSITORY.AWR_GLOBAL_DIFF_REPORT_HTML ( dbid1 IN NUMBER, inst_num1 IN AWRRPT_INSTANCE_LIST_TYPE, bid1 IN NUMBER, eid1 IN NUMBER, dbid2 IN NUMBER, inst_num2 IN AWRRPT_INSTANCE_LIST_TYPE, bid2 IN NUMBER, eid2 IN NUMBER) RETURN awrrpt_html_type_table PIPELINED; DBMS_WORKLOAD_REPOSITORY.AWR_GLOBAL_DIFF_REPORT_HTML ( dbid1 IN NUMBER, inst_num1 IN VARCHAR2, bid1 IN NUMBER, eid1 IN NUMBER, dbid2 IN NUMBER, inst_num2 IN VARCHAR2, bid2 IN NUMBER, eid2 IN NUMBER) RETURN awrrpt_html_type_table PIPELINED; Parameters Table 192-16 AWR_GLOBAL_DIFF_REPORT_HTML Function Parameters Parameter Description dbid 1 1st database identifier inst_num 1 1st list of instance numbers. If set to NULL , all instances for which begin and end snapshots are available, and which have not been restarted between snapshots, will be included in the report. bid1 1st beginning snapshot ID eid 1 1st ending snapshot ID dbid 2 2nd database identifier inst_num 2 2nd list of instance numbers to be included in report. If set to NULL , all instances for which begin and end snapshots are available, and which have not been restarted between snapshots, will be included in the report. bid2 2nd beginning snapshot ID eid 2 2nd ending snapshot ID Return Values The output will be one column of VARCHAR2(1500) .