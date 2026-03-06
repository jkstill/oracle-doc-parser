---
id: 19c__V$DB_CACHE_ADVICE
name: V$DB_CACHE_ADVICE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DB_CACHE_ADVICE.html
---

# V$DB_CACHE_ADVICE

V$DB_CACHE_ADVICE contains rows that predict the number of physical reads for the cache size corresponding to each row.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ID | NUMBER |  |
| NAME | VARCHAR2(20) |  |
| BLOCK_SIZE | NUMBER |  |
| ADVICE_STATUS | VARCHAR2(3) |  |
| SIZE_FOR_ESTIMATE | NUMBER |  |
| SIZE_FACTOR | NUMBER |  |
| BUFFERS_FOR_ESTIMATE | NUMBER |  |
| ESTD_PHYSICAL_READ_FACTOR | NUMBER |  |
| ESTD_PHYSICAL_READS | NUMBER |  |
| ESTD_PHYSICAL_READ_TIME | NUMBER |  |
| ESTD_PCT_OF_DB_TIME_FOR_READS | NUMBER |  |
| ESTD_CLUSTER_READS | NUMBER |  |
| ESTD_CLUSTER_READ_TIME | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

The rows also compute a "physical read factor," which is the ratio of the number of estimated reads to the number of reads actually performed by the real buffer cache during the measurement interval. See Also: " DB_CACHE_ADVICE " See Also: " DB_CACHE_ADVICE "