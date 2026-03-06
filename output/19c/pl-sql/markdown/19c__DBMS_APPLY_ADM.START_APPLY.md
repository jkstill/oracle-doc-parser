---
id: 19c__DBMS_APPLY_ADM.START_APPLY
name: DBMS_APPLY_ADM.START_APPLY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.START_APPLY

This procedure directs the apply component to start applying messages.

## Syntax

```sql
DBMS_APPLY_ADM.START_APPLY(
   apply_name  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| apply_name | VARCHAR2) | IN | The apply component name. A NULL setting is not allowed. Do not specify an owner. |

## Usage Notes

Syntax DBMS_APPLY_ADM.START_APPLY( apply_name IN VARCHAR2); Parameter Table 21-29 START_APPLY Procedure Parameter Parameter Description apply_name The apply component name. A NULL setting is not allowed. Do not specify an owner. Usage Notes The following usage notes apply to this procedure: Apply Component Status The START_APPLY Procedure and XStream Outbound Servers The START_APPLY Procedure and XStream Inbound Servers Apply Component Status The apply component status is persistently recorded. Hence, if the status is ENABLED , then the apply component is started upon database instance startup. An apply component ( a nnn ) is an Oracle background process. The enqueue and dequeue state of DBMS_AQADM.START_QUEUE and DBMS_AQADM.STOP_QUEUE have no effect on the start status of an apply component. The START_APPLY Procedure and XStream Outbound Servers This procedure functions the same way for apply processes and outbound servers. The START_APPLY Procedure and XStream Inbound Servers This procedure functions the same way for apply processes and inbound servers.