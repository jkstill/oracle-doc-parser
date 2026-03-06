---
id: 19c__DBA_AQ_AGENT_PRIVS
name: DBA_AQ_AGENT_PRIVS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_AQ_AGENT_PRIVS.html
---

# DBA_AQ_AGENT_PRIVS

DBA_AQ_AGENT_PRIVS displays information about the registered AQ agents that are mapped to all users in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| AGENT_NAME | VARCHAR2(128) | Name of the AQ agent |
| DB_USERNAME | VARCHAR2(128) | Name of the database user that the agent maps to |
| HTTP_ENABLED | VARCHAR2(4) | Indicates whether the agent is allowed to access AQ through HTTP ( YES ) or not ( NO ) |
| SMTP_ENABLED | VARCHAR2(4) | Indicates whether the agent is allowed to access AQ through SMTP ( YES ) or not ( NO ) |

## Usage Notes

Related View USER_AQ_AGENT_PRIVS displays information about the registered AQ agents that are mapped to the current user. This view does not display the DB_USERNAME column. See Also: " USER_AQ_AGENT_PRIVS " See Also: " USER_AQ_AGENT_PRIVS "