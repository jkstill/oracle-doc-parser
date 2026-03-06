---
id: 19c__DBMS_UTILITY.ANALYZE_SCHEMA
name: DBMS_UTILITY.ANALYZE_SCHEMA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.ANALYZE_SCHEMA

This procedure analyzes all the tables, clusters and indexes in a schema.

## Syntax

```sql
DBMS_UTILITY.ANALYZE_SCHEMA (
   schema             IN  VARCHAR2,
   method             IN  VARCHAR2,
   estimate_rows      IN  NUMBER DEFAULT NULL,
   estimate_percent   IN  NUMBER DEFAULT NULL,
   method_opt         IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema | VARCHAR2 | IN | Name of the schema |
| method | VARCHAR2 | IN | One of ESTIMATE , COMPUTE or DELETE . If ESTIMATE then either estimate_rows or estimate_percent must be nonzero. |
| estimate_rows | NUMBER | IN | Number of rows to estimate |
| estimate_percent | NUMBER | IN | Percentage of rows to estimate. If estimate_rows is specified ignore this parameter. |
| method_opt | VARCHAR2 | IN | Method options of the following format: [ FOR TABLE ] [ FOR ALL [ INDEXED ] COLUMNS ] [ SIZE n ] [ FOR ALL INDEXES ] |

## Usage Notes

Syntax DBMS_UTILITY.ANALYZE_SCHEMA ( schema IN VARCHAR2, method IN VARCHAR2, estimate_rows IN NUMBER DEFAULT NULL, estimate_percent IN NUMBER DEFAULT NULL, method_opt IN VARCHAR2 DEFAULT NULL); Parameters Table 187-8 ANALYZE_SCHEMA Procedure Parameters Parameter Description schema Name of the schema method One of ESTIMATE , COMPUTE or DELETE . If ESTIMATE then either estimate_rows or estimate_percent must be nonzero. estimate_rows Number of rows to estimate estimate_percent Percentage of rows to estimate. If estimate_rows is specified ignore this parameter. method_opt Method options of the following format: [ FOR TABLE ] [ FOR ALL [ INDEXED ] COLUMNS ] [ SIZE n ] [ FOR ALL INDEXES ] Exceptions ORA - 20000 : Insufficient privileges for some object in this schema