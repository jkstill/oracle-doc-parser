---
id: 19c__V$GC_ELEMENT
name: V$GC_ELEMENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-GC_ELEMENT.html
---

# V$GC_ELEMENT

V$GC_ELEMENT displays one entry for each global cache resource that is used by the buffer cache. The name of the global cache resource that corresponds to a lock element is {'BL', indx, class}. This is an Oracle Real Application Clusters view.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GC_ELEMENT_ADDR | RAW(4 | 8) |  |
| INDX | NUMBER |  |
| CLASS | NUMBER |  |
| GC_ELEMENT_NAME | NUMBER |  |
| MODE_HELD | NUMBER |  |
| BLOCK_COUNT | NUMBER |  |
| RELEASING | NUMBER |  |
| ACQUIRING | NUMBER |  |
| WRITING | NUMBER |  |
| RECOVERING | NUMBER |  |
| LOCAL | NUMBER |  |
| FLAGS | NUMBER |  |
| CON_ID | NUMBER |  |