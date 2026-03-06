---
id: 19c__ALL_SEQUENCES
name: ALL_SEQUENCES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_SEQUENCES.html
---

# ALL_SEQUENCES

ALL_SEQUENCES describes all sequences accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SEQUENCE_OWNER | VARCHAR2(128) | Owner of the sequence |
| SEQUENCE_NAME | VARCHAR2(128) | Sequence name |
| MIN_VALUE | NUMBER | Minimum value of the sequence |
| MAX_VALUE | NUMBER | Maximum value of the sequence |
| INCREMENT_BY | NUMBER | Value by which sequence is incremented |
| CYCLE_FLAG | VARCHAR2(1) | Indicates whether the sequence wraps around on reaching the limit ( Y ) or not ( N ) |
| ORDER_FLAG | VARCHAR2(1) | Indicates whether sequence numbers are generated in order ( Y ) or not ( N ) |
| CACHE_SIZE | NUMBER | Number of sequence numbers to cache |
| LAST_NUMBER | NUMBER | Last sequence number written to disk. If a sequence uses caching, the number written to disk is the last number placed in the sequence cache. This number is likely to be greater than the last sequence number that was used. For session sequences, the value in this column should be ignored. |
| SCALE_FLAG | VARCHAR2(1) | Indicates whether this is a scalable sequence ( Y ) or not ( N ) |
| EXTEND_FLAG | VARCHAR2(1) | Indicates whether this scalable sequence’s generated values extend beyond MAX_VALUE or MIN_VALUE ( Y ) or not ( N ) |
| SHARDED_FLAG Foot 1 | VARCHAR2(1) | Indicates whether this is a sharded sequence ( Y ) or not ( N ) |
| SESSION_FLAG | VARCHAR2(1) | Indicates whether sequence values are session private ( Y ) or not ( N ) |
| KEEP_VALUE | VARCHAR2(1) | Indicates whether sequence values are kept during replay after a failure ( Y ) or not ( N ) |

## Usage Notes

Related Views DBA_SEQUENCES describes all sequences in the database. USER_SEQUENCES describes all sequences owned by the current user. This view does not display the SEQUENCE_OWNER column. See Also: " DBA_SEQUENCES " " USER_SEQUENCES " See Also: " DBA_SEQUENCES " " USER_SEQUENCES "