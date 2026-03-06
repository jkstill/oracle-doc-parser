---
id: 19c__DBMS_SCHEDULER
name: DBMS_SCHEDULER
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER

The DBMS_SCHEDULER package defines OBJECT types and TABLE types.

## Syntax

```sql
TYPE jobarg IS OBJECT (
   arg_position         NUMBER,
   arg_text_value       VARCHAR2(4000),
   arg_anydata_value    ANYDATA,
   arg_operation        VARCHAR2(5));
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| arg_position | NUMBER | IN | Position of the argument |
| arg_value |  |  | Value of the argument |
| arg_reset |  |  | If arg_reset is TRUE , then the argument at that position is reset. Setting arg_reset to FALSE (which is the default) will create an argument with a NULL value. |

## Usage Notes

OBJECT Types JOBARG Object Type JOB_DEFINITION Object Type JOBATTR Object Type SCHEDULER$_STEP_TYPE Object Type SCHEDULER$_EVENT_INFO Object Type SCHEDULER_FILEWATCHER_RESULT Object Type SCHEDULER_FILEWATCHER_REQUEST Object Type TABLE Types JOBARG_ARRAY Table Type JOB_DEFINITION_ARRAY Table Type JOBATTR_ARRAY Table Type SCHEDULER$_STEP_TYPE_LIST Table Type Syntax TYPE jobarg IS OBJECT ( arg_position NUMBER, arg_text_value VARCHAR2(4000), arg_anydata_value ANYDATA, arg_operation VARCHAR2(5)); Attributes Table 151-2 JOBARG Object Type Attributes Attribute Description arg_position Position of the argument arg_text_value Value of the argument if the type is VARCHAR2 arg_anydata_value Value of the argument if the type is AnyData arg_operation Type of the operation: SET RESET JOBARG Constructor Function This constructor function constructs a job argument. It is overloaded to construct job arguments with different types of values. Syntax Constructs a job argument with a text value. constructor function jobarg ( arg_position IN POSITIVEN, arg_value IN VARCHAR2) RETURN SELF AS RESULT; Constructs a job argument with an AnyData value. constructor function jobarg ( arg_position IN POSITIVEN, arg_value IN ANYDATA) RETURN SELF AS RESULT; Constructs a job argument with a NULL value. constructor function jobarg ( arg_position IN POSITIVEN, arg_reset IN BOOLEAN DEFAULT FALSE) RETURN SELF AS RESULT; Parameters Table 151-3 JOBARG Constructor Function Parameters Parameter Description arg_position Position of the argument arg_value Value of the argument arg_reset If arg_reset is TRUE , then the argument at that position is reset. Setting arg_reset to FALSE (which is the default) will create an argument with a NULL value.