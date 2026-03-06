---
id: 19c__V$SES_OPTIMIZER_ENV
name: V$SES_OPTIMIZER_ENV
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-SES_OPTIMIZER_ENV.html
---

# V$SES_OPTIMIZER_ENV

Session identifier. This column can be used to join with V$SESSION on the SID column.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| ID | NUMBER |  |
| NAME | VARCHAR2(40) |  |
| SQL_FEATURE | VARCHAR2(64) |  |
| ISDEFAULT | VARCHAR2(3) |  |
| VALUE | VARCHAR2(25) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " V$SYS_OPTIMIZER_ENV " See Also: " V$SYS_OPTIMIZER_ENV "