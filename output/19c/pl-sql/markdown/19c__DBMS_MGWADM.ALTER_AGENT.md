---
id: 19c__DBMS_MGWADM.ALTER_AGENT
name: DBMS_MGWADM.ALTER_AGENT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.ALTER_AGENT

This procedure configures Messaging Gateway agent parameters.

## Syntax

```sql
DBMS_MGWADM.ALTER_AGENT (
   max_memory       IN  BINARY_INTEGER DEFAULT NULL,
   max_threads      IN  BINARY_INTEGER DEFAULT NULL,
   service          IN  VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| max_memory | BINARY_INTEGER | IN | The maximum heap size, in MB, used by the Messaging Gateway agent. If it is NULL, then the current value is unchanged. |
| max_threads | BINARY_INTEGER | IN | The number of messaging threads that the Messaging Gateway agent creates. If it is NULL , then the current value is unchanged. The maximum value of max_threads is limited to 128. |
| service | VARCHAR2 | IN | Specifies the database service that the Oracle Scheduler job class used by this agent will have affinity to. In an Oracle RAC environment, this means that the Messaging Gateway agent will run on only those database instances that are assigned to the service. If NULL , the job class used by this agent will be altered to belong to the default service which is mapped to every instance. If DBMS_MGWADM . NO_CHANGE , the current value is unchanged. |
| agent_name |  |  | Identifies the Messaging Gateway agent. DBMS_MGWADM . DEFAULT_AGENT specifies the default agent. |
| username |  |  | Specifies the username used for connections to the Oracle Database. NULL is not allowed. If DBMS_MGWADM . NO_CHANGE , then the current value is unchanged. If a username is specified then a password must also be specified. |
| password |  |  | Specifies the password used for connections to the Oracle Database. NULL is not allowed. If DBMS_MGWADM . NO_CHANGE , then the current value is unchanged. A password must be specified if a username is specified. |
| database |  |  | Specifies the database connect string used for connections to the Oracle Database. NULL indicates that a local connection should be used. If DBMS_MGWADM . NO_CHANGE , then the current value is unchanged.Oracle strongly recommends that a connect string, rather than NULL , be specified. Usually it will be a net service name from tnsnames . ora . |
| conntype |  |  | Specifies the type of connection to the Oracle Database, DBMS_MGWADM . JDBC_OCI or DBMS_MGWADM . JDBC_THIN . If DBMS_MGWADM . NO_CHANGE , then the current value is unchanged |
| initfile |  |  | Specifies a Messaging Gateway initialization file used by this agent. NULL indicates that the default initialization file is used. If a value is specified, it should be the full path name of the file. If DBMS_MGWADM . NO_CHANGE , then the current value is unchanged. |
| comment |  |  | Optional comments for this agent. NULL if a comment is not desired. If DBMS_MGWADM . NO_CHANGE , then the current value is unchanged. |

## Usage Notes

Syntax DBMS_MGWADM.ALTER_AGENT ( max_memory IN BINARY_INTEGER DEFAULT NULL, max_threads IN BINARY_INTEGER DEFAULT NULL, service IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE ); DBMS_MGWADM.ALTER_AGENT ( agent_name IN VARCHAR2, username IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE, password IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE, database IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE, conntype IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE, max_memory IN PLS_INTEGER DEFAULT NULL, max_threads IN PLS_INTEGER DEFAULT NULL, service IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE, initfile IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE, comment IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE ); Parameters Table 110-21 ALTER_AGENT Procedure Parameters Parameter Description max_memory The maximum heap size, in MB, used by the Messaging Gateway agent. If it is NULL, then the current value is unchanged. max_threads The number of messaging threads that the Messaging Gateway agent creates. If it is NULL , then the current value is unchanged. The maximum value of max_threads is limited to 128. service Specifies the database service that the Oracle Scheduler job class used by this agent will have affinity to. In an Oracle RAC environment, this means that the Messaging Gateway agent will run on only those database instances that are assigned to the service. If NULL , the job class used by this agent will be altered to belong to the default service which is mapped to every instance. If DBMS_MGWADM . NO_CHANGE , the current value is unchanged. agent_name Identifies the Messaging Gateway agent. DBMS_MGWADM . DEFAULT_AGENT specifies the default agent. username Specifies the username used for connections to the Oracle Database. NULL is not allowed. If DBMS_MGWADM . NO_CHANGE , then the current value is unchanged. If a username is specified then a password must also be specified. password Specifies the password used for connections to the Oracle Database. NULL is not allowed. If DBMS_MGWADM . NO_CHANGE , then the current value is unchanged. A password must be specified if a username is specified. database Specifies the database connect string used for connections to the Oracle Database. NULL indicates that a local connection should be used. If DBMS_MGWADM . NO_CHANGE , then the current value is unchanged.Oracle strongly recommends that a connect string, rather than NULL , be specified. Usually it will be a net service name from tnsnames . ora . conntype Specifies the type of connection to the Oracle Database, DBMS_MGWADM . JDBC_OCI or DBMS_MGWADM . JDBC_THIN . If DBMS_MGWADM . NO_CHANGE , then the current value is unchanged initfile Specifies a Messaging Gateway initialization file used by this agent. NULL indicates that the default initialization file is used. If a value is specified, it should be the full path name of the file. If DBMS_MGWADM . NO_CHANGE , then the current value is unchanged. comment Optional comments for this agent. NULL if a comment is not desired. If DBMS_MGWADM . NO_CHANGE , then the current value is unchanged. Usage Notes Default values for these configuration parameters are set when the Messaging Gateway agent is installed. Changes to the max_memory and max_threads parameters take effect the next time the Messaging Gateway agent is active. If the Messaging Gateway agent is currently active, then it must be shut down and restarted for the changes to take effect. The service parameter is used to set an Oracle Scheduler job class attribute. The job class is used to create a Scheduler job that starts the Messaging Gateway agent. An Oracle administrator must create the database service. If the value is NULL, the job class will belong to an internal service that is mapped to all instances. The username , password , and database parameters specify connection information used by the Messaging Gateway agent for connections to the Oracle Database. An Oracle administrator should create the user and grant it the role MGW_AGENT_ROLE .