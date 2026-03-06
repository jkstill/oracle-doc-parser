---
id: 19c__DBMS_ADVISOR.UPDATE_SQLWKLD_STATEMENT
name: DBMS_ADVISOR.UPDATE_SQLWKLD_STATEMENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.UPDATE_SQLWKLD_STATEMENT

This procedure updates an existing SQL statement in a specified SQL workload.

## Syntax

```sql
DBMS_ADVISOR.UPDATE_SQLWKLD_STATEMENT (
   workload_name     IN VARCHAR2,
   sql_id            IN NUMBER,
   application       IN VARCHAR2 := NULL,
   action            IN VARCHAR2 := NULL,
   priority          IN NUMBER := NULL,
   username          IN VARCHAR2 := NULL);

DBMS_ADVISOR.UPDATE_SQLWKLD_STATEMENT (
   workload_name     IN VARCHAR2,
   search            IN VARCHAR2,
   updated           OUT NUMBER,
   application       IN VARCHAR2 := NULL,
   action            IN VARCHAR2 := NULL,
   priority          IN NUMBER := NULL,
   username          IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| workload_name | VARCHAR2 | IN | The SQL Workload object name that uniquely identifies an existing workload. |
| sql_id | NUMBER | IN | The Advisor-generated identifier number that is assigned to the statement. To specify all workload statements, use the constant DBMS_ADVISOR.ADVISOR_ALL . |
| updated | NUMBER | OUT | Returns the number of statements changed by a searched update. |
| application | VARCHAR2 | IN | Specifies a business application name that will be associated with the SQL statement. If the value is NULL or contains the value ADVISOR_UNUSED , then the column will not be updated in the repository. |
| action | VARCHAR2 | IN | Specifies the application action for the statement. If the value is NULL or contains the value ADVISOR_UNUSED , then the column will not be updated in the repository. |
| priority | NUMBER | IN | The relative priority of the SQL statement. The value must be one of the following: 1 - HIGH , 2 - MEDIUM , or 3 - LOW . If the value is NULL or contains the value ADVISOR_UNUSED , then the column will not be updated in the repository. |
| username | VARCHAR2 | IN | The Oracle user name that executed the SQL statement. If the value is NULL or contains the value ADVISOR_UNUSED , then the column will not be updated in the repository. Because a user name is an Oracle identifier, the username value must be entered exactly like it is stored in the database. For example, if the user SCOTT is the executing user, then you must provide the user identifier SCOTT in all uppercase letters. The database does not recognize the user scott as a match for SCOTT . |
| search | VARCHAR2 | IN | Disabled. |

## Usage Notes

Note: This procedure is deprecated starting in Oracle Database 11 g . Note: This procedure is deprecated starting in Oracle Database 11 g . Syntax DBMS_ADVISOR.UPDATE_SQLWKLD_STATEMENT ( workload_name IN VARCHAR2, sql_id IN NUMBER, application IN VARCHAR2 := NULL, action IN VARCHAR2 := NULL, priority IN NUMBER := NULL, username IN VARCHAR2 := NULL); DBMS_ADVISOR.UPDATE_SQLWKLD_STATEMENT ( workload_name IN VARCHAR2, search IN VARCHAR2, updated OUT NUMBER, application IN VARCHAR2 := NULL, action IN VARCHAR2 := NULL, priority IN NUMBER := NULL, username IN VARCHAR2 := NULL); Parameters Table 16-44 UPDATE_SQLWKLD_STATEMENT Procedure Parameters Parameter Description workload_name The SQL Workload object name that uniquely identifies an existing workload. sql_id The Advisor-generated identifier number that is assigned to the statement. To specify all workload statements, use the constant DBMS_ADVISOR.ADVISOR_ALL . updated Returns the number of statements changed by a searched update. application Specifies a business application name that will be associated with the SQL statement. If the value is NULL or contains the value ADVISOR_UNUSED , then the column will not be updated in the repository. action Specifies the application action for the statement. If the value is NULL or contains the value ADVISOR_UNUSED , then the column will not be updated in the repository. priority The relative priority of the SQL statement. The value must be one of the following: 1 - HIGH , 2 - MEDIUM , or 3 - LOW . If the value is NULL or contains the value ADVISOR_UNUSED , then the column will not be updated in the repository. username The Oracle user name that executed the SQL statement. If the value is NULL or contains the value ADVISOR_UNUSED , then the column will not be updated in the repository. Because a user name is an Oracle identifier, the username value must be entered exactly like it is stored in the database. For example, if the user SCOTT is the executing user, then you must provide the user identifier SCOTT in all uppercase letters. The database does not recognize the user scott as a match for SCOTT . search Disabled. Usage Notes A workload cannot be modified or deleted if it is currently referenced by an active task. A task is considered active if it is not in its initial state. See RESET_TASK Procedure to set a task to its initial state.