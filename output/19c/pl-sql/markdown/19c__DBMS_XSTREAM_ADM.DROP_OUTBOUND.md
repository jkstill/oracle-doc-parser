---
id: 19c__DBMS_XSTREAM_ADM.DROP_OUTBOUND
name: DBMS_XSTREAM_ADM.DROP_OUTBOUND
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.DROP_OUTBOUND

This procedure removes an outbound server configuration.

## Syntax

```sql
DBMS_XSTREAM_ADM.DROP_OUTBOUND(
   server_name IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| server_name | VARCHAR2) | IN | The name of the outbound server being removed. Specify an existing outbound server. Do not specify an owner. |

## Usage Notes

This procedure always drops the specified outbound server. This procedure also drops the queue used by the outbound server if both of the following conditions are met: The queue was created by the CREATE_OUTBOUND procedure in this package. The outbound server is the only subscriber to the queue. If either one of the preceding conditions is not met, then the DROP_OUTBOUND procedure only drops the outbound server. It does not drop the queue. This procedure also drops the capture process for the outbound server if both of the following conditions are met: The procedure can drop the outbound server's queue. The capture process was created by the CREATE_OUTBOUND procedure. If the procedure can drop the queue but cannot manage the capture process, then it drops the queue without dropping the capture process. See Also: " ADD_OUTBOUND Procedure " " CREATE_OUTBOUND Procedure " See Also: " ADD_OUTBOUND Procedure " " CREATE_OUTBOUND Procedure " Syntax DBMS_XSTREAM_ADM.DROP_OUTBOUND( server_name IN VARCHAR2); Parameters Table 217-19 DROP_OUTBOUND Procedure Parameters Parameter Description server_name The name of the outbound server being removed. Specify an existing outbound server. Do not specify an owner.