---
id: 19c__V$MANAGED_STANDBY
name: V$MANAGED_STANDBY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-MANAGED_STANDBY.html
---

# V$MANAGED_STANDBY

V$MANAGED_STANDBY displays current status information for some Oracle Database processes related to physical standby databases in the Data Guard environment. This view does not persist after an instance shutdown.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PROCESS | VARCHAR2(9) |  |
| PID | VARCHAR2(24) |  |
| STATUS | VARCHAR2(12) |  |
| CLIENT_PROCESS | VARCHAR2(8) |  |
| CLIENT_PID | VARCHAR2(40) |  |
| CLIENT_DBID | VARCHAR2(40) |  |
| GROUP# | VARCHAR2(40) |  |
| RESETLOG_ID | NUMBER |  |
| THREAD# | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| BLOCK# | NUMBER |  |
| BLOCKS | NUMBER |  |
| DELAY_MINS | NUMBER |  |
| KNOWN_AGENTS | NUMBER |  |
| ACTIVE_AGENTS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: This view is deprecated in Oracle Database 12 c Release 2 (12.2.0.1) and may be desupported in a future release. The V$DATAGUARD_PROCESS view should be used, instead. See Also: " V$DATAGUARD_PROCESS " Note: This view is deprecated in Oracle Database 12 c Release 2 (12.2.0.1) and may be desupported in a future release. The V$DATAGUARD_PROCESS view should be used, instead. See Also: " V$DATAGUARD_PROCESS "