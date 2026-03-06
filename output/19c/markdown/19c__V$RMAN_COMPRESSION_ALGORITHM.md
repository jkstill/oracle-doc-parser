---
id: 19c__V$RMAN_COMPRESSION_ALGORITHM
name: V$RMAN_COMPRESSION_ALGORITHM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RMAN_COMPRESSION_ALGORITHM.html
---

# V$RMAN_COMPRESSION_ALGORITHM

V$RMAN_COMPRESSION_ALGORITHM provides descriptions of supported compression algorithms. It is used by the RMAN client.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ALGORITHM_ID | NUMBER |  |
| ALGORITHM_NAME | VARCHAR2(64) |  |
| INITIAL_RELEASE | VARCHAR2(18) |  |
| TERMINAL_RELEASE | VARCHAR2(18) |  |
| ALGORITHM_DESCRIPTION | VARCHAR2(64) |  |
| ALGORITHM_COMPATIBILITY | VARCHAR2(18) |  |
| IS_VALID | VARCHAR2(3) |  |
| REQUIRES_ACO | VARCHAR2(3) |  |
| IS_DEFAULT | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |