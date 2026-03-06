---
id: 19c__V$BUFFER_POOL_STATISTICS
name: V$BUFFER_POOL_STATISTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-BUFFER_POOL_STATISTICS.html
---

# V$BUFFER_POOL_STATISTICS

V$BUFFER_POOL_STATISTICS displays statistics about all buffer pools available for the instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ID | NUMBER |  |
| NAME | VARCHAR2(20) |  |
| BLOCK_SIZE | NUMBER |  |
| SET_MSIZE | NUMBER |  |
| CNUM_REPL | NUMBER |  |
| CNUM_WRITE | NUMBER |  |
| CNUM_SET | NUMBER |  |
| BUF_GOT | NUMBER |  |
| SUM_WRITE | NUMBER |  |
| SUM_SCAN | NUMBER |  |
| FREE_BUFFER_WAIT | NUMBER |  |
| WRITE_COMPLETE_WAIT | NUMBER |  |
| BUFFER_BUSY_WAIT | NUMBER |  |
| FREE_BUFFER_INSPECTED | NUMBER |  |
| DIRTY_BUFFERS_INSPECTED | NUMBER |  |
| DB_BLOCK_CHANGE | NUMBER |  |
| DB_BLOCK_GETS | NUMBER |  |
| CONSISTENT_GETS | NUMBER |  |
| PHYSICAL_READS | NUMBER |  |
| PHYSICAL_WRITES | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " DB_CACHE_SIZE " See Also: " DB_CACHE_SIZE "