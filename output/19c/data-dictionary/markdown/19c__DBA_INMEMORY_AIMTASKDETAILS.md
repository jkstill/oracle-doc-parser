---
id: 19c__DBA_INMEMORY_AIMTASKDETAILS
name: DBA_INMEMORY_AIMTASKDETAILS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_INMEMORY_AIMTASKDETAILS.html
---

# DBA_INMEMORY_AIMTASKDETAILS

DBA_INMEMORY_AIMTASKDETAILS displays details for an Automatic In-Memory management task.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TASK_ID | NUMBER | Number that uniquely identifies a specific automatic IM column store management task |
| OBJECT_OWNER | VARCHAR2(128) | Owner of the object subject to automatic IM column store management task action |
| OBJECT_NAME | VARCHAR2(128) | Name of the object subject to automatic IM column store management task action |
| SUBOBJECT_NAME | VARCHAR2(128) | Name of the subobject subject to automatic IM column store management task action |
| ACTION | VARCHAR2(16) | Action taken on the object |
| STATE | VARCHAR2(10) | Status of the action on the object |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database In-Memory Guide for more information about configuring the Automatic In-Memory feature See Also: Oracle Database In-Memory Guide for more information about configuring the Automatic In-Memory feature