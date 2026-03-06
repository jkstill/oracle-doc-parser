---
id: 19c__DBMS_AQADM.GRANT_SYSTEM_PRIVILEGE
name: DBMS_AQADM.GRANT_SYSTEM_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.GRANT_SYSTEM_PRIVILEGE

This procedure grants Oracle Database Advanced Queuing system privileges to users and roles.

## Syntax

```sql
DBMS_AQADM.GRANT_SYSTEM_PRIVILEGE (
   privilege         IN    VARCHAR2,
   grantee           IN    VARCHAR2,
   admin_option      IN    BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| privilege | VARCHAR2 | IN | The Oracle Database Advanced Queuing system privilege to grant. The options are ENQUEUE_ANY , DEQUEUE_ANY , and MANAGE_ANY . ENQUEUE_ANY means users granted this privilege are allowed to enqueue messages to any queues in the database. DEQUEUE_ANY means users granted this privilege are allowed to dequeue messages from any queues in the database. MANAGE_ANY means users granted this privilege are allowed to run DBMS_AQADM calls on any schemas in the database. Note: Starting from Oracle Database 12 c Release 2, MANAGE_ANY , ENQUEUE_ANY , and DEQUEUE_ANY privileges will not allow access to SYS owned queues by users other than SYS . |
| grantee | VARCHAR2 | IN | Grantee(s). The grantee(s) can be a user, a role, or the PUBLIC role. |
| admin_option | BOOLEAN | IN | Specifies if the system privilege is granted with the ADMIN option or not. If the privilege is granted with the ADMIN option, then the grantee is allowed to use this procedure to grant the system privilege to other users or roles. The default is FALSE . |

## Usage Notes

The privileges are ENQUEUE_ANY , DEQUEUE_ANY , and MANAGE_ANY . Initially, only SYS and SYSTEM can use this procedure successfully. Note: Starting from Oracle Database 12 c Release 2, MANAGE_ANY , ENQUEUE_ANY , and DEQUEUE_ANY privileges will not allow access to SYS owned queues by users other than SYS . Note: Starting from Oracle Database 12 c Release 2, MANAGE_ANY , ENQUEUE_ANY , and DEQUEUE_ANY privileges will not allow access to SYS owned queues by users other than SYS . Syntax DBMS_AQADM.GRANT_SYSTEM_PRIVILEGE ( privilege IN VARCHAR2, grantee IN VARCHAR2, admin_option IN BOOLEAN := FALSE); Parameters Table 23-42 GRANT_SYSTEM_PRIVILEGE Procedure Parameters Parameter Description privilege The Oracle Database Advanced Queuing system privilege to grant. The options are ENQUEUE_ANY , DEQUEUE_ANY , and MANAGE_ANY . ENQUEUE_ANY means users granted this privilege are allowed to enqueue messages to any queues in the database. DEQUEUE_ANY means users granted this privilege are allowed to dequeue messages from any queues in the database. MANAGE_ANY means users granted this privilege are allowed to run DBMS_AQADM calls on any schemas in the database. Note: Starting from Oracle Database 12 c Release 2, MANAGE_ANY , ENQUEUE_ANY , and DEQUEUE_ANY privileges will not allow access to SYS owned queues by users other than SYS . grantee Grantee(s). The grantee(s) can be a user, a role, or the PUBLIC role. admin_option Specifies if the system privilege is granted with the ADMIN option or not. If the privilege is granted with the ADMIN option, then the grantee is allowed to use this procedure to grant the system privilege to other users or roles. The default is FALSE . Note: Starting from Oracle Database 12 c Release 2, MANAGE_ANY , ENQUEUE_ANY , and DEQUEUE_ANY privileges will not allow access to SYS owned queues by users other than SYS .