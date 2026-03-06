---
id: 19c__DBA_RSRC_MAPPING_PRIORITY
name: DBA_RSRC_MAPPING_PRIORITY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_RSRC_MAPPING_PRIORITY.html
---

# DBA_RSRC_MAPPING_PRIORITY

DBA_RSRC_MAPPING_PRIORITY displays information about all consumer group mapping attribute priorities.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ATTRIBUTE | VARCHAR2(128) | Session attribute |
| PRIORITY | NUMBER | Priority ( 1 is the highest) |
| STATUS | VARCHAR2(128) | Indicates whether the consumer group is part of the pending area ( PENDING ) or not (NULL) |