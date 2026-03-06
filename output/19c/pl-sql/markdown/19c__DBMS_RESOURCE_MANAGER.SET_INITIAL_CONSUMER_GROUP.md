---
id: 19c__DBMS_RESOURCE_MANAGER.SET_INITIAL_CONSUMER_GROUP
name: DBMS_RESOURCE_MANAGER.SET_INITIAL_CONSUMER_GROUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.SET_INITIAL_CONSUMER_GROUP

This deprecated procedure sets the initial resource consumer group for a user.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.SET_INITIAL_CONSUMER_GROUP (
   user             IN   VARCHAR2, 
   consumer_group   IN   VARCHAR2);
```

## Usage Notes

The initial consumer group of a user is the consumer group to which any session created by that user initially belongs. Note: This procedure is deprecated in Release 11gR1. While the procedure remains available in the package, Initial Consumer Group is set by the session-to-consumer group mapping rules. Note: This procedure is deprecated in Release 11gR1. While the procedure remains available in the package, Initial Consumer Group is set by the session-to-consumer group mapping rules. Syntax DBMS_RESOURCE_MANAGER.SET_INITIAL_CONSUMER_GROUP ( user IN VARCHAR2, consumer_group IN VARCHAR2); Parameters Table 142-23 SET_INITIAL_CONSUMER_GROUP Procedure Parameters Parameters Description user Name of the user consumer_group User's initial consumer group Usage Notes The ADMINISTER_RESOURCE_MANAGER or the ALTER USER system privilege are required to be able to execute this procedure. The user, or PUBLIC , must be directly granted switch privilege to a consumer group before it can be set to be the user's initial consumer group. Switch privilege for the initial consumer group cannot come from a role granted to that user. Note: These semantics are similar to those for ALTER USER DEFAULT ROLE . If the initial consumer group for a user has never been set, then the user's initial consumer group is automatically the consumer group: DEFAULT_CONSUMER_GROUP . DEFAULT_CONSUMER_GROUP has switch privileges granted to PUBLIC ; therefore, all users are automatically granted switch privilege for this consumer group. Upon deletion of a consumer group, all users having the deleted group as their initial consumer group now have DEFAULT_CONSUMER_GROUP as their initial consumer group. All currently active sessions belonging to a deleted consumer group are switched to DEFAULT_CONSUMER_GROUP .