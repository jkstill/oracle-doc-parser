---
id: 19c__DBMS_SCHEDULER.CREATE_DATABASE_DESTINATION
name: DBMS_SCHEDULER.CREATE_DATABASE_DESTINATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.CREATE_DATABASE_DESTINATION

This procedure creates a database destination. A database destination represents an Oracle database on which remote database jobs run.

## Syntax

```sql
DBMS_SCHEDULER.CREATE_DATABASE_DESTINATION (
   destination_name        IN VARCHAR2,
   agent                   IN VARCHAR2,
   tns_name                IN VARCHAR2,
   comments                IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| destination_name | VARCHAR2 | IN | The name to assign to the database destination. It can optionally be prefixed with a schema name. Cannot be NULL . It is converted to uppercase unless enclosed in double quotation marks. |
| agent | VARCHAR2 | IN | The external destination name of the Scheduler agent to connect. Equivalent to an agent name. The external destination must already exist. The external destination representing an agent is created automatically on a database instance when the agent registers with that instance. An agent's name is specified in its agent configuration file. If it is not specified, it defaults to the first part (before the first period) of the name of the host it resides on. |
| tns_name | VARCHAR2 | IN | An Oracle Net connect identifier that is resolved to the Oracle database instance being connected to. The exact syntax depends on the Oracle Net configuration.The connect identifier can be a complete Oracle Net connect descriptor (network address and database service name) or a net service name , which is an alias for a connect descriptor. The alias must be resolved in the tnsnames.ora file on the local computer. The maximum size for tns_name is 2000 characters. If tns_name is NULL , the agent connects to the default Oracle database on its host. You specify the default database by assigning values to the ORACLE_HOME and ORACLE_SID parameters in the agent configuration file, schagent.conf, located in the agent home directory. See Oracle Database Net Services Administrator's Guide for more information on connect identifiers. |
| comments | VARCHAR2 | IN | A text string that describes the database destination. Scheduler does not use this argument. |

## Usage Notes

The host that the remote database resides on must have a running Scheduler agent that is registered with the database that this procedure is called from. Syntax DBMS_SCHEDULER.CREATE_DATABASE_DESTINATION ( destination_name IN VARCHAR2, agent IN VARCHAR2, tns_name IN VARCHAR2, comments IN VARCHAR2 DEFAULT NULL); Parameters Table 151-23 CREATE_DATABASE_DESTINATION Procedure Parameters Parameter Description destination_name The name to assign to the database destination. It can optionally be prefixed with a schema name. Cannot be NULL . It is converted to uppercase unless enclosed in double quotation marks. agent The external destination name of the Scheduler agent to connect. Equivalent to an agent name. The external destination must already exist. The external destination representing an agent is created automatically on a database instance when the agent registers with that instance. An agent's name is specified in its agent configuration file. If it is not specified, it defaults to the first part (before the first period) of the name of the host it resides on. tns_name An Oracle Net connect identifier that is resolved to the Oracle database instance being connected to. The exact syntax depends on the Oracle Net configuration.The connect identifier can be a complete Oracle Net connect descriptor (network address and database service name) or a net service name , which is an alias for a connect descriptor. The alias must be resolved in the tnsnames.ora file on the local computer. The maximum size for tns_name is 2000 characters. If tns_name is NULL , the agent connects to the default Oracle database on its host. You specify the default database by assigning values to the ORACLE_HOME and ORACLE_SID parameters in the agent configuration file, schagent.conf, located in the agent home directory. See Oracle Database Net Services Administrator's Guide for more information on connect identifiers. comments A text string that describes the database destination. Scheduler does not use this argument. Usage Notes Database destinations reside in a particular schema and can be created by any user with the CREATE JOB system privilege. To create a database destination in a schema other than your own, you must have the CREATE ANY JOB privilege.