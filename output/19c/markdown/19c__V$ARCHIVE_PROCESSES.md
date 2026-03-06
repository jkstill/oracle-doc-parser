---
id: 19c__V$ARCHIVE_PROCESSES
name: V$ARCHIVE_PROCESSES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-ARCHIVE_PROCESSES.html
---

# V$ARCHIVE_PROCESSES

V$ARCHIVE_PROCESSES displays the state of the various ARCH processes for the instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PROCESS | NUMBER |  |
| STATUS | VARCHAR2(10) |  |
| LOG_SEQUENCE | NUMBER |  |
| STATE | VARCHAR2(4) |  |
| ROLES | VARCHAR2(36) |  |
| CON_ID | NUMBER |  |