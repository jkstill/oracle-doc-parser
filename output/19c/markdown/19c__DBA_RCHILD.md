---
id: 19c__DBA_RCHILD
name: DBA_RCHILD
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_RCHILD.html
---

# DBA_RCHILD

DBA_RCHILD displays all the children in any refresh group.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REFGROUP | NUMBER | Internal identifier of the refresh group |
| OWNER | VARCHAR2(128) | Owner of the object in the refresh group |
| NAME | VARCHAR2(128) | Name of the object in the refresh group |
| TYPE# | VARCHAR2(128) | Type of the object in the refresh group |