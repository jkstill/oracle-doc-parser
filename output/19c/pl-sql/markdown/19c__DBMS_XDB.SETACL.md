---
id: 19c__DBMS_XDB.SETACL
name: DBMS_XDB.SETACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.SETACL

This deprecated procedure set the ACL on a specified resource to be the ACL specified by path.

## Syntax

```sql
DBMS_XDB.SETACL(
   res_path   IN  VARCHAR2,
   acl_path   IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res_path | VARCHAR2 | IN | Absolute path in the Hierarchy for resource |
| acl_path | VARCHAR2) | IN | Absolute path in the Hierarchy for ACL |

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the SETACL Procedure . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the SETACL Procedure . Syntax DBMS_XDB.SETACL( res_path IN VARCHAR2, acl_path IN VARCHAR2); Parameters Table 194-34 SETACL Procedure Parameters Parameter Description res_path Absolute path in the Hierarchy for resource acl_path Absolute path in the Hierarchy for ACL Usage Notes The user must have <write-acl> privileges on the resource.