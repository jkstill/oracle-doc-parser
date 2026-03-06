---
id: 19c__V$COPY_CORRUPTION
name: V$COPY_CORRUPTION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-COPY_CORRUPTION.html
---

# V$COPY_CORRUPTION

V$COPY_CORRUPTION displays information about data file copy corruptions from the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| COPY_RECID | NUMBER |  |
| COPY_STAMP | NUMBER |  |
| FILE# | NUMBER |  |
| BLOCK# | NUMBER |  |
| BLOCKS | NUMBER |  |
| CORRUPTION_CHANGE# | NUMBER |  |
| MARKED_CORRUPT | VARCHAR2(3) |  |
| CORRUPTION_TYPE | VARCHAR2(9) |  |
| CON_ID | NUMBER |  |