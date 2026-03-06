---
id: 19c__DBMS_MGWADM
name: DBMS_MGWADM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM

The DBMS_MGWADM package defines several OBJECT types.

## Syntax

```sql
TYPE SYS.MGW_MQSERIES_PROPERTIES IS OBJECT (
   queue_manager       VARCHAR2(64),
   hostname            VARCHAR2(64),
   port                INTEGER,
   channel             VARCHAR2(64),
   interface_type      INTEGER,
   username            VARCHAR2(64),
   password            VARCHAR2(64),
   inbound_log_queue   VARCHAR2(64),
   outbound_log_queue  VARCHAR2(64),

-- Methods 
STATIC FUNCTION construct 
RETURN SYS.MGW_MQSERIES_PROPERTIES,

STATIC FUNCTION alter_construct 
RETURN SYS.MGW_MQSERIES_PROPERTIES );
```

**Returns:** `SYS.MGW_MQSERIES_PROPERTIES`

## Usage Notes

DBMS_MGWADM Object Types SYS.MGW_MQSERIES_PROPERTIES Object Type SYS.MGW_PROPERTIES Object Type SYS.MGW_PROPERTY Object Type SYS.MGW_TIBRV_PROPERTIES Object Type Syntax TYPE SYS.MGW_MQSERIES_PROPERTIES IS OBJECT ( queue_manager VARCHAR2(64), hostname VARCHAR2(64), port INTEGER, channel VARCHAR2(64), interface_type INTEGER, username VARCHAR2(64), password VARCHAR2(64), inbound_log_queue VARCHAR2(64), outbound_log_queue VARCHAR2(64), -- Methods STATIC FUNCTION construct RETURN SYS.MGW_MQSERIES_PROPERTIES, STATIC FUNCTION alter_construct RETURN SYS.MGW_MQSERIES_PROPERTIES ); Attributes Table 110-12 SYS.MGW_MQSERIES_PROPERTIES Attributes Attribute Description queue_manager The name of the WebSphere MQ queue manager hostname The host on which the WebSphere MQ messaging system resides. If hostname is NULL, then a WebSphere MQ bindings connection is used. If not NULL , then a client connection is used and requires that a port and channel be specified. port The port number. This is used only for client connections; that is, when hostname is not NULL . channel The channel used when establishing a connection to the queue manager. This is used only for client connections; that is, when hostname is not NULL . interface_type The type of messaging interface to use. Values: DBMS_MGWADM.MQSERIES_BASE_JAVA_INTERFACE if the WebSphere MQ Base Java interface should be used. DBMS_MGWADM.JMS_CONNECTION if the link is to be used to access JMS destinations in a unified, domain-independent manner. DBMS_MGWADM.JMS_QUEUE_CONNECTION if the link is to be used for accessing JMS queues DBMS_MGWADM.JMS_TOPIC_CONNECTION if the link is to be used for accessing JMS topics. username The username used for authentication to the WebSphere MQ messaging system password The password used for authentication to the WebSphere MQ messaging system inbound_log_queue The name of the WebSphere MQ queue used for propagation recovery purposes when this messaging link is used for inbound propagation; that is, when queues associated with this link serve as a propagation source: For MQSERIES_BASE_JAVA_INTERFACE , this is the name of a physical WebSphere MQ queue created using WebSphere MQ administration tools. For the JMS_CONNECTION interface and the JMS_QUEUE_CONNECTION interface, this is the name of a physical WebSphere MQ queue created using WebSphere MQ administration tools. For JMS_TOPIC_CONNECTION interface, this specifies the name of a WebSphere MQ JMS topic. The physical WebSphere MQ queue used by subscribers of that topic must be created using WebSphere MQ administration tools. By default, the physical queue used is SYSTEM.JMS.D.SUBSCRIBER.QUEUE . outbound_log_queue The name of the WebSphere MQ queue used for propagation recovery purposes when this messaging link is used for outbound propagation; that is, when queues associated with this link serve as a propagation destination: For MQSERIES_BASE_JAVA_INTERFACE , this is the name of a physical WebSphere MQ queue created using WebSphere MQ administration tools. For the JMS_CONNECTION interface and the JMS_QUEUE_CONNECTION interface, this is the name of a physical WebSphere MQ queue created using WebSphere MQ administration tools. For JMS_TOPIC_CONNECTION interface, this specifies the name of a WebSphere MQ JMS topic. The physical WebSphere MQ queue used by subscribers of that topic must be created using WebSphere MQ administration tools. By default, the physical queue used is SYSTEM.JMS.D.SUBSCRIBER.QUEUE . Methods Table 110-13 SYS.MGW_MQSERIES_PROPERTIES Methods Method Description construct Constructs a new SYS.MGW_MQSERIES_PROPERTIES instance. All attributes are assigned a value of NULL alter_construct Constructs a new SYS . MGW_MQSERIES_PROPERTIES instance for altering the properties of an existing messaging link. All attributes having a VARCHAR2 datatype are assigned a value of DBMS_MGWADM . NO_CHANGE . Attributes of other datatypes are assigned a value of NULL . Syntax TYPE SYS.MGW_PROPERTIES AS VARRAY (2000) OF SYS.MGW_PROPERTY;