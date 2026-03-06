---
id: 19c__V$LIBRARYCACHE
name: V$LIBRARYCACHE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-LIBRARYCACHE.html
---

# V$LIBRARYCACHE

V$LIBRARYCACHE contains statistics about library cache performance and activity.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAMESPACE | VARCHAR2(64) |  |
| GETS | NUMBER |  |
| GETHITS | NUMBER |  |
| GETHITRATIO | NUMBER |  |
| PINS | NUMBER |  |
| PINHITS | NUMBER |  |
| PINHITRATIO | NUMBER |  |
| RELOADS | NUMBER |  |
| INVALIDATIONS | NUMBER |  |
| DLM_LOCK_REQUESTS | NUMBER |  |
| DLM_PIN_REQUESTS | NUMBER |  |
| DLM_PIN_RELEASES | NUMBER |  |
| DLM_INVALIDATION_REQUESTS | NUMBER |  |
| DLM_INVALIDATIONS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content