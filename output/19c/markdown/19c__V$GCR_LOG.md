---
id: 19c__V$GCR_LOG
name: V$GCR_LOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-GCR_LOG.html
---

# V$GCR_LOG

V$GCR_LOG provides information on the last 30 significant events that have occurred in GCR in the recent past.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INST_ID | NUMBER |  |
| ITERATION | NUMBER |  |
| TIME | TIMESTAMP(6) |  |
| TYPE | VARCHAR2(14) |  |
| DESCRIPTION | VARCHAR2(40) |  |
| RESULT | VARCHAR2(7) |  |
| CON_ID | NUMBER |  |