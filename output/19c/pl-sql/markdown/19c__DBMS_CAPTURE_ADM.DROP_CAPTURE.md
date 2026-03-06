---
id: 19c__DBMS_CAPTURE_ADM.DROP_CAPTURE
name: DBMS_CAPTURE_ADM.DROP_CAPTURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CAPTURE_ADM
tags: [dbms_capture_adm]
source_file: DBMS_CAPTURE_ADM.html
---

# DBMS_CAPTURE_ADM.DROP_CAPTURE

This procedure drops a capture process.

## Syntax

```sql
DBMS_CAPTURE_ADM.DROP_CAPTURE(
   capture_name           IN  VARCHAR2,
   drop_unused_rule_sets  IN  BOOLEAN  DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| capture_name | VARCHAR2 | IN | The name of the capture process being dropped. Specify an existing capture process name. Do not specify an owner. |
| drop_unused_rule_sets | BOOLEAN | IN | If TRUE , then the procedure drops any rule sets, positive and negative, used by the specified capture process if these rule sets are not used by any other Oracle Replication client. Oracle Replication clients include capture processes, propagations, apply processes, and messaging clients. If this procedure drops a rule set, then this procedure also drops any rules in the rule set that are not in another rule set. If FALSE , then the procedure does not drop the rule sets used by the specified capture process, and the rule sets retain their rules. |

## Usage Notes

Syntax DBMS_CAPTURE_ADM.DROP_CAPTURE( capture_name IN VARCHAR2, drop_unused_rule_sets IN BOOLEAN DEFAULT FALSE); Parameters Table 35-11 DROP_CAPTURE Procedure Parameters Parameter Description capture_name The name of the capture process being dropped. Specify an existing capture process name. Do not specify an owner. drop_unused_rule_sets If TRUE , then the procedure drops any rule sets, positive and negative, used by the specified capture process if these rule sets are not used by any other Oracle Replication client. Oracle Replication clients include capture processes, propagations, apply processes, and messaging clients. If this procedure drops a rule set, then this procedure also drops any rules in the rule set that are not in another rule set. If FALSE , then the procedure does not drop the rule sets used by the specified capture process, and the rule sets retain their rules. Usage Notes The following usage notes apply to this procedure: The Capture Process Must Be Stopped Before It Is Dropped The DROP_CAPTURE Procedure and Rules-related Information The Capture Process Must Be Stopped Before It Is Dropped A capture process must be stopped before it can be dropped. See Also: STOP_CAPTURE Procedure The DROP_CAPTURE Procedure and Rules-related Information When you use this procedure to drop a capture process, rules-related information for the capture process is removed from the data dictionary views for Oracle Replication rules. Information about such a rule is removed even if the rule is not in either rule set for the capture process. The following are the data dictionary views for Oracle Replication rules: ALL_STREAMS_GLOBAL_RULES DBA_STREAMS_GLOBAL_RULES ALL_STREAMS_SCHEMA_RULES DBA_STREAMS_SCHEMA_RULES ALL_STREAMS_TABLE_RULES DBA_STREAMS_TABLE_RULES DBA_STREAMS_RULES See Also: STOP_CAPTURE Procedure