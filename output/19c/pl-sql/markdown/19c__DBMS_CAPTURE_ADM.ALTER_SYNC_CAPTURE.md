---
id: 19c__DBMS_CAPTURE_ADM.ALTER_SYNC_CAPTURE
name: DBMS_CAPTURE_ADM.ALTER_SYNC_CAPTURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CAPTURE_ADM
tags: [dbms_capture_adm]
source_file: DBMS_CAPTURE_ADM.html
---

# DBMS_CAPTURE_ADM.ALTER_SYNC_CAPTURE

This procedure alters a synchronous capture.

## Syntax

```sql
DBMS_CAPTURE_ADM.ALTER_SYNC_CAPTURE(
   capture_name   IN  VARCHAR2,
   rule_set_name  IN  VARCHAR2  DEFAULT NULL,
   capture_user   IN  VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| capture_name | VARCHAR2 | IN | The name of the synchronous capture being altered. You must specify an existing synchronous capture name. Do not specify an owner. |
| rule_set_name | VARCHAR2 | IN | The name of the positive rule set for the synchronous capture. The positive rule set contains the rules that instruct the synchronous capture to capture changes. To change the rule set for the synchronous capture, specify an existing rule set in the form [ schema_name .] rule_set_name . For example, to specify a positive rule set in the strmadmin schema named sync_cap_rules , enter strmadmin.sync_cap_rules . If the schema is not specified, then the current user is the default. An error is returned if the specified rule set does not exist. If NULL , then the rule set is not changed. |
| capture_user | VARCHAR2 | IN | The user in whose security domain a synchronous capture captures changes that satisfy its rule set and runs custom rule-based transformations configured for synchronous capture rules. If NULL , then the capture user is not changed. To change the capture user, the user who invokes the ALTER_SYNC_CAPTURE procedure must be granted the DBA role. Only the SYS user can set the capture_user to SYS . If you change the capture user, then this procedure grants the new capture user enqueue privilege on the queue used by the synchronous capture and configures the user as a secure queue user of the queue. In addition, ensure that capture user has the following privileges: EXECUTE privilege on the rule sets used by the synchronous capture EXECUTE privilege on all rule-based transformation functions used in the rule set These privileges can be granted directly to the capture user, or they can be granted through roles. In addition, the capture user must be granted EXECUTE privilege on all packages, including Oracle-supplied packages, that are invoked in rule-based transformations run by the synchronous capture. These privileges must be granted directly to the capture user. They cannot be granted through roles. |

## Usage Notes

Syntax DBMS_CAPTURE_ADM.ALTER_SYNC_CAPTURE( capture_name IN VARCHAR2, rule_set_name IN VARCHAR2 DEFAULT NULL, capture_user IN VARCHAR2 DEFAULT NULL); Parameters Table 35-7 ALTER_SYNC_CAPTURE Procedure Parameters Parameter Description capture_name The name of the synchronous capture being altered. You must specify an existing synchronous capture name. Do not specify an owner. rule_set_name The name of the positive rule set for the synchronous capture. The positive rule set contains the rules that instruct the synchronous capture to capture changes. To change the rule set for the synchronous capture, specify an existing rule set in the form [ schema_name .] rule_set_name . For example, to specify a positive rule set in the strmadmin schema named sync_cap_rules , enter strmadmin.sync_cap_rules . If the schema is not specified, then the current user is the default. An error is returned if the specified rule set does not exist. If NULL , then the rule set is not changed. capture_user The user in whose security domain a synchronous capture captures changes that satisfy its rule set and runs custom rule-based transformations configured for synchronous capture rules. If NULL , then the capture user is not changed. To change the capture user, the user who invokes the ALTER_SYNC_CAPTURE procedure must be granted the DBA role. Only the SYS user can set the capture_user to SYS . If you change the capture user, then this procedure grants the new capture user enqueue privilege on the queue used by the synchronous capture and configures the user as a secure queue user of the queue. In addition, ensure that capture user has the following privileges: EXECUTE privilege on the rule sets used by the synchronous capture EXECUTE privilege on all rule-based transformation functions used in the rule set These privileges can be granted directly to the capture user, or they can be granted through roles. In addition, the capture user must be granted EXECUTE privilege on all packages, including Oracle-supplied packages, that are invoked in rule-based transformations run by the synchronous capture. These privileges must be granted directly to the capture user. They cannot be granted through roles. Usage Notes If the capture user for a synchronous capture is dropped using DROP USER . . . CASCADE , then the synchronous capture is also dropped automatically.