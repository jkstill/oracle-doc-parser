---
id: 19c__V$FILEMETRIC_HISTORY
name: V$FILEMETRIC_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-FILEMETRIC_HISTORY.html
---

# V$FILEMETRIC_HISTORY

V$FILEMETRIC_HISTORY displays values of file metrics for all intervals in the last one hour.

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