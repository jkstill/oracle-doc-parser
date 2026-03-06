---
id: 19c__V$AQ_IPC_ACTIVE_MSGS
name: V$AQ_IPC_ACTIVE_MSGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-AQ_IPC_ACTIVE_MSGS.html
---

# V$AQ_IPC_ACTIVE_MSGS

V$AQ_IPC_ACTIVE_MSGS displays the information related to active IPC messages being processed by AQ background processes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PROCESS_NAME | VARCHAR2(48) |  |
| PROCESS_ID | NUMBER |  |
| SLAVE_STATE | NUMBER |  |
| SLAVEOBJ_STATE | NUMBER |  |
| SEQUENCE_NUMBER | NUMBER |  |
| MSG_CLASS_NAME | VARCHAR2(30) |  |
| MSG_FLAGS | NUMBER |  |
| MSG_SUBMT_TIME | NUMBER |  |
| MSG_PICKD_TIME | NUMBER |  |
| CON_ID | NUMBER |  |