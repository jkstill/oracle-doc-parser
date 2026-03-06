---
id: 19c__V$SESSION_FIX_CONTROL
name: V$SESSION_FIX_CONTROL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SESSION_FIX_CONTROL.html
---

# V$SESSION_FIX_CONTROL

V$SESSION_FIX_CONTROL displays information about Fix Control (enabled/disabled) for the current session.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER |  |
| BUGNO | NUMBER |  |
| VALUE | NUMBER |  |
| SQL_FEATURE | VARCHAR2(64) |  |
| DESCRIPTION | VARCHAR2(64) |  |
| OPTIMIZER_FEATURE_ENABLE | VARCHAR2(25) |  |
| EVENT | NUMBER |  |
| IS_DEFAULT | NUMBER |  |
| CON_ID | NUMBER |  |