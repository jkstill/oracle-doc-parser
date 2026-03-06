---
id: 19c__V$HM_CHECK
name: V$HM_CHECK
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-HM_CHECK.html
---

# V$HM_CHECK

V$HM_CHECK displays information about all the checks registered with Health Monitor. Each check is uniquely identified by a name or an ID.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ID | NUMBER |  |
| NAME | VARCHAR2(64) |  |
| NAME_NLS | VARCHAR2(1024) |  |
| CLSID | NUMBER |  |
| CLS_NAME | VARCHAR2(15) |  |
| FLAGS | NUMBER |  |
| INTERNAL_CHECK | VARCHAR2(1) |  |
| OFFLINE_CAPABLE | VARCHAR2(1) |  |
| DESCRIPTION | VARCHAR2(1024) |  |
| CON_ID | NUMBER |  |