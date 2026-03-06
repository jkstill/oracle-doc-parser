---
id: 19c__DBMS_XDB_REPOS.SETACL
name: DBMS_XDB_REPOS.SETACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.SETACL

This procedure sets the ACL on a specified resource to be the ACL specified by path.

## Syntax

```sql
DBMS_XDB_REPOS.SETACL(
   res_path   IN  VARCHAR2,
   acl_path   IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res_path | VARCHAR2 | IN | Absolute path in the Hierarchy for resource |
| acl_path | VARCHAR2) | IN | Absolute path in the Hierarchy for ACL |

## Usage Notes

Syntax DBMS_XDB_REPOS.SETACL( res_path IN VARCHAR2, acl_path IN VARCHAR2); Parameters Table 198-33 SETACL Procedure Parameters Parameter Description res_path Absolute path in the Hierarchy for resource acl_path Absolute path in the Hierarchy for ACL Usage Notes The user must have <write-acl> privileges on the resource.