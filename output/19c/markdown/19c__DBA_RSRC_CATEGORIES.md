---
id: 19c__DBA_RSRC_CATEGORIES
name: DBA_RSRC_CATEGORIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_RSRC_CATEGORIES.html
---

# DBA_RSRC_CATEGORIES

DBA_RSRC_CATEGORIES displays all resource consumer group categories.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(128) | Name of the consumer group category |
| COMMENTS | VARCHAR2(2000) | Text comment on the consumer group category |
| STATUS | VARCHAR2(128) | Indicates whether the consumer group category is part of the pending area ( PENDING ) or not (NULL) |
| MANDATORY | VARCHAR2(3) | Indicates whether the consumer group category is mandatory ( YES ) or not ( NO ) |