---
id: 19c__DBMS_XSTREAM_ADM.STOP_OUTBOUND
name: DBMS_XSTREAM_ADM.STOP_OUTBOUND
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.STOP_OUTBOUND

This procedure stops an XStream outbound server. The outbound server streams out the LCRs to an XStream client application.

## Syntax

```sql
DBMS_XSTREAM_ADM.STOP_OUTBOUND(
   server_name  IN  VARCHAR2,
   force        IN  BOOLEAN   DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| server_name | VARCHAR2 | IN | The name of the outbound server being stopped. A NULL specification is not allowed. Do not specify an owner. |
| force | BOOLEAN | IN | If TRUE , then the procedure stops the outbound server and its capture process as soon as possible. If FALSE , then the procedure stops the outbound server after ensuring that there are no gaps in the set of applied transactions. The behavior of the apply component depends on the setting specified for the force parameter and the setting specified for the commit_serialization apply component parameter. |

## Usage Notes

Syntax DBMS_XSTREAM_ADM.STOP_OUTBOUND( server_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 217-38 STOP_OUTBOUND Procedure Parameters Parameter Description server_name The name of the outbound server being stopped. A NULL specification is not allowed. Do not specify an owner. force If TRUE , then the procedure stops the outbound server and its capture process as soon as possible. If FALSE , then the procedure stops the outbound server after ensuring that there are no gaps in the set of applied transactions. The behavior of the apply component depends on the setting specified for the force parameter and the setting specified for the commit_serialization apply component parameter.