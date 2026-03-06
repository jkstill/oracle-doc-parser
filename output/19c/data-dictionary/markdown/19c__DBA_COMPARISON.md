---
id: 19c__DBA_COMPARISON
name: DBA_COMPARISON
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_COMPARISON.html
---

# DBA_COMPARISON

DBA_COMPARISON displays information about all comparison objects in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the comparison |
| COMPARISON_NAME | VARCHAR2(128) | Name of the comparison |
| COMPARISON_MODE | VARCHAR2(5) | Mode of the comparison: TABLE |
| SCHEMA_NAME | VARCHAR2(128) | Schema name of the local object |
| OBJECT_NAME | VARCHAR2(128) | Name of the local object |
| OBJECT_TYPE | VARCHAR2(17) | Type of the local object: TABLE VIEW SYNONYM MATERIALIZED VIEW |
| REMOTE_SCHEMA_NAME | VARCHAR2(128) | Schema name of the remote object |
| REMOTE_OBJECT_NAME | VARCHAR2(128) | Name of the remote object |
| REMOTE_OBJECT_TYPE | VARCHAR2(17) | Type of the remote object: TABLE VIEW SYNONYM MATERIALIZED VIEW |
| DBLINK_NAME | VARCHAR2(128) | Database link name to the remote database |
| SCAN_MODE | VARCHAR2(9) | Scan mode of the comparison: FULL FULL RANDOM CYCLIC CUSTOM |
| SCAN_PERCENT | NUMBER | Scan percent of the comparison; applicable to random and cyclic modes |
| CYCLIC_INDEX_VALUE | VARCHAR2(4000) | Last index column value used in a cyclic scan |
| NULL_VALUE | VARCHAR2(4000) | Value to use for NULL columns |
| LOCAL_CONVERGE_TAG | RAW(2000) | Local Replication tag used while performing converge DMLs |
| REMOTE_CONVERGE_TAG | RAW(2000) | Remote Replication tag used while performing converge DMLs |
| MAX_NUM_BUCKETS | NUMBER | Suggested maximum number of buckets in a scan |
| MIN_ROWS_IN_BUCKET | NUMBER | Suggested minimum number of rows in a bucket |
| LAST_UPDATE_TIME | TIMESTAMP(6) | Time that this row was last updated |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_COMPARISON displays information about the comparison objects owned by the current user. This view does not display the OWNER column. See Also: " USER_COMPARISON " See Also: " USER_COMPARISON "