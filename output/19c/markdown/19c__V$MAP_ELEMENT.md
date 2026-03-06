---
id: 19c__V$MAP_ELEMENT
name: V$MAP_ELEMENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-MAP_ELEMENT.html
---

# V$MAP_ELEMENT

V$MAP_ELEMENT displays a list of all element mapping structures in the SGA of the instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ELEM_NAME | VARCHAR2(256) |  |
| ELEM_IDX | NUMBER |  |
| ELEM_CFGID | VARCHAR2(256) |  |
| ELEM_TYPE | VARCHAR2(12) |  |
| ELEM_SIZE | NUMBER |  |
| ELEM_NSUBELEM | NUMBER |  |
| ELEM_DESCR | VARCHAR2(256) |  |
| STRIPE_SIZE | NUMBER |  |
| LIB_IDX | NUMBER |  |
| CON_ID | NUMBER |  |