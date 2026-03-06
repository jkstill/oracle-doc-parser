---
id: 19c__V$DB_PIPES
name: V$DB_PIPES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DB_PIPES.html
---

# V$DB_PIPES

V$DB_PIPES displays the pipes that are currently represented in the shared pool for this instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNERID | NUMBER |  |
| NAME | VARCHAR2(1000) |  |
| TYPE | VARCHAR2(7) |  |
| PIPE_SIZE | NUMBER |  |
| CON_ID | NUMBER |  |
| CON_NAME | VARCHAR2(64) |  |