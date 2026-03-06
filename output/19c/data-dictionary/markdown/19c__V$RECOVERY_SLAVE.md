---
id: 19c__V$RECOVERY_SLAVE
name: V$RECOVERY_SLAVE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RECOVERY_SLAVE.html
---

# V$RECOVERY_SLAVE

V$RECOVERY_SLAVE is used to track database media recovery processes to monitor their performance statistics and analyze a media recovery session.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| START_TIME | DATE |  |
| TYPE | VARCHAR2(64) |  |
| ITEM | VARCHAR2(32) |  |
| UNITS | VARCHAR2(32) |  |
| SOFAR | NUMBER |  |
| TOTAL | NUMBER |  |
| COMMENTS | VARCHAR2(248) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Backup and Recovery User’s Guide See Also: Oracle Database Backup and Recovery User’s Guide