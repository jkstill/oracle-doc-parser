---
id: 19c__DBMS_WORKLOAD_REPOSITORY.AWR_DIFF_REPORT_HTML
name: DBMS_WORKLOAD_REPOSITORY.AWR_DIFF_REPORT_HTML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.AWR_DIFF_REPORT_HTML

This table function displays the AWR Compare Periods report in HTML.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.AWR_DIFF_REPORT_HTML(
   dbid1     IN NUMBER,
   inst_num1 IN NUMBER,
   bid1      IN NUMBER,
   eid1      IN NUMBER,
   dbid2     IN NUMBER,
   inst_num2 IN NUMBER,
   bid2      IN NUMBER,
   eid2      IN NUMBER)
  RETURN awrdrpt_text_type_table PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dbid 1 |  |  | 1st database identifier |
| inst_num 1 |  |  | 1st instance number |
| bid 1 |  |  | 1st beginning snapshot ID |
| eid 1 |  |  | 1st ending snapshot ID |
| dbid 2 |  |  | 2nd database identifier |
| inst_num 2 |  |  | 2nd instance number |
| bid 2 |  |  | 2nd beginning snapshot ID |
| eid 2 |  |  | 2nd ending snapshot ID |

**Returns:** `awrdrpt_text_type_table`

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.AWR_DIFF_REPORT_HTML( dbid1 IN NUMBER, inst_num1 IN NUMBER, bid1 IN NUMBER, eid1 IN NUMBER, dbid2 IN NUMBER, inst_num2 IN NUMBER, bid2 IN NUMBER, eid2 IN NUMBER) RETURN awrdrpt_text_type_table PIPELINED; Parameters Table 192-13 AWR_DIFF_REPORT_HTML Parameters Parameter Description dbid 1 1st database identifier inst_num 1 1st instance number bid 1 1st beginning snapshot ID eid 1 1st ending snapshot ID dbid 2 2nd database identifier inst_num 2 2nd instance number bid 2 2nd beginning snapshot ID eid 2 2nd ending snapshot ID Return Values The output will be one column of VARCHAR2(500) . Usage Notes You can call the function directly but Oracle recommends you use the awrddrpt.sql script which prompts users for the required information.