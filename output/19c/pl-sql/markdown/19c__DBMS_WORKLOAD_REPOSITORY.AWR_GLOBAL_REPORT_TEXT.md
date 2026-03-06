---
id: 19c__DBMS_WORKLOAD_REPOSITORY.AWR_GLOBAL_REPORT_TEXT
name: DBMS_WORKLOAD_REPOSITORY.AWR_GLOBAL_REPORT_TEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.AWR_GLOBAL_REPORT_TEXT

This table function displays the Global AWR report in text.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.AWR_GLOBAL_REPORT_TEXT(
   l_dbid        IN    NUMBER,
   l_inst_num    IN    AWRRPT_INSTANCE_LIST_TYPE,
   l_bid         IN    NUMBER,
   l_eid         IN    NUMBER,
   l_options     IN    NUMBER DEFAULT 0)
  RETURN awrdrpt_text_type_table PIPELINED;

DBMS_WORKLOAD_REPOSITORY.AWR_GLOBAL_REPORT_TEXT(
   l_dbid       IN    NUMBER,
   l_inst_num   IN    VARCHAR2,
   l_bid        IN    NUMBER,
   l_eid        IN    NUMBER,
   l_options    IN    NUMBER DEFAULT 0)
  RETURN awrdrpt_text_type_table PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| l_dbid | NUMBER | IN | Database identifier |
| l_inst_num | AWRRPT_INSTANCE_LIST_TYPE | IN | List of instance numbers to be included in report. If set to NULL , all instances for which begin and end snapshots are available, and which have not been restarted between snapshots, will be included in the report. |
| l_bid | NUMBER | IN | Beginning snapshot ID |
| l_eid | NUMBER | IN | Ending snapshot ID |
| l_options | NUMBER | IN | A flag to specify to control the output of the report. Currently, not used. |

**Returns:** `awrdrpt_text_type_table`

## Usage Notes

The first overload accepts a comma-separated list of instance numbers. No leading zeroes are allowed and there is a limit of 1023 characters Syntax DBMS_WORKLOAD_REPOSITORY.AWR_GLOBAL_REPORT_TEXT( l_dbid IN NUMBER, l_inst_num IN AWRRPT_INSTANCE_LIST_TYPE, l_bid IN NUMBER, l_eid IN NUMBER, l_options IN NUMBER DEFAULT 0) RETURN awrdrpt_text_type_table PIPELINED; DBMS_WORKLOAD_REPOSITORY.AWR_GLOBAL_REPORT_TEXT( l_dbid IN NUMBER, l_inst_num IN VARCHAR2, l_bid IN NUMBER, l_eid IN NUMBER, l_options IN NUMBER DEFAULT 0) RETURN awrdrpt_text_type_table PIPELINED; Parameters Table 192-19 AWR_GLOBAL_REPORT_TEXT Function Parameters Parameter Description l_dbid Database identifier l_inst_num List of instance numbers to be included in report. If set to NULL , all instances for which begin and end snapshots are available, and which have not been restarted between snapshots, will be included in the report. l_bid Beginning snapshot ID l_eid Ending snapshot ID l_options A flag to specify to control the output of the report. Currently, not used. Return Values The output will be one column of VARCHAR2 (320) .