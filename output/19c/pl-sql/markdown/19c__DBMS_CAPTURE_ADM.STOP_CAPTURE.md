---
id: 19c__DBMS_CAPTURE_ADM.STOP_CAPTURE
name: DBMS_CAPTURE_ADM.STOP_CAPTURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CAPTURE_ADM
tags: [dbms_capture_adm]
source_file: DBMS_CAPTURE_ADM.html
---

# DBMS_CAPTURE_ADM.STOP_CAPTURE

This procedure stops the capture process from mining redo logs.

## Syntax

```sql
DBMS_CAPTURE_ADM.STOP_CAPTURE(
   capture_name  IN  VARCHAR2,
   force         IN  BOOLEAN  DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| capture_name | VARCHAR2 | IN | The name of the capture process. A NULL setting is not allowed. Do not specify an owner. |
| force | BOOLEAN | IN | If TRUE , then the procedure stops the capture process as soon as possible. If the capture process cannot stop normally, then it aborts. If FALSE , then the procedure stops the capture process as soon as possible. If the capture process cannot stop normally, then an ORA-26672 error is returned, and the capture process might continue to run. |

## Usage Notes

Syntax DBMS_CAPTURE_ADM.STOP_CAPTURE( capture_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 35-22 STOP_CAPTURE Procedure Parameters Parameter Description capture_name The name of the capture process. A NULL setting is not allowed. Do not specify an owner. force If TRUE , then the procedure stops the capture process as soon as possible. If the capture process cannot stop normally, then it aborts. If FALSE , then the procedure stops the capture process as soon as possible. If the capture process cannot stop normally, then an ORA-26672 error is returned, and the capture process might continue to run. Usage Notes The following usage notes apply to this procedure: The capture process status is persistently recorded. Hence, if the status is DISABLED or ABORTED , then the capture process is not started upon database instance startup. A capture process is an Oracle background process with a name in the form CP nn , where nn can include letters and numbers. The enqueue and dequeue state of DBMS_AQADM.START_QUEUE and DBMS_AQADM.STOP_QUEUE have no effect on the stop status of a capture process.