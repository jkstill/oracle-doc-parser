---
id: 19c__V$CIRCUIT
name: V$CIRCUIT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-CIRCUIT.html
---

# V$CIRCUIT

V$CIRCUIT contains information about virtual circuits, which are user connections to the database through dispatchers and servers.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CIRCUIT | RAW(4 | 8) |  |
| DISPATCHER | RAW(4 | 8) |  |
| SERVER | RAW(4 | 8) |  |
| WAITER | RAW(4 | 8) |  |
| SADDR | RAW(4 | 8) |  |
| STATUS | VARCHAR2(16) |  |
| QUEUE | VARCHAR2(16) |  |
| MESSAGE0 | NUMBER |  |
| MESSAGE1 | NUMBER |  |
| MESSAGE2 | NUMBER |  |
| MESSAGE3 | NUMBER |  |
| MESSAGES | NUMBER |  |
| BYTES | NUMBER |  |
| BREAKS | NUMBER |  |
| PRESENTATION | VARCHAR2(257) |  |
| PCIRCUIT | RAW(4 | 8) |  |
| BOUND_TIME Foot 1 | NUMBER |  |
| BOUND_REASON Foot 1 | VARCHAR2(32) |  |
| CON_ID | NUMBER |  |