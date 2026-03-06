---
id: 19c__DBA_SUPPLEMENTAL_LOGGING
name: DBA_SUPPLEMENTAL_LOGGING
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_SUPPLEMENTAL_LOGGING.html
---

# DBA_SUPPLEMENTAL_LOGGING

The script content on this page is for navigation purposes only and does not alter the content in any way.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| MINIMAL | VARCHAR2(3) | Identifies whether minimal supplemental logging is on ( YES or NO ) |
| PRIMARY_KEY | VARCHAR2(3) | Identifies whether primary key supplemental logging is on ( YES or NO ) |
| UNIQUE_INDEX | VARCHAR2(3) | Identifies whether unique column supplemental logging is on ( YES or NO ) |
| FOREIGN_KEY | VARCHAR2(3) | Identifies whether foreign key supplemental logging is on ( YES or NO ) |
| ALL_COLUMN | VARCHAR2(3) | Identifies whether all column supplemental logging is on ( YES or NO ) |
| PROCEDURAL | VARCHAR2(3) | Identifies whether supplemental logging for procedural replication is on ( YES or NO ) |
| SUBSET_REP Foot 1 | VARCHAR2(3) | Indicates whether subset database replication is on ( YES or NO ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Utilities for more information about supplemental logging " V$DATABASE " for information about supplemental logging in a CDB See Also: Oracle Database Utilities for more information about supplemental logging " V$DATABASE " for information about supplemental logging in a CDB