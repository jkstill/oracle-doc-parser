---
id: 19c__DBMS_XDB.LINK
name: DBMS_XDB.LINK
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.LINK

This deprecated procedure creates a link from a specified folder to a specified resource.

## Syntax

```sql
DBMS_XDB.LINK(
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

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the LINK Procedures . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the LINK Procedures . Syntax DBMS_XDB.LINK( srcpath IN VARCHAR2, linkfolder IN VARCHAR2, linkname IN VARCHAR2); DBMS_XDB.LINK( srcpath IN VARCHAR2, linkfolder IN VARCHAR2, linkname IN VARCHAR2, linktype IN PLS_INTEGER := DBMS_XDB.LINK_TYPE_HARD); Parameters Table 194-29 LINK Procedure Parameters Parameter Description srcpath Path name of the resource to which a link is created linkfolder Folder in which the new link is placed linkname Name of the new link linktype Type of link to be created: DBMS_XDB . LINK_TYPE_HARD (default) DBMS_XDB . LINK_TYPE_WEAK DBMS_XDB . LINK_TYPE_SYMBOLIC