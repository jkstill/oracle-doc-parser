---
id: 19c__V$CONFIGURED_INTERCONNECTS
name: V$CONFIGURED_INTERCONNECTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-CONFIGURED_INTERCONNECTS.html
---

# V$CONFIGURED_INTERCONNECTS

V$CONFIGURED_INTERCONNECTS displays all the interconnects that Oracle is aware of. This view attempts to answer the question of where Oracle found the information about a specific interconnect.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(15) |  |
| IP_ADDRESS | VARCHAR2(64) |  |
| IS_PUBLIC | VARCHAR2(3) |  |
| SOURCE | VARCHAR2(31) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content