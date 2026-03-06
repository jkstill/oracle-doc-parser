---
id: 19c__ALL_GOLDENGATE_RULES
name: ALL_GOLDENGATE_RULES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_GOLDENGATE_RULES.html
---

# ALL_GOLDENGATE_RULES

ALL_GOLDENGATE_RULES displays information about the GoldenGate rules accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| COMPONENT_NAME | VARCHAR2(128) | Name of the GoldenGate process |
| COMPONENT_TYPE | VARCHAR2(12) | Type of the GoldenGate process: CAPTURE APPLY |
| COMPONENT_RULE_TYPE | VARCHAR2(9) | For global, schema or table rules, the GoldenGate type of the rule: TABLE SCHEMA GLOBAL |
| RULE_SET_OWNER | VARCHAR2(128) | Owner of the rule set |
| RULE_SET_NAME | VARCHAR2(128) | Name of the rule set |
| RULE_SET_TYPE | CHAR(8) | Type of the rule set: POSITIVE NEGATIVE |
| RULE_OWNER | VARCHAR2(128) | Owner of the rule |
| RULE_NAME | VARCHAR2(128) | Name of the rule |
| RULE_TYPE | VARCHAR2(9) | For global, schema or table rules, the type of the rule: DML DDL |
| RULE_CONDITION | CLOB | Current rule condition |
| SCHEMA_NAME | VARCHAR2(128) | For table and schema rules, the schema name |
| OBJECT_NAME | VARCHAR2(128) | For table rules, the table name |
| INCLUDE_TAGGED_LCR | VARCHAR2(3) | For global, schema or table rules, indicates whether to include tagged LCRs ( YES ) or not ( NO ) |
| SUBSETTING_OPERATION | VARCHAR2(6) | For subset rules, the type of operation: INSERT UPDATE DELETE |
| DML_CONDITION | VARCHAR2(4000) | For subset rules, the row subsetting condition |
| SOURCE_DATABASE | VARCHAR2(128) | For global, schema or table rules, the name of the database where the LCRs originated |
| ORIGINAL_RULE_CONDITION | VARCHAR2(4000) | For rules created by GoldenGate administrative APIs, the original rule condition when the rule was created |
| SAME_RULE_CONDITION | VARCHAR2(3) | For rules created by GoldenGate administrative APIs, indicates whether the current rule condition is the same as the original rule condition ( YES ) or not ( NO ) |
| SOURCE_ROOT_NAME | VARCHAR2(128) | The global name of the source root database where the transactions originated |
| SOURCE_CONTAINER_NAME | VARCHAR2(128) | The container name of the database where the transactions originated |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_GOLDENGATE_RULES displays information about all GoldenGate server rules in the database. See Also: " DBA_GOLDENGATE_RULES " See Also: " DBA_GOLDENGATE_RULES "