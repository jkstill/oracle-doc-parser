---
id: 19c__V$GES_BLOCKING_ENQUEUE
name: V$GES_BLOCKING_ENQUEUE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-GES_BLOCKING_ENQUEUE.html
---

# V$GES_BLOCKING_ENQUEUE

V$GES_BLOCKING_ENQUEUE describes all locks currently known to lock manager that are being blocked or blocking others.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| HANDLE | RAW(4 | 8) |  |
| GRANT_LEVEL | VARCHAR2(9) |  |
| REQUEST_LEVEL | VARCHAR2(9) |  |
| RESOURCE_NAME1 | VARCHAR2(30) |  |
| RESOURCE_NAME2 | VARCHAR2(30) |  |
| PID | NUMBER |  |
| TRANSACTION_ID0 | NUMBER |  |
| TRANSACTION_ID1 | NUMBER |  |
| GROUP_ID | NUMBER |  |
| OPEN_OPT_DEADLOCK | NUMBER |  |
| OPEN_OPT_PERSISTENT | NUMBER |  |
| OPEN_OPT_PROCESS_OWNED | NUMBER |  |
| OPEN_OPT_NO_XID | NUMBER |  |
| CONVERT_OPT_GETVALUE | NUMBER |  |
| CONVERT_OPT_PUTVALUE | NUMBER |  |
| CONVERT_OPT_NOVALUE | NUMBER |  |
| CONVERT_OPT_DUBVALUE | NUMBER |  |
| CONVERT_OPT_NOQUEUE | NUMBER |  |
| CONVERT_OPT_EXPRESS | NUMBER |  |
| CONVERT_OPT_NODEADLOCKWAIT | NUMBER |  |
| CONVERT_OPT_NODEADLOCKBLOCK | NUMBER |  |
| WHICH_QUEUE | NUMBER |  |
| STATE | VARCHAR2(64) |  |
| AST_EVENT0 | NUMBER |  |
| OWNER_NODE | NUMBER |  |
| BLOCKED | NUMBER |  |
| BLOCKER | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

The output of this view is a subset of the output from V$GES_ENQUEUE . This is an Oracle Real Application Clusters view. See Also: " V$GES_ENQUEUE " for a description of all locks known to the lock manager See Also: " V$GES_ENQUEUE " for a description of all locks known to the lock manager