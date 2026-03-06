---
id: 19c__DBMS_SCHEDULER.ADD_GROUP_
name: DBMS_SCHEDULER.ADD_GROUP_
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.ADD_GROUP_

This procedure adds one or more members to an existing group.

## Syntax

```sql
DBMS_SCHEDULER.ADD_GROUP_MEMBER (
   group_name              IN VARCHAR2,
   member                  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| group_name | VARCHAR2 | IN | The name of the group. |
| member | VARCHAR2) | IN | A comma-separated list of members to add to the group. Members must match the group type. A group of the same type can be a member. The Scheduler immediately expands the included group name into its list of members. An error is returned if any of the members do not exist. A member that is already in the group is skipped, and no error is generated. The keyword LOCAL can be included as a member for database destination or external destination groups. See the " CREATE_GROUP Procedure " for information about this keyword. |

## Usage Notes

Syntax DBMS_SCHEDULER.ADD_GROUP_MEMBER ( group_name IN VARCHAR2, member IN VARCHAR2); Parameters Table 151-13 ADD_GROUP_MEMBER Procedure Parameters Parameter Description group_name The name of the group. member A comma-separated list of members to add to the group. Members must match the group type. A group of the same type can be a member. The Scheduler immediately expands the included group name into its list of members. An error is returned if any of the members do not exist. A member that is already in the group is skipped, and no error is generated. The keyword LOCAL can be included as a member for database destination or external destination groups. See the " CREATE_GROUP Procedure " for information about this keyword. Usage Notes The following users may add members to a group: The group owner A user that has been granted the ALTER object privilege on the group A user with the CREATE ANY JOB system privilege You must have the MANAGE SCHEDULER privilege to add a member to a group of type WINDOW . See Also: " CREATE_GROUP Procedure " See Also: " CREATE_GROUP Procedure "