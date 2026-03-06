---
id: 19c__DBA_LOGSTDBY_SKIP_TRANSACTION
name: DBA_LOGSTDBY_SKIP_TRANSACTION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_LOGSTDBY_SKIP_TRANSACTION.html
---

# DBA_LOGSTDBY_SKIP_TRANSACTION

DBA_LOGSTDBY_SKIP_TRANSACTION displays the skip settings chosen. This view is for logical standby databases only.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| XIDUSN | NUMBER | Transaction ID undo segment number |
| XIDSLT | NUMBER | Transaction ID slot number |
| XIDSQN | NUMBER | Transaction ID sequence number |
| CON_NAME | VARCHAR2(384) | Container name |