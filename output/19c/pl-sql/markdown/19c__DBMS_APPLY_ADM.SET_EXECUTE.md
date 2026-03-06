---
id: 19c__DBMS_APPLY_ADM.SET_EXECUTE
name: DBMS_APPLY_ADM.SET_EXECUTE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.SET_EXECUTE

This procedure specifies whether a message that satisfies the specified rule is executed by an apply component.

## Syntax

```sql
DBMS_APPLY_ADM.SET_EXECUTE(
  rule_name  IN  VARCHAR2,
  execute    IN  BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_name | VARCHAR2 | IN | The name of the rule, specified as [ schema_name .] rule_name . For example, to specify a rule named hr5 in the hr schema, enter hr.hr5 for this parameter. If the schema is not specified, then the current user is the default. |
| execute | BOOLEAN) | IN | If TRUE , then the procedure removes the name-value pair with the name APPLY$_EXECUTE for the specified rule. Removing the name-value pair means that the apply component executes messages that satisfy the rule. If no name-value pair with name APPLY$_EXECUTE exists for the rule, then no action is taken. If FALSE , then the procedure adds a name-value pair to the rule's action context. The name is APPLY$_EXECUTE and the value is NO . An apply component does not execute a message that satisfies the rule and does not send the message to any apply handler. If a name-value pair exists for the rule with the name APPLY$_EXECUTE , then it is removed, and a new one with the value NO is added. If NULL , then the procedure raises an error. |

## Usage Notes

This procedure modifies the specified rule's action context to specify message execution. A rule action context is optional information associated with a rule that is interpreted by the client of the rules engine after the rule evaluates to TRUE for a message. In this case, the client of the rules engine is an apply component. The information in an action context is an object of type SYS.RE$NV_LIST , which consists of a list of name-value pairs. A message execution directive specified by this procedure always consists of the following name-value pair in an action context: The name is APPLY$_EXECUTE . The value is an ANYDATA instance that contains NO as a VARCHAR2 . When the value is NO , an apply component does not execute the message and does not send the message to any apply handler. Syntax DBMS_APPLY_ADM.SET_EXECUTE( rule_name IN VARCHAR2, execute IN BOOLEAN); Parameters Table 21-19 SET_EXECUTE Procedure Parameters Parameter Description rule_name The name of the rule, specified as [ schema_name .] rule_name . For example, to specify a rule named hr5 in the hr schema, enter hr.hr5 for this parameter. If the schema is not specified, then the current user is the default. execute If TRUE , then the procedure removes the name-value pair with the name APPLY$_EXECUTE for the specified rule. Removing the name-value pair means that the apply component executes messages that satisfy the rule. If no name-value pair with name APPLY$_EXECUTE exists for the rule, then no action is taken. If FALSE , then the procedure adds a name-value pair to the rule's action context. The name is APPLY$_EXECUTE and the value is NO . An apply component does not execute a message that satisfies the rule and does not send the message to any apply handler. If a name-value pair exists for the rule with the name APPLY$_EXECUTE , then it is removed, and a new one with the value NO is added. If NULL , then the procedure raises an error. Usage Notes The following usage notes apply to this procedure: Considerations for the SET_EXECUTE Procedure The SET_EXECUTE Procedure and XStream Outbound Servers The SET_EXECUTE Procedure and XStream Inbound Servers Considerations for the SET_EXECUTE Procedure The following are considerations for using this procedure: If the message is a logical change record (LCR) and the message is not executed, then the change encapsulated in the LCR is not made to the relevant local database object. Also, if the message is not executed, then it is not sent to any apply handler. Oracle Replication capture processes, propagations, and messaging clients ignore the action context created by this procedure. The specified rule must be in the positive rule set for an apply component for the apply component to follow the execution directive. If the rule is in the negative rule set for an apply component, then the apply component ignores the execution directive for the rule. The SET_EXECUTE Procedure and XStream Outbound Servers This procedure has no effect on XStream outbound servers. The SET_EXECUTE Procedure and XStream Inbound Servers This procedure functions the same way for apply processes and inbound servers.