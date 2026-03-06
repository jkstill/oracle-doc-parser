---
id: 19c__V$IOFUNCMETRIC
name: V$IOFUNCMETRIC
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-IOFUNCMETRIC.html
---

# V$IOFUNCMETRIC

V$IOFUNCMETRIC displays I/O statistics information by database function for the most recent time interval period.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| INTSIZE_CSEC | NUMBER |  |
| FUNCTION_ID | NUMBER |  |
| FUNCTION_NAME | VARCHAR2(18) |  |
| SMALL_READ_MBPS | NUMBER |  |
| SMALL_WRITE_MBPS | NUMBER |  |
| LARGE_READ_MBPS | NUMBER |  |
| LARGE_WRITE_MBPS | NUMBER |  |
| SMALL_READ_IOPS | NUMBER |  |
| SMALL_WRITE_IOPS | NUMBER |  |
| LARGE_READ_IOPS | NUMBER |  |
| LARGE_WRITE_IOPS | NUMBER |  |
| AVG_WAIT_TIME | NUMBER |  |
| CON_ID | NUMBER |  |