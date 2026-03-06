---
id: 19c__DBMS_SCHEDULER.CREATE_EVENT_SCHEDULE
name: DBMS_SCHEDULER.CREATE_EVENT_SCHEDULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.CREATE_EVENT_SCHEDULE

This procedure creates an event schedule, which is used to start a job when a particular event is raised.

## Syntax

```sql
DBMS_SCHEDULER.CREATE_EVENT_SCHEDULE (
   schedule_name           IN VARCHAR2,
   start_date              IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   event_condition         IN VARCHAR2 DEFAULT NULL,
   queue_spec              IN VARCHAR2,
   end_date                IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   comments                IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schedule_name | VARCHAR2 | IN | The name to assign to the schedule. The name must be unique in the SQL namespace. For example, a schedule cannot have the same name as a table in a schema. If no name is specified, then an error occurs. |
| start_date | TIMESTAMP | IN | This attribute specifies the date and time that this schedule becomes valid. Occurrences of the event before this date and time are ignored in the context of this schedule. |
| event_condition | VARCHAR2 | IN | This is a conditional expression based on the columns of the event source queue table. The expression must have the syntax of an Advanced Queuing rule. Accordingly, you can include user data properties in the expression, provided that the message payload is an object type, and that you prefix object attributes in the expression with tab.user_data . For more information on rules, see the DBMS_AQADM . ADD_SUBSCRIBER procedure. |
| queue_spec | VARCHAR2 | IN | This argument specifies either a file watcher name or the queue into which events that start this particular job are enqueued (the source queue ). If the source queue is a secure queue, the queue_spec argument is a string containing a pair of values of the form queue_name , agent name . For non-secure queues, only the queue name need be provided. If a fully qualified queue name is not provided, the queue is assumed to be in the job owner's schema. In the case of secure queues, the agent name provided should belong to a valid agent that is currently subscribed to the queue. |
| end_date | TIMESTAMP | IN | The date and time after which jobs do not run and windows do not open. An event schedule that has no end_date is valid forever. end_date must be after the start_date . If it is not, then an error is generated when the schedule is created. |
| comments | VARCHAR2 | IN | This attribute specifies an optional comment about the schedule. By default, this attribute is NULL . |

## Usage Notes

Syntax DBMS_SCHEDULER.CREATE_EVENT_SCHEDULE ( schedule_name IN VARCHAR2, start_date IN TIMESTAMP WITH TIME ZONE DEFAULT NULL, event_condition IN VARCHAR2 DEFAULT NULL, queue_spec IN VARCHAR2, end_date IN TIMESTAMP WITH TIME ZONE DEFAULT NULL, comments IN VARCHAR2 DEFAULT NULL); Parameters Table 151-24 CREATE_EVENT_SCHEDULE Parameters Parameter Description schedule_name The name to assign to the schedule. The name must be unique in the SQL namespace. For example, a schedule cannot have the same name as a table in a schema. If no name is specified, then an error occurs. start_date This attribute specifies the date and time that this schedule becomes valid. Occurrences of the event before this date and time are ignored in the context of this schedule. event_condition This is a conditional expression based on the columns of the event source queue table. The expression must have the syntax of an Advanced Queuing rule. Accordingly, you can include user data properties in the expression, provided that the message payload is an object type, and that you prefix object attributes in the expression with tab.user_data . For more information on rules, see the DBMS_AQADM . ADD_SUBSCRIBER procedure. queue_spec This argument specifies either a file watcher name or the queue into which events that start this particular job are enqueued (the source queue ). If the source queue is a secure queue, the queue_spec argument is a string containing a pair of values of the form queue_name , agent name . For non-secure queues, only the queue name need be provided. If a fully qualified queue name is not provided, the queue is assumed to be in the job owner's schema. In the case of secure queues, the agent name provided should belong to a valid agent that is currently subscribed to the queue. end_date The date and time after which jobs do not run and windows do not open. An event schedule that has no end_date is valid forever. end_date must be after the start_date . If it is not, then an error is generated when the schedule is created. comments This attribute specifies an optional comment about the schedule. By default, this attribute is NULL . Usage Notes You must have the CREATE JOB privilege to create a schedule in your own schema or the CREATE ANY JOB privilege to create a schedule in someone else's schema by specifying schema.schedule_name . Once a schedule has been created, it can be used by other users. The schedule is created with access to PUBLIC . Therefore, there is no need to explicitly grant access to the schedule. See Also: " CREATE_FILE_WATCHER Procedure " See Also: " CREATE_FILE_WATCHER Procedure "