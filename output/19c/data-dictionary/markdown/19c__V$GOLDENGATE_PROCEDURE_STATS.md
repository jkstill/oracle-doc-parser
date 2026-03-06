---
id: 19c__V$GOLDENGATE_PROCEDURE_STATS
name: V$GOLDENGATE_PROCEDURE_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-GOLDENGATE_PROCEDURE_STATS.html
---

# V$GOLDENGATE_PROCEDURE_STATS

V$GOLDENGATE_PROCEDURE_STATS displays procedural replication statistics processed by each Oracle GoldenGate apply server.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| APPLY_NAME | VARCHAR2(128) |  |
| SERVER_ID | NUMBER |  |
| PROCEDURE_OWNER | VARCHAR2(128) |  |
| PACKAGE_NAME | VARCHAR2(128) |  |
| PROCEDURE_NAME | VARCHAR2(128) |  |
| LAST_UPDATE | DATE |  |
| TOTAL_EXECUTIONS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content