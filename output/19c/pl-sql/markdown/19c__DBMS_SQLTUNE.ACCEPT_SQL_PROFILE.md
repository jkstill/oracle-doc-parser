---
id: 19c__DBMS_SQLTUNE.ACCEPT_SQL_PROFILE
name: DBMS_SQLTUNE.ACCEPT_SQL_PROFILE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.ACCEPT_SQL_PROFILE

This subprogram creates a SQL profile recommended by SQL Tuning Advisor.

## Syntax

```sql
DBMS_SQLTUNE.ACCEPT_SQL_PROFILE (
   task_name    IN  VARCHAR2,
   object_id    IN  NUMBER   := NULL,
   name         IN  VARCHAR2 := NULL,
   description  IN  VARCHAR2 := NULL,
   category     IN  VARCHAR2 := NULL);
   task_owner   IN VARCHAR2  := NULL,
   replace      IN BOOLEAN   := FALSE,
   force_match  IN BOOLEAN   := FALSE,
   profile_type IN VARCHAR2  := REGULAR_PROFILE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | The (mandatory) name of the SQL tuning task |
| object_id | NUMBER | IN | The identifier of the advisor framework object representing the SQL statement associated with the tuning task |
| name | VARCHAR2 | IN | The name of the SQL profile. It cannot contain double quotation marks. The name is case sensitive. If not specified, the system generates a unique name for the SQL profile. |
| description | VARCHAR2 | IN | A user specified string describing the purpose of the SQL profile. The description is truncated if longer than 256 characters. The maximum size is 500 characters. |
| category | VARCHAR2 | IN | The category name. This name must match the value of the SQLTUNE_CATEGORY parameter in a session for the session to use this SQL profile. It defaults to the value " DEFAULT ". This is also the default of the SQLTUNE_CATEGORY parameter. The category must be a valid Oracle identifier. The category name specified is always converted to upper case. The combination of the normalized SQL text and category name creates a unique key for a SQL profile. An ACCEPT_SQL_PROFILE fails if this combination is duplicated. |
| task_owner | VARCHAR2 | IN | Owner of the tuning task. This is an optional parameter that has to be specified to accept a SQL profile associated to a tuning task owned by another user. The current user is the default value. |
| replace | BOOLEAN | IN | If the profile already exists, it is replaced if this argument is TRUE . It is an error to pass a name that is already being used for another signature/category pair, even with replace set to TRUE . |
| force_match | BOOLEAN | IN | If TRUE this causes SQL profiles to target all SQL statements which have the same text after normalizing all literal values into bind variables. (Note that if a combination of literal values and bind values is used in a SQL statement, no bind transformation occurs.) This is analogous to the matching algorithm used by the FORCE option of the cursor_sharing parameter. If FALSE , literals are not transformed. This is analogous to the matching algorithm used by the EXACT option of the cursor_sharing parameter. |
| profile_type | VARCHAR2 | IN | Options: REGULAR_PROFILE - profile without a change to parallel execution (Default, equivalent to NULL ). Note that if the SQL statement currently has a parallel execution plan, the regular profile will cause the optimizer to choose a different, but still parallel, execution plan. PX_PROFILE - regular profile with a change to parallel execution |
| database_link_to |  |  | Name of a database link that exists on a standby database. The link specifies the connection to a primary database. By default, the value is null, which means that the SQL Tuning Advisor session is local. Use DBMS_SQLTUNE to tune high-load SQL statements running on a standby database in an Active Data Guard scenario. When you execute REPORT_TUNING_TASK locally on the standby database, the function uses the database link to obtain the data from the primary database, and then constructs it locally on the standby database. The database_link_to parameter must specify a private database link. This link must be owned by SYS and accessed by the default privileged user SYS$UMF . The following sample statement creates a link named lnk_to_pri : CREATE DATABASE LINK lnk_to_pri CONNECT TO SYS$UMF IDENTIFIED BY password USING 'inst1'; |

**Returns:** `UNKNOWN`

## Usage Notes

The SQL text is normalized for matching purposes although it is stored in the data dictionary in denormalized form for readability. SQL text is provided through a reference to the SQL Tuning task. If the referenced SQL statement does not exist, then the database reports an error. See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.ACCEPT_SQL_PROFILE ( task_name IN VARCHAR2, object_id IN NUMBER := NULL, name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, category IN VARCHAR2 := NULL); task_owner IN VARCHAR2 := NULL, replace IN BOOLEAN := FALSE, force_match IN BOOLEAN := FALSE, profile_type IN VARCHAR2 := REGULAR_PROFILE); DBMS_SQLTUNE.ACCEPT_SQL_PROFILE ( task_name IN VARCHAR2, object_id IN NUMBER := NULL, name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, category IN VARCHAR2 := NULL; task_owner IN VARCHAR2 := NULL, replace IN BOOLEAN := FALSE, force_match IN BOOLEAN := FALSE, profile_type IN VARCHAR2 := REGULAR_PROFILE, database_link_to IN VARCHAR2 := NULL) RETURN VARCHAR2; Parameters Table 169-9 ACCEPT_SQL_PROFILE Procedure and Function Parameters Parameter Description task_name The (mandatory) name of the SQL tuning task object_id The identifier of the advisor framework object representing the SQL statement associated with the tuning task name The name of the SQL profile. It cannot contain double quotation marks. The name is case sensitive. If not specified, the system generates a unique name for the SQL profile. description A user specified string describing the purpose of the SQL profile. The description is truncated if longer than 256 characters. The maximum size is 500 characters. category The category name. This name must match the value of the SQLTUNE_CATEGORY parameter in a session for the session to use this SQL profile. It defaults to the value " DEFAULT ". This is also the default of the SQLTUNE_CATEGORY parameter. The category must be a valid Oracle identifier. The category name specified is always converted to upper case. The combination of the normalized SQL text and category name creates a unique key for a SQL profile. An ACCEPT_SQL_PROFILE fails if this combination is duplicated. task_owner Owner of the tuning task. This is an optional parameter that has to be specified to accept a SQL profile associated to a tuning task owned by another user. The current user is the default value. replace If the profile already exists, it is replaced if this argument is TRUE . It is an error to pass a name that is already being used for another signature/category pair, even with replace set to TRUE . force_match If TRUE this causes SQL profiles to target all SQL statements which have the same text after normalizing all literal values into bind variables. (Note that if a combination of literal values and bind values is used in a SQL statement, no bind transformation occurs.) This is analogous to the matching algorithm used by the FORCE option of the cursor_sharing parameter. If FALSE , literals are not transformed. This is analogous to the matching algorithm used by the EXACT option of the cursor_sharing parameter. profile_type Options: REGULAR_PROFILE - profile without a change to parallel execution (Default, equivalent to NULL ). Note that if the SQL statement currently has a parallel execution plan, the regular profile will cause the optimizer to choose a different, but still parallel, execution plan. PX_PROFILE - regular profile with a change to parallel execution database_link_to Name of a database link that exists on a standby database. The link specifies the connection to a primary database. By default, the value is null, which means that the SQL Tuning Advisor session is local. Use DBMS_SQLTUNE to tune high-load SQL statements running on a standby database in an Active Data Guard scenario. When you execute REPORT_TUNING_TASK locally on the standby database, the function uses the database link to obtain the data from the primary database, and then constructs it locally on the standby database. The database_link_to parameter must specify a private database link. This link must be owned by SYS and accessed by the default privileged user SYS$UMF . The following sample statement creates a link named lnk_to_pri : CREATE DATABASE LINK lnk_to_pri CONNECT TO SYS$UMF IDENTIFIED BY password USING 'inst1'; Return Values The name of the SQL profile.