---
id: 19c__DBMS_ADDM.INSERT_SEGMENT_DIRECTIVE
name: DBMS_ADDM.INSERT_SEGMENT_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADDM
tags: [dbms_addm]
source_file: DBMS_ADDM.html
---

# DBMS_ADDM.INSERT_SEGMENT_DIRECTIVE

This procedure creates a directive to prevent ADDM from creating actions to "run Segment Advisor" for specific segments. The directive can be created for a specific task (only when the task is in INITIAL status), or for all subsequently created ADDM tasks (such as a system directive).

## Syntax

```sql
DBMS_ADDM.INSERT_SEGMENT_DIRECTIVE (
   task_name             IN VARCHAR2,
   dir_name              IN VARCHAR2,
   owner_name            IN VARCHAR2,
   object_name           IN VARCHAR2 := NULL,
   sub_object_name       IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task this directive applies to. If the value is NULL , it applies to all subsequently created ADDM Tasks. |
| dir_name | VARCHAR2 | IN | Name of the directive. All directives must be given unique names. |
| owner_name | VARCHAR2 | IN | Specifies the owner of the segment/s to be filtered. A wildcard is allowed in the same syntax used for "like" constraints. |
| object_name | VARCHAR2 | IN | Name of the main object to be filtered. Again, wildcards are allowed. The default value of NULL is equivalent to a value of '%'. |
| sub_object_name | VARCHAR2 | IN | Name of the part of the main object to be filtered. This could be a partition name, or even sub partitions (separated by a '.'). Again, wildcards are allowed. The default value of NULL is equivalent to a value of '%'. |
| object_number |  |  | Object number of the SEGMENT that this directive is to filter, found in views DBA_OBJECTS or DBA_SEGMENTS |

## Usage Notes

Syntax DBMS_ADDM.INSERT_SEGMENT_DIRECTIVE ( task_name IN VARCHAR2, dir_name IN VARCHAR2, owner_name IN VARCHAR2, object_name IN VARCHAR2 := NULL, sub_object_name IN VARCHAR2 := NULL); DBMS_ADDM.INSERT_SEGMENT_DIRECTIVE ( task_name IN VARCHAR2, dir_name IN VARCHAR2, object_number IN NUMBER); Parameters Table 14-18 INSERT_SEGMENT_DIRECTIVE Procedure Parameters Parameter Description task_name Name of the task this directive applies to. If the value is NULL , it applies to all subsequently created ADDM Tasks. dir_name Name of the directive. All directives must be given unique names. owner_name Specifies the owner of the segment/s to be filtered. A wildcard is allowed in the same syntax used for "like" constraints. object_name Name of the main object to be filtered. Again, wildcards are allowed. The default value of NULL is equivalent to a value of '%'. sub_object_name Name of the part of the main object to be filtered. This could be a partition name, or even sub partitions (separated by a '.'). Again, wildcards are allowed. The default value of NULL is equivalent to a value of '%'. object_number Object number of the SEGMENT that this directive is to filter, found in views DBA_OBJECTS or DBA_SEGMENTS Examples A new ADDM task is created to analyze a local instance. However, it has special treatment for all segments that belong to user SCOTT . The result of GET_REPORT does not show actions for running Segment advisor for segments that belong to SCOTT . var tname VARCHAR2(60); BEGIN DBMS_ADDM.INSERT_SEGMENT_DIRECTIVE(NULL, 'my Segment directive', 'SCOTT'); :tname := 'my_instance_analysis_mode_task'; DBMS_ADDM.ANALYZE_INST(:tname, 1, 2); END; To see a report containing all actions regardless of the directive: SELECT DBMS_ADVISOR.GET_TASK_REPORT(:tname, 'TEXT', 'ALL') FROM DUAL;