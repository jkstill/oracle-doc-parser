---
id: 19c__V$VERSION
name: V$VERSION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-VERSION.html
---

# V$VERSION

V$VERSION displays the version number of Oracle Database. The database components have the same version number as the database, so the version number is returned only once.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BANNER | VARCHAR2(80) |  |
| BANNER_FULL | VARCHAR2(160) |  |
| BANNER_LEGACY | VARCHAR2(80) |  |
| CON_ID | NUMBER |  |