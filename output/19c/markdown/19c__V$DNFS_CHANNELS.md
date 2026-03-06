---
id: 19c__V$DNFS_CHANNELS
name: V$DNFS_CHANNELS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DNFS_CHANNELS.html
---

# V$DNFS_CHANNELS

V$DNFS_CHANNELS displays information about the Oracle process connections (channels) open to NFS servers.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PNUM | NUMBER |  |
| SVRNAME | VARCHAR2(255) |  |
| PATH | VARCHAR2(255) |  |
| LOCAL | VARCHAR2(255) |  |
| CH_ID | NUMBER |  |
| SVR_ID | NUMBER |  |
| SENDS | NUMBER |  |
| RECVS | NUMBER |  |
| PINGS | NUMBER |  |
| SPRECO | NUMBER |  |
| DPRECO | NUMBER |  |
| CON_ID | NUMBER |  |
| RDMA | NUMBER |  |
| RDMA_CREDITS | NUMBER |  |
| CLIENTPORT | NUMBER |  |
| ACTIVE_SPEED | NUMBER |  |
| PEAK_FMR | NUMBER |  |
| CURRENT_FMR | NUMBER |  |
| FMRREG_COUNT | NUMBER |  |

## Usage Notes

Note: RDMA functionality is enabled only for the Exadata environment Note: RDMA functionality is enabled only for the Exadata environment