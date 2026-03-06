---
id: 19c__DBMS_SCHEDULER.CREATE_GROUP
name: DBMS_SCHEDULER.CREATE_GROUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.CREATE_GROUP

This procedure creates a group. Groups contain members, which you can specify when you create the group or at a later time. There are three types of groups: window groups, database destination groups, and external destination groups.

## Syntax

```sql
DBMS_SCHEDULER.CREATE_GROUP (
   group_name           IN VARCHAR2,
   group_type           IN VARCHAR2,
   member               IN VARCHAR2 DEFAULT NULL,
   comments             IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| group_name | VARCHAR2 | IN | The name to assign to the group. It can optionally be prefixed with a schema name. It cannot be NULL . It is converted to uppercase unless enclosed in double quotation marks. |
| group_type | VARCHAR2 | IN | The type of members in the group. All members must be of the same type. Possible types are: ' DB_DEST ' Database destination: Members are database destinations, for running remote database jobs. ' EXTERNAL_DEST External destination: Members are external destinations, for running remote external jobs. ' WINDOW ' Members are Scheduler windows. You must have the MANAGE SCHEDULER privilege to create a group of this type. Members in database destination and external destination groups have the following format: [[ schema .] credential @][ schema .] destination where: credential is the name of an existing credential. destination is the name of an existing database destination or external destination. The credential portion of a destination member is optional. If omitted, the job using this destination member uses its default credential. Members in window groups are window names. Because all Scheduler windows reside in the SYS schema, you do not specify a schema name for windows. |
| member | VARCHAR2 | IN | Optional comma-separated list of group members. The default is NULL . If NULL , use the ADD_GROUP_MEMBER procedure to add members. You can also use ADD_GROUP_MEMBER to add additional members at a later time. The keyword LOCAL can be used as a member in database destination groups and external destination groups. In database destination groups, LOCAL represents the source database on which the job is created. It cannot be preceded with a credential. In external destination groups, LOCAL represents the host on which the source database resides. It can be optionally preceded with a credential name. If no credential is provided, jobs that use this group as their destination must have a default credential. |
| comments | VARCHAR2 | IN | A text string that describes the group. Scheduler does not use this argument. |

## Usage Notes

You can use a group name in other DBMS_SCHEDULER package procedures to specify a list of objects. For example, to specify multiple destinations for a remote database job, you provide a group name for the DESTINATION_NAME parameter of the job. Syntax DBMS_SCHEDULER.CREATE_GROUP ( group_name IN VARCHAR2, group_type IN VARCHAR2, member IN VARCHAR2 DEFAULT NULL, comments IN VARCHAR2 DEFAULT NULL); Parameters Table 151-26 CREATE_GROUP Procedure Parameters Parameter Description group_name The name to assign to the group. It can optionally be prefixed with a schema name. It cannot be NULL . It is converted to uppercase unless enclosed in double quotation marks. group_type The type of members in the group. All members must be of the same type. Possible types are: ' DB_DEST ' Database destination: Members are database destinations, for running remote database jobs. ' EXTERNAL_DEST External destination: Members are external destinations, for running remote external jobs. ' WINDOW ' Members are Scheduler windows. You must have the MANAGE SCHEDULER privilege to create a group of this type. Members in database destination and external destination groups have the following format: [[ schema .] credential @][ schema .] destination where: credential is the name of an existing credential. destination is the name of an existing database destination or external destination. The credential portion of a destination member is optional. If omitted, the job using this destination member uses its default credential. Members in window groups are window names. Because all Scheduler windows reside in the SYS schema, you do not specify a schema name for windows. member Optional comma-separated list of group members. The default is NULL . If NULL , use the ADD_GROUP_MEMBER procedure to add members. You can also use ADD_GROUP_MEMBER to add additional members at a later time. The keyword LOCAL can be used as a member in database destination groups and external destination groups. In database destination groups, LOCAL represents the source database on which the job is created. It cannot be preceded with a credential. In external destination groups, LOCAL represents the host on which the source database resides. It can be optionally preceded with a credential name. If no credential is provided, jobs that use this group as their destination must have a default credential. comments A text string that describes the group. Scheduler does not use this argument. Usage Notes Groups reside in a particular schema and can be created by any user with the CREATE JOB system privilege. To create a group in a schema other than your own, you must have the CREATE ANY JOB privilege. The group name must be unique among all Scheduler objects. You can grant the SELECT or READ privilege on a group so that other users can reference the group when creating jobs or schedules. To enable other users to modify a group, you can grant the ALTER privilege on the group. Each group member must be unique within the group. For destination groups, the credential/destination name pairs must be unique within the group. An error is generated if any of the group members do not exist. For destination groups, both the credential and destination portions of a member must exist. Another group of the same type can be a group member. The Scheduler immediately expands the included group name into its list of members. Groups are created enabled, but you can disable them. Example The following PL/SQL block creates a group named production_dest1 , whose members are database destinations for a collection of production databases. BEGIN DBMS_SCHEDULER.CREATE_GROUP( GROUP_NAME => 'production_dest1', GROUP_TYPE => 'DB_DEST', MEMBER => 'LOCAL, oracle_cred@prodhost1, prodhost2', COMMENTS => 'All sector1 production machines'); END;