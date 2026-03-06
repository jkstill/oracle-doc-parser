---
id: 19c__V$DISPATCHER_CONFIG
name: V$DISPATCHER_CONFIG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DISPATCHER_CONFIG.html
---

# V$DISPATCHER_CONFIG

V$DISPATCHER_CONFIG displays information about the dispatcher configurations and their attributes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CONF_INDX | NUMBER |  |
| NETWORK | VARCHAR2(1024) |  |
| DISPATCHERS | NUMBER |  |
| CONNECTIONS | NUMBER |  |
| SESSIONS | NUMBER |  |
| MULTIPLEX | VARCHAR2(4) |  |
| LISTENER | VARCHAR2(1200) |  |
| SERVICE | VARCHAR2(512) |  |
| CON_ID | NUMBER |  |