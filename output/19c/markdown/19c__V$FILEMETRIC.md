---
id: 19c__V$FILEMETRIC
name: V$FILEMETRIC
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-FILEMETRIC.html
---

# V$FILEMETRIC

V$FILEMETRIC displays values of file metrics for the most recent 10-minute interval. A history of the last one hour will be kept in the system.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| INTSIZE_CSEC | NUMBER |  |
| FILE_ID | NUMBER |  |
| CREATION_TIME | NUMBER |  |
| AVERAGE_READ_TIME | NUMBER |  |
| AVERAGE_WRITE_TIME | NUMBER |  |
| PHYSICAL_READS | NUMBER |  |
| PHYSICAL_WRITES | NUMBER |  |
| PHYSICAL_BLOCK_READS | NUMBER |  |
| PHYSICAL_BLOCK_WRITES | NUMBER |  |
| CON_ID | NUMBER |  |