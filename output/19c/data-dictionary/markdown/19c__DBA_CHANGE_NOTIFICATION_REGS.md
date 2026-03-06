---
id: 19c__DBA_CHANGE_NOTIFICATION_REGS
name: DBA_CHANGE_NOTIFICATION_REGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_CHANGE_NOTIFICATION_REGS.html
---

# DBA_CHANGE_NOTIFICATION_REGS

DBA_CHANGE_NOTIFICATION_REGS describes all change notification registrations in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USERNAME | VARCHAR2(31) | For invoker's rights units, the user creating the registration For definer's rights units, the owner of the registration |
| REGID | NUMBER | Internal registration ID |
| REGFLAGS | NUMBER | Registration flags |
| CALLBACK | VARCHAR2(256) | Notification callback |
| OPERATIONS_FILTER | NUMBER | Operations filter (if specified) |
| CHANGELAG | NUMBER | Transaction lag between notifications (if specified) |
| TIMEOUT | NUMBER | Registration timeout (if specified) |
| TABLE_NAME | VARCHAR2(63) | Name of the registered table |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_CHANGE_NOTIFICATION_REGS describes the change notification registrations owned by the current user. This view does not display the USERNAME column. See Also: " USER_CHANGE_NOTIFICATION_REGS " See Also: " USER_CHANGE_NOTIFICATION_REGS "