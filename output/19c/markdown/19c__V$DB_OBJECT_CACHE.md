---
id: 19c__V$DB_OBJECT_CACHE
name: V$DB_OBJECT_CACHE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dynamic_performance]
source_file: V-DB_OBJECT_CACHE.html
---

# V$DB_OBJECT_CACHE

V$DB_OBJECT_CACHE displays database objects that are cached in the library cache. Objects include tables, indexes, clusters, synonym definitions, PL/SQL procedures and packages, and triggers.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(64) |  |
| NAME | VARCHAR2(1000) |  |
| DB_LINK | VARCHAR2(64) |  |
| NAMESPACE | VARCHAR2(64) |  |
| TYPE | VARCHAR2(64) |  |
| SHARABLE_MEM | NUMBER |  |
| LOADS | NUMBER |  |
| EXECUTIONS | NUMBER |  |
| LOCKS | NUMBER |  |
| PINS | NUMBER |  |
| KEPT | VARCHAR2(3) |  |
| CHILD_LATCH | NUMBER |  |
| INVALIDATIONS | NUMBER |  |
| HASH_VALUE | NUMBER |  |
| LOCK_MODE | VARCHAR2(9) |  |
| PIN_MODE | VARCHAR2(9) |  |
| STATUS | VARCHAR2(19) |  |
| TIMESTAMP | VARCHAR2(19) |  |
| PREVIOUS_TIMESTAMP | VARCHAR2(19) |  |
| LOCKED_TOTAL | NUMBER |  |
| PINNED_TOTAL | NUMBER |  |
| PROPERTY | VARCHAR2(80) |  |
| FULL_HASH_VALUE | VARCHAR2(32) |  |
| CON_ID | NUMBER |  |
| CON_NAME | VARCHAR2(64) |  |
| ADDR | RAW(8) |  |
| EDITION | VARCHAR2(138) |  |

## Usage Notes

See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SHARED_POOL.KEEP procedure Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SHARED_POOL.MARKHOT procedure See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SHARED_POOL.KEEP procedure Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SHARED_POOL.MARKHOT procedure