---
id: 19c__V$SYS_OPTIMIZER_ENV
name: V$SYS_OPTIMIZER_ENV
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dynamic_performance]
source_file: V-SYS_OPTIMIZER_ENV.html
---

# V$SYS_OPTIMIZER_ENV

The parameters displayed by this view are either regular initialization parameters (such as OPTIMIZER_FEATURES_ENABLE ) or pseudo parameters (such as ACTIVE_INSTANCE_COUNT ).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ID | NUMBER |  |
| NAME | VARCHAR2(40) |  |
| SQL_FEATURE | VARCHAR2(64) |  |
| ISDEFAULT | VARCHAR2(3) |  |
| VALUE | VARCHAR2(25) |  |
| DEFAULT_VALUE | VARCHAR2(25) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " OPTIMIZER_FEATURES_ENABLE " " ACTIVE_INSTANCE_COUNT " See Also: " OPTIMIZER_FEATURES_ENABLE " " ACTIVE_INSTANCE_COUNT "