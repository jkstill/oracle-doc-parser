---
id: 19c__DBMS_CAPTURE_ADM.CREATE_SYNC_CAPTURE
name: DBMS_CAPTURE_ADM.CREATE_SYNC_CAPTURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CAPTURE_ADM
tags: [dbms_capture_adm]
source_file: DBMS_CAPTURE_ADM.html
---

# DBMS_CAPTURE_ADM.CREATE_SYNC_CAPTURE

This procedure creates a synchronous capture.

## Syntax

```sql
DBMS_CAPTURE_ADM.CREATE_SYNC_CAPTURE(
   queue_name     IN  VARCHAR2,
   capture_name   IN  VARCHAR2,
   rule_set_name  IN  VARCHAR2,
   capture_user   IN  VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | The name of the queue into which the synchronous capture enqueues changes. You must specify an existing queue in the form [ schema_name .] queue_name . For example, to specify a queue in the strmadmin schema named streams_queue , enter strmadmin.streams_queue . If the schema is not specified, then the current user is the default. Note: The queue_name setting cannot be altered after the synchronous capture is created. |
| capture_name | VARCHAR2 | IN | The name of the synchronous capture being created. A NULL specification is not allowed. Do not specify an owner. Note: The capture_name setting cannot be altered after the synchronous capture is created. |
| rule_set_name | VARCHAR2 | IN | The name of the positive rule set for the synchronous capture. The positive rule set contains the rules that instruct the synchronous capture to capture changes. Specify an existing rule set in the form [ schema_name .] rule_set_name . For example, to specify a positive rule set in the strmadmin schema named sync_cap_rules , enter strmadmin.sync_cap_rules . If the schema is not specified, then the current user is the default. An error is returned if the specified rule set does not exist. If NULL , then an error is returned. |
| capture_user | VARCHAR2 | IN | The user in whose security domain the synchronous capture captures changes that satisfy its rule set and runs custom rule-based transformations configured for synchronous capture rules. If NULL , then the user who runs the CREATE_SYNC_CAPTURE procedure is used. Only a user who is granted the DBA role can set a capture user. Only the SYS user can set the capture_user to SYS . Note: If the capture user for a synchronous capture is dropped using DROP USER . . . CASCADE , then the synchronous capture is also dropped automatically. See Also: " Usage Notes " for more information about this parameter. |

## Usage Notes

Syntax DBMS_CAPTURE_ADM.CREATE_SYNC_CAPTURE( queue_name IN VARCHAR2, capture_name IN VARCHAR2, rule_set_name IN VARCHAR2, capture_user IN VARCHAR2 DEFAULT NULL); Parameters Table 35-10 CREATE_SYNC_CAPTURE Procedure Parameters Parameter Description queue_name The name of the queue into which the synchronous capture enqueues changes. You must specify an existing queue in the form [ schema_name .] queue_name . For example, to specify a queue in the strmadmin schema named streams_queue , enter strmadmin.streams_queue . If the schema is not specified, then the current user is the default. Note: The queue_name setting cannot be altered after the synchronous capture is created. capture_name The name of the synchronous capture being created. A NULL specification is not allowed. Do not specify an owner. Note: The capture_name setting cannot be altered after the synchronous capture is created. rule_set_name The name of the positive rule set for the synchronous capture. The positive rule set contains the rules that instruct the synchronous capture to capture changes. Specify an existing rule set in the form [ schema_name .] rule_set_name . For example, to specify a positive rule set in the strmadmin schema named sync_cap_rules , enter strmadmin.sync_cap_rules . If the schema is not specified, then the current user is the default. An error is returned if the specified rule set does not exist. If NULL , then an error is returned. capture_user The user in whose security domain the synchronous capture captures changes that satisfy its rule set and runs custom rule-based transformations configured for synchronous capture rules. If NULL , then the user who runs the CREATE_SYNC_CAPTURE procedure is used. Only a user who is granted the DBA role can set a capture user. Only the SYS user can set the capture_user to SYS . Note: If the capture user for a synchronous capture is dropped using DROP USER . . . CASCADE , then the synchronous capture is also dropped automatically. See Also: " Usage Notes " for more information about this parameter. Usage Notes When the CREATE_SYNC_CAPTURE procedure creates a synchronous capture, the procedure must obtain an exclusive lock on each table for which it will capture changes. The rules in the specified rule set for the synchronous capture determine these tables. If there are outstanding transactions on a table for which the synchronous capture will capture changes, then the procedure waits until it can obtain a lock. The capture_user parameter specifies the user who captures changes that satisfy the synchronous capture rule set. This user must have the necessary privileges to capture changes. In addition, ensure that the capture user has the following privileges: ENQUEUE privilege on the queue specified in the queue_name parameter EXECUTE privilege on the rule set used by the synchronous capture EXECUTE privilege on all rule-based transformation functions used in the rule set These privileges can be granted directly to the capture user, or they can be granted through roles. In addition, the capture user must be granted EXECUTE privilege on all packages, including Oracle-supplied packages, that are invoked in rule-based transformations run by the synchronous capture. These privileges must be granted directly to the capture user. These privileges cannot be granted through roles. Note: A capture user does not require privileges on a database object to capture changes to the database object. The synchronous capture can pass these changes to a rule-based transformation function. Therefore, ensure that you consider security implications when you configure a synchronous capture. Note: A capture user does not require privileges on a database object to capture changes to the database object. The synchronous capture can pass these changes to a rule-based transformation function. Therefore, ensure that you consider security implications when you configure a synchronous capture.