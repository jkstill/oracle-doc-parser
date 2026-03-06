---
id: 19c__DBMS_AQADM.ALTER_SUBSCRIBER
name: DBMS_AQADM.ALTER_SUBSCRIBER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.ALTER_SUBSCRIBER

This procedure alters existing properties of a subscriber to a specified queue. Only the rule can be altered.

## Syntax

```sql
DBMS_AQADM.ALTER_SUBSCRIBER (
   queue_name     IN    VARCHAR2,
   subscriber     IN    sys.aq$_agent,
   rule           IN    VARCHAR2
   transformation IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | Name of the queue. |
| subscriber | sys.aq$_agent | IN | Agent on whose behalf the subscription is being altered. See " AQ__AGENT Type " . |
| rule | VARCHAR2 | IN | A conditional expression based on the message properties, the message data properties and PL/SQL functions. The rule parameter cannot exceed 4000 characters. To eliminate the rule, set the rule parameter to NULL . |
| transformation | VARCHAR2) | IN | Specifies a transformation that will be applied when this subscriber dequeues the message. The source type of the transformation must match the type of the queue. If the subscriber is remote, then the transformation is applied before propagation to the remote queue. |

## Usage Notes

Syntax DBMS_AQADM.ALTER_SUBSCRIBER ( queue_name IN VARCHAR2, subscriber IN sys.aq$_agent, rule IN VARCHAR2 transformation IN VARCHAR2); Parameters Table 23-18 ALTER_SUBSCRIBER Procedure Parameters Parameter Description queue_name Name of the queue. subscriber Agent on whose behalf the subscription is being altered. See " AQ__AGENT Type " . rule A conditional expression based on the message properties, the message data properties and PL/SQL functions. The rule parameter cannot exceed 4000 characters. To eliminate the rule, set the rule parameter to NULL . transformation Specifies a transformation that will be applied when this subscriber dequeues the message. The source type of the transformation must match the type of the queue. If the subscriber is remote, then the transformation is applied before propagation to the remote queue. Usage Notes This procedure alters both the rule and the transformation for the subscriber. If you want to retain the existing value for either of them, you must specify its old value. The current values for rule and transformation for a subscriber can be obtained from the schema .AQ$ queue_table _R and schema .AQ$ queue_table _S views.