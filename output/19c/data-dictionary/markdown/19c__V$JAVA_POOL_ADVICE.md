---
id: 19c__V$JAVA_POOL_ADVICE
name: V$JAVA_POOL_ADVICE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-JAVA_POOL_ADVICE.html
---

# V$JAVA_POOL_ADVICE

V$JAVA_POOL_ADVICE displays information about estimated parse time in the Java pool for different pool sizes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| JAVA_POOL_SIZE_FOR_ESTIMATE | NUMBER |  |
| JAVA_POOL_SIZE_FACTOR | NUMBER |  |
| ESTD_LC_SIZE | NUMBER |  |
| ESTD_LC_MEMORY_OBJECTS | NUMBER |  |
| ESTD_LC_TIME_SAVED | NUMBER |  |
| ESTD_LC_TIME_SAVED_FACTOR | NUMBER |  |
| ESTD_LC_LOAD_TIME | NUMBER |  |
| ESTD_LC_LOAD_TIME_FACTOR | NUMBER |  |
| ESTD_LC_MEMORY_OBJECT_HITS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The sizes range from 10% of the current Java pool size or the amount of pinned Java library cache memory (whichever is higher) to 200% of the current Java pool size, in equal intervals. The value of the interval depends on the current size of the Java pool. Parse time saved refers to the amount of time saved by keeping library cache memory objects in the Java pool, as opposed to having to reload these objects.