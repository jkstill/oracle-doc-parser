---
id: 19c__DBMS_UTILITY.DB_VERSION
name: DBMS_UTILITY.DB_VERSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.DB_VERSION

This procedure returns version information for the database.

## Syntax

```sql
DBMS_UTILITY.DB_VERSION (
   version       OUT VARCHAR2,
   compatibility OUT VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| version | VARCHAR2 | OUT | A string which represents the internal software version of the database (for example, 7.1.0.0.0). The length of this string is variable and is determined by the database version. |
| compatibility | VARCHAR2) | OUT | The compatibility setting of the database determined by the "compatible" init . ora parameter. If the parameter is not specified in the init.ora file, then NULL is returned. |

## Usage Notes

Syntax DBMS_UTILITY.DB_VERSION ( version OUT VARCHAR2, compatibility OUT VARCHAR2); Parameters Table 187-16 DB_VERSION Procedure Parameters Parameter Description version A string which represents the internal software version of the database (for example, 7.1.0.0.0). The length of this string is variable and is determined by the database version. compatibility The compatibility setting of the database determined by the "compatible" init . ora parameter. If the parameter is not specified in the init.ora file, then NULL is returned.