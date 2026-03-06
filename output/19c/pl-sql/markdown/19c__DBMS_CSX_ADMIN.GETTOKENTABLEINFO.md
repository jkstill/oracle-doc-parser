---
id: 19c__DBMS_CSX_ADMIN.GETTOKENTABLEINFO
name: DBMS_CSX_ADMIN.GETTOKENTABLEINFO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CSX_ADMIN
tags: [dbms_csx_admin]
source_file: DBMS_CSX_ADMIN.html
---

# DBMS_CSX_ADMIN.GETTOKENTABLEINFO

This procedure is overloaded. The specific forms of functionality are described along with the syntax declarations.

## Syntax

```sql
DBMS_CSX_ADMIN.GETTOKENTABLEINFO  (
   ownername      IN   VARCHAR2,
   tablename      IN   VARCHAR2,
   guid           OUT  RAW,
   qnametable     OUT  VARCHAR2,
   nmspctable     OUT  VARCHAR2,
   level          OUT  NUMBER,
   tabno          OUT  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownername | VARCHAR2 | IN | Owner of the table |
| tablename | VARCHAR2 | IN | Name of the table |
| guid | RAW | OUT | GUID of the token table set used by the given table |
| qnametable | VARCHAR2 | OUT | Name of the qname-ID table in the new set |
| nmspctable | VARCHAR2 | OUT | Name of the namespace-ID table in the new set |
| level | NUMBER | OUT | DEFAULT_LEVEL if default token table set, TBS_LEVEL if same token table set is used by all tables in the same tablespace as the given table, TAB_LEVEL otherwise |
| tabno | NUMBER) | OUT | Table object number |

**Returns:** `UNKNOWN`

## Usage Notes

Given the table name and the owner, the first overload of the procedure returns the globally unique identifier (GUID) of the token table set where token mappings for this table can be found. The procedure returns also the names of the token tables, and whether the token table set is the default one. Given the object number of a table, the second overload of the procedure returns the GUID of the token table set used by the table, and whether this is the default token table set. Syntax DBMS_CSX_ADMIN.GETTOKENTABLEINFO ( ownername IN VARCHAR2, tablename IN VARCHAR2, guid OUT RAW, qnametable OUT VARCHAR2, nmspctable OUT VARCHAR2, level OUT NUMBER, tabno OUT NUMBER); DBMS_CSX_ADMIN.GETTOKENTABLEINFO ( tabno IN NUMBER, guid OUT RAW); RETURN BOOLEAN; Parameters Table 43-3 GETTOKENTABLEINFO Procedure & Function Parameters Parameter Description ownername Owner of the table tablename Name of the table guid GUID of the token table set used by the given table qnametable Name of the qname-ID table in the new set nmspctable Name of the namespace-ID table in the new set level DEFAULT_LEVEL if default token table set, TBS_LEVEL if same token table set is used by all tables in the same tablespace as the given table, TAB_LEVEL otherwise tabno Table object number