---
id: 19c__V$ROWCACHE
name: V$ROWCACHE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ROWCACHE.html
---

# V$ROWCACHE

V$ROWCACHE displays statistics for data dictionary activity. Each row contains statistics for one data dictionary cache.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CACHE# | NUMBER |  |
| TYPE | VARCHAR2(11) |  |
| SUBORDINATE# | NUMBER |  |
| PARAMETER | VARCHAR2(32) |  |
| COUNT | NUMBER |  |
| USAGE | NUMBER |  |
| FIXED | NUMBER |  |
| GETS | NUMBER |  |
| FASTGETS | NUMBER |  |
| GETMISSES | NUMBER |  |
| SCANS | NUMBER |  |
| SCANMISSES | NUMBER |  |
| SCANCOMPLETES | NUMBER |  |
| MODIFICATIONS | NUMBER |  |
| FLUSHES | NUMBER |  |
| DLM_REQUESTS | NUMBER |  |
| DLM_CONFLICTS | NUMBER |  |
| DLM_RELEASES | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content