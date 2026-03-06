---
id: 19c__V$RECOVERY_FILE_DEST
name: V$RECOVERY_FILE_DEST
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RECOVERY_FILE_DEST.html
---

# V$RECOVERY_FILE_DEST

V$RECOVERY_FILE_DEST displays information about the disk quota and current disk usage in the fast recovery area.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(513) |  |
| SPACE_LIMIT | NUMBER |  |
| SPACE_USED | NUMBER |  |
| SPACE_RECLAIMABLE | NUMBER |  |
| NUMBER_OF_FILES | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " DB_RECOVERY_FILE_DEST " " DB_RECOVERY_FILE_DEST_SIZE " See Also: " DB_RECOVERY_FILE_DEST " " DB_RECOVERY_FILE_DEST_SIZE "