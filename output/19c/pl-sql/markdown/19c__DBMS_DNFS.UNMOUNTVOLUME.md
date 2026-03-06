---
id: 19c__DBMS_DNFS.UNMOUNTVOLUME
name: DBMS_DNFS.UNMOUNTVOLUME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DNFS
tags: [dbms_dnfs]
source_file: DBMS_DNFS.html
---

# DBMS_DNFS.UNMOUNTVOLUME

This procedure cleans up the cached Direct NFS file handles in SGA. This procedure must be used when any NFS mount changes are being made via the operating system and the OS unmount and mount commands are invoked.

## Syntax

```sql
DBMS_DNFS.UNMOUNTVOLUME (
   server         IN         VARCHAR2,
   volume         IN         VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| server | VARCHAR2 | IN | NFS server host name or IP address. |
| volume | VARCHAR2) | IN | Exported path from the NFS server. |

## Usage Notes

The server is the host name or IP address of the NFS server. The volume is the exported path from the NFS server. This procedure will fail if the database has any open files in the volume that is being unmounted. Syntax DBMS_DNFS.UNMOUNTVOLUME ( server IN VARCHAR2, volume IN VARCHAR2); Parameters Table 64-4 UNMOUNTVOLUME Procedure Parameters Parameter Description server NFS server host name or IP address. volume Exported path from the NFS server.