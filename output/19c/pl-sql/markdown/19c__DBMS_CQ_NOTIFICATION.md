---
id: 19c__DBMS_CQ_NOTIFICATION
name: DBMS_CQ_NOTIFICATION
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CQ_NOTIFICATION
tags: [dbms_cq_notification]
source_file: DBMS_CQ_NOTIFICATION.html
---

# DBMS_CQ_NOTIFICATION

The DBMS_CQ_NOTIFICATION package defines several OBJECT types.

## Syntax

```sql
TYPE SYS.CHNF$_DESC IS OBJECT(
   registration_id    NUMBER,
   transaction_id     RAW(8),
   dbname             VARCHAR2(30),
   event_type         NUMBER,
   numtables          NUMBER,
   table_desc_array   CQ_NOTIFICATION$_TABLE_ARRAY,
   query_desc_array   CQ_NOTIFICATION$_QUERY_ARRAY);
```

## Usage Notes

OBJECT Types CQ_NOTIFICATION$_DESCRIPTOR Object Type CQ_NOTIFICATION$_QUERY Object Type CQ_NOTIFICATION$_QUERY_ARRAY Object (Array) Type CQ_NOTIFICATION$_TABLE Object Type CQ_NOTIFICATION$_TABLE_ARRAY Object (Array) Type CQ_NOTIFICATION$_ROW Object Type CQ_NOTIFICATION$_ROW_ARRAY Object (Array) Type CQ_NOTIFICATION$_REG_INFO Object Type Syntax TYPE SYS.CHNF$_DESC IS OBJECT( registration_id NUMBER, transaction_id RAW(8), dbname VARCHAR2(30), event_type NUMBER, numtables NUMBER, table_desc_array CQ_NOTIFICATION$_TABLE_ARRAY, query_desc_array CQ_NOTIFICATION$_QUERY_ARRAY); Attributes Table 40-2 CQ_NOTIFICATION$_DESCRIPTOR Object Type Attribute Description registration_id Registration ID returned during registration transaction_id Transaction ID. transaction_id of the transaction that made the change. Will be NULL unless the event_type is EVENT_OBJCHANGE or EVENT_QUERYCHANGE . dbname Name of database event_type Database event associated with the notification. Can be one of EVENT_OBJCHANGE (change to a registered object), EVENT_STARTUP , or EVENT_QUERYCHANGE , EVENT_SHUTDOWN or EVENT_DEREG (registration has been removed due to a timeout or other reason) numtables Number of modified tables. Will be NULL unless the event_type is EVENT_OBJCHANGE . table_desc_array Array of table descriptors. Will be NULL unless the event_type is EVENT_OBJCHANGE . query_desc_array Array of queries changed. This will be NULL unless event_type is EVENT_QUERYCHANGE An array of CQ_NOTIFICATION$_QUERY descriptors is embedded inside the top level notification descriptor ( CQ_NOTIFICATION$_DESCRIPTOR ) for events of type EVENT_QUERYCHANGE . The array corresponds to the SET of queryids which were invalidated as a result of the event. This is a synonym for the base type SYS.CHNF$_QDESC . Syntax TYPE SYS.CHNF$_QDESC IS OBJECT ( queryid NUMBER, queryop NUMBER, table_desc_array CQ_NOTIFICATION$_TABLE_ARRAY);