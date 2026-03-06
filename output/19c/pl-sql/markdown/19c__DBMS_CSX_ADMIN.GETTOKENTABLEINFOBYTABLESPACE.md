---
id: 19c__DBMS_CSX_ADMIN.GETTOKENTABLEINFOBYTABLESPACE
name: DBMS_CSX_ADMIN.GETTOKENTABLEINFOBYTABLESPACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CSX_ADMIN
tags: [dbms_csx_admin]
source_file: DBMS_CSX_ADMIN.html
---

# DBMS_CSX_ADMIN.GETTOKENTABLEINFOBYTABLESPACE

Given a tablespace number, this procedure returns the GUID and the token table names for this tablespace.

## Syntax

```sql
DBMS_CSX_ADMIN.GETTOKENTABLEINFOBYTABLESPACE  (
   tsname          IN   VARCHAR2,
   tablespaceno    IN   NUMBER,
   guid            OUT  RAW,
   qnametable      OUT  VARCHAR2,
   nmspctable      OUT  VARCHAR2,
   isdefault       OUT  BOOLEAN,
   containTokTab   OUT  BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tsname | VARCHAR2 | IN | Tablespace name |
| tablespaceno | NUMBER | IN | Tablespace number |
| guid | RAW | OUT | GUID of the token table set associated with this tablespace (if any) |
| qnametable | VARCHAR2 | OUT | Name of the qname-ID table |
| nmspctable | VARCHAR2 | OUT | Name of the namespace-ID table |
| isdefault | BOOLEAN | OUT | TRUE if the token table is the default one |
| containTokTab | BOOLEAN) | OUT | TRUE if the tablespace contains its own token table set |

## Usage Notes

Syntax DBMS_CSX_ADMIN.GETTOKENTABLEINFOBYTABLESPACE ( tsname IN VARCHAR2, tablespaceno IN NUMBER, guid OUT RAW, qnametable OUT VARCHAR2, nmspctable OUT VARCHAR2, isdefault OUT BOOLEAN, containTokTab OUT BOOLEAN); Parameters Table 43-4 GETTOKENTABLEINFOBYTABLESPACE Procedure Parameters Parameter Description tsname Tablespace name tablespaceno Tablespace number guid GUID of the token table set associated with this tablespace (if any) qnametable Name of the qname-ID table nmspctable Name of the namespace-ID table isdefault TRUE if the token table is the default one containTokTab TRUE if the tablespace contains its own token table set