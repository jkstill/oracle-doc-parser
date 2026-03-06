---
id: 19c__V$CACHE
name: V$CACHE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-CACHE.html
---

# V$CACHE

V$CACHE displays information from the block header of each block in the SGA of the current instance as related to particular database objects. This is an Oracle Real Application Clusters view.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE# | NUMBER |  |
| BLOCK# | NUMBER |  |
| CLASS# | NUMBER |  |
| STATUS | VARCHAR2(10) |  |
| XNC | NUMBER |  |
| FORCED_READS | NUMBER |  |
| FORCED_WRITES | NUMBER |  |
| NAME | VARCHAR2(128) |  |
| PARTITION_NAME | VARCHAR2(128) |  |
| KIND | VARCHAR2(15) |  |
| OWNER# | NUMBER |  |
| LOCK_ELEMENT_ADDR | RAW(4 | 8) |  |
| LOCK_ELEMENT_NAME | NUMBER |  |
| CON_ID | NUMBER |  |