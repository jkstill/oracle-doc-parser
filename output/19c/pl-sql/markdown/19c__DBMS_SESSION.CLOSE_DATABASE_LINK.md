---
id: 19c__DBMS_SESSION.CLOSE_DATABASE_LINK
name: DBMS_SESSION.CLOSE_DATABASE_LINK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.CLOSE_DATABASE_LINK

This procedure closes an open database link. It is equivalent to the following SQL statement: ALTER SESSION CLOSE DATABASE LINK <name>

## Syntax

```sql
DBMS_SESSION.CLOSE_DATABASE_LINK (
   dblink VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dblink | VARCHAR2) | IN | Name of the database link to close |

## Usage Notes

Syntax DBMS_SESSION.CLOSE_DATABASE_LINK ( dblink VARCHAR2); Parameters Table 154-5 CLOSE_DATABASE_LINK Procedure Parameters Parameter Description dblink Name of the database link to close