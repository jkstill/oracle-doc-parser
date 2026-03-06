---
id: 19c__V$JAVA_LIBRARY_CACHE_MEMORY
name: V$JAVA_LIBRARY_CACHE_MEMORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-JAVA_LIBRARY_CACHE_MEMORY.html
---

# V$JAVA_LIBRARY_CACHE_MEMORY

V$JAVA_LIBRARY_CACHE_MEMORY displays information about memory allocated to library cache memory objects in different namespaces for Java objects.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| LC_NAMESPACE | VARCHAR2(15) |  |
| LC_INUSE_MEMORY_OBJECTS | NUMBER |  |
| LC_INUSE_MEMORY_SIZE | NUMBER |  |
| LC_FREEABLE_MEMORY_OBJECTS | NUMBER |  |
| LC_FREEABLE_MEMORY_SIZE | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content A memory object is an internal grouping of memory for efficient management. A library cache object may consist of one or more memory objects.