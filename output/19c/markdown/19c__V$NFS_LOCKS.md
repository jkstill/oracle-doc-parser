---
id: 19c__V$NFS_LOCKS
name: V$NFS_LOCKS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-NFS_LOCKS.html
---

# V$NFS_LOCKS

V$NFS_LOCKS displays information about byte range locks held on different files by NFS clients.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OPENSTATEID | RAW(16) |  |
| OPENSEQUENCEID | NUMBER |  |
| LOCKSTATEID | RAW(16) |  |
| LOCKSEQUENCEID | NUMBER |  |
| LOCKOWNER | VARCHAR2(2000) |  |
| OFFSET | NUMBER |  |
| LENGTH | NUMBER |  |
| LOCKTYPE | VARCHAR2(20) |  |
| CON_ID | NUMBER |  |