---
id: 19c__DBMS_MGWADM.ALTER_MSGSYSTEM_LINK
name: DBMS_MGWADM.ALTER_MSGSYSTEM_LINK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.ALTER_MSGSYSTEM_LINK

This procedure alters the properties of a WebSphere MQ messaging system link.

## Syntax

```sql
DBMS_MGWADM.ALTER_MSGSYSTEM_LINK (
   linkname   IN  VARCHAR2,
   properties IN  SYS.MGW_MQSERIES_PROPERTIES,
   options    IN  SYS.MGW_PROPERTIES DEFAULT NULL,
   comment    IN  VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE);
```

## Usage Notes

Syntax DBMS_MGWADM.ALTER_MSGSYSTEM_LINK ( linkname IN VARCHAR2, properties IN SYS.MGW_MQSERIES_PROPERTIES, options IN SYS.MGW_PROPERTIES DEFAULT NULL, comment IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE); Parameters Table 110-24 ALTER_MSGSYSTEM_LINK Procedure Parameters for WebSphere MQ Parameters Description linkname The messaging system link name properties Basic properties for a WebSphere MQ messaging system link. If it is NULL , then no link properties are changed. options Optional link properties. NULL if no options are changed. If not NULL , then the properties specified in this list are combined with the current options properties to form a new set of link options. comment An optional description or NULL if not desired. If DBMS_MGWADM.NO_CHANGE is specified, then the current value is not changed. Usage Notes To retain an existing value for a messaging link property with a VARCHAR2 datatype, specify DBMS_MGWADM.NO_CHANGE for that particular property. To preserve an existing value for a property of another datatype, specify NULL for that property. The options parameter specifies a set of properties used to alter the current optional properties. Each property affects the current property list in a particular manner: add a new property, replace an existing property, remove an existing property, or remove all properties. See Also: SYS.MGW_PROPERTIES Object Type Some properties cannot be modified, and this procedure will fail if an attempt is made to alter such a property. For properties and options that can be changed, a few are dynamic, and Messaging Gateway uses the new values immediately. Others require the Messaging Gateway agent to be shut down and restarted before they take effect. See Also: "WebSphere MQ System Properties" in Oracle Database Advanced Queuing User's Guide for more information about the messaging system properties and options See Also: SYS.MGW_PROPERTIES Object Type See Also: "WebSphere MQ System Properties" in Oracle Database Advanced Queuing User's Guide for more information about the messaging system properties and options