---
id: 19c__V$FS_FAILOVER_OBSERVERS
name: V$FS_FAILOVER_OBSERVERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-FS_FAILOVER_OBSERVERS.html
---

# V$FS_FAILOVER_OBSERVERS

V$FS_FAILOVER_OBSERVERS provides information about fast-start failover observers.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(513) |  |
| REGISTERED | VARCHAR2(4) |  |
| HOST | VARCHAR2(513) |  |
| ISMASTER | VARCHAR2(4) |  |
| TIME_SELECTED | TIMESTAMP(9) |  |
| PINGING_PRIMARY | VARCHAR2(4) |  |
| PINGING_TARGET | VARCHAR2(4) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content If you are querying on the primary database, this view returns three rows, each describing one observer. However, only a row having an non-empty value in column NAME corresponds to a started observer. If you are querying on a non-primary database, the behavior of this view is not defined.