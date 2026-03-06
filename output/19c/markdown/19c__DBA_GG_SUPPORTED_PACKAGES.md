---
id: 19c__DBA_GG_SUPPORTED_PACKAGES
name: DBA_GG_SUPPORTED_PACKAGES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_GG_SUPPORTED_PACKAGES.html
---

# DBA_GG_SUPPORTED_PACKAGES

DBA_GG_SUPPORTED_PACKAGES provides details about supported procedure packages for Oracle GoldenGate replication.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(384) | Procedure package owner |
| NAME | VARCHAR2(384) | Procedure package name |
| FEATURE | VARCHAR2(384) | DBMS feature that the procedure package belongs to |
| MIN_DB_VERSION | VARCHAR2(100) | Minimum database version for the supported package |
| MAX_DB_VERSION | VARCHAR2(100) | Maximum database version for the supported package |
| MIN_REDO_COMPAT_LEVEL | VARCHAR2(100) | Minimum redo compatibility for the supported package |
| MAX_REDO_COMPAT_LEVEL | VARCHAR2(100) | Maximum redo compatibility for the supported package |
| SUPPORTED_LEVEL | VARCHAR2(100) | Supported level of the package |