---
id: 19c__V$SQL_SHARD
name: V$SQL_SHARD
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_SHARD.html
---

# V$SQL_SHARD

V$SQL_SHARD displays the shard information for a shard query's previous execution. This view uniquely maps a shard SQL fragment of a cross shard query to the target shard database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SQL_ID | VARCHAR2(13) |  |
| CHILD_NUMBER | NUMBER |  |
| OPERATION_ID | NUMBER |  |
| SHARD_SQL_ID | VARCHAR2(13) |  |
| SHARD_ID | NUMBER |  |
| SHARD_CHILD_NUMBER | NUMBER |  |
| CON_ID | NUMBER |  |