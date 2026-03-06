---
id: 19c__DBMS_AQADM.REVOKE_SYSTEM_PRIVILEGE
name: DBMS_AQADM.REVOKE_SYSTEM_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.REVOKE_SYSTEM_PRIVILEGE

This procedure revokes Oracle Database Advanced Queuing system privileges from users and roles. The privileges are ENQUEUE_ANY , DEQUEUE_ANY and MANAGE_ANY . The ADMIN option for a system privilege cannot be selectively revoked. Starting from Oracle Database 12 c Release 2, MANAGE_ANY , ENQUEUE_ANY , and DEQUEUE_ANY privileges will not allow access to SYS owned queues by users other than SYS .

## Syntax

```sql
DBMS_AQADM.REVOKE_SYSTEM_PRIVILEGE (
   privilege         IN   VARCHAR2,
   grantee           IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| privilege | VARCHAR2 | IN | The Oracle Database Advanced Queuing system privilege to revoke. The options are ENQUEUE_ANY , DEQUEUE_ANY , and MANAGE_ANY . The ADMIN option for a system privilege cannot be selectively revoked. Note: Starting from Oracle Database 12 c Release 2, MANAGE_ANY , ENQUEUE_ANY , and DEQUEUE_ANY privileges will not allow access to SYS owned queues by users other than SYS . |
| grantee | VARCHAR2) | IN | Grantee(s). The grantee(s) can be a user, a role, or the PUBLIC role. |

## Usage Notes

Syntax DBMS_AQADM.REVOKE_SYSTEM_PRIVILEGE ( privilege IN VARCHAR2, grantee IN VARCHAR2); Parameters Table 23-48 REVOKE_SYSTEM_PRIVILEGE Procedure Parameters Parameter Description privilege The Oracle Database Advanced Queuing system privilege to revoke. The options are ENQUEUE_ANY , DEQUEUE_ANY , and MANAGE_ANY . The ADMIN option for a system privilege cannot be selectively revoked. Note: Starting from Oracle Database 12 c Release 2, MANAGE_ANY , ENQUEUE_ANY , and DEQUEUE_ANY privileges will not allow access to SYS owned queues by users other than SYS . grantee Grantee(s). The grantee(s) can be a user, a role, or the PUBLIC role. Note: Starting from Oracle Database 12 c Release 2, MANAGE_ANY , ENQUEUE_ANY , and DEQUEUE_ANY privileges will not allow access to SYS owned queues by users other than SYS .