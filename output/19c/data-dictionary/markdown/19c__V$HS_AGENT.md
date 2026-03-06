---
id: 19c__V$HS_AGENT
name: V$HS_AGENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-HS_AGENT.html
---

# V$HS_AGENT

V$HS_AGENT displays the set of HS agents currently running on a given host. There is one row per agent process.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| AGENT_ID | NUMBER |  |
| MACHINE | VARCHAR2(64) |  |
| PROCESS | VARCHAR2(9) |  |
| PROGRAM | VARCHAR2(48) |  |
| OSUSER | VARCHAR2(128) |  |
| STARTTIME | DATE |  |
| AGENT_TYPE | NUMBER |  |
| FDS_CLASS_ID | NUMBER |  |
| FDS_INST_ID | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content