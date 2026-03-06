---
id: 19c__DBMS_RANDOM
name: DBMS_RANDOM
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RANDOM
tags: [dbms_random]
source_file: DBMS_RANDOM.html
---

# DBMS_RANDOM

These operational notes apply to DBMS_RANDOM.

## Usage Notes

DBMS_RANDOM.RANDOM produces integers in [-2^^31, 2^^31). DBMS_RANDOM.VALUE produces numbers in [0,1) with 38 digits of precision. DBMS_RANDOM can be explicitly initialized, but does not need to be initialized before calling the random number generator. It will automatically initialize with the date, user ID, and process ID if no explicit initialization is performed. If this package is seeded twice with the same seed, then accessed in the same way, it will produce the same results in both cases. In some cases, such as when testing, you may want the sequence of random numbers to be the same on every run. In that case, you seed the generator with a constant value by calling one of the overloads of DBMS_RANDOM.SEED . To produce different output for every run, simply to omit the call to "Seed" and the system will choose a suitable seed for you.