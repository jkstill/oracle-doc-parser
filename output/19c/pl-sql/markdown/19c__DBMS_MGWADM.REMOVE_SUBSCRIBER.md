---
id: 19c__DBMS_MGWADM.REMOVE_SUBSCRIBER
name: DBMS_MGWADM.REMOVE_SUBSCRIBER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.REMOVE_SUBSCRIBER

This procedure removes a subscriber used to consume messages from a source queue for propagation to a destination.

## Syntax

```sql
DBMS_MGWADM.REMOVE_SUBSCRIBER (
   subscriber_id  IN VARCHAR2,
   force          IN BINARY_INTEGER DEFAULT DBMS_MGWADM.NO_FORCE );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| subscriber_id | VARCHAR2 | IN | Identifies the subscriber to be removed |
| force | BINARY_INTEGER | IN | Specifies whether this procedure should succeed even if Messaging Gateway is not able to perform all cleanup actions pertaining to this subscriber. Values: DBMS_MGWADM . NO_FORCE , DBMS_MGWADM . FORCE NO_FORCE means the subscriber is not removed if Messaging Gateway is unable to clean up successfully (default) FORCE means the subscriber is removed even though all cleanup actions may not be done |

## Usage Notes

Note: This subprogram has been deprecated as a result of improved technology (see REMOVE_JOB Procedure ), and is retained only for reasons of backward compatibility. Note: This subprogram has been deprecated as a result of improved technology (see REMOVE_JOB Procedure ), and is retained only for reasons of backward compatibility. Syntax DBMS_MGWADM.REMOVE_SUBSCRIBER ( subscriber_id IN VARCHAR2, force IN BINARY_INTEGER DEFAULT DBMS_MGWADM.NO_FORCE ); Parameters Table 110-42 REMOVE_SUBSCRIBER Procedure Parameters Parameter Description subscriber_id Identifies the subscriber to be removed force Specifies whether this procedure should succeed even if Messaging Gateway is not able to perform all cleanup actions pertaining to this subscriber. Values: DBMS_MGWADM . NO_FORCE , DBMS_MGWADM . FORCE NO_FORCE means the subscriber is not removed if Messaging Gateway is unable to clean up successfully (default) FORCE means the subscriber is removed even though all cleanup actions may not be done Usage Notes The Messaging Gateway agent uses various resources of Oracle Database and the non-Oracle messaging system for its propagation work. These resources are typically associated with each subscriber and need to be released when the subscriber is no longer needed. Therefore, this procedure should only be called when the Messaging Gateway agent is running and able to access the non-Oracle messaging system associated with this subscriber. For outbound propagation, a local subscriber is removed from the Oracle Database Advanced Queuing queue.