---
id: 19c__ALL_SCHEDULER_CHAINS
name: ALL_SCHEDULER_CHAINS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SCHEDULER_CHAINS.html
---

# ALL_SCHEDULER_CHAINS

ALL_SCHEDULER_CHAINS displays information about the chains accessible to the current user (that is, those chains that the user has ALTER or EXECUTE privileges for).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the Scheduler chain |
| CHAIN_NAME | VARCHAR2(128) | Name of the Scheduler chain |
| RULE_SET_OWNER | VARCHAR2(128) | Owner of the rule set describing the dependencies |
| RULE_SET_NAME | VARCHAR2(128) | Name of the rule set describing the dependencies |
| NUMBER_OF_RULES | NUMBER | Number of rules in the chain |
| NUMBER_OF_STEPS | NUMBER | Number of defined steps in the chain |
| ENABLED | VARCHAR2(5) | Indicates whether the chain is enabled ( TRUE ) or disabled ( FALSE ) |
| EVALUATION_INTERVAL | INTERVAL DAY(3) TO SECOND(0) | Periodic interval at which to reevaluate rules for the chain |
| USER_RULE_SET | VARCHAR2(5) | Indicates whether the chain uses a user-specified rule set ( TRUE ) or not ( FALSE ) |
| COMMENTS | VARCHAR2(4000) | Comments on the chain |

## Usage Notes

Related Views DBA_SCHEDULER_CHAINS displays information about all chains in the database. USER_SCHEDULER_CHAINS displays information about the chains owned by the current user. This view does not display the OWNER column. See Also: " DBA_SCHEDULER_CHAINS " " USER_SCHEDULER_CHAINS " See Also: " DBA_SCHEDULER_CHAINS " " USER_SCHEDULER_CHAINS "