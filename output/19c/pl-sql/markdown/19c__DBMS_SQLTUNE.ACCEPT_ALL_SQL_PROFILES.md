---
id: 19c__DBMS_SQLTUNE.ACCEPT_ALL_SQL_PROFILES
name: DBMS_SQLTUNE.ACCEPT_ALL_SQL_PROFILES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.ACCEPT_ALL_SQL_PROFILES

This procedure accepts all SQL profiles recommended by a specific execution of a tuning task, and sets the attributes of the SQL profiles according to the parameter values passed by the user.

## Syntax

```sql
DBMS_SQLTUNE.ACCEPT_ALL_SQL_PROFILES (
   task_name         IN VARCHAR2,
   category          IN VARCHAR2 := NULL,
   replace           IN BOOLEAN  := FALSE,
   force_match       IN BOOLEAN  := FALSE,
   profile_type      IN VARCHAR2 := REGULAR_PROFILE,
   autotune_period   IN NUMBER   := NULL,
   execution_name    IN VARCHAR2 := NULL,
   task_owner        IN VARCHAR2 := NULL,
   description       IN VARCHAR2 := NULL,
   database_link_to  IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | The (mandatory) name of the SQL tuning task |
| category | VARCHAR2 | IN | This is the category name which must match the value of the SQLTUNE_CATEGORY parameter in a session for the session to use this SQL profile. It defaults to the value " DEFAULT ". This is also the default of the SQLTUNE_CATEGORY parameter. The category must be a valid Oracle identifier. The category name specified is always converted to upper case. The combination of the normalized SQL text and category name creates a unique key for a SQL profile. An ACCEPT_SQL_PROFILE fails if this combination is duplicated. |
| replace | BOOLEAN | IN | If the profile already exists, it is replaced if this argument is TRUE . It is an error to pass a name that is already being used for another signature/category pair, even with replace set to TRUE . |
| force_match | BOOLEAN | IN | If TRUE this causes SQL profiles to target all SQL statements which have the same text after normalizing all literal values into bind variables. (Note that if a combination of literal values and bind values is used in a SQL statement, no bind transformation occurs.) This is analogous to the matching algorithm used by the FORCE option of the cursor_sharing parameter. If FALSE , literals are not transformed. This is analogous to the matching algorithm used by the EXACT option of the cursor_sharing parameter. |
| profile_type | VARCHAR2 | IN | Options: REGULAR_PROFILE - profile without a change to parallel execution (Default, equivalent to NULL ). Note that if the SQL statement currently has a parallel execution plan, the regular profile will cause the optimizer to choose a different, but still parallel, execution plan. PX_PROFILE - regular profile with a change to parallel execution |
| autotune_period | NUMBER | IN | The time period for the automatic SQL tuning. This setting applies only to the automatic SQL Tuning Advisor task. Possible values are as follows: null or negative value (default) - all or full. The result includes all task executions. 0 - result of the current or most recent task execution. 1 - result for the most recent 24-hour period. 7 - result for the most recent 7-day period. The procedure interprets any other value as the time of the most recent task execution minus the value of this argument. |
| execution_name | VARCHAR2 | IN | Name of the task execution to use. If null, then the procedure generates the report for the most recent task execution. |
| task_owner | VARCHAR2 | IN | Owner of the tuning task. This is an optional parameter that must be specified to accept a SQL profile associated to a tuning task owned by another user. The current user is the default value. |
| description | VARCHAR2 | IN | A user specified string describing the purpose of the SQL profile. The description is truncated if longer than 256 characters. The maximum size is 500 characters. |
| database_link_to | VARCHAR2 | IN | Name of a database link that exists on a standby database. The link specifies the connection to a primary database. By default, the value is null, which means that the SQL Tuning Advisor session is local. Use DBMS_SQLTUNE to tune high-load SQL statements running on a standby database in an Active Data Guard scenario. When you execute REPORT_TUNING_TASK locally on the standby database, the function uses the database link to obtain the data from the primary database, and then constructs it locally on the standby database. The database_link_to parameter must specify a private database link. This link must be owned by SYS and accessed by the default privileged user SYS$UMF . The following sample statement creates a link named lnk_to_pri : CREATE DATABASE LINK lnk_to_pri CONNECT TO SYS$UMF IDENTIFIED BY password USING 'inst1'; |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.ACCEPT_ALL_SQL_PROFILES ( task_name IN VARCHAR2, category IN VARCHAR2 := NULL, replace IN BOOLEAN := FALSE, force_match IN BOOLEAN := FALSE, profile_type IN VARCHAR2 := REGULAR_PROFILE, autotune_period IN NUMBER := NULL, execution_name IN VARCHAR2 := NULL, task_owner IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, database_link_to IN VARCHAR2 := NULL); Parameters Table 169-8 ACCEPT_ALL_SQL_PROFILES Procedure Parameters Parameter Description task_name The (mandatory) name of the SQL tuning task category This is the category name which must match the value of the SQLTUNE_CATEGORY parameter in a session for the session to use this SQL profile. It defaults to the value " DEFAULT ". This is also the default of the SQLTUNE_CATEGORY parameter. The category must be a valid Oracle identifier. The category name specified is always converted to upper case. The combination of the normalized SQL text and category name creates a unique key for a SQL profile. An ACCEPT_SQL_PROFILE fails if this combination is duplicated. replace If the profile already exists, it is replaced if this argument is TRUE . It is an error to pass a name that is already being used for another signature/category pair, even with replace set to TRUE . force_match If TRUE this causes SQL profiles to target all SQL statements which have the same text after normalizing all literal values into bind variables. (Note that if a combination of literal values and bind values is used in a SQL statement, no bind transformation occurs.) This is analogous to the matching algorithm used by the FORCE option of the cursor_sharing parameter. If FALSE , literals are not transformed. This is analogous to the matching algorithm used by the EXACT option of the cursor_sharing parameter. profile_type Options: REGULAR_PROFILE - profile without a change to parallel execution (Default, equivalent to NULL ). Note that if the SQL statement currently has a parallel execution plan, the regular profile will cause the optimizer to choose a different, but still parallel, execution plan. PX_PROFILE - regular profile with a change to parallel execution autotune_period The time period for the automatic SQL tuning. This setting applies only to the automatic SQL Tuning Advisor task. Possible values are as follows: null or negative value (default) - all or full. The result includes all task executions. 0 - result of the current or most recent task execution. 1 - result for the most recent 24-hour period. 7 - result for the most recent 7-day period. The procedure interprets any other value as the time of the most recent task execution minus the value of this argument. execution_name Name of the task execution to use. If null, then the procedure generates the report for the most recent task execution. task_owner Owner of the tuning task. This is an optional parameter that must be specified to accept a SQL profile associated to a tuning task owned by another user. The current user is the default value. description A user specified string describing the purpose of the SQL profile. The description is truncated if longer than 256 characters. The maximum size is 500 characters. database_link_to Name of a database link that exists on a standby database. The link specifies the connection to a primary database. By default, the value is null, which means that the SQL Tuning Advisor session is local. Use DBMS_SQLTUNE to tune high-load SQL statements running on a standby database in an Active Data Guard scenario. When you execute REPORT_TUNING_TASK locally on the standby database, the function uses the database link to obtain the data from the primary database, and then constructs it locally on the standby database. The database_link_to parameter must specify a private database link. This link must be owned by SYS and accessed by the default privileged user SYS$UMF . The following sample statement creates a link named lnk_to_pri : CREATE DATABASE LINK lnk_to_pri CONNECT TO SYS$UMF IDENTIFIED BY password USING 'inst1'; Security Model The ADMINISTER SQL MANAGEMENT OBJECT privilege is required. The CREATE ANY SQL PROFILE privilege is deprecated.