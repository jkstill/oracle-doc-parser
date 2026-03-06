---
id: 19c__DBMS_AQADM.REMOVE_SUBSCRIBER
name: DBMS_AQADM.REMOVE_SUBSCRIBER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.REMOVE_SUBSCRIBER

This procedure removes a default subscriber from a queue. This operation takes effect immediately, and the containing transaction is committed. All references to the subscriber in existing messages are removed as part of the operation.

## Syntax

```sql
DBMS_AQADM.REMOVE_SUBSCRIBER (
   queue_name         IN         VARCHAR2,
   subscriber         IN         sys.aq$_agent);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | Name of the queue. |
| subscriber | sys.aq$_agent) | IN | Agent who is being removed. See AQ$_AGENT Type . |

## Usage Notes

Syntax DBMS_AQADM.REMOVE_SUBSCRIBER ( queue_name IN VARCHAR2, subscriber IN sys.aq$_agent); Parameters Table 23-46 REMOVE_SUBSCRIBER Procedure Parameters Parameter Description queue_name Name of the queue. subscriber Agent who is being removed. See AQ$_AGENT Type .