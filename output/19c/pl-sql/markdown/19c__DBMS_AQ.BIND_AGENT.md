---
id: 19c__DBMS_AQ.BIND_AGENT
name: DBMS_AQ.BIND_AGENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQ
tags: [dbms_aq]
source_file: DBMS_AQ.html
---

# DBMS_AQ.BIND_AGENT

This procedure creates an entry for an Oracle Database Advanced Queuing agent in the LDAP server.

## Syntax

```sql
DBMS_AQ.BIND_AGENT(
   agent        IN SYS.AQ$_AGENT,
   certificate  IN VARCHAR2 default NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| agent | SYS.AQ$_AGENT | IN | Agent that is to be registered in LDAP server. |
| certificate | VARCHAR2 | IN | Location (LDAP distinguished name) of the "organizationalperson" entry in LDAP whose digital certificate (attribute usercertificate ) is to be used for this agent. Example: "cn=OE, cn=ACME, cn=com" is a distinguished name for a OrganizationalPerson OE whose certificate will be used with the specified agent. |

## Usage Notes

Syntax DBMS_AQ.BIND_AGENT( agent IN SYS.AQ$_AGENT, certificate IN VARCHAR2 default NULL); Parameters Table 22-6 BIND_AGENT Procedure Parameters Parameter Description agent Agent that is to be registered in LDAP server. certificate Location (LDAP distinguished name) of the "organizationalperson" entry in LDAP whose digital certificate (attribute usercertificate ) is to be used for this agent. Example: "cn=OE, cn=ACME, cn=com" is a distinguished name for a OrganizationalPerson OE whose certificate will be used with the specified agent. Usage Notes In the LDAP server, digital certificates are stored as an attribute ( usercertificate ) of the OrganizationalPerson entity. The distinguished name for this OrganizationalPerson must be specified when binding the agent.