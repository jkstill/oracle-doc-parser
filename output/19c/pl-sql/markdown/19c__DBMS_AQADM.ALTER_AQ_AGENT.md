---
id: 19c__DBMS_AQADM.ALTER_AQ_AGENT
name: DBMS_AQADM.ALTER_AQ_AGENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.ALTER_AQ_AGENT

This procedure alters an agent registered for Oracle Database Advanced Queuing Internet access. It is also used to alter an Oracle Database Advanced Queuing agent that accesses secure queues.

## Syntax

```sql
DBMS_AQADM.ALTER_AQ_AGENT (
  agent_name                IN VARCHAR2,
  certificate_location      IN VARCHAR2 DEFAULT NULL,
  enable_http               IN BOOLEAN DEFAULT FALSE,
  enable_smtp               IN BOOLEAN DEFAULT FALSE,
  enable_anyp               IN BOOLEAN DEFAULT FALSE )
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| agent_name | VARCHAR2 | IN | Specifies the username of the Oracle Database Advanced Queuing Internet agent. |
| certification_location |  |  | Agent's certificate location in LDAP (default is NULL ). If the agent is allowed to access Oracle Database Advanced Queuing through SMTP, then its certificate must be registered in LDAP. For access through HTTP, the certificate location is not required. |
| enable_http | BOOLEAN | IN | TRUE means the agent can access Oracle Database Advanced Queuing through HTTP. FALSE means the agent cannot access Oracle Database Advanced Queuing through HTTP. |
| enable_smtp | BOOLEAN | IN | TRUE means the agent can access Oracle Database Advanced Queuing through SMTP (e-mail). FALSE means the agent cannot access Oracle Database Advanced Queuing through SMTP. |
| enable_anyp | BOOLEAN | IN | TRUE means the agent can access Oracle Database Advanced Queuing through any protocol (HTTP or SMTP). |

## Usage Notes

Syntax DBMS_AQADM.ALTER_AQ_AGENT ( agent_name IN VARCHAR2, certificate_location IN VARCHAR2 DEFAULT NULL, enable_http IN BOOLEAN DEFAULT FALSE, enable_smtp IN BOOLEAN DEFAULT FALSE, enable_anyp IN BOOLEAN DEFAULT FALSE ) Parameters Table 23-13 ALTER_AQ_AGENT Procedure Parameters Parameter Description agent_name Specifies the username of the Oracle Database Advanced Queuing Internet agent. certification_location Agent's certificate location in LDAP (default is NULL ). If the agent is allowed to access Oracle Database Advanced Queuing through SMTP, then its certificate must be registered in LDAP. For access through HTTP, the certificate location is not required. enable_http TRUE means the agent can access Oracle Database Advanced Queuing through HTTP. FALSE means the agent cannot access Oracle Database Advanced Queuing through HTTP. enable_smtp TRUE means the agent can access Oracle Database Advanced Queuing through SMTP (e-mail). FALSE means the agent cannot access Oracle Database Advanced Queuing through SMTP. enable_anyp TRUE means the agent can access Oracle Database Advanced Queuing through any protocol (HTTP or SMTP).