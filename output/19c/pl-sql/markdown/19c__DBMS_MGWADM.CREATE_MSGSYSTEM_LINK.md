---
id: 19c__DBMS_MGWADM.CREATE_MSGSYSTEM_LINK
name: DBMS_MGWADM.CREATE_MSGSYSTEM_LINK
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.CREATE_MSGSYSTEM_LINK

This procedure creates a messaging system link to a WebSphere MQ messaging system.

## Syntax

```sql
DBMS_MGWADM.CREATE_MSGSYSTEM_LINK(
   linkname    IN VARCHAR2,
   properties  IN SYS.MGW_MQSERIES_PROPERTIES,
   options     IN SYS.MGW_PROPERTIES DEFAULT NULL,
   comment     IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| linkname | VARCHAR2 | IN | A user-defined name to identify the messaging system link |
| properties | SYS.MGW_MQSERIES_PROPERTIES | IN | Basic properties of a WebSphere MQ messaging system link |
| options | SYS.MGW_PROPERTIES | IN | Optional link properties. NULL if there are none. These are less frequently used configuration properties supported by the messaging system. |
| comment | VARCHAR2 | IN | A user-specified description. NULL if one is not desired |
| agent_name |  |  | Specifies the Messaging Gateway agent that will be used to process all propagation jobs associated with this link. DBMS_MGWADM . DEFAULT_AGENT specifies the default agent. |

## Usage Notes

Syntax DBMS_MGWADM.CREATE_MSGSYSTEM_LINK( linkname IN VARCHAR2, properties IN SYS.MGW_MQSERIES_PROPERTIES, options IN SYS.MGW_PROPERTIES DEFAULT NULL, comment IN VARCHAR2 DEFAULT NULL); DBMS_MGWADM.CREATE_MSGSYSTEM_LINK( linkname IN VARCHAR2, agent_name IN VARCHAR2, properties IN SYS.MGW_MQSERIES_PROPERTIES, options IN SYS.MGW_PROPERTIES DEFAULT NULL, comment IN VARCHAR2 DEFAULT NULL); Parameters Table 110-31 CREATE_MSGSYSTEM_LINK Procedure Parameters for WebSphere MQ Parameter Description linkname A user-defined name to identify the messaging system link properties Basic properties of a WebSphere MQ messaging system link options Optional link properties. NULL if there are none. These are less frequently used configuration properties supported by the messaging system. comment A user-specified description. NULL if one is not desired agent_name Specifies the Messaging Gateway agent that will be used to process all propagation jobs associated with this link. DBMS_MGWADM . DEFAULT_AGENT specifies the default agent. Usage Notes The Messaging Gateway default agent will process the propagation jobs associated with this link if an agent name is not specified. See Also: "WebSphere MQ System Properties" in Oracle Database Advanced Queuing User's Guide for more information about the messaging system properties and options See Also: "WebSphere MQ System Properties" in Oracle Database Advanced Queuing User's Guide for more information about the messaging system properties and options