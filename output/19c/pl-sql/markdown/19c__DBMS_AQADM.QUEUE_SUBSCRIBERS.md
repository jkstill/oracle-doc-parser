---
id: 19c__DBMS_AQADM.QUEUE_SUBSCRIBERS
name: DBMS_AQADM.QUEUE_SUBSCRIBERS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.QUEUE_SUBSCRIBERS

This function returns the subscribers to an 8.0-compatible multiconsumer queue in the PL/SQL index by table collection type DBMS_AQADM.AQ$_subscriber_list_t .

## Syntax

```sql
DBMS_AQADM.QUEUE_SUBSCRIBERS (
   queue_name         IN         VARCHAR2);
RETURN aq$_subscriber_list_t IS
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2) | IN | Specifies the queue whose subscribers are to be printed. |

**Returns:** `aq$_subscriber_list_t`

## Usage Notes

Each element of the collection is of type sys.aq$_agent . This functionality is provided for 8.1-compatible queues by the AQ$ queue_table_name _S view. Syntax DBMS_AQADM.QUEUE_SUBSCRIBERS ( queue_name IN VARCHAR2); RETURN aq$_subscriber_list_t IS Parameters Table 23-45 QUEUE_SUBSCRIBERS Function Parameters Parameter Description queue_name Specifies the queue whose subscribers are to be printed.