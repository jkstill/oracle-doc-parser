---
id: 19c__DBMS_AQADM.REVOKE_QUEUE_PRIVILEGE
name: DBMS_AQADM.REVOKE_QUEUE_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.REVOKE_QUEUE_PRIVILEGE

This procedure revokes privileges on a queue from users and roles. The privileges are ENQUEUE or DEQUEUE .

## Syntax

```sql
DBMS_AQADM.REVOKE_QUEUE_PRIVILEGE (
   privilege         IN      VARCHAR2,
   queue_name        IN      VARCHAR2,
   grantee           IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| privilege | VARCHAR2 | IN | The Oracle Database Advanced Queuing queue privilege to revoke. The options are ENQUEUE , DEQUEUE , and ALL . ALL means both ENQUEUE and DEQUEUE . |
| queue_name | VARCHAR2 | IN | Name of the queue. |
| grantee | VARCHAR2) | IN | Grantee(s). The grantee(s) can be a user, a role, or the PUBLIC role. If the privilege has been propagated by the grantee through the GRANT option, then the propagated privilege is also revoked. |

## Usage Notes

Syntax DBMS_AQADM.REVOKE_QUEUE_PRIVILEGE ( privilege IN VARCHAR2, queue_name IN VARCHAR2, grantee IN VARCHAR2); Parameters Table 23-47 REVOKE_QUEUE_PRIVILEGE Procedure Parameters Parameter Description privilege The Oracle Database Advanced Queuing queue privilege to revoke. The options are ENQUEUE , DEQUEUE , and ALL . ALL means both ENQUEUE and DEQUEUE . queue_name Name of the queue. grantee Grantee(s). The grantee(s) can be a user, a role, or the PUBLIC role. If the privilege has been propagated by the grantee through the GRANT option, then the propagated privilege is also revoked. Usage Notes To revoke a privilege, the revoker must be the original grantor of the privilege. The privileges propagated through the GRANT option are revoked if the grantor's privileges are revoked.