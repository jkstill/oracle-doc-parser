---
id: 19c__DBMS_XSTREAM_ADM.SET_UP_QUEUE
name: DBMS_XSTREAM_ADM.SET_UP_QUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.SET_UP_QUEUE

This procedure creates a queue table and a ANYDATA queue.

## Syntax

```sql
DBMS_XSTREAM_ADM.SET_UP_QUEUE(
   queue_table     IN  VARCHAR2  DEFAULT 'streams_queue_table',
   storage_clause  IN  VARCHAR2  DEFAULT NULL,
   queue_name      IN  VARCHAR2  DEFAULT 'streams_queue',
   queue_user      IN  VARCHAR2  DEFAULT NULL,
   comment         IN  VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_table | VARCHAR2 | IN | The name of the queue table specified as [ schema_name .] queue_table_name . For example, strmadmin.streams_queue_table . If the schema is not specified, then the current user is the default. If the queue table owner is not specified, then the procedure specifies the user who runs this procedure automatically as the queue table owner. Queue table names can be a maximum of 24 bytes. |
| storage_clause | VARCHAR2 | IN | The storage clause for queue table The storage parameter is included in the CREATE TABLE statement when the queue table is created. You can specify any valid table storage clause. If a tablespace is not specified here, then the procedure creates the queue table and all its related objects in the default user tablespace of the user who runs this procedure. If a tablespace is specified here, then the procedure creates the queue table and all its related objects in the tablespace specified in the storage clause. If NULL , then the procedure uses the storage characteristics of the tablespace in which the queue table is created. See Also: Oracle Database SQL Language Reference for more information about storage clauses |
| queue_name | VARCHAR2 | IN | The name of the queue that will function as the ANYDATA queue, specified as [ schema_name .] queue_name . For example, strmadmin.streams_queue . If the schema is not specified, then the procedure uses the queue table owner. The owner of the queue table must also be the owner of the queue. The queue owner automatically has privileges to perform all queue operations on the queue. If the schema is not specified for this parameter, and the queue table owner is not specified in queue_table , then the current user is the default. Queue names can be a maximum of 24 bytes. |
| queue_user | VARCHAR2 | IN | The name of the user who requires ENQUEUE and DEQUEUE privileges for the queue. This user also is configured as a secure queue user of the queue. The queue user cannot grant these privileges to other users because they are not granted with the GRANT option. If NULL , then the procedure does not grant any privileges. You can also grant queue privileges to the appropriate users using the DBMS_AQADM package. |
| comment | VARCHAR2 | IN | The comment for the queue |

## Usage Notes

Syntax DBMS_XSTREAM_ADM.SET_UP_QUEUE( queue_table IN VARCHAR2 DEFAULT 'streams_queue_table', storage_clause IN VARCHAR2 DEFAULT NULL, queue_name IN VARCHAR2 DEFAULT 'streams_queue', queue_user IN VARCHAR2 DEFAULT NULL, comment IN VARCHAR2 DEFAULT NULL); Parameters Table 217-35 SET_UP_QUEUE Procedure Parameters Parameter Description queue_table The name of the queue table specified as [ schema_name .] queue_table_name . For example, strmadmin.streams_queue_table . If the schema is not specified, then the current user is the default. If the queue table owner is not specified, then the procedure specifies the user who runs this procedure automatically as the queue table owner. Queue table names can be a maximum of 24 bytes. storage_clause The storage clause for queue table The storage parameter is included in the CREATE TABLE statement when the queue table is created. You can specify any valid table storage clause. If a tablespace is not specified here, then the procedure creates the queue table and all its related objects in the default user tablespace of the user who runs this procedure. If a tablespace is specified here, then the procedure creates the queue table and all its related objects in the tablespace specified in the storage clause. If NULL , then the procedure uses the storage characteristics of the tablespace in which the queue table is created. See Also: Oracle Database SQL Language Reference for more information about storage clauses queue_name The name of the queue that will function as the ANYDATA queue, specified as [ schema_name .] queue_name . For example, strmadmin.streams_queue . If the schema is not specified, then the procedure uses the queue table owner. The owner of the queue table must also be the owner of the queue. The queue owner automatically has privileges to perform all queue operations on the queue. If the schema is not specified for this parameter, and the queue table owner is not specified in queue_table , then the current user is the default. Queue names can be a maximum of 24 bytes. queue_user The name of the user who requires ENQUEUE and DEQUEUE privileges for the queue. This user also is configured as a secure queue user of the queue. The queue user cannot grant these privileges to other users because they are not granted with the GRANT option. If NULL , then the procedure does not grant any privileges. You can also grant queue privileges to the appropriate users using the DBMS_AQADM package. comment The comment for the queue Usage Notes Set up includes the following actions: If the specified queue table does not exist, then this procedure runs the CREATE_QUEUE_TABLE procedure in the DBMS_AQADM package to create the queue table with the specified storage clause. If this procedure creates the queue table, then it creates a multiple consumer ANYDATA queue that is both a secure queue and a transactional queue. Also, if the database is Oracle Database 10 g release 2 or later, the sort_list setting in CREATE_QUEUE_TABLE is set to commit_time . If the database is a release before Oracle Database 10 g release 2, the sort_list setting in CREATE_QUEUE_TABLE is set to enq_time . If the specified queue table exists, then the queue uses the properties of the existing queue table. If the specified queue name does not exist, then this procedure runs the CREATE_QUEUE procedure in the DBMS_AQADM package to create the queue. This procedure starts the queue. If a queue user is specified, then this procedure configures this user as a secure queue user of the queue and grants ENQUEUE and DEQUEUE privileges on the queue to the specified queue user. To configure the queue user as a secure queue user, this procedure creates an Advanced Queuing agent with the same name as the user name, if one does not exist. If an agent with this name exists and is associated with the queue user only, then it is used. SET_UP_QUEUE then runs the ENABLE_DB_ACCESS procedure in the DBMS_AQADM package, specifying the agent and the user. Note: If the agent that SET_UP_QUEUE tries to create exists and is associated with a user other than the user specified by queue_user , then the procedure raises an error. In this case, rename or remove the existing agent, and retry SET_UP_QUEUE . Note: If the agent that SET_UP_QUEUE tries to create exists and is associated with a user other than the user specified by queue_user , then the procedure raises an error. In this case, rename or remove the existing agent, and retry SET_UP_QUEUE .