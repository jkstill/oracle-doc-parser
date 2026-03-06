---
id: 19c__V$WAITSTAT
name: V$WAITSTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-WAITSTAT.html
---

# V$WAITSTAT

Number of waits by this OPERATION for this CLASS of block

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLASS | VARCHAR2(18) |  |
| COUNT | NUMBER |  |
| TIME | NUMBER |  |
| CON_ID | NUMBER |  |