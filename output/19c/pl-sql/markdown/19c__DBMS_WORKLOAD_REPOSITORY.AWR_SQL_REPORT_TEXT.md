---
id: 19c__DBMS_WORKLOAD_REPOSITORY.AWR_SQL_REPORT_TEXT
name: DBMS_WORKLOAD_REPOSITORY.AWR_SQL_REPORT_TEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.AWR_SQL_REPORT_TEXT

This table function displays the AWR SQL Report in text format.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.AWR_SQL_REPORT_TEXT(
   l_dbid       IN    NUMBER,
   l_inst_num   IN    NUMBER,
   l_bid        IN    NUMBER,
   l_eid        IN    NUMBER,
   l_sqlid      IN    VARCHAR2,
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
| l_sqlid | VARCHAR2 | IN | SQL ID of statement to be analyzed |
| l_options | NUMBER | IN | Flag to specify to control the output of the report. Currently, not used. |

**Returns:** `awrrpt_text_type_table`

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.AWR_SQL_REPORT_TEXT( l_dbid IN NUMBER, l_inst_num IN NUMBER, l_bid IN NUMBER, l_eid IN NUMBER, l_sqlid IN VARCHAR2, l_options IN NUMBER DEFAULT 0) RETURN awrrpt_text_type_table PIPELINED; Parameters Table 192-25 AWR_SQL_REPORT_TEXT Parameters Parameter Description l_dbid Database identifier l_inst_num Instance number l_bid Beginning snapshot ID l_eid Ending snapshot ID l_sqlid SQL ID of statement to be analyzed l_options Flag to specify to control the output of the report. Currently, not used. Return Values The output will be one column of VARCHAR2(120) . Usage Notes You can call the function directly but Oracle recommends you use the awrsqrpt.sql script which prompts users for the required information.