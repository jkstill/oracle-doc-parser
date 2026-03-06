---
id: 19c__DBMS_AQADM.GRANT_QUEUE_PRIVILEGE
name: DBMS_AQADM.GRANT_QUEUE_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.GRANT_QUEUE_PRIVILEGE

This procedure grants privileges on a queue to users and roles. The privileges are ENQUEUE or DEQUEUE . Initially, only the queue table owner can use this procedure to grant privileges on the queues.

## Syntax

```sql
DBMS_AQADM.GRANT_QUEUE_PRIVILEGE (
   privilege        IN    VARCHAR2,
   queue_name       IN    VARCHAR2,
   grantee          IN    VARCHAR2,
   grant_option     IN    BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| privilege | VARCHAR2 | IN | The Oracle Database Advanced Queuing queue privilege to grant. The options are ENQUEUE , DEQUEUE , and ALL . ALL means both ENQUEUE and DEQUEUE . |
| queue_name | VARCHAR2 | IN | Name of the queue. |
| grantee | VARCHAR2 | IN | Grantee(s). The grantee(s) can be a user, a role, or the PUBLIC role. |
| grant_option | BOOLEAN | IN | Specifies if the access privilege is granted with the GRANT option or not. If the privilege is granted with the GRANT option, then the grantee is allowed to use this procedure to grant the access privilege to other users or roles, regardless of the ownership of the queue table. The default is FALSE . |

## Usage Notes

Syntax DBMS_AQADM.GRANT_QUEUE_PRIVILEGE ( privilege IN VARCHAR2, queue_name IN VARCHAR2, grantee IN VARCHAR2, grant_option IN BOOLEAN := FALSE); Parameters Table 23-41 GRANT_QUEUE_PRIVILEGE Procedure Parameters Parameter Description privilege The Oracle Database Advanced Queuing queue privilege to grant. The options are ENQUEUE , DEQUEUE , and ALL . ALL means both ENQUEUE and DEQUEUE . queue_name Name of the queue. grantee Grantee(s). The grantee(s) can be a user, a role, or the PUBLIC role. grant_option Specifies if the access privilege is granted with the GRANT option or not. If the privilege is granted with the GRANT option, then the grantee is allowed to use this procedure to grant the access privilege to other users or roles, regardless of the ownership of the queue table. The default is FALSE .