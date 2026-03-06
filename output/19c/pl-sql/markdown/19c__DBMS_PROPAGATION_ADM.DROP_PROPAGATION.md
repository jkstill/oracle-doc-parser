---
id: 19c__DBMS_PROPAGATION_ADM.DROP_PROPAGATION
name: DBMS_PROPAGATION_ADM.DROP_PROPAGATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PROPAGATION_ADM
tags: [dbms_propagation_adm]
source_file: DBMS_PROPAGATION_ADM.html
---

# DBMS_PROPAGATION_ADM.DROP_PROPAGATION

This procedure drops a propagation and deletes all messages for the destination queue in the source queue. This procedure also removes the schedule for propagation from the source queue to the destination queue.

## Syntax

```sql
DBMS_PROPAGATION_ADM.DROP_PROPAGATION(
   propagation_name       IN  VARCHAR2,
   drop_unused_rule_sets  IN  BOOLEAN  DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| propagation_name | VARCHAR2 | IN | The name of the propagation you are dropping. You must specify an existing propagation name. Do not specify an owner. |
| drop_unused_rule_sets | BOOLEAN | IN | If TRUE , then the procedure drops any rule sets, positive and negative, used by the specified propagation if these rule sets are not used by any other Oracle Replication client, which includes capture processes, propagations, apply processes, and messaging clients. If this procedure drops a rule set, then this procedure also drops any rules in the rule set that are not in another rule set. If FALSE , then the procedure does not drop the rule sets used by the specified propagation, and the rule sets retain their rules. |

## Usage Notes

Syntax DBMS_PROPAGATION_ADM.DROP_PROPAGATION( propagation_name IN VARCHAR2, drop_unused_rule_sets IN BOOLEAN DEFAULT FALSE); Parameters Table 134-4 DROP_PROPAGATION Procedure Parameters Parameter Description propagation_name The name of the propagation you are dropping. You must specify an existing propagation name. Do not specify an owner. drop_unused_rule_sets If TRUE , then the procedure drops any rule sets, positive and negative, used by the specified propagation if these rule sets are not used by any other Oracle Replication client, which includes capture processes, propagations, apply processes, and messaging clients. If this procedure drops a rule set, then this procedure also drops any rules in the rule set that are not in another rule set. If FALSE , then the procedure does not drop the rule sets used by the specified propagation, and the rule sets retain their rules. Usage Notes When you use this procedure to drop a propagation, information about rules created for the propagation is removed from the data dictionary views for Oracle Replication rules. Information about such a rule is removed even if the rule is not in either rule set for the propagation. The following are the data dictionary views for Oracle Replication rules: ALL_STREAMS_GLOBAL_RULES DBA_STREAMS_GLOBAL_RULES ALL_STREAMS_SCHEMA_RULES DBA_STREAMS_SCHEMA_RULES ALL_STREAMS_TABLE_RULES DBA_STREAMS_TABLE_RULES Note: When you drop a propagation, the propagation job used by the propagation is dropped automatically, if no other propagations are using the propagation job. Note: When you drop a propagation, the propagation job used by the propagation is dropped automatically, if no other propagations are using the propagation job.