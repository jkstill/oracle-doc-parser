---
id: 19c__DBMS_RULE_ADM.DROP_RULE
name: DBMS_RULE_ADM.DROP_RULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE_ADM
tags: [dbms_rule_adm]
source_file: DBMS_RULE_ADM.html
---

# DBMS_RULE_ADM.DROP_RULE

This procedure drops a rule.

## Syntax

```sql
DBMS_RULE_ADM.DROP_RULE(
   rule_name  IN  VARCHAR2,
   force      IN  BOOLEAN   DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_name | VARCHAR2 | IN | The name of the rule you are dropping, specified as [ schema_name .] rule_name . For example, to drop a rule named all_a in the hr schema, enter hr.all_a for this parameter. If the schema is not specified, then the current user is the default. |
| force | BOOLEAN | IN | If TRUE , then the procedure removes the rule from all rule sets that contain it. If FALSE and no rule sets contain the rule, then the procedure drops the rule. If FALSE and one or more rule sets contain the rule, then the procedure raises an exception. |

## Usage Notes

Syntax DBMS_RULE_ADM.DROP_RULE( rule_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 150-9 DROP_RULE Procedure Parameters Parameter Description rule_name The name of the rule you are dropping, specified as [ schema_name .] rule_name . For example, to drop a rule named all_a in the hr schema, enter hr.all_a for this parameter. If the schema is not specified, then the current user is the default. force If TRUE , then the procedure removes the rule from all rule sets that contain it. If FALSE and no rule sets contain the rule, then the procedure drops the rule. If FALSE and one or more rule sets contain the rule, then the procedure raises an exception. Usage Notes To run this procedure, a user must meet at least one of the following requirements: Be the owner of the rule Have DROP _ ANY _ RULE system privilege Note: To remove a rule from a rule set without dropping the rule from the database, use the REMOVE_RULE procedure. The rule evaluation context associated with the rule, if any, is not dropped when you run this procedure. Note: To remove a rule from a rule set without dropping the rule from the database, use the REMOVE_RULE procedure. The rule evaluation context associated with the rule, if any, is not dropped when you run this procedure.