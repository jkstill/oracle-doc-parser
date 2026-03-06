---
id: 19c__INDEX_HISTOGRAM
name: INDEX_HISTOGRAM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: index
source_file: INDEX_HISTOGRAM.html
---

# INDEX_HISTOGRAM

INDEX_HISTOGRAM contains information from the ANALYZE INDEX ... VALIDATE STRUCTURE statement.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REPEAT_COUNT | NUMBER | Number of times that one or more index keys is repeated in the table |
| KEYS_WITH_REPEAT_COUNT | NUMBER | Number of index keys that are repeated that many times |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: The ANALYZE INDEX ... VALIDATE STRUCTURE OFFLINE statement must be used to collect statistics. Note: The ANALYZE INDEX ... VALIDATE STRUCTURE OFFLINE statement must be used to collect statistics.