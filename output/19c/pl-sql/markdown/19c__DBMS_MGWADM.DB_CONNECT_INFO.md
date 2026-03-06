---
id: 19c__DBMS_MGWADM.DB_CONNECT_INFO
name: DBMS_MGWADM.DB_CONNECT_INFO
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.DB_CONNECT_INFO

This deprecated procedure configures connection information used by the Messaging Gateway default agent for connections to Oracle Database.

## Syntax

```sql
DBMS_MGWADM.DB_CONNECT_INFO (
   username      IN VARCHAR2,
   password      IN VARCHAR2,
   database      IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| username | VARCHAR2 | IN | The username used for connections to Oracle Database. NULL is not allowed |
| password | VARCHAR2 | IN | The password used for connections to Oracle Database. NULL is not allowed |
| database | VARCHAR2 | IN | The database connect string used by the Messaging Gateway agent. NULL indicates that a local connection should be used. Oracle strongly recommends that a not NULL value be specified. Usually it will be a net service name from tnsnames.ora . |

## Usage Notes

Note: This subprogram has been deprecated as a result of improved technology (see ALTER_AGENT Procedures ), and is retained only for reasons of backward compatibility. Note: This subprogram has been deprecated as a result of improved technology (see ALTER_AGENT Procedures ), and is retained only for reasons of backward compatibility. Syntax DBMS_MGWADM.DB_CONNECT_INFO ( username IN VARCHAR2, password IN VARCHAR2, database IN VARCHAR2 DEFAULT NULL); Parameters Table 110-32 DB_CONNECT_INFO Procedure Parameters Parameter Description username The username used for connections to Oracle Database. NULL is not allowed password The password used for connections to Oracle Database. NULL is not allowed database The database connect string used by the Messaging Gateway agent. NULL indicates that a local connection should be used. Oracle strongly recommends that a not NULL value be specified. Usually it will be a net service name from tnsnames.ora . Usage Notes The Messaging Gateway agent connects to Oracle Database as the user configured by this procedure. An Oracle administrator should create the user, grant it the role MGW_AGENT_ROLE, and then call this procedure to configure Messaging Gateway. Role MGW_AGENT_ROLE is used to grant this user special privileges needed to access Messaging Gateway configuration information stored in the database, enqueue or dequeue messages to and from Oracle Database Advanced Queuing queues, and perform certain Oracle Database Advanced Queuing administration tasks.