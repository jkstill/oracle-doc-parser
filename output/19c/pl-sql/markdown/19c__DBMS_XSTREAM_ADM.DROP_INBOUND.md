---
id: 19c__DBMS_XSTREAM_ADM.DROP_INBOUND
name: DBMS_XSTREAM_ADM.DROP_INBOUND
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.DROP_INBOUND

This procedure removes an inbound server configuration.

## Syntax

```sql
DBMS_XSTREAM_ADM.DROP_INBOUND(
   server_name IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| server_name | VARCHAR2) | IN | The name of the inbound server being removed. Specify an existing inbound server. Do not specify an owner. |

## Usage Notes

This procedure always removes the specified inbound server. This procedure also removes the queue for the inbound server if all of the following conditions are met: One call to the CREATE_INBOUND procedure created the queue. The inbound server is the only subscriber to the queue. See Also: " CREATE_INBOUND Procedure " See Also: " CREATE_INBOUND Procedure " Syntax DBMS_XSTREAM_ADM.DROP_INBOUND( server_name IN VARCHAR2); Parameters Table 217-18 DROP_INBOUND Procedure Parameters Parameter Description server_name The name of the inbound server being removed. Specify an existing inbound server. Do not specify an owner.