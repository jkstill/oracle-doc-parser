---
id: 19c__DBMS_SCHEDULER.DEFINE_METADATA_ARGUMENT
name: DBMS_SCHEDULER.DEFINE_METADATA_ARGUMENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DEFINE_METADATA_ARGUMENT

This procedure defines a special metadata argument for the program. The Scheduler can pass Scheduler metadata through this argument to your stored procedure or other executable. You cannot set values for jobs using this argument.

## Syntax

```sql
DBMS_SCHEDULER.DEFINE_METADATA_ARGUMENT (
  program_name            IN VARCHAR2,
  metadata_attribute      IN VARCHAR2,
  argument_position       IN PLS_INTEGER,
  argument_name           IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| program_name | VARCHAR2 | IN | The name of the program to be altered |
| metadata_attribute | VARCHAR2 | IN | The metadata to be passed. Valid metadata attributes are: ' job_name ', ' job_subname ', ' job_owner ', ' job_start ', ' window_start ', ' window_end ', and ' event_message '. Table 151-40 describes these attributes in detail. |
| argument_position | PLS_INTEGER | IN | The position of the argument as it is passed to the executable. The position cannot be greater than the number_of_arguments specified for the program. It must be unique, so it replaces any argument already defined at this position. |
| argument_name | VARCHAR2 | IN | The name to assign to the argument. It is optional, but must be unique for the program if it is specified. If you assign a name, the name can then be used by other package procedures. |

## Usage Notes

Syntax DBMS_SCHEDULER.DEFINE_METADATA_ARGUMENT ( program_name IN VARCHAR2, metadata_attribute IN VARCHAR2, argument_position IN PLS_INTEGER, argument_name IN VARCHAR2 DEFAULT NULL); Parameters Table 151-39 DEFINE_METADATA_ARGUMENT Procedure Parameters Parameter Description program_name The name of the program to be altered metadata_attribute The metadata to be passed. Valid metadata attributes are: ' job_name ', ' job_subname ', ' job_owner ', ' job_start ', ' window_start ', ' window_end ', and ' event_message '. Table 151-40 describes these attributes in detail. argument_position The position of the argument as it is passed to the executable. The position cannot be greater than the number_of_arguments specified for the program. It must be unique, so it replaces any argument already defined at this position. argument_name The name to assign to the argument. It is optional, but must be unique for the program if it is specified. If you assign a name, the name can then be used by other package procedures. Table 151-40 Metadata Attributes Metadata Attribute Datatype Description job_name VARCHAR2 Name of the currently running job job_subname VARCHAR2 Subname of the currently running job. The name + subname form a unique identifier for a job that is running a chain step. NULL if the job is not part of a chain. job_owner VARCHAR2 Owner of the currently running job job_scheduled_start TIMESTAMP WITH TIME ZONE When the currently running job was scheduled to start job_start TIMESTAMP WITH TIME ZONE When the currently running job started window_start TIMESTAMP WITH TIME ZONE If the job was started by a window, the time that the window opened window_end TIMESTAMP WITH TIME ZONE If the job was started by a window, the time that the window is scheduled to close event_message (See Description) For an event-based job, the message content of the event that started the job. The datatype of this attribute depends on the queue used for the event. It has the same type as the USER_DATA column of the queue table. In the case of a file arrival event, event_message is of type SYS.SCHEDULER_FILEWATCHER_RESULT . See " SCHEDULER_FILEWATCHER_RESULT Object Type " . Usage Notes Defining a program argument requires that you be the owner of the program or have ALTER privileges on that program. You can also define a program argument if you have the CREATE ANY JOB privilege. All metadata attributes except event_message can be used in PL/SQL blocks that you enter into the job_action or program_action attributes of jobs or programs, respectively. You use the attribute name as you use any other PL/SQL identifier, and the Scheduler assigns it a value.