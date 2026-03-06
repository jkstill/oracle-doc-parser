---
id: 19c__DBA_CPU_USAGE_STATISTICS
name: DBA_CPU_USAGE_STATISTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_CPU_USAGE_STATISTICS.html
---

# DBA_CPU_USAGE_STATISTICS

DBA_CPU_USAGE_STATISTICS displays database CPU usage statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| VERSION | VARCHAR2(17) | Database version |
| TIMESTAMP | DATE | Time at which the CPU usage changed |
| CPU_COUNT | NUMBER | CPU count of the database |
| CPU_CORE_COUNT | NUMBER | CPU core count of the database |
| CPU_SOCKET_COUNT | NUMBER | CPU socket count of the database |