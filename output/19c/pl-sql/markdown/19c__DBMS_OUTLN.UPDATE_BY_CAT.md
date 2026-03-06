---
id: 19c__DBMS_OUTLN.UPDATE_BY_CAT
name: DBMS_OUTLN.UPDATE_BY_CAT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OUTLN
tags: [dbms_outln]
source_file: DBMS_OUTLN.html
---

# DBMS_OUTLN.UPDATE_BY_CAT

This procedure changes the category of all outlines in one category to a new category.

## Syntax

```sql
DBMS_OUTLN.UPDATE_BY_CAT (
   oldcat    VARCHAR2 default 'DEFAULT',
   newcat    VARCHAR2 default 'DEFAULT');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| oldcat | VARCHAR2 | IN | The current category of outlines. |
| newcat | VARCHAR2 | IN | The new category of outlines. |

## Usage Notes

Syntax DBMS_OUTLN.UPDATE_BY_CAT ( oldcat VARCHAR2 default 'DEFAULT', newcat VARCHAR2 default 'DEFAULT'); Parameters Table 119-5 UPDATE_BY_CAT Procedure Parameters Parameter Description oldcat The current category of outlines. newcat The new category of outlines.