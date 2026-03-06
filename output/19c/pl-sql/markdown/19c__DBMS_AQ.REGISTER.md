---
id: 19c__DBMS_AQ.REGISTER
name: DBMS_AQ.REGISTER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQ
tags: [dbms_aq]
source_file: DBMS_AQ.html
---

# DBMS_AQ.REGISTER

This procedure registers an e-mail address, user-defined PL/SQL procedure, or HTTP URL for message notification.

## Syntax

```sql
DBMS_AQ.REGISTER (
   reg_list     IN  SYS.AQ$_REG_INFO_LIST,
   count        IN  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| reg_list | SYS.AQ$_REG_INFO_LIST | IN | Specifies the list of subscriptions to which you want to register for message notifications. It is a list of AQ$_REG_INFO Type . |
| count | NUMBER) | IN | Specifies the number of entries in the reg_list . |

## Usage Notes

Syntax DBMS_AQ.REGISTER ( reg_list IN SYS.AQ$_REG_INFO_LIST, count IN NUMBER); Parameters Table 22-13 REGISTER Procedure Parameters Parameter Description reg_list Specifies the list of subscriptions to which you want to register for message notifications. It is a list of AQ$_REG_INFO Type . count Specifies the number of entries in the reg_list . Usage Notes This procedure is used to register for notifications. You can specify an e-mail address to which message notifications are sent, register a procedure to be invoked on a notification, or register an HTTP URL to which the notification is posted. Interest in several subscriptions can be registered at one time. The procedure can also be used to register for grouping notifications using five grouping attributes: Class – grouping criterion (currently only TIME criterion is supported) Value – the value of the grouping criterion (currently only time in seconds for criterion TIME ) Type – summary or last, also contains count of notifications received in group (for AQ namespace only, not for DBCHANGE namespace) Repeat count – how many times to perform grouping (Default is FOREVER ) Start time – when to start grouping (Default is current time) If you register for e-mail notifications, you should set the host name and port name for the SMTP server that will be used by the database to send e-mail notifications. If required, you should set the send-from e-mail address, which is set by the database as the sent from field. You need a Java-enabled database to use this feature. If you register for HTTP notifications, you may want to set the host name and port number for the proxy server and a list of no-proxy domains that will be used by the database to post HTTP notifications. See Also: DBMS_AQELM for more information on e-mail and HTTP notifications See Also: DBMS_AQELM for more information on e-mail and HTTP notifications