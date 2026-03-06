---
id: 19c__DBMS_AQ.UNBIND_AGENT
name: DBMS_AQ.UNBIND_AGENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQ
tags: [dbms_aq]
source_file: DBMS_AQ.html
---

# DBMS_AQ.UNBIND_AGENT

This procedure removes the entry for an Oracle Database Advanced Queuing agent from the LDAP server.

## Syntax

```sql
DBMS_AQ.UNBIND_AGENT(
   agent    IN SYS.AQ$_AGENT);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| agent | SYS.AQ$_AGENT) | IN | Agent that is to be removed from the LDAP server |

## Usage Notes

Syntax DBMS_AQ.UNBIND_AGENT( agent IN SYS.AQ$_AGENT); Parameters Table 22-14 BIND_AGENT Procedure Parameters Parameter Description agent Agent that is to be removed from the LDAP server