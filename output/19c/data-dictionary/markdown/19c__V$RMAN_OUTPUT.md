---
id: 19c__V$RMAN_OUTPUT
name: V$RMAN_OUTPUT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RMAN_OUTPUT.html
---

# V$RMAN_OUTPUT

The script content on this page is for navigation purposes only and does not alter the content in any way.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| SESSION_RECID | NUMBER |  |
| SESSION_STAMP | NUMBER |  |
| OUTPUT | VARCHAR2(130) |  |
| RMAN_STATUS_RECID | NUMBER |  |
| RMAN_STATUS_STAMP | NUMBER |  |
| SESSION_KEY | NUMBER |  |
| GUID Foot 1 | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This is an in-memory view and is not recorded in the controlfile. The view can hold 32768 rows.