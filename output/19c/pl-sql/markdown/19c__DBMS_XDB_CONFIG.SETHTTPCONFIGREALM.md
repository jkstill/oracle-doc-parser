---
id: 19c__DBMS_XDB_CONFIG.SETHTTPCONFIGREALM
name: DBMS_XDB_CONFIG.SETHTTPCONFIGREALM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.SETHTTPCONFIGREALM

This procedure modifies the realm value.

## Syntax

```sql
DBMS_XDB_CONFIG.SETHTTPCONFIGREALM(
   realm IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| realm | VARCHAR2) | IN | Realm as defined in IETF's RFC2617 |

## Usage Notes

Syntax DBMS_XDB_CONFIG.SETHTTPCONFIGREALM( realm IN VARCHAR2); Parameters Table 196-22 SETHTTPPORT Procedure Parameters Parameter Description realm Realm as defined in IETF's RFC2617