---
id: 19c__DBMS_XSTREAM_ADM.START_OUTBOUND
name: DBMS_XSTREAM_ADM.START_OUTBOUND
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.START_OUTBOUND

This procedure starts an XStream outbound server. The outbound server streams out the LCRs to an XStream client application.

## Syntax

```sql
DBMS_XSTREAM_ADM.START_OUTBOUND(
   server_name      IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| server_name | VARCHAR2) | IN | The name of the outbound server being started. A NULL specification is not allowed. Do not specify an owner. |

## Usage Notes

Syntax DBMS_XSTREAM_ADM.START_OUTBOUND( server_name IN VARCHAR2); Parameters Table 217-37 START_OUTBOUND Procedure Parameters Parameter Description server_name The name of the outbound server being started. A NULL specification is not allowed. Do not specify an owner.