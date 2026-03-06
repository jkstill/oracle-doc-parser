---
id: 19c__DBMS_WORKLOAD_REPOSITORY.AWR_REPORT_HTML
name: DBMS_WORKLOAD_REPOSITORY.AWR_REPORT_HTML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.AWR_REPORT_HTML

This table function displays the AWR report in HTML.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.AWR_REPORT_HTML(
   l_dbid       IN    NUMBER,
   l_inst_num   IN    NUMBER,
   l_bid        IN    NUMBER,
   l_eid        IN    NUMBER,
   l_options    IN    NUMBER DEFAULT 0)
 RETURN awrrpt_text_type_table PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| l_dbid | NUMBER | IN | Database identifier |
| l_inst_num | NUMBER | IN | Instance number |
| l_bid | NUMBER | IN | Beginning snapshot ID |
| l_eid | NUMBER | IN | Ending snapshot ID |
| l_options | NUMBER | IN | A flag to specify to control the output of the report. Currently, Oracle supports one value: l_options - 8 . Displays the ADDM specific portions of the report. These sections include the Buffer Pool Advice, Shared Pool Advice, and PGA Target Advice. |

**Returns:** `awrrpt_text_type_table`

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.AWR_REPORT_HTML( l_dbid IN NUMBER, l_inst_num IN NUMBER, l_bid IN NUMBER, l_eid IN NUMBER, l_options IN NUMBER DEFAULT 0) RETURN awrrpt_text_type_table PIPELINED; Parameters Table 192-21 AWR_REPORT_HTML Parameters Parameter Description l_dbid Database identifier l_inst_num Instance number l_bid Beginning snapshot ID l_eid Ending snapshot ID l_options A flag to specify to control the output of the report. Currently, Oracle supports one value: l_options - 8 . Displays the ADDM specific portions of the report. These sections include the Buffer Pool Advice, Shared Pool Advice, and PGA Target Advice. Return Values The output will be one column of VARCHAR2(1500) . Usage Notes You can call the function directly but Oracle recommends you use the awrrpt.sql script which prompts users for the required information.