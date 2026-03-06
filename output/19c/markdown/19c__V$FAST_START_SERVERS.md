---
id: 19c__V$FAST_START_SERVERS
name: V$FAST_START_SERVERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-FAST_START_SERVERS.html
---

# V$FAST_START_SERVERS

V$FAST_START_SERVERS provides information about all the recovery slaves performing parallel transaction recovery.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| STATE | VARCHAR2(11) |  |
| UNDOBLOCKSDONE | NUMBER |  |
| PID | NUMBER |  |
| XID | RAW(8) |  |
| CON_ID | NUMBER |  |