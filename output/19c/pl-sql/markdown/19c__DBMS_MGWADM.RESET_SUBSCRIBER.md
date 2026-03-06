---
id: 19c__DBMS_MGWADM.RESET_SUBSCRIBER
name: DBMS_MGWADM.RESET_SUBSCRIBER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.RESET_SUBSCRIBER

This procedure resets the propagation error state for a subscriber.

## Syntax

```sql
DBMS_MGWADM.RESET_SUBSCRIBER (
   subscriber_id  IN VARCHAR2 );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| subscriber_id | VARCHAR2 | IN | Identifies the subscriber |

## Usage Notes

Note: This subprogram has been deprecated as a result of improved technology (see RESET_JOB Procedure ), and is retained only for reasons of backward compatibility. Note: This subprogram has been deprecated as a result of improved technology (see RESET_JOB Procedure ), and is retained only for reasons of backward compatibility. Syntax DBMS_MGWADM.RESET_SUBSCRIBER ( subscriber_id IN VARCHAR2 ); Parameters Table 110-44 RESET_SUBSCRIBER Procedure Parameters Parameter Description subscriber_id Identifies the subscriber