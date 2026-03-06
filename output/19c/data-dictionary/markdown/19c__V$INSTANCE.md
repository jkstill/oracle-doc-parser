---
id: 19c__V$INSTANCE
name: V$INSTANCE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-INSTANCE.html
---

# V$INSTANCE

V$INSTANCE displays the state of the current instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INSTANCE_NUMBER | NUMBER |  |
| INSTANCE_NAME | VARCHAR2(16) |  |
| HOST_NAME | VARCHAR2(64) |  |
| VERSION | VARCHAR2(17) |  |
| VERSION_LEGACY | VARCHAR2(17) |  |
| VERSION_FULL | VARCHAR2(17) |  |
| STARTUP_TIME | DATE |  |
| STATUS | VARCHAR2(12) |  |
| PARALLEL | VARCHAR2(3) |  |
| THREAD# | NUMBER |  |
| ARCHIVER | VARCHAR2(7) |  |
| LOG_SWITCH_WAIT | VARCHAR2(15) |  |
| LOGINS | VARCHAR2(10) |  |
| SHUTDOWN_PENDING | VARCHAR2(3) |  |
| DATABASE_STATUS | VARCHAR2(17) |  |
| INSTANCE_ROLE | VARCHAR2(18) |  |
| ACTIVE_STATE | VARCHAR2(9) |  |
| BLOCKED | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |
| INSTANCE_MODE | VARCHAR2(11) |  |
| EDITION | VARCHAR2(7) |  |
| FAMILY | VARCHAR2(80) |  |
| DATABASE_TYPE | VARCHAR2(15) |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content