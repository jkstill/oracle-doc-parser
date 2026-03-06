---
id: 19c__DBMS_ADVISOR.UPDATE_TASK_ATTRIBUTES
name: DBMS_ADVISOR.UPDATE_TASK_ATTRIBUTES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.UPDATE_TASK_ATTRIBUTES

This procedure changes various attributes of a task or a task template.

## Syntax

```sql
DBMS_ADVISOR.UPDATE_TASK_ATTRIBUTES (
   task_name          IN VARCHAR2
   new_name           IN VARCHAR2 := NULL,
   description        IN VARCHAR2 := NULL,
   read_only          IN VARCHAR2 := NULL,
   is_template        IN VARCHAR2 := NULL,
   how_created        IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | The Advisor task name that uniquely identifies an existing task. |
| new_name | VARCHAR2 | IN | The new Advisor task name. If the value is NULL or contains the value ADVISOR_UNUSED , the task will not be renamed. A task name can be up to 30 characters long. |
| description | VARCHAR2 | IN | A new task description. If the value is NULL or contains the value ADVISOR_UNUSED , the description will not be changed. Names can be up to 256 characters long. |
| read_only | VARCHAR2 | IN | Sets the task to read-only. Possible values are: TRUE and FALSE . If the value is NULL or contains the value ADVISOR_UNUSED , the setting will not be changed. |
| is_template | VARCHAR2 | IN | Marks the task as a template. Physically, there is no difference between a task and a template; however, a template cannot be executed. Possible values are: TRUE and FALSE . If the value is NULL or contains the value ADVISOR_UNUSED , the setting will not be changed. |
| how_created | VARCHAR2 | IN | Indicates a source application name that initiated the task creation. If the value is NULL or contains the value ADVISOR_UNUSED , the source will not be changed. |

## Usage Notes

Syntax DBMS_ADVISOR.UPDATE_TASK_ATTRIBUTES ( task_name IN VARCHAR2 new_name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, read_only IN VARCHAR2 := NULL, is_template IN VARCHAR2 := NULL, how_created IN VARCHAR2 := NULL); Parameters Table 16-45 UPDATE_TASK_ATTRIBUTES Procedure Parameters Parameter Description task_name The Advisor task name that uniquely identifies an existing task. new_name The new Advisor task name. If the value is NULL or contains the value ADVISOR_UNUSED , the task will not be renamed. A task name can be up to 30 characters long. description A new task description. If the value is NULL or contains the value ADVISOR_UNUSED , the description will not be changed. Names can be up to 256 characters long. read_only Sets the task to read-only. Possible values are: TRUE and FALSE . If the value is NULL or contains the value ADVISOR_UNUSED , the setting will not be changed. is_template Marks the task as a template. Physically, there is no difference between a task and a template; however, a template cannot be executed. Possible values are: TRUE and FALSE . If the value is NULL or contains the value ADVISOR_UNUSED , the setting will not be changed. how_created Indicates a source application name that initiated the task creation. If the value is NULL or contains the value ADVISOR_UNUSED , the source will not be changed. Examples DECLARE task_id NUMBER; task_name VARCHAR2(30); BEGIN task_name := 'My Task'; DBMS_ADVISOR.CREATE_TASK(DBMS_ADVISOR.SQLACCESS_ADVISOR, task_id, task_name); DBMS_ADVISOR.UPDATE_TASK_ATTRIBUTES(task_name,'New Task Name'); DBMS_ADVISOR.UPDATE_TASK_ATTRIBUTES('New Task Name',NULL,'New description'); END; /