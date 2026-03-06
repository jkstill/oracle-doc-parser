---
id: 19c__DBMS_UTILITY.TABLE_TO_COMMA
name: DBMS_UTILITY.TABLE_TO_COMMA
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.TABLE_TO_COMMA

This procedure converts a PL/SQL table of names into a comma-delimited list of names.

## Syntax

```sql
DBMS_UTILITY.TABLE_TO_COMMA ( 
   tab    IN  UNCL_ARRAY, 
   tablen OUT BINARY_INTEGER,
   list   OUT VARCHAR2);

DBMS_UTILITY.TABLE_TO_COMMA ( 
   tab    IN  lname_array,
   tablen OUT BINARY_INTEGER,
   list   OUT VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tab | UNCL_ARRAY | IN | PL/SQL table which contains list of table names |
| tablen | BINARY_INTEGER | OUT | Number of tables in the PL/SQL table |
| list | VARCHAR2) | OUT | Comma separated list of tables |

## Usage Notes

This takes a PL/SQL table, 1..n , terminated with n+1 null . The second version supports fully-qualified attribute names. Syntax DBMS_UTILITY.TABLE_TO_COMMA ( tab IN UNCL_ARRAY, tablen OUT BINARY_INTEGER, list OUT VARCHAR2); DBMS_UTILITY.TABLE_TO_COMMA ( tab IN lname_array, tablen OUT BINARY_INTEGER, list OUT VARCHAR2); Parameters Table 187-33 TABLE_TO_COMMA Procedure Parameters Parameter Description tab PL/SQL table which contains list of table names tablen Number of tables in the PL/SQL table list Comma separated list of tables Return Values A comma-delimited list and the number of elements found in the table.