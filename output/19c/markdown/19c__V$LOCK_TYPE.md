---
id: 19c__V$LOCK_TYPE
name: V$LOCK_TYPE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-LOCK_TYPE.html
---

# V$LOCK_TYPE

V$LOCK_TYPE describes the type of locks available.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TYPE | VARCHAR2(64) |  |
| NAME | VARCHAR2(64) |  |
| ID1_TAG | VARCHAR2(64) |  |
| ID2_TAG | VARCHAR2(64) |  |
| IS_USER | VARCHAR2(3) |  |
| IS_RECYCLE | VARCHAR2(3) |  |
| DESCRIPTION | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |