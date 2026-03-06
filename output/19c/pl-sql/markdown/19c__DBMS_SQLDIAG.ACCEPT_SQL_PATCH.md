---
id: 19c__DBMS_SQLDIAG.ACCEPT_SQL_PATCH
name: DBMS_SQLDIAG.ACCEPT_SQL_PATCH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.ACCEPT_SQL_PATCH

This procedure accepts a recommended SQL patch as recommended by the specified SQL diagnosis task.

## Syntax

```sql
DBMS_SQLDIAG.ACCEPT_SQL_PATCH (
   task_name      IN  VARCHAR2,
   object_id      IN  NUMBER := NULL,
   name           IN  VARCHAR2 := NULL,
   description    IN  VARCHAR2 := NULL,
   category       IN  VARCHAR2 := NULL,
   task_owner     IN  VARCHAR2 := NULL,
   replace        IN  BOOLEAN := FALSE,
   force_match    IN  BOOLEAN := FALSE)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| taskname |  |  | Name of the SQL diagnosis task |
| object_id | NUMBER | IN | Identifier of the advisor framework object representing the SQL statement associated to the diagnosis task |
| name | VARCHAR2 | IN | Name of the patch. It cannot contain double quotation marks. The name is case sensitive. If not specified, the system will generate a unique name for the SQL patch. |
| description | VARCHAR2 | IN | User specified string describing the purpose of this SQL patch. Maximum size of description is 500 . |
| category | VARCHAR2 | IN | Category name which must match the value of the SQLDIAGNOSE_CATEGORY parameter in a session for the session to use this patch. It defaults to the value DEFAULT . This is also the default of the SQLDIAGNOSE_CATEGORY parameter. The category must be a valid Oracle identifier. The category name specified is always converted to upper case. The combination of the normalized SQL text and category name create a unique key for a patch. An accept will fail if this combination is duplicated. |
| task_owner | VARCHAR2 | IN | Owner of the diagnosis task. This is an optional parameter that has to be specified to accept a SQL Patch associated to a diagnosis task owned by another user. The current user is the default value. |
| replace | BOOLEAN | IN | If the patch already exists, it will be replaced if this argument is TRUE . It is an error to pass a name that is already being used for another signature/category pair, even with replace set to TRUE . |
| force_match | BOOLEAN | IN | If TRUE this causes SQL Patches to target all SQL statements which have the same text after normalizing all literal values into bind variables. (Note that if a combination of literal values and bind values is used in a SQL statement, no bind transformation occurs.) This is analogous to the matching algorithm used by the FORCE option of the CURSOR_SHARING parameter. If FALSE , literals are not transformed. This is analogous to the matching algorithm used by the EXACT option of the CURSOR_SHARING parameter. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_SQLDIAG.ACCEPT_SQL_PATCH ( task_name IN VARCHAR2, object_id IN NUMBER := NULL, name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, category IN VARCHAR2 := NULL, task_owner IN VARCHAR2 := NULL, replace IN BOOLEAN := FALSE, force_match IN BOOLEAN := FALSE) RETURN VARCHAR2; DBMS_SQLDIAG.ACCEPT_SQL_PATCH ( task_name IN VARCHAR2, object_id IN NUMBER := NULL, name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, category IN VARCHAR2 := NULL, task_owner IN VARCHAR2 := NULL, replace IN BOOLEAN := FALSE, force_match IN BOOLEAN := FALSE); Parameters Table 165-10 ACCEPT_SQL_PATCH Function & Procedure Parameters Parameter Description taskname Name of the SQL diagnosis task object_id Identifier of the advisor framework object representing the SQL statement associated to the diagnosis task name Name of the patch. It cannot contain double quotation marks. The name is case sensitive. If not specified, the system will generate a unique name for the SQL patch. description User specified string describing the purpose of this SQL patch. Maximum size of description is 500 . category Category name which must match the value of the SQLDIAGNOSE_CATEGORY parameter in a session for the session to use this patch. It defaults to the value DEFAULT . This is also the default of the SQLDIAGNOSE_CATEGORY parameter. The category must be a valid Oracle identifier. The category name specified is always converted to upper case. The combination of the normalized SQL text and category name create a unique key for a patch. An accept will fail if this combination is duplicated. task_owner Owner of the diagnosis task. This is an optional parameter that has to be specified to accept a SQL Patch associated to a diagnosis task owned by another user. The current user is the default value. replace If the patch already exists, it will be replaced if this argument is TRUE . It is an error to pass a name that is already being used for another signature/category pair, even with replace set to TRUE . force_match If TRUE this causes SQL Patches to target all SQL statements which have the same text after normalizing all literal values into bind variables. (Note that if a combination of literal values and bind values is used in a SQL statement, no bind transformation occurs.) This is analogous to the matching algorithm used by the FORCE option of the CURSOR_SHARING parameter. If FALSE , literals are not transformed. This is analogous to the matching algorithm used by the EXACT option of the CURSOR_SHARING parameter. Return Values Name of the SQL patch Usage Notes Requires CREATE ANY SQL PROFILE privilege