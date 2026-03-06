---
id: 19c__DBMS_UTILITY.COMMA_TO_TABLE
name: DBMS_UTILITY.COMMA_TO_TABLE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.COMMA_TO_TABLE

These procedures convert a comma-delimited list of names into a PL/SQL table of names. The second version supports fully-qualified attribute names.

## Syntax

```sql
DBMS_UTILITY.COMMA_TO_TABLE ( 
   list   IN  VARCHAR2,
   tablen OUT BINARY_INTEGER,
   tab    OUT uncl_array); 

DBMS_UTILITY.COMMA_TO_TABLE ( 
   list   IN  VARCHAR2,
   tablen OUT BINARY_INTEGER,
   tab    OUT lname_array);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| list | VARCHAR2 | IN | Comma separated list of list of 'names', where a name should have the following format for the first overloading: a [. b [. c ]][ @ d ] and the following format for the second overloading: a [. b]* where a , b , c , d are simple identifiers (quoted or unquoted). |
| tablen | BINARY_INTEGER | OUT | Number of tables in the PL/SQL table |
| tab | uncl_array) | OUT | PL/SQL table which contains list of names |

## Usage Notes

Syntax DBMS_UTILITY.COMMA_TO_TABLE ( list IN VARCHAR2, tablen OUT BINARY_INTEGER, tab OUT uncl_array); DBMS_UTILITY.COMMA_TO_TABLE ( list IN VARCHAR2, tablen OUT BINARY_INTEGER, tab OUT lname_array); Parameters Table 187-10 COMMA_TO_TABLE Procedure Parameters Parameter Description list Comma separated list of list of 'names', where a name should have the following format for the first overloading: a [. b [. c ]][ @ d ] and the following format for the second overloading: a [. b]* where a , b , c , d are simple identifiers (quoted or unquoted). tablen Number of tables in the PL/SQL table tab PL/SQL table which contains list of names Return Values A PL/SQL table is returned, with values 1..n and n+1 is null . Usage Notes The list must be a non-empty comma-delimited list: Anything other than a comma-delimited list is rejected. Commas inside double quotes do not count. Entries in the comma-delimited list cannot include multibyte characters. The values in tab are copied from the original list, with no transformations. The procedure fails if the string between separators is longer than 30 bytes.