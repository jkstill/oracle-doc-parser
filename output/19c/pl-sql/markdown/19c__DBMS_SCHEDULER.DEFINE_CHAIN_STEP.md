---
id: 19c__DBMS_SCHEDULER.DEFINE_CHAIN_STEP
name: DBMS_SCHEDULER.DEFINE_CHAIN_STEP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DEFINE_CHAIN_STEP

This procedure adds or replaces a chain step and associates it with a program or a nested chain. When the chain step is started, the specified program or chain is run. If a step already exists with the name supplied in the chain_name argument, the new step replaces the old one.

## Syntax

```sql
DBMS_SCHEDULER.DEFINE_CHAIN_STEP (
   chain_name              IN VARCHAR2,
   step_name               IN VARCHAR2,
   program_name            IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| chain_name | VARCHAR2 | IN | The name of the chain to alter. |
| step_name | VARCHAR2 | IN | The name of the step being defined. If a step already exists with this name, the new step replaces the old one. |
| program_name | VARCHAR2) | IN | The name of a program or chain to run during this step. The chain owner must have EXECUTE privileges on this program or chain. |

## Usage Notes

The chain owner must have EXECUTE privileges on the program or chain associated with the step. Only one program or chain can run during a step. You cannot set all possible step attributes with this procedure. Use the ALTER_CHAIN procedure to set additional chain step attributes, such as credential_name and destination_name . Syntax DBMS_SCHEDULER.DEFINE_CHAIN_STEP ( chain_name IN VARCHAR2, step_name IN VARCHAR2, program_name IN VARCHAR2); Parameters Table 151-38 DEFINE_CHAIN_STEP Procedure Parameters Parameter Description chain_name The name of the chain to alter. step_name The name of the step being defined. If a step already exists with this name, the new step replaces the old one. program_name The name of a program or chain to run during this step. The chain owner must have EXECUTE privileges on this program or chain. Usage Notes Defining a chain step requires ALTER privileges on the chain (either as the owner, or a user with ALTER privileges on the chain or the CREATE ANY JOB system privilege). See Also: " ALTER_CHAIN Procedure " " DEFINE_CHAIN_EVENT_STEP Procedure " See Also: " ALTER_CHAIN Procedure " " DEFINE_CHAIN_EVENT_STEP Procedure "