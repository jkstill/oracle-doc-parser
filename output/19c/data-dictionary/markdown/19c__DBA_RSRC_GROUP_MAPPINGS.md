---
id: 19c__DBA_RSRC_GROUP_MAPPINGS
name: DBA_RSRC_GROUP_MAPPINGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_RSRC_GROUP_MAPPINGS.html
---

# DBA_RSRC_GROUP_MAPPINGS

DBA_RSRC_GROUP_MAPPINGS displays the mapping between session attributes and consumer groups in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ATTRIBUTE | VARCHAR2(128) | Session attribute to match |
| VALUE | VARCHAR2(128) | Attribute value |
| CONSUMER_GROUP | VARCHAR2(128) | Target consumer group name |
| STATUS | VARCHAR2(128) | Indicates whether the consumer group is part of the pending area ( PENDING ) or not (NULL) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content