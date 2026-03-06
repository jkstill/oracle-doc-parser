---
id: 19c__V$NFS_CLIENTS
name: V$NFS_CLIENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-NFS_CLIENTS.html
---

# V$NFS_CLIENTS

V$NFS_CLIENTS displays information about NFS clients currently connected to the XML DB NFS Server.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLIENTID | NUMBER |  |
| PRINCIPAL | VARCHAR2(2000) |  |
| CLIENTOPAQUEIDENTIFIER | VARCHAR2(1000) |  |
| VERIFIER | RAW(8) |  |
| LEASEEXPIRY | NUMBER |  |
| CLIENTADDR | VARCHAR2(2000) |  |
| CONFIRMED | VARCHAR2(5) |  |
| CON_ID | NUMBER |  |