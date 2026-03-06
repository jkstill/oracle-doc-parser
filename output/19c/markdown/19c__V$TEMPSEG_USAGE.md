---
id: 19c__V$TEMPSEG_USAGE
name: V$TEMPSEG_USAGE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-TEMPSEG_USAGE.html
---

# V$TEMPSEG_USAGE

V$TEMPSEG_USAGE describes temporary segment usage.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USERNAME | VARCHAR2(128) |  |
| USER | VARCHAR2(128) |  |
| SESSION_ADDR | RAW(4 | 8) |  |
| SESSION_NUM | NUMBER |  |
| SQLADDR | RAW(4 | 8) |  |
| SQLHASH | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| TABLESPACE | VARCHAR2(30) |  |
| CONTENTS | VARCHAR2(9) |  |
| SEGTYPE | VARCHAR2(9) |  |
| SEGFILE# | NUMBER |  |
| SEGBLK# | NUMBER |  |
| EXTENTS | NUMBER |  |
| BLOCKS | NUMBER |  |
| SEGRFNO# | NUMBER |  |
| TS# | NUMBER |  |
| CON_ID | NUMBER |  |
| SQL_ID_TEMPSEG | VARCHAR2(13) |  |