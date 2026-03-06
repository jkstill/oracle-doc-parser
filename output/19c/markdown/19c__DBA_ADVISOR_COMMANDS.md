---
id: 19c__DBA_ADVISOR_COMMANDS
name: DBA_ADVISOR_COMMANDS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ADVISOR_COMMANDS.html
---

# DBA_ADVISOR_COMMANDS

DBA_ADVISOR_COMMANDS displays information about the commands used by all advisors in the database for specifying recommendation actions.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| COMMAND_ID | NUMBER | Identifier of the command |
| COMMAND_NAME | VARCHAR2(64) | Name of the command |

## Usage Notes

In addition to the set of commands in the COMMAND column of V$SESSION , the following additional commands are defined: RUN ADVISOR CHECK EXECUTION PLAN ALTER PARAMETER ENABLE TRACE