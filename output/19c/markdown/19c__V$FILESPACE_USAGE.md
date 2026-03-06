---
id: 19c__V$FILESPACE_USAGE
name: V$FILESPACE_USAGE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-FILESPACE_USAGE.html
---

# V$FILESPACE_USAGE

V$FILESPACE_USAGE summarizes space allocation information of each data file and temp file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLESPACE_ID | NUMBER |  |
| RFNO | NUMBER |  |
| ALLOCATED_SPACE | NUMBER |  |
| FILE_SIZE | NUMBER |  |
| FILE_MAXSIZE | NUMBER |  |
| CHANGESCN_BASE | NUMBER |  |
| CHANGESCN_WRAP | NUMBER |  |
| CHANGESCN8 | NUMBER |  |
| FLAG | NUMBER |  |
| CON_ID | NUMBER |  |