---
id: 19c__DBMS_UTILITY.SQLID_TO_SQLHASH
name: DBMS_UTILITY.SQLID_TO_SQLHASH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.SQLID_TO_SQLHASH

This function converts a SQL ID into a hash value.

## Syntax

```sql
DBMS_UTILITY.SQLID_TO_SQLHASH (
   sql_id    IN   VARCHAR2) 
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_id | VARCHAR2) | IN | SQL ID of a SQL statement. Must be VARCHAR2 (13) . |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_UTILITY.SQLID_TO_SQLHASH ( sql_id IN VARCHAR2) RETURN NUMBER; Parameters Table 187-32 SQLID_TO_SQLHASH Function Parameters Parameter Description sql_id SQL ID of a SQL statement. Must be VARCHAR2 (13) .