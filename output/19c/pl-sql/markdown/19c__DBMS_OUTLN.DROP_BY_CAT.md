---
id: 19c__DBMS_OUTLN.DROP_BY_CAT
name: DBMS_OUTLN.DROP_BY_CAT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OUTLN
tags: [dbms_outln]
source_file: DBMS_OUTLN.html
---

# DBMS_OUTLN.DROP_BY_CAT

This procedure drops outlines that belong to a particular category. While outlines are put into the DEFAULT category unless otherwise specified, users have the option of grouping their outlines into groups called categories.

## Syntax

```sql
DBMS_OUTLN.DROP_BY_CAT (
   cat VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cat | VARCHAR2) | IN | Category of outlines to drop. |

## Usage Notes

Syntax DBMS_OUTLN.DROP_BY_CAT ( cat VARCHAR2); Parameters Table 119-4 DROP_BY_CAT Procedure Parameters Parameter Description cat Category of outlines to drop. Usage Notes This procedure purges a category of outlines in a single call. Examples This example drops all outlines in the DEFAULT category: DBMS_OUTLN.DROP_BY_CAT('DEFAULT');