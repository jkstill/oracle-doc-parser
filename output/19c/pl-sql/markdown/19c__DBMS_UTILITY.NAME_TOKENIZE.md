---
id: 19c__DBMS_UTILITY.NAME_TOKENIZE
name: DBMS_UTILITY.NAME_TOKENIZE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.NAME_TOKENIZE

This procedure calls the parser to parse the given name as a [. b [. c ]][@ dblink ] .

## Syntax

```sql
DBMS_UTILITY.NAME_TOKENIZE ( 
   name    IN  VARCHAR2,
   a       OUT VARCHAR2,
   b       OUT VARCHAR2,
   c       OUT VARCHAR2,
   dblink  OUT VARCHAR2, 
   nextpos OUT BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Input name, consisting of SQL identifiers (for example, scott.foo@dblink) |
| a | VARCHAR2 | OUT | Output for the first token of the name |
| b | VARCHAR2 | OUT | Output for the second token of the name (if applicable) |
| c | VARCHAR2 | OUT | Output for the third token of the name (if applicable) |
| dblink | VARCHAR2 | OUT | Output for the dblink of the name |
| nextpos | BINARY_INTEGER) | OUT | Next position after parsing the input name |

## Usage Notes

It strips double quotes, or converts to uppercase if there are no quotes. It ignores comments of all sorts, and does no semantic analysis. Missing values are left as NULL . Syntax DBMS_UTILITY.NAME_TOKENIZE ( name IN VARCHAR2, a OUT VARCHAR2, b OUT VARCHAR2, c OUT VARCHAR2, dblink OUT VARCHAR2, nextpos OUT BINARY_INTEGER); Parameters Table 187-31 NAME_RESOLVE Procedure Parameters Parameter Description name Input name, consisting of SQL identifiers (for example, scott.foo@dblink) a Output for the first token of the name b Output for the second token of the name (if applicable) c Output for the third token of the name (if applicable) dblink Output for the dblink of the name nextpos Next position after parsing the input name