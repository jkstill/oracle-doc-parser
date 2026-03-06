---
id: 19c__V$ROLLSTAT
name: V$ROLLSTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-ROLLSTAT.html
---

# V$ROLLSTAT

V$ROLLSTAT contains rollback segment statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USN | NUMBER |  |
| LATCH | NUMBER |  |
| EXTENTS | NUMBER |  |
| RSSIZE | NUMBER |  |
| WRITES | NUMBER |  |
| XACTS | NUMBER |  |
| GETS | NUMBER |  |
| WAITS | NUMBER |  |
| OPTSIZE | NUMBER |  |
| HWMSIZE | NUMBER |  |
| SHRINKS | NUMBER |  |
| WRAPS | NUMBER |  |
| EXTENDS | NUMBER |  |
| AVESHRINK | NUMBER |  |
| AVEACTIVE | NUMBER |  |
| STATUS | VARCHAR2(15) |  |
| CUREXT | NUMBER |  |
| CURBLK | NUMBER |  |
| CON_ID | NUMBER |  |