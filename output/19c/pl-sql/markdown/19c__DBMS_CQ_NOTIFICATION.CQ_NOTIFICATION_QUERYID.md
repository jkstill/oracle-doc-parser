---
id: 19c__DBMS_CQ_NOTIFICATION.CQ_NOTIFICATION_QUERYID
name: DBMS_CQ_NOTIFICATION.CQ_NOTIFICATION_QUERYID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CQ_NOTIFICATION
tags: [dbms_cq_notification]
source_file: DBMS_CQ_NOTIFICATION.html
---

# DBMS_CQ_NOTIFICATION.CQ_NOTIFICATION_QUERYID

This function returns the queryid of the most recent query that was attempted to be registered in a registration block.

## Syntax

```sql
DBMS_CQ_NOTIFICATION.CQ_NOTIFICATION_QUERYID
 RETURN NUMBER;
```

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_CQ_NOTIFICATION.CQ_NOTIFICATION_QUERYID RETURN NUMBER; Return Values Returns the queryid of the most recently registered query.