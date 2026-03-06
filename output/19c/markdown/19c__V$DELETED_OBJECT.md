---
id: 19c__V$DELETED_OBJECT
name: V$DELETED_OBJECT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dynamic_performance]
source_file: V-DELETED_OBJECT.html
---

# V$DELETED_OBJECT

V$DELETED_OBJECT displays information about deleted archived logs, data file copies and backup pieces from the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| TYPE | VARCHAR2(26) |  |
| OBJECT_RECID | NUMBER |  |
| OBJECT_STAMP | NUMBER |  |
| OBJECT_DATA | NUMBER |  |
| SET_STAMP | NUMBER |  |
| SET_COUNT | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

The only purpose of this view is to optimize the recovery catalog resync operation. When an archived log, data file copy, or backup piece is deleted, the corresponding record is marked deleted.