---
id: 19c__DBMS_CAPTURE_ADM.START_CAPTURE
name: DBMS_CAPTURE_ADM.START_CAPTURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CAPTURE_ADM
tags: [dbms_capture_adm]
source_file: DBMS_CAPTURE_ADM.html
---

# DBMS_CAPTURE_ADM.START_CAPTURE

This procedure starts the capture process, which mines redo logs and enqueues the mined redo information into the associated queue.

## Syntax

```sql
DBMS_CAPTURE_ADM.START_CAPTURE(
   capture_name  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| capture_name | VARCHAR2) | IN | The name of the capture process. Do not specify an owner. The capture process uses LogMiner to capture changes in the redo information. A NULL setting is not allowed. |

## Usage Notes

The start status is persistently recorded. Hence, if the status is ENABLED , then the capture process is started upon database instance startup. The capture process is a background Oracle process and is prefixed by c . The enqueue and dequeue state of DBMS_AQADM.START_QUEUE and DBMS_AQADM.STOP_QUEUE have no effect on the start status of a capture process. Syntax DBMS_CAPTURE_ADM.START_CAPTURE( capture_name IN VARCHAR2); Parameters Table 35-21 START_CAPTURE Procedure Parameter Parameter Description capture_name The name of the capture process. Do not specify an owner. The capture process uses LogMiner to capture changes in the redo information. A NULL setting is not allowed. Usage Notes The capture process status is persistently recorded. Hence, if the status is ENABLED , then the capture process is started upon database instance startup. A capture process ( c nnn ) is an Oracle background process.