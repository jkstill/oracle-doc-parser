---
id: 19c__DBMS_SQL
name: DBMS_SQL
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL

The DBMS_SQL package defines RECORD type and TABLE type data structures.

## Syntax

```sql
TYPE desc_rec IS RECORD (
      col_type            BINARY_INTEGER := 0,
      col_max_len         BINARY_INTEGER := 0,
      col_name            VARCHAR2(32)   := '',
      col_name_len        BINARY_INTEGER := 0,
      col_schema_name     VARCHAR2(32)   := '',
      col_schema_name_len BINARY_INTEGER := 0,
      col_precision       BINARY_INTEGER := 0,
      col_scale           BINARY_INTEGER := 0,
      col_charsetid       BINARY_INTEGER := 0,
      col_charsetform     BINARY_INTEGER := 0,
      col_null_ok         BOOLEAN        := TRUE);
TYPE desc_tab IS TABLE OF desc_rec INDEX BY BINARY_INTEGER;
```

## Usage Notes

RECORD Types DBMS_SQL DESC_REC Record Type (deprecated) DBMS_SQL DESC_REC2 Record Type DBMS_SQL DESC_REC3 Record Type DBMS_SQL DESC_REC4 Record Type TABLE Types for DESCRIBE_COLUMNS Procedures DBMS_SQL DESC_TAB Table Type DBMS_SQL DESC_TAB2 Table Type DBMS_SQL DESC_TAB3 Table Type DBMS_SQL DESC_TAB4 Table Type TABLE Types For Scalar and LOB Collections DBMS_SQL bulk operations are only supported with these predefined DBMS_SQL TABLE types. BFILE_TABLE Table Type BINARY_DOUBLE_TABLE Table Type BINARY_FLOAT_TABLE Table Type BLOB_TABLE Table Type CLOB_TABLE Table Type DATE_TABLE Table Type INTERVAL_DAY_TO_SECOND_TABLE Table Type INTERVAL_YEAR_TO_MONTH_TABLE Table Type NUMBER_TABLE Table Type TIME_TABLE Table Type TIME_WITH_TIME_ZONE_TABLE Table Type TIMESTAMP_TABLE Table Type TIMESTAMP_WITH_LTZ_TABLE Table Type TIMESTAMP_WITH_TIME_ZONE_TABLE Table Type UROWID_TABLE Table Type VARCHAR2_TABLE Table Type VARCHAR2A Table Type VARCHAR2S Table Type Note: This type has been deprecated in favor of the DESC_REC2 Record Type . It is the element type of the DESC_TAB table type and the DESCRIBE_COLUMNS Procedure . Note: This type has been deprecated in favor of the DESC_REC2 Record Type .