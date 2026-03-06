---
id: 19c__V$CONTAINERS
name: V$CONTAINERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-CONTAINERS.html
---

# V$CONTAINERS

V$CONTAINERS displays information about PDBs and the root associated with the current instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CON_ID | NUMBER |  |
| DBID | NUMBER |  |
| CON_UID | NUMBER |  |
| GUID | RAW(16) |  |
| NAME | VARCHAR2(128) |  |
| OPEN_MODE | VARCHAR2(10) |  |
| RESTRICTED | VARCHAR2(3) |  |
| OPEN_TIME | TIMESTAMP(3) |  |
| CREATE_SCN | NUMBER |  |
| TOTAL_SIZE | NUMBER |  |
| BLOCK_SIZE | NUMBER |  |
| RECOVERY_STATUS | VARCHAR2(8) |  |
| SNAPSHOT_PARENT_CON_ID | NUMBER |  |
| APPLICATION_ROOT | VARCHAR2(3) |  |
| APPLICATION_PDB | VARCHAR2(3) |  |
| APPLICATION_SEED | VARCHAR2(3) |  |
| APPLICATION_ROOT_CON_ID | NUMBER |  |
| APPLICATION_ROOT_CLONE | VARCHAR2(3) |  |
| PROXY_PDB | VARCHAR2(3) |  |
| LOCAL_UNDO | NUMBER |  |
| UNDO_SCN | NUMBER |  |
| UNDO_TIMESTAMP | DATE |  |
| CREATION_TIME | DATE |  |
| PDB_COUNT | NUMBER |  |
| AUDIT_FILES_SIZE | NUMBER |  |
| MAX_SIZE | NUMBER |  |
| MAX_DIAGNOSTICS_SIZE | NUMBER |  |
| MAX_AUDIT_SIZE | NUMBER |  |
| LAST_CHANGED_BY | VARCHAR2(11) |  |
| MEMBER_CDB | VARCHAR2(3) |  |
| TENANT_ID | VARCHAR2(256) |  |
| UPGRADE_LEVEL | NUMBER |  |
| GUID_BASE64 | VARCHAR2(30) |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content