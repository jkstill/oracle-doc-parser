---
id: 19c__DBMS_APPLY_ADM.DROP_APPLY
name: DBMS_APPLY_ADM.DROP_APPLY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.DROP_APPLY

This procedure drops an apply component.

## Syntax

```sql
DBMS_APPLY_ADM.DROP_APPLY(
     apply_name             IN  VARCHAR2,
     drop_unused_rule_sets  IN  BOOLEAN  DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| apply_name | VARCHAR2 | IN | The name of the apply component being dropped. You must specify an existing apply component name. Do not specify an owner. |
| drop_unused_rule_sets | BOOLEAN | IN | If TRUE , then the procedure drops any rule sets, positive and negative, used by the specified apply component if these rule sets are not used by any other Oracle Replication or XStream component. These components include capture processes, propagations, apply processes, inbound servers, and messaging clients. If this procedure drops a rule set, then this procedure also drops any rules in the rule set that are not in another rule set. If FALSE , then the procedure does not drop the rule sets used by the specified apply component, and the rule sets retain their rules. |

## Usage Notes

Syntax DBMS_APPLY_ADM.DROP_APPLY( apply_name IN VARCHAR2, drop_unused_rule_sets IN BOOLEAN DEFAULT FALSE); Parameters Table 21-9 DROP_APPLY Procedure Parameters Parameter Description apply_name The name of the apply component being dropped. You must specify an existing apply component name. Do not specify an owner. drop_unused_rule_sets If TRUE , then the procedure drops any rule sets, positive and negative, used by the specified apply component if these rule sets are not used by any other Oracle Replication or XStream component. These components include capture processes, propagations, apply processes, inbound servers, and messaging clients. If this procedure drops a rule set, then this procedure also drops any rules in the rule set that are not in another rule set. If FALSE , then the procedure does not drop the rule sets used by the specified apply component, and the rule sets retain their rules. Usage Notes The following usage notes apply to this procedure: The DROP_APPLY Procedure and Rules The DROP_APPLY Procedure and XStream Outbound Servers The DROP_APPLY Procedure and XStream Inbound Servers The DROP_APPLY Procedure and Rules When you use this procedure to drop an apply component, information about rules created for the apply component is removed from the data dictionary views for rules. Information about such a rule is removed even if the rule is not in either the positive or negative rule set for the apply component. The following are the data dictionary views for rules: ALL_STREAMS_GLOBAL_RULES DBA_STREAMS_GLOBAL_RULES ALL_STREAMS_SCHEMA_RULES DBA_STREAMS_SCHEMA_RULES ALL_STREAMS_TABLE_RULES DBA_STREAMS_TABLE_RULES The DROP_APPLY Procedure and XStream Outbound Servers When the DROP_APPLY procedure is executed on an outbound server, it runs the DROP_OUTBOUND procedure in the DBMS_XSTREAM_ADM package. Therefore, it might also drop the outbound server's capture process and queue. The DROP_APPLY Procedure and XStream Inbound Servers When the DROP_APPLY procedure is executed on an inbound server, it runs the DROP_INBOUND procedure in the DBMS_XSTREAM_ADM package. Therefore, it might also drop the inbound server's queue.