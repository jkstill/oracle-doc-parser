---
id: 19c__V$HS_PARAMETER
name: V$HS_PARAMETER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dynamic_performance]
source_file: V-HS_PARAMETER.html
---

# V$HS_PARAMETER

V$HS_PARAMETER describes the initialization parameters in use by the server and agent.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| HS_SESSION_ID | NUMBER |  |
| PARAMETER | VARCHAR2(128) |  |
| VALUE | VARCHAR2(64) |  |
| SOURCE | VARCHAR2(1) |  |
| ENV | VARCHAR2(1) |  |
| CON_ID | NUMBER |  |