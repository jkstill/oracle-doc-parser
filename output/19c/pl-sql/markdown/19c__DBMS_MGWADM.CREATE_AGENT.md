---
id: 19c__DBMS_MGWADM.CREATE_AGENT
name: DBMS_MGWADM.CREATE_AGENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.CREATE_AGENT

This procedure creates a Messaging Gateway agent that will be used to process propagation jobs.

## Syntax

```sql
DBMS_MGWADM.CREATE_AGENT (
   agent_name     IN   VARCHAR2,
   username       IN   VARCHAR2 DEFAULT NULL,
   password       IN   VARCHAR2 DEFAULT NULL,
   database       IN   VARCHAR2 DEFAULT NULL,
   conntype       IN   VARCHAR2 DEFAULT DBMS_MGWADM.JDBC_OCI,
   max_memory     IN   PLS_INTEGER DEFAULT 64,
   max_threads    IN   PLS_INTEGER DEFAULT 1,
   service        IN   VARCHAR2 DEFAULT NULL,
   initfile       IN   VARCHAR2 DEFAULT NULL,
   comment        IN   VARCHAR2  DEFAULT NULL );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| agent_name | VARCHAR2 | IN | A name used to identify the agent |
| username | VARCHAR2 | IN | Specifies the username used for connections to the Oracle Database |
| password | VARCHAR2 | IN | Specifies the password used for connections to the Oracle Database. A password must be specified if a username is specified. |
| database | VARCHAR2 | IN | Specifies the database connect string used for connections to the Oracle Database. NULL indicates that a local connection should be used. A value can be specified only if username is specified. Oracle strong recommends that a connect string, rather than NULL be specified. Usually it will be a net service name from tnsnames . ora . |
| conntype | VARCHAR2 | IN | Specifies the type of connection to the Oracle Database.Values: DBMS_MGWADM . JDBC_OCI , DBMS_MGWADM . JDBC_THIN |
| max_memory | PLS_INTEGER | IN | Specifies the maximum heap size, in MB, used by the Messaging Gateway agent |
| max_threads | PLS_INTEGER | IN | Specifies the number of messaging threads that the Messaging Gateway agent creates. This determines the number of propagation jobs that the agent can concurrently process. The maximum value of max_threads is limited to 128. |
| service | VARCHAR2 | IN | Specifies the database service that the Oracle Scheduler job class used by this agent will have affinity to. In an Oracle RAC environment, this means that the Messaging Gateway agent will only run on those database instances that are assigned to the service. If NULL, then the job class will belong to the default service which is mapped to every instance. |
| initfile | VARCHAR2 | IN | Specifies a Messaging Gateway initialization file used by this agent. NULL indicates that the default initialization file is used. If a value is specified, it should be the full path name of the file. |
| comment | VARCHAR2 | IN | An optional comment for this agent. NULL if one is not desired. |

## Usage Notes

Syntax DBMS_MGWADM.CREATE_AGENT ( agent_name IN VARCHAR2, username IN VARCHAR2 DEFAULT NULL, password IN VARCHAR2 DEFAULT NULL, database IN VARCHAR2 DEFAULT NULL, conntype IN VARCHAR2 DEFAULT DBMS_MGWADM.JDBC_OCI, max_memory IN PLS_INTEGER DEFAULT 64, max_threads IN PLS_INTEGER DEFAULT 1, service IN VARCHAR2 DEFAULT NULL, initfile IN VARCHAR2 DEFAULT NULL, comment IN VARCHAR2 DEFAULT NULL ); Parameters Table 110-28 CREATE_AGENT Procedure Parameters Parameter Description agent_name A name used to identify the agent username Specifies the username used for connections to the Oracle Database password Specifies the password used for connections to the Oracle Database. A password must be specified if a username is specified. database Specifies the database connect string used for connections to the Oracle Database. NULL indicates that a local connection should be used. A value can be specified only if username is specified. Oracle strong recommends that a connect string, rather than NULL be specified. Usually it will be a net service name from tnsnames . ora . conntype Specifies the type of connection to the Oracle Database.Values: DBMS_MGWADM . JDBC_OCI , DBMS_MGWADM . JDBC_THIN max_memory Specifies the maximum heap size, in MB, used by the Messaging Gateway agent max_threads Specifies the number of messaging threads that the Messaging Gateway agent creates. This determines the number of propagation jobs that the agent can concurrently process. The maximum value of max_threads is limited to 128. service Specifies the database service that the Oracle Scheduler job class used by this agent will have affinity to. In an Oracle RAC environment, this means that the Messaging Gateway agent will only run on those database instances that are assigned to the service. If NULL, then the job class will belong to the default service which is mapped to every instance. initfile Specifies a Messaging Gateway initialization file used by this agent. NULL indicates that the default initialization file is used. If a value is specified, it should be the full path name of the file. comment An optional comment for this agent. NULL if one is not desired. Usage Notes The Messaging Gateway automatically configures a default agent when Messaging Gateway is installed. The name of the default agent is DEFAULT_AGENT . This procedure can be used to create additional agents. The username , password , and database parameters specify connection information used by the Messaging Gateway agent for connections to the Oracle Database. An Oracle administrator should create the database user and grant it the role MGW_AGENT_ROLE . It is not mandatory that the connection information be specified when this procedure is called but it must be set before the agent can be started. The service parameter is used to create an Oracle Scheduler job class. The job class is used to create a Scheduler job that starts the Messaging Gateway agent. An Oracle administrator must create the database service. If the value is NULL , the job class will belong to an internal service that is mapped to all instances.