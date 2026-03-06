---
id: 19c__V$DISPATCHER
name: V$DISPATCHER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DISPATCHER.html
---

# V$DISPATCHER

V$DISPATCHER displays information about the dispatcher processes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(4) |  |
| NETWORK | VARCHAR2(1024) |  |
| PADDR | RAW(4 | 8) |  |
| STATUS | VARCHAR2(16) |  |
| ACCEPT | VARCHAR2(3) |  |
| MESSAGES | NUMBER |  |
| BYTES | NUMBER |  |
| BREAKS | NUMBER |  |
| OWNED | NUMBER |  |
| CREATED | NUMBER |  |
| IDLE | NUMBER |  |
| BUSY | NUMBER |  |
| CPU | NUMBER |  |
| LISTENER | NUMBER |  |
| CONF_INDX | NUMBER |  |
| CON_ID | NUMBER |  |