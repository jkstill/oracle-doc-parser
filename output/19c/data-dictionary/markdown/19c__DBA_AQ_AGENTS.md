---
id: 19c__DBA_AQ_AGENTS
name: DBA_AQ_AGENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_AQ_AGENTS.html
---

# DBA_AQ_AGENTS

DBA_AQ_AGENTS displays information about all registered AQ agents in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| AGENT_NAME | VARCHAR2(128) | Name of the AQ agent |
| HTTP_ENABLED | VARCHAR2(4) | Indicates whether the agent is allowed to access AQ through HTTP ( YES ) or not ( NO ) |
| SMTP_ENABLED | VARCHAR2(4) | Indicates whether the agent is allowed to access AQ through SMTP ( YES ) or not ( NO ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content