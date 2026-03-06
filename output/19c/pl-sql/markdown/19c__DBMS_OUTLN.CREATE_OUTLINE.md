---
id: 19c__DBMS_OUTLN.CREATE_OUTLINE
name: DBMS_OUTLN.CREATE_OUTLINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OUTLN
tags: [dbms_outln]
source_file: DBMS_OUTLN.html
---

# DBMS_OUTLN.CREATE_OUTLINE

This procedure generates an outline by reparsing the SQL statement from the shared cursor identified by hash value and child number.

## Syntax

```sql
DBMS_OUTLN.CREATE_OUTLINE (
   hash_value    IN NUMBER,
   child_number  IN NUMBER,
   category      IN VARCHAR2 DEFAULT 'DEFAULT');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| hash_value | NUMBER | IN | Hash value identifying the target shared cursor. |
| child_number | NUMBER | IN | Child number of the target shared cursor. |
| category | VARCHAR2 | IN | Category in which to create outline (optional). |

## Usage Notes

Syntax DBMS_OUTLN.CREATE_OUTLINE ( hash_value IN NUMBER, child_number IN NUMBER, category IN VARCHAR2 DEFAULT 'DEFAULT'); Parameters Table 119-3 CREATE_OUTLINE Procedure Parameters Parameter Description hash_value Hash value identifying the target shared cursor. child_number Child number of the target shared cursor. category Category in which to create outline (optional).