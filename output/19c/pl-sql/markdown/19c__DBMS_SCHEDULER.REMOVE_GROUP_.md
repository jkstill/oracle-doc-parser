---
id: 19c__DBMS_SCHEDULER.REMOVE_GROUP_
name: DBMS_SCHEDULER.REMOVE_GROUP_
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.REMOVE_GROUP_

This procedure removes one or more members from an existing group.

## Syntax

```sql
DBMS_SCHEDULER.REMOVE_GROUP_MEMBER (
   group_name              IN VARCHAR2,
   member                  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| group_name | VARCHAR2 | IN | The name of the group. |
| member_name |  |  | The name of the member to remove from group. Comma-separated list of members to remove. An error is returned if any of the members is not part of the group. A group of the same type can be named as a member. The Scheduler immediately expands the included group name into its list of members. If the member is a destination, any job instances that run on this destination are removed from the *_SCHEDULER_JOB_DESTS views. |

## Usage Notes

Syntax DBMS_SCHEDULER.REMOVE_GROUP_MEMBER ( group_name IN VARCHAR2, member IN VARCHAR2); Parameters Table 151-75 REMOVE_GROUP_MEMBER Procedure Parameters Parameter Description group_name The name of the group. member_name The name of the member to remove from group. Comma-separated list of members to remove. An error is returned if any of the members is not part of the group. A group of the same type can be named as a member. The Scheduler immediately expands the included group name into its list of members. If the member is a destination, any job instances that run on this destination are removed from the *_SCHEDULER_JOB_DESTS views. Usage Notes The following users may remove members from a group: The group owner A user that has been granted the ALTER object privilege on the group A user with the CREATE ANY JOB system privilege You must have the MANAGE SCHEDULER privilege to remove a member from a group of type WINDOW . See Also: " CREATE_GROUP Procedure " See Also: " CREATE_GROUP Procedure "