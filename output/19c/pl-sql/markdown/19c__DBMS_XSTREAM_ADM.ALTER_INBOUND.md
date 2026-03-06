---
id: 19c__DBMS_XSTREAM_ADM.ALTER_INBOUND
name: DBMS_XSTREAM_ADM.ALTER_INBOUND
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.ALTER_INBOUND

This procedure modifies an XStream inbound server.

## Syntax

```sql
DBMS_XSTREAM_ADM.ALTER_INBOUND(
   server_name IN VARCHAR2,
   apply_user  IN VARCHAR2  DEFAULT NULL,  
   comment     IN VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| server_name | VARCHAR2 | IN | The name of the inbound server being altered. Specify an existing inbound server. Do not specify an owner. |
| apply_user | VARCHAR2 | IN | The user who applies all DML and DDL changes that satisfy the inbound server rule sets, who runs user-defined apply handlers, and who runs custom rule-based transformations configured for inbound server rules. The client application must attach to the inbound server as the apply user. Specify a user to change the apply user. In this case, the user who invokes the ALTER_INBOUND procedure must be granted the DBA role. Only the SYS user can set the apply_user to SYS . If NULL , then the apply user is not changed. See " CREATE_INBOUND Procedure " for information about the required privileges for an apply user. |
| comment | VARCHAR2 | IN | An optional comment associated with the inbound server. If non- NULL , then the specified comment replaces the existing comment. If NULL , then the existing comment is not changed. |

## Usage Notes

Syntax DBMS_XSTREAM_ADM.ALTER_INBOUND( server_name IN VARCHAR2, apply_user IN VARCHAR2 DEFAULT NULL, comment IN VARCHAR2 DEFAULT NULL); Parameters Table 217-13 ALTER_INBOUND Procedure Parameters Parameter Description server_name The name of the inbound server being altered. Specify an existing inbound server. Do not specify an owner. apply_user The user who applies all DML and DDL changes that satisfy the inbound server rule sets, who runs user-defined apply handlers, and who runs custom rule-based transformations configured for inbound server rules. The client application must attach to the inbound server as the apply user. Specify a user to change the apply user. In this case, the user who invokes the ALTER_INBOUND procedure must be granted the DBA role. Only the SYS user can set the apply_user to SYS . If NULL , then the apply user is not changed. See " CREATE_INBOUND Procedure " for information about the required privileges for an apply user. comment An optional comment associated with the inbound server. If non- NULL , then the specified comment replaces the existing comment. If NULL , then the existing comment is not changed.