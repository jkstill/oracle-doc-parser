---
id: 19c__V$FIXED_VIEW_DEFINITION
name: V$FIXED_VIEW_DEFINITION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dynamic_performance]
source_file: V-FIXED_VIEW_DEFINITION.html
---

# V$FIXED_VIEW_DEFINITION

V$FIXED_VIEW_DEFINITION contains the definitions of all the fixed views (views beginning with V$ ).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| VIEW_NAME | VARCHAR2(128) |  |
| VIEW_DEFINITION | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Use this table with caution. Oracle tries to keep the behavior of fixed views the same from release to release, but the definitions of the fixed views can change without notice. Use these definitions to optimize your queries by using indexed columns of the dynamic performance tables.