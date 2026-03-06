---
id: 19c__DBMS_AQADM.ADD_SUBSCRIBER
name: DBMS_AQADM.ADD_SUBSCRIBER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.ADD_SUBSCRIBER

This procedure adds a default subscriber to a queue.

## Syntax

```sql
DBMS_AQADM.ADD_SUBSCRIBER (
   queue_name      IN    VARCHAR2,
   subscriber      IN    sys.aq$_agent,
   rule            IN    VARCHAR2 DEFAULT NULL,
   transformation  IN    VARCHAR2 DEFAULT NULL
   queue_to_queue  IN    BOOLEAN DEFAULT FALSE,
   delivery_mode   IN    PLS_INTEGER DEFAULT DBMS_AQADM.PERSISTENT);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | Name of the queue. |
| subscriber | sys.aq$_agent | IN | Agent on whose behalf the subscription is being defined. |
| rule | VARCHAR2 | IN | A conditional expression based on the message properties, the message data properties and PL/SQL functions. A rule is specified as a Boolean expression using syntax similar to the WHERE clause of a SQL query. This Boolean expression can include conditions on message properties, user data properties (object payloads only), and PL/SQL or SQL functions (as specified in the where clause of a SQL query). Currently supported message properties are priority and corrid . To specify rules on a message payload (object payload), use attributes of the object type in clauses. You must prefix each attribute with tab . user_data as a qualifier to indicate the specific column of the queue table that stores the payload. The rule parameter cannot exceed 4000 characters. |
| transformation | VARCHAR2 | IN | Specifies a transformation that will be applied when this subscriber dequeues the message. The source type of the transformation must match the type of the queue. If the subscriber is remote, then the transformation is applied before propagation to the remote queue. |
| queue_to_queue | BOOLEAN | IN | If TRUE , propagation is from queue-to-queue. |
| delivery_mode | PLS_INTEGER | IN | The administrator may specify one of DBMS_AQADM . PERSISTENT , DBMS_AQADM . BUFFERED , or DBMS_AQADM . PERSISTENT_OR_BUFFERED for the delivery mode of the messages the subscriber is interested in. This parameter will not be modifiable by ALTER_SUBSCRIBER . |

## Usage Notes

Syntax DBMS_AQADM.ADD_SUBSCRIBER ( queue_name IN VARCHAR2, subscriber IN sys.aq$_agent, rule IN VARCHAR2 DEFAULT NULL, transformation IN VARCHAR2 DEFAULT NULL queue_to_queue IN BOOLEAN DEFAULT FALSE, delivery_mode IN PLS_INTEGER DEFAULT DBMS_AQADM.PERSISTENT); Parameters Table 23-12 ADD_SUBSCRIBER Procedure Parameters Parameter Description queue_name Name of the queue. subscriber Agent on whose behalf the subscription is being defined. rule A conditional expression based on the message properties, the message data properties and PL/SQL functions. A rule is specified as a Boolean expression using syntax similar to the WHERE clause of a SQL query. This Boolean expression can include conditions on message properties, user data properties (object payloads only), and PL/SQL or SQL functions (as specified in the where clause of a SQL query). Currently supported message properties are priority and corrid . To specify rules on a message payload (object payload), use attributes of the object type in clauses. You must prefix each attribute with tab . user_data as a qualifier to indicate the specific column of the queue table that stores the payload. The rule parameter cannot exceed 4000 characters. transformation Specifies a transformation that will be applied when this subscriber dequeues the message. The source type of the transformation must match the type of the queue. If the subscriber is remote, then the transformation is applied before propagation to the remote queue. queue_to_queue If TRUE , propagation is from queue-to-queue. delivery_mode The administrator may specify one of DBMS_AQADM . PERSISTENT , DBMS_AQADM . BUFFERED , or DBMS_AQADM . PERSISTENT_OR_BUFFERED for the delivery mode of the messages the subscriber is interested in. This parameter will not be modifiable by ALTER_SUBSCRIBER . Usage Notes A program can enqueue messages to a specific list of recipients or to the default list of subscribers. This operation only succeeds on queues that allow multiple consumers. This operation takes effect immediately, and the containing transaction is committed. Enqueue requests that are executed after the completion of this call will reflect the new behavior. Any string within the rule must be quoted: rule => 'PRIORITY <= 3 AND CORRID = ''FROM JAPAN''' Note that these are all single quotation marks.