---
id: 19c__DBMS_RULE_ADM.DROP_RULE_SET
name: DBMS_RULE_ADM.DROP_RULE_SET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE_ADM
tags: [dbms_rule_adm]
source_file: DBMS_RULE_ADM.html
---

# DBMS_RULE_ADM.DROP_RULE_SET

This procedure drops a rule set.

## Syntax

```sql
DBMS_RULE_ADM.DROP_RULE_SET(
   rule_set_name  IN  VARCHAR2,
   delete_rules   IN  BOOLEAN   DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_set_name | VARCHAR2 | IN | The name of the rule set you are dropping, specified as [ schema_name .] rule_set_name . For example, to drop a rule set named apply_rules in the hr schema, enter hr.apply_rules for this parameter. If the schema is not specified, then the current user is the default. |
| delete_rules | BOOLEAN | IN | If TRUE , then the procedure drops any rules that are in the rule set. If any of the rules in the rule set are also in another rule set, then these rules are not dropped. If FALSE , then the procedure does not drop the rules in the rule set. |

## Usage Notes

Syntax DBMS_RULE_ADM.DROP_RULE_SET( rule_set_name IN VARCHAR2, delete_rules IN BOOLEAN DEFAULT FALSE); Parameters Table 150-10 DROP_RULE_SET Procedure Parameters Parameter Description rule_set_name The name of the rule set you are dropping, specified as [ schema_name .] rule_set_name . For example, to drop a rule set named apply_rules in the hr schema, enter hr.apply_rules for this parameter. If the schema is not specified, then the current user is the default. delete_rules If TRUE , then the procedure drops any rules that are in the rule set. If any of the rules in the rule set are also in another rule set, then these rules are not dropped. If FALSE , then the procedure does not drop the rules in the rule set. Usage Notes To run this procedure, a user must meet at least one of the following requirements: Have DROP _ ANY _ RULE _ SET system privilege Be the owner of the rule set Note: The rule evaluation context associated with the rule set, if any, is not dropped when you run this procedure. Note: The rule evaluation context associated with the rule set, if any, is not dropped when you run this procedure.