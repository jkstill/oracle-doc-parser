---
id: 19c__DBA_RSRC_CONSUMER_GROUPS
name: DBA_RSRC_CONSUMER_GROUPS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_RSRC_CONSUMER_GROUPS.html
---

# DBA_RSRC_CONSUMER_GROUPS

DBA_RSRC_CONSUMER_GROUPS displays information about all resource consumer groups in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CONSUMER_GROUP_ID | NUMBER | ID of the consumer group |
| CONSUMER_GROUP | VARCHAR2(128) | Name of the consumer group |
| CPU_METHOD | VARCHAR2(128) | CPU resource allocation method for the consumer group |
| MGMT_METHOD | VARCHAR2(128) | Resource allocation method for the consumer group |
| INTERNAL_USE | VARCHAR2(3) | Indicates whether the consumer group is for internal use only ( YES ) or not ( NO ) |
| COMMENTS | VARCHAR2(2000) | Text comment on the consumer group |
| CATEGORY | VARCHAR2(128) | Category of the consumer group |
| STATUS | VARCHAR2(128) | Indicates whether the consumer group is part of the pending area ( PENDING ) or not (NULL) |
| MANDATORY | VARCHAR2(3) | Indicates whether the consumer group is mandatory ( YES ) or not ( NO ) |