---
id: 19c__V$PX_SESSION
name: V$PX_SESSION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-PX_SESSION.html
---

# V$PX_SESSION

V$PX_SESSION contains information about the sessions running parallel execution.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SADDR | RAW(4 | 8) |  |
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| QCSID | NUMBER |  |
| QCSERIAL# | NUMBER |  |
| QCINST_ID | NUMBER |  |
| SERVER_GROUP | NUMBER |  |
| SERVER_SET | NUMBER |  |
| SERVER# | NUMBER |  |
| DEGREE | NUMBER |  |
| REQ_DEGREE | NUMBER |  |
| CON_ID | NUMBER |  |