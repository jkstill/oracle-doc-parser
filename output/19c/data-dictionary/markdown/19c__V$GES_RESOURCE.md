---
id: 19c__V$GES_RESOURCE
name: V$GES_RESOURCE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-GES_RESOURCE.html
---

# V$GES_RESOURCE

V$GES_RESOURCE is an Oracle Real Application Clusters view. It displays information of all resources currently known to the lock manager.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RESP | RAW(4 | 8) |  |
| RESOURCE_NAME | VARCHAR2(30) |  |
| ON_CONVERT_Q | NUMBER |  |
| ON_GRANT_Q | NUMBER |  |
| PERSISTENT_RES | NUMBER |  |
| MASTER_NODE | NUMBER |  |
| NEXT_CVT_LEVEL | VARCHAR2(9) |  |
| VALUE_BLK_STATE | VARCHAR2(32) |  |
| VALUE_BLK | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content