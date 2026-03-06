---
id: 19c__DBMS_AQADM.ALTER_QUEUE_TABLE
name: DBMS_AQADM.ALTER_QUEUE_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.ALTER_QUEUE_TABLE

This procedure alters the existing properties of a queue table.

## Syntax

```sql
DBMS_AQADM.ALTER_QUEUE_TABLE (
   queue_table          IN   VARCHAR2, 
   comment              IN   VARCHAR2       DEFAULT NULL,
   primary_instance     IN   BINARY_INTEGER DEFAULT NULL, 
   secondary_instance   IN   BINARY_INTEGER DEFAULT NULL,
   replication_mode     IN   BINARY_INTEGER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_table | VARCHAR2 | IN | Name of a queue table to be created. |
| comment | VARCHAR2 | IN | Modifies the user-specified description of the queue table. This user comment is added to the queue catalog. The default value is NULL which means that the value will not be changed. |
| primary_instance | BINARY_INTEGER | IN | This is the primary owner of the queue table. Queue monitor scheduling and propagation for the queues in the queue table will be done in this instance. The default value is NULL , which means that the current value will not be changed. |
| secondary_instance | BINARY_INTEGER | IN | The queue table fails over to the secondary instance if the primary instance is not available. The default value is NULL , which means that the current value will not be changed. |
| replication_mode | BINARY_INTEGER | IN | DBMS_AQADM.REPLICATION_MODE if queue is being altered to be in the Replication Mode. DBMS_AQADM.NONE if queue is being altered to not be replicated. The default value is NULL . |

## Usage Notes

Syntax DBMS_AQADM.ALTER_QUEUE_TABLE ( queue_table IN VARCHAR2, comment IN VARCHAR2 DEFAULT NULL, primary_instance IN BINARY_INTEGER DEFAULT NULL, secondary_instance IN BINARY_INTEGER DEFAULT NULL, replication_mode IN BINARY_INTEGER DEFAULT NULL); Parameters Table 23-16 ALTER_QUEUE_TABLE Procedure Parameters Parameter Description queue_table Name of a queue table to be created. comment Modifies the user-specified description of the queue table. This user comment is added to the queue catalog. The default value is NULL which means that the value will not be changed. primary_instance This is the primary owner of the queue table. Queue monitor scheduling and propagation for the queues in the queue table will be done in this instance. The default value is NULL , which means that the current value will not be changed. secondary_instance The queue table fails over to the secondary instance if the primary instance is not available. The default value is NULL , which means that the current value will not be changed. replication_mode DBMS_AQADM.REPLICATION_MODE if queue is being altered to be in the Replication Mode. DBMS_AQADM.NONE if queue is being altered to not be replicated. The default value is NULL .