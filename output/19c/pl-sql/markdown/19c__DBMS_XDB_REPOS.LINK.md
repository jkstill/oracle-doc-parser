---
id: 19c__DBMS_XDB_REPOS.LINK
name: DBMS_XDB_REPOS.LINK
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.LINK

This procedure creates from a specified folder to a specified resource.

## Syntax

```sql
DBMS_XDB_REPOS.LINK(
   srcpath      IN   VARCHAR2,
   linkfolder   IN   VARCHAR2,
   linkname     IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| srcpath | VARCHAR2 | IN | Path name of the resource to which a link is created |
| linkfolder | VARCHAR2 | IN | Folder in which the new link is placed |
| linkname | VARCHAR2) | IN | Name of the new link |
| linktype |  |  | Type of link to be created: DBMS_XDB . LINK_TYPE_HARD (default) DBMS_XDB . LINK_TYPE_WEAK DBMS_XDB . LINK_TYPE_SYMBOLIC |

## Usage Notes

Syntax DBMS_XDB_REPOS.LINK( srcpath IN VARCHAR2, linkfolder IN VARCHAR2, linkname IN VARCHAR2); DBMS_XDB_REPOS.LINK( srcpath IN VARCHAR2, linkfolder IN VARCHAR2, linkname IN VARCHAR2, linktype IN PLS_INTEGER := DBMS_XDB_REPOS.LINK_TYPE_HARD); Parameters Table 198-28 LINK Procedure Parameters Parameter Description srcpath Path name of the resource to which a link is created linkfolder Folder in which the new link is placed linkname Name of the new link linktype Type of link to be created: DBMS_XDB . LINK_TYPE_HARD (default) DBMS_XDB . LINK_TYPE_WEAK DBMS_XDB . LINK_TYPE_SYMBOLIC