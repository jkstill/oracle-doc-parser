---
id: 19c__DBMS_MGWADM.REMOVE_MSGSYSTEM_LINK
name: DBMS_MGWADM.REMOVE_MSGSYSTEM_LINK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.REMOVE_MSGSYSTEM_LINK

This procedure removes a messaging system link for a non-Oracle messaging system.

## Syntax

```sql
DBMS_MGWADM.REMOVE_MSGSYSTEM_LINK(
   linkname  IN VARCHAR2);
```

## Usage Notes

Syntax DBMS_MGWADM.REMOVE_MSGSYSTEM_LINK( linkname IN VARCHAR2); Parameters Table 110-40 REMOVE_MSGSYSTEM_LINK Procedure Parameters Parameters Description linkname The messaging system link name Usage Notes All registered queues associated with this link must be removed before the messaging system link can be removed. This procedure fails if there is a registered foreign (non-Oracle) queue that references this link.