---
id: 19c__V$DNFS_SERVERS
name: V$DNFS_SERVERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DNFS_SERVERS.html
---

# V$DNFS_SERVERS

V$DNFS_SERVERS displays information about the Direct NFS servers accessed by Direct NFS.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ID | NUMBER |  |
| SVRNAME | VARCHAR2(255) |  |
| DIRNAME | VARCHAR2(1024) |  |
| MNTPORT | NUMBER |  |
| NFSPORT | NUMBER |  |
| NFSVERSION | VARCHAR2(8) |  |
| WTMAX | NUMBER |  |
| RTMAX | NUMBER |  |
| CON_ID | NUMBER |  |
| RDMAENABLE | VARCHAR2(16) |  |
| RDMAPORT | NUMBER |  |
| SECURITY | VARCHAR2(32) |  |

## Usage Notes

Note: RDMA functionality is enabled only for the Exadata environment Note: RDMA functionality is enabled only for the Exadata environment