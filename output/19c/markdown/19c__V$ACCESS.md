---
id: 19c__V$ACCESS
name: V$ACCESS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ACCESS.html
---

# V$ACCESS

V$ACCESS displays information about locks that are currently imposed on library cache objects.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| OWNER | VARCHAR2(64) |  |
| OBJECT | VARCHAR2(1000) |  |
| TYPE | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

The locks are imposed to ensure that they are not aged out of the library cache while they are required for SQL execution.