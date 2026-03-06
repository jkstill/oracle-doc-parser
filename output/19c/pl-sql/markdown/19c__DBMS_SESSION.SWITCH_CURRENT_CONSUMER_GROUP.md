---
id: 19c__DBMS_SESSION.SWITCH_CURRENT_CONSUMER_GROUP
name: DBMS_SESSION.SWITCH_CURRENT_CONSUMER_GROUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.SWITCH_CURRENT_CONSUMER_GROUP

This procedure changes the current resource consumer group of a user's current session.

## Syntax

```sql
DBMS_SESSION.switch_current_consumer_group (
   new_consumer_group     IN  VARCHAR2, 
   old_consumer_group     OUT VARCHAR2, 
   initial_group_on_error IN  BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| new_consumer_group | VARCHAR2 | IN | Name of consumer group to which you want to switch |
| old_consumer_group | VARCHAR2 | OUT | Name of the consumer group from which you just switched out |
| initial_group_on_error | BOOLEAN) | IN | If TRUE , then sets the current consumer group of the caller to his/her initial consumer group in the event of an error |

## Usage Notes

This lets you switch to a consumer group if you have the switch privilege for that particular group. If the caller is another procedure, then this enables the user to switch to a consumer group for which the owner of that procedure has switch privilege. Syntax DBMS_SESSION.switch_current_consumer_group ( new_consumer_group IN VARCHAR2, old_consumer_group OUT VARCHAR2, initial_group_on_error IN BOOLEAN); Parameters Table 154-25 SWITCH_CURRENT_CONSUMER_GROUP Procedure Parameters Parameter Description new_consumer_group Name of consumer group to which you want to switch old_consumer_group Name of the consumer group from which you just switched out initial_group_on_error If TRUE , then sets the current consumer group of the caller to his/her initial consumer group in the event of an error Return Values This procedure outputs the old consumer group of the user in the parameter old_consumer_group . Note: The old_consumer_group parameter returns the name of old consumer group only if it were set explicitly. That is, you might get NULL if the old consumer group was set by some mapping rules. You can switch back to the old consumer group later using the value returned in old_consumer_group . Note: The old_consumer_group parameter returns the name of old consumer group only if it were set explicitly. That is, you might get NULL if the old consumer group was set by some mapping rules. You can switch back to the old consumer group later using the value returned in old_consumer_group .