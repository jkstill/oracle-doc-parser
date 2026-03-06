---
id: 19c__DBMS_RANDOM.SEED
name: DBMS_RANDOM.SEED
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RANDOM
tags: [dbms_random]
source_file: DBMS_RANDOM.html
---

# DBMS_RANDOM.SEED

This procedure resets the seed.

## Syntax

```sql
DBMS_RANDOM.SEED (
   val  IN  BINARY_INTEGER);

DBMS_RANDOM.SEED (
   val  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| val | BINARY_INTEGER) | IN | Seed number or string used to generate a random number |

## Usage Notes

Syntax DBMS_RANDOM.SEED ( val IN BINARY_INTEGER); DBMS_RANDOM.SEED ( val IN VARCHAR2); Pragmas PRAGMA restrict_references (seed, WNDS); Parameters Table 136-5 SEED Procedure Parameters Parameter Description val Seed number or string used to generate a random number Usage Notes The seed can be a string up to length 2000.