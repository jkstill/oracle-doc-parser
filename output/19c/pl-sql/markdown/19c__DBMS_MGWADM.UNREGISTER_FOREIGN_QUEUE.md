---
id: 19c__DBMS_MGWADM.UNREGISTER_FOREIGN_QUEUE
name: DBMS_MGWADM.UNREGISTER_FOREIGN_QUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.UNREGISTER_FOREIGN_QUEUE

This procedure removes a non-Oracle queue entity in Messaging Gateway.

## Syntax

```sql
DBMS_MGWADM.UNREGISTER_FOREIGN_QUEUE(
   name         IN VARCHAR2,
   linkname     IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | The queue name |
| linkname | VARCHAR2) | IN | The link name for the messaging system on which the queue exists |

## Usage Notes

Syntax DBMS_MGWADM.UNREGISTER_FOREIGN_QUEUE( name IN VARCHAR2, linkname IN VARCHAR2); Parameters Table 110-50 UNREGISTER_FOREIGN_QUEUE Procedure Parameters Parameter Description name The queue name linkname The link name for the messaging system on which the queue exists Usage Notes This procedure does not remove the physical queue in the non-Oracle messaging system. All propagation jobs, subscribers and schedules referencing this queue must be removed before it can be unregistered. This procedure fails if a propagation job, subscriber, or propagation schedule references the non-Oracle queue.