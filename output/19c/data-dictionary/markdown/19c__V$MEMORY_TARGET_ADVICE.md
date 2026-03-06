---
id: 19c__V$MEMORY_TARGET_ADVICE
name: V$MEMORY_TARGET_ADVICE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-MEMORY_TARGET_ADVICE.html
---

# V$MEMORY_TARGET_ADVICE

V$MEMORY_TARGET_ADVICE provides information about how the MEMORY_TARGET parameter should be sized based on current sizing and satisfaction metrics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| MEMORY_SIZE | NUMBER |  |
| MEMORY_SIZE_FACTOR | NUMBER |  |
| ESTD_DB_TIME | NUMBER |  |
| ESTD_DB_TIME_FACTOR | NUMBER |  |
| VERSION | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Table 8-2 shows how the information provided in V$MEMORY_TARGET_ADVICE could be used to improve performance. The data indicates that if current memory size is 380M, and you were to increase it to 760M (2x), the current workload would take 80525 units of DBtime as opposed to 115475 units of DBtime, which is a significant improvement in performance. See Also: " MEMORY_TARGET " See Also: " MEMORY_TARGET "