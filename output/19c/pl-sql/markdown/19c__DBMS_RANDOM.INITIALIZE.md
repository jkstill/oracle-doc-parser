---
id: 19c__DBMS_RANDOM.INITIALIZE
name: DBMS_RANDOM.INITIALIZE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RANDOM
tags: [dbms_random]
source_file: DBMS_RANDOM.html
---

# DBMS_RANDOM.INITIALIZE

This deprecated procedure initializes the generator.

## Syntax

```sql
DBMS_RANDOM.INITIALIZE (
   val  IN  BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| val | BINARY_INTEGER) | IN | Seed number used to generate a random number |

## Usage Notes

Note: This procedure is deprecated with Release 11gR1 and, although currently supported, it should not be used. Note: This procedure is deprecated with Release 11gR1 and, although currently supported, it should not be used. Syntax DBMS_RANDOM.INITIALIZE ( val IN BINARY_INTEGER); Pragmas PRAGMA restrict_references (initialize, WNDS); Parameters Table 136-2 INITIALIZE Procedure Parameters Parameter Description val Seed number used to generate a random number