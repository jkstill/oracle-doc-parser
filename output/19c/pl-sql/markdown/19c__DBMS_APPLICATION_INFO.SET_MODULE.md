---
id: 19c__DBMS_APPLICATION_INFO.SET_MODULE
name: DBMS_APPLICATION_INFO.SET_MODULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLICATION_INFO
tags: [dbms_application_info]
source_file: DBMS_APPLICATION_INFO.html
---

# DBMS_APPLICATION_INFO.SET_MODULE

This procedure sets the name of the current application or module.

## Syntax

```sql
DBMS_APPLICATION_INFO.SET_MODULE ( 
   module_name IN VARCHAR2, 
   action_name IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| module_name | VARCHAR2 | IN | Name of module that is currently running. When the current module terminates, call this procedure with the name of the new module if there is one, or NULL if there is not. Names longer than 48 bytes are truncated. |
| action_name | VARCHAR2) | IN | Name of current action within the current module. If you do not want to specify an action, this value should be NULL . Names longer than 32 bytes are truncated. |

## Usage Notes

Syntax DBMS_APPLICATION_INFO.SET_MODULE ( module_name IN VARCHAR2, action_name IN VARCHAR2); Parameters Table 20-6 SET_MODULE Procedure Parameters Parameter Description module_name Name of module that is currently running. When the current module terminates, call this procedure with the name of the new module if there is one, or NULL if there is not. Names longer than 48 bytes are truncated. action_name Name of current action within the current module. If you do not want to specify an action, this value should be NULL . Names longer than 32 bytes are truncated. Example CREATE or replace PROCEDURE add_employee( name VARCHAR2, salary NUMBER, manager NUMBER, title VARCHAR2, commission NUMBER, department NUMBER) AS BEGIN DBMS_APPLICATION_INFO.SET_MODULE( module_name => 'add_employee', action_name => 'insert into emp'); INSERT INTO emp (ename, empno, sal, mgr, job, hiredate, comm, deptno) VALUES (name, emp_seq.nextval, salary, manager, title, SYSDATE, commission, department); DBMS_APPLICATION_INFO.SET_MODULE(null,null); END;