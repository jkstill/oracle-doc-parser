---
id: 19c__DBMS_SQLQ.ALTER_QUARANTINE
name: DBMS_SQLQ.ALTER_QUARANTINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLQ
tags: [dbms_sqlq]
source_file: DBMS_SQLQ.html
---

# DBMS_SQLQ.ALTER_QUARANTINE

This procedure specifies a quarantine threshold for a resource in a quarantine configuration for execution plans of a SQL statement.

## Syntax

```sql
DBMS_SQLQ.ALTER_QUARANTINE (
   quarantine_name   IN VARCHAR2,
   parameter_name    IN VARCHAR2,
   parameter_value   IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| quarantine_name | VARCHAR2 | IN | Name of the quarantine configuration. |
| parameter_name | VARCHAR2 | IN | Name of the resource for which quarantine threshold needs to be specified. You can specify any one of the following values: CPU_TIME : CPU time ELAPSED_TIME : Elapsed time IO_MEGABYTES : I/O in megabytes IO_REQUESTS : Number of physical I/O requests IO_LOGICAL : Number of logical I/O requests ENABLED : Flag to enable or disable the quarantine configuration. Specify YES to enable it and NO to disable it. The default value is YES . AUTOPURGE : Flag to enable or disable automatic purging of the quarantine configuration. If it is set to YES , the quarantine configuration is automatically purged after 53 weeks, if not used. If it is set to NO , the quarantine configuration is never purged. The default value is YES . |
| parameter_value | VARCHAR2) | IN | Quarantine threshold for the resource specified in parameter_name . |

## Usage Notes

Syntax DBMS_SQLQ.ALTER_QUARANTINE ( quarantine_name IN VARCHAR2, parameter_name IN VARCHAR2, parameter_value IN VARCHAR2); Parameters Table 167-2 ALTER_QUARANTINE Procedure Parameters Parameter Description quarantine_name Name of the quarantine configuration. parameter_name Name of the resource for which quarantine threshold needs to be specified. You can specify any one of the following values: CPU_TIME : CPU time ELAPSED_TIME : Elapsed time IO_MEGABYTES : I/O in megabytes IO_REQUESTS : Number of physical I/O requests IO_LOGICAL : Number of logical I/O requests ENABLED : Flag to enable or disable the quarantine configuration. Specify YES to enable it and NO to disable it. The default value is YES . AUTOPURGE : Flag to enable or disable automatic purging of the quarantine configuration. If it is set to YES , the quarantine configuration is automatically purged after 53 weeks, if not used. If it is set to NO , the quarantine configuration is never purged. The default value is YES . parameter_value Quarantine threshold for the resource specified in parameter_name . Examples In the following example, the quarantine threshold specified for CPU time is 5 seconds and elapsed time is 10 seconds for the quarantine configuration SQL_QUARANTINE_3z0mwuq3aqsm8cfe7a0e4 . BEGIN DBMS_SQLQ.ALTER_QUARANTINE( QUARANTINE_NAME => 'SQL_QUARANTINE_3z0mwuq3aqsm8cfe7a0e4', PARAMETER_NAME => 'CPU_TIME', PARAMETER_VALUE => '5'); DBMS_SQLQ.ALTER_QUARANTINE( QUARANTINE_NAME => 'SQL_QUARANTINE_3z0mwuq3aqsm8cfe7a0e4', PARAMETER_NAME => 'ELAPSED_TIME', PARAMETER_VALUE => '10'); END; / When the SQL statement is executed using the execution plan specified in the quarantine configuration, and if the Resource Manager threshold for CPU time is 5 seconds or less, or elapsed time is 10 seconds or less, then the SQL statement is not allowed to run.