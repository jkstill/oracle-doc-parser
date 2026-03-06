---
id: 19c__DBA_HIST_DB_CACHE_ADVICE
name: DBA_HIST_DB_CACHE_ADVICE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_DB_CACHE_ADVICE.html
---

# DBA_HIST_DB_CACHE_ADVICE

DBA_HIST_DB_CACHE_ADVICE displays historical predictions of the number of physical reads for the cache size corresponding to each row.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| BPID | NUMBER | Buffer Pool identifier (ranges from 1 to 8) |
| BUFFERS_FOR_ESTIMATE | NUMBER | Cache size for prediction (in terms of buffers) |
| NAME | VARCHAR2(20) | Buffer pool name |
| BLOCK_SIZE | NUMBER | Block size in bytes for buffers in the pool (the standard block size, the power of 2 nonstandard block sizes, 2048, 4096, 8192, 16384, or 32768) |
| ADVICE_STATUS | VARCHAR2(3) | Status of the advisory: ON - Currently running OFF - Disabled (the estimates are historical and calculated when last enabled) |
| SIZE_FOR_ESTIMATE | NUMBER | Cache size for prediction (in megabytes) |
| SIZE_FACTOR | NUMBER | Size factor with respect to the current cache size |
| PHYSICAL_READS | NUMBER | Physical reads for the cache size |
| BASE_PHYSICAL_READS | NUMBER | Base physical reads for the cache size |
| ACTUAL_PHYSICAL_READS | NUMBER | Actual physical reads for the cache size |
| ESTD_PHYSICAL_READ_TIME | NUMBER | Estimated physical read time for the cache size |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$DB_CACHE_ADVICE . See Also: " V$DB_CACHE_ADVICE " See Also: " V$DB_CACHE_ADVICE "