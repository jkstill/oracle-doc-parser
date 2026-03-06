---
id: 19c__DBMS_XDB.ACLCHECKPRIVILEGES
name: DBMS_XDB.ACLCHECKPRIVILEGES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.ACLCHECKPRIVILEGES

This function checks access privileges granted to the current user by specified ACL document by the OWNER of the resource. Returns positive integer if all privileges are granted.

## Syntax

```sql
DBMS_XDB.ACLCHECKPRIVILEGES(
   acl_path  IN  VARCHAR2,
   owner     IN  VARCHAR2,
   privs     IN  xmltype)
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| acl_path | VARCHAR2 | IN | Absolute path in the Hierarchy for ACL document |
| owner | VARCHAR2 | IN | Resource owner name; the pseudo user "DAV:owner" is replaced by this user during ACL privilege resolution |
| privs | xmltype) | IN | An XMLType instance of the privilege element specifying the requested set of access privileges. See description for CHECKPRIVILEGES Function . |

**Returns:** `PLS_INTEGER`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the ACLCHECKPRIVILEGES Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the ACLCHECKPRIVILEGES Function . Syntax DBMS_XDB.ACLCHECKPRIVILEGES( acl_path IN VARCHAR2, owner IN VARCHAR2, privs IN xmltype) RETURN PLS_INTEGER; Parameters Table 194-3 ACLCHECKPRIVILEGES Function Parameters Parameter Description acl_path Absolute path in the Hierarchy for ACL document owner Resource owner name; the pseudo user "DAV:owner" is replaced by this user during ACL privilege resolution privs An XMLType instance of the privilege element specifying the requested set of access privileges. See description for CHECKPRIVILEGES Function .