---
id: 19c__DBMS_SCHEDULER.DEFINE_CHAIN_RULE
name: DBMS_SCHEDULER.DEFINE_CHAIN_RULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DEFINE_CHAIN_RULE

This procedure adds a new rule to an existing chain, specified as a condition-action pair. The condition is expressed using either SQL or the Scheduler chain condition syntax and indicates the prerequisites for the action to occur. The action is a result of the condition being met.

## Syntax

```sql
DBMS_SCHEDULER.DEFINE_CHAIN_RULE (
   chain_name              IN VARCHAR2,
   condition               IN VARCHAR2,
   action                  IN VARCHAR2,
   rule_name               IN VARCHAR2 DEFAULT NULL,
   comments                IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| chain_name | VARCHAR2 | IN | The name of the chain to alter |
| condition | VARCHAR2 | IN | A boolean expression which must evaluate to TRUE for the action to be performed. Every chain must have a rule that evaluates to TRUE to start the chain. For this purpose, you can use a rule that has ' TRUE ' as its condition if you are using Scheduler chain condition syntax, or ' 1=1 ' as its condition if you are using SQL syntax. Scheduler Chain Condition Syntax See " Scheduler Chain Condition Syntax " and Oracle Database Administrator’s Guide for details SQL WHERE Clause Syntax Conditions expressed with SQL must use the syntax of a SELECT statement WHERE clause. You can refer to chain step attributes by using the chain step name as a bind variable. The bind variable syntax is : step_name.attribute . ( step_name refers to a typed object.) Possible attributes are: completed , state , start_date , end_date , error_code , and duration . Possible values for the state attribute include: 'NOT_STARTED', 'SCHEDULED', 'RUNNING', 'PAUSED', 'STALLED', 'SUCCEEDED', 'FAILED' , and 'STOPPED' . If a step is in the state 'SUCCEEDED' , 'FAILED' , or 'STOPPED' , its completed attribute is set to 'TRUE' , otherwise completed is 'FALSE' . |
| action | VARCHAR2 | IN | The action to be performed when the rule evaluates to TRUE . The action must consist of at least one keyword with an optional value and an optional delay clause. Possible actions include: [ AFTER delay_interval ] START step_1 [, step_2 ...] STOP step_1 [, step_2 ...] END [{ end_value | step_name.error_code }] At the beginning of the START action, a delay clause can specify a delay interval before performing the action. delay_interval is a formatted datetime interval of the form HH:MM:SS . The END action ends the chain with an error code equal to either the supplied end_value or the error code that step_name completes with. The default error code is 0, indicating a successful chain run. |
| rule_name | VARCHAR2 | IN | The name of the rule being created. If no rule_name is given, one is generated in the form SCHED_RULE$_{N} . |
| comments | VARCHAR2 | IN | An optional comment describing the rule. This is stored in the rule object created. |

## Usage Notes

An actual rule object is created to store the rule in the schema where the chain resides. If a rule name is given, this name is used for the rule object. If an existing rule name in the schema of the chain is given, the existing rule is altered. (A schema different than the schema of the chain cannot be specified). If no rule name is given, one is generated in the form SCHED_RULE${N} . Syntax DBMS_SCHEDULER.DEFINE_CHAIN_RULE ( chain_name IN VARCHAR2, condition IN VARCHAR2, action IN VARCHAR2, rule_name IN VARCHAR2 DEFAULT NULL, comments IN VARCHAR2 DEFAULT NULL); Parameters Table 151-37 DEFINE_CHAIN_RULE Procedure Parameters Parameter Description chain_name The name of the chain to alter condition A boolean expression which must evaluate to TRUE for the action to be performed. Every chain must have a rule that evaluates to TRUE to start the chain. For this purpose, you can use a rule that has ' TRUE ' as its condition if you are using Scheduler chain condition syntax, or ' 1=1 ' as its condition if you are using SQL syntax. Scheduler Chain Condition Syntax See " Scheduler Chain Condition Syntax " and Oracle Database Administrator’s Guide for details SQL WHERE Clause Syntax Conditions expressed with SQL must use the syntax of a SELECT statement WHERE clause. You can refer to chain step attributes by using the chain step name as a bind variable. The bind variable syntax is : step_name.attribute . ( step_name refers to a typed object.) Possible attributes are: completed , state , start_date , end_date , error_code , and duration . Possible values for the state attribute include: 'NOT_STARTED', 'SCHEDULED', 'RUNNING', 'PAUSED', 'STALLED', 'SUCCEEDED', 'FAILED' , and 'STOPPED' . If a step is in the state 'SUCCEEDED' , 'FAILED' , or 'STOPPED' , its completed attribute is set to 'TRUE' , otherwise completed is 'FALSE' . action The action to be performed when the rule evaluates to TRUE . The action must consist of at least one keyword with an optional value and an optional delay clause. Possible actions include: [ AFTER delay_interval ] START step_1 [, step_2 ...] STOP step_1 [, step_2 ...] END [{ end_value | step_name.error_code }] At the beginning of the START action, a delay clause can specify a delay interval before performing the action. delay_interval is a formatted datetime interval of the form HH:MM:SS . The END action ends the chain with an error code equal to either the supplied end_value or the error code that step_name completes with. The default error code is 0, indicating a successful chain run. rule_name The name of the rule being created. If no rule_name is given, one is generated in the form SCHED_RULE$_{N} . comments An optional comment describing the rule. This is stored in the rule object created. Scheduler Chain Condition Syntax The Scheduler chain condition syntax provides an easy way to construct a condition using the states and error codes of steps in the current chain. Chain Condition Syntax The following are the available constructs for Scheduler chain condition syntax, which are all boolean expressions: TRUE FALSE stepname [NOT] SUCCEEDED stepname [NOT] FAILED stepname [NOT] STOPPED stepname [NOT] COMPLETED stepname ERROR_CODE IN ( integer, integer, integer ...) stepname ERROR_CODE NOT IN ( integer, integer, integer ...) stepname ERROR_CODE = integer stepname ERROR_CODE != integer stepname ERROR_CODE <> integer stepname ERROR_CODE > integer stepname ERROR_CODE >= integer stepname ERROR_CODE < integer stepname ERROR_CODE <= integer These boolean operators are available to create more complex conditions: expression AND expression expression OR expression NOT ( expression ) integer can be positive or negative. Parentheses may be used for clarity or to enforce ordering. You must use parentheses with the NOT operator. PL/SQL code that runs as part of a step can set the value of ERROR_CODE for that step with the RAISE_APPLICATION_ERROR statement. Usage Notes Defining a chain rule requires ALTER privileges on the chain (either as the owner, or as a user with ALTER privileges on the chain or the CREATE ANY JOB system privilege). You must define at least one rule that starts the chain and at least one that ends it. See the section "Adding Rules to a Chain" in Oracle Database Administrator's Guide for more information.