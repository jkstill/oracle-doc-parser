---
id: 19c__V$LOCKED_OBJECT
name: V$LOCKED_OBJECT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dynamic_performance]
source_file: V-LOCKED_OBJECT.html
---

# V$LOCKED_OBJECT

V$LOCKED_OBJECT lists all locks acquired by every transaction on the system. It shows which sessions are holding DML locks (that is, TM-type enqueues) on what objects and in what mode.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| XIDUSN | NUMBER |  |
| XIDSLOT | NUMBER |  |
| XIDSQN | NUMBER |  |
| OBJECT_ID | NUMBER |  |
| SESSION_ID | NUMBER |  |
| ORACLE_USERNAME | VARCHAR2(128) |  |
| OS_USER_NAME | VARCHAR2(128) |  |
| PROCESS | VARCHAR2(24) |  |
| LOCKED_MODE | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content