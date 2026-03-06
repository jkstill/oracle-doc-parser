---
id: 19c__DBMS_APPLICATION_INFO.READ_MODULE
name: DBMS_APPLICATION_INFO.READ_MODULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLICATION_INFO
tags: [dbms_application_info]
source_file: DBMS_APPLICATION_INFO.html
---

# DBMS_APPLICATION_INFO.READ_MODULE

This procedure reads the values of the module and action fields of the current session.

## Syntax

```sql
DBMS_APPLICATION_INFO.READ_MODULE ( 
   module_name OUT VARCHAR2, 
   action_name OUT VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| module_name | VARCHAR2 | OUT | Last value that the module name was set to by calling SET_MODULE . |
| action_name | VARCHAR2) | OUT | Last value that the action name was set to by calling SET_ACTION or SET_MODULE . |

## Usage Notes

Syntax DBMS_APPLICATION_INFO.READ_MODULE ( module_name OUT VARCHAR2, action_name OUT VARCHAR2); Parameters Table 20-3 READ_MODULE Procedure Parameters Parameter Description module_name Last value that the module name was set to by calling SET_MODULE . action_name Last value that the action name was set to by calling SET_ACTION or SET_MODULE . Usage Notes Module and action names for a registered application can be retrieved by querying V$SQLAREA or by calling the READ_MODULE procedure. Client information can be retrieved by querying the V$SESSION view, or by calling the READ_CLIENT_INFO Procedure . Examples The following sample query illustrates the use of the MODULE and ACTION column of the V$SQLAREA . SELECT sql_text, disk_reads, module, action FROM v$sqlarea WHERE module = 'add_employee'; SQL_TEXT DISK_READS MODULE ACTION ------------------- ---------- ------------------ ---------------- INSERT INTO emp 1 add_employee insert into emp (ename, empno, sal, mgr, job, hiredate, comm, deptno) VALUES (name, next.emp_seq, manager, title, SYSDATE, commission, department) 1 row selected.