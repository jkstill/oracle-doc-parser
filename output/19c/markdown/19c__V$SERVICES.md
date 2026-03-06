---
id: 19c__V$SERVICES
name: V$SERVICES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-SERVICES.html
---

# V$SERVICES

V$SERVICES displays information about the services in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SERVICE_ID | NUMBER |  |
| NAME | VARCHAR2(64) |  |
| NAME_HASH | NUMBER |  |
| NETWORK_NAME | VARCHAR2(512) |  |
| CREATION_DATE | DATE |  |
| CREATION_DATE_HASH | NUMBER |  |
| GOAL | VARCHAR2(12) |  |
| DTP | VARCHAR2(1) |  |
| AQ_HA_NOTIFICATION | VARCHAR2(3) |  |
| CLB_GOAL | VARCHAR2(5) |  |
| COMMIT_OUTCOME | VARCHAR2(3) |  |
| RETENTION_TIME | NUMBER |  |
| REPLAY_INITIATION_TIMEOUT | NUMBER |  |
| SESSION_STATE_CONSISTENCY | VARCHAR2(128) |  |
| GLOBAL | VARCHAR2(3) |  |
| PDB | VARCHAR2(128) |  |
| SQL_TRANSLATION_PROFILE | VARCHAR2(261) |  |
| MAX_LAG_TIME | VARCHAR2(128) |  |
| STOP_OPTION | VARCHAR2(128) |  |
| FAILOVER_RESTORE | VARCHAR2(128) |  |
| DRAIN_TIMEOUT | NUMBER |  |
| TABLE_FAMILY_ID Foot 1 | NUMBER |  |
| CON_ID | NUMBER |  |