---
id: 19c__DBMS_AQADM.CREATE_EXCEPTION_QUEUE
name: DBMS_AQADM.CREATE_EXCEPTION_QUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.CREATE_EXCEPTION_QUEUE

The CREATE_EXCEPTION_QUEUE API creates an exception queue for a sharded queue.

## Syntax

```sql
PROCEDURE CREATE_EXCEPTION_QUEUE(
    sharded_queue_name     IN VARCHAR2,
    exception_queue_name   IN VARCHAR2 DEFAULT NULL
    );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sharded_queue_name | VARCHAR2 | IN | The name of the sharded queue. |
| exception_queue_name | VARCHAR2 | IN | The name of the exception queue. |

## Usage Notes

Syntax PROCEDURE CREATE_EXCEPTION_QUEUE( sharded_queue_name IN VARCHAR2, exception_queue_name IN VARCHAR2 DEFAULT NULL ); Parameters Table 23-24 CREATE_EXCEPTION_QUEUE Procedure Parameters Parameter Description sharded_queue_name The name of the sharded queue. exception_queue_name The name of the exception queue.