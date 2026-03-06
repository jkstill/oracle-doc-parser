---
id: 19c__ALL_STREAMS_SCHEMA_RULES
name: ALL_STREAMS_SCHEMA_RULES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_STREAMS_SCHEMA_RULES.html
---

# ALL_STREAMS_SCHEMA_RULES

ALL_STREAMS_SCHEMA_RULES displays information about several types of schema rules.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| STREAMS_NAME | VARCHAR2(128) | Name of the Replication process or propagation |
| STREAMS_TYPE | VARCHAR2(11) | Type of the Replication process or propagation: CAPTURE PROPAGATION APPLY |
| SCHEMA_NAME | VARCHAR2(128) | Schema name in the rule condition. The rule evaluates to true for a redo entry or logical change record (LCR) only if the redo entry or LCR contains this schema name. |
| RULE_TYPE | VARCHAR2(7) | Type of the rule: DML DDL |
| INCLUDE_TAGGED_LCR | VARCHAR2(3) | Indicates whether a redo entry or logical change record (LCR) with a non-NULL tag is considered for capture, propagation, or apply ( YES ) or not ( NO ) |
| SOURCE_DATABASE | VARCHAR2(128) | Source database in the rule condition. The rule evaluates to true for a redo entry or logical change record (LCR) only if the redo entry or LCR contains this source database. |
| RULE_NAME | VARCHAR2(128) | Name of the rule |
| RULE_OWNER | VARCHAR2(128) | Owner of the rule |
| RULE_CONDITION | VARCHAR2(4000) | First 4000 bytes of the system-generated rule condition evaluated by the rules engine |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content ALL_STREAMS_SCHEMA_RULES displays information about these types of schema rules: Schema rules created for the capture processes that enqueue the captured changes into queues accessible to the current user Schema rules created for the propagations that have a source queue accessible to the current user Schema rules created for the apply processes that dequeue events from queues accessible to the current user This view does not contain information about rules created using the DBMS_RULE_ADM package. Related View DBA_STREAMS_SCHEMA_RULES displays information about the schema rules created for all capture processes, propagations, and apply processes in the database. See Also: " DBA_STREAMS_SCHEMA_RULES " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_RULE_ADM package