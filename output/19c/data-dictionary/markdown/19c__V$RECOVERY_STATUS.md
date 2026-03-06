---
id: 19c__V$RECOVERY_STATUS
name: V$RECOVERY_STATUS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-RECOVERY_STATUS.html
---

# V$RECOVERY_STATUS

RECOVERY_CHECKPOINT

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECOVERY_CHECKPOINT | DATE |  |
| THREAD | NUMBER |  |
| SEQUENCE_NEEDED | NUMBER |  |
| SCN_NEEDED | VARCHAR2(16) |  |
| TIME_NEEDED | DATE |  |
| PREVIOUS_LOG_NAME | VARCHAR2(513) |  |
| PREVIOUS_LOG_STATUS | VARCHAR2(13) |  |
| REASON | VARCHAR2(13) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Backup and Recovery User’s Guide See Also: Oracle Database Backup and Recovery User’s Guide