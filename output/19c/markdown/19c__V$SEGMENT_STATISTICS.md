---
id: 19c__V$SEGMENT_STATISTICS
name: V$SEGMENT_STATISTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [dynamic_performance]
source_file: V-SEGMENT_STATISTICS.html
---

# V$SEGMENT_STATISTICS

V$SEGMENT_STATISTICS displays information about segment-level statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) |  |
| OBJECT_NAME | VARCHAR2(128) |  |
| SUBOBJECT_NAME | VARCHAR2(128) |  |
| TABLESPACE_NAME | VARCHAR2(30) |  |
| TS# | NUMBER |  |
| OBJ# | NUMBER |  |
| DATAOBJ# | NUMBER |  |
| OBJECT_TYPE | VARCHAR2(18) |  |
| STATISTIC_NAME | VARCHAR2(64) |  |
| STATISTIC# | NUMBER |  |
| VALUE | NUMBER |  |
| CON_ID | NUMBER |  |