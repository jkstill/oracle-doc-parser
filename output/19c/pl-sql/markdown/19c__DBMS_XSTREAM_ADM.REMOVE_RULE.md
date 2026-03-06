---
id: 19c__DBMS_XSTREAM_ADM.REMOVE_RULE
name: DBMS_XSTREAM_ADM.REMOVE_RULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.REMOVE_RULE

This procedure removes the specified rule or all rules from the rule set associated with the specified capture process, apply process, or propagation.

## Syntax

```sql
DBMS_XSTREAM_ADM.REMOVE_RULE(
   rule_name         IN  VARCHAR2,
   streams_type      IN  VARCHAR2,
   streams_name      IN  VARCHAR2,
   drop_unused_rule  IN  BOOLEAN  DEFAULT TRUE,
   inclusion_rule    IN  BOOLEAN  DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_name | VARCHAR2 | IN | The name of the rule to remove, specified as [ schema_name .] rule_name . If NULL , then the procedure removes all rules from the specified capture process, apply process, or propagation rule set. For example, to specify a rule in the hr schema named prop_rule1 , enter hr.prop_rule1 . If the schema is not specified, then the current user is the default. |
| streams_type | VARCHAR2 | IN | The type of XStream client: Specify capture for a capture process. Specify propagation for a propagation. Specify apply for an apply process. |
| streams_name | VARCHAR2 | IN | The name of the XStream client, which can be a capture process, propagation, or apply process. Do not specify an owner. If the specified XStream client does not exist, but there is metadata in the data dictionary that associates the rule with this client, then the procedure removes the metadata. If the specified XStream client does not exist, and there is no metadata in the data dictionary that associates the rule with this client, then the procedure raises an error. |
| drop_unused_rule | BOOLEAN | IN | If TRUE and the rule is not in any rule set, then the procedure drops the rule from the database. If TRUE and the rule exists in any rule set, then the procedure does not drop the rule from the database. If FALSE , then the procedure does not drop the rule from the database. |
| inclusion_rule | BOOLEAN | IN | If inclusion_rule is TRUE , then the procedure removes the rule from the positive rule set for the XStream client. If inclusion_rule is FALSE , then the procedure removes the rule from the negative rule set for the XStream client. |

## Usage Notes

Note: If a rule was automatically created by the system, and you want to drop the rule, then you should use this procedure to remove the rule instead of the DBMS_RULE_ADM.DROP_RULE procedure. If you use the DBMS_RULE_ADM.DROP_RULE procedure, then some metadata about the rule might remain. Note: If a rule was automatically created by the system, and you want to drop the rule, then you should use this procedure to remove the rule instead of the DBMS_RULE_ADM.DROP_RULE procedure. If you use the DBMS_RULE_ADM.DROP_RULE procedure, then some metadata about the rule might remain. Syntax DBMS_XSTREAM_ADM.REMOVE_RULE( rule_name IN VARCHAR2, streams_type IN VARCHAR2, streams_name IN VARCHAR2, drop_unused_rule IN BOOLEAN DEFAULT TRUE, inclusion_rule IN BOOLEAN DEFAULT TRUE); Parameters Table 217-27 REMOVE_RULE Procedure Parameters Parameter Description rule_name The name of the rule to remove, specified as [ schema_name .] rule_name . If NULL , then the procedure removes all rules from the specified capture process, apply process, or propagation rule set. For example, to specify a rule in the hr schema named prop_rule1 , enter hr.prop_rule1 . If the schema is not specified, then the current user is the default. streams_type The type of XStream client: Specify capture for a capture process. Specify propagation for a propagation. Specify apply for an apply process. streams_name The name of the XStream client, which can be a capture process, propagation, or apply process. Do not specify an owner. If the specified XStream client does not exist, but there is metadata in the data dictionary that associates the rule with this client, then the procedure removes the metadata. If the specified XStream client does not exist, and there is no metadata in the data dictionary that associates the rule with this client, then the procedure raises an error. drop_unused_rule If TRUE and the rule is not in any rule set, then the procedure drops the rule from the database. If TRUE and the rule exists in any rule set, then the procedure does not drop the rule from the database. If FALSE , then the procedure does not drop the rule from the database. inclusion_rule If inclusion_rule is TRUE , then the procedure removes the rule from the positive rule set for the XStream client. If inclusion_rule is FALSE , then the procedure removes the rule from the negative rule set for the XStream client.