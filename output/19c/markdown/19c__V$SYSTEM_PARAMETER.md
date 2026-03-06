---
id: 19c__V$SYSTEM_PARAMETER
name: V$SYSTEM_PARAMETER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dynamic_performance]
source_file: V-SYSTEM_PARAMETER.html
---

# V$SYSTEM_PARAMETER

V$SYSTEM_PARAMETER displays information about the initialization parameters that are currently in effect for the instance. A new session inherits parameter values from the instance-wide values.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NUM | NUMBER |  |
| NAME | VARCHAR2(80) |  |
| TYPE | NUMBER |  |
| VALUE | VARCHAR2(4000) |  |
| DISPLAY_VALUE | VARCHAR2(4000) |  |
| DEFAULT_VALUE | VARCHAR2(255) |  |
| ISDEFAULT | VARCHAR2(9) |  |
| ISSES_MODIFIABLE | VARCHAR2(5) |  |
| ISSYS_MODIFIABLE | VARCHAR2(9) |  |
| ISPDB_MODIFIABLE | VARCHAR2(5) |  |
| ISINSTANCE_MODIFIABLE | VARCHAR2(5) |  |
| ISMODIFIED | VARCHAR2(8) |  |
| ISADJUSTED | VARCHAR2(5) |  |
| ISDEPRECATED | VARCHAR2(5) |  |
| ISBASIC | VARCHAR2(5) |  |
| DESCRIPTION | VARCHAR2(255) |  |
| UPDATE_COMMENT | VARCHAR2(255) |  |
| HASH | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " V$PARAMETER " for information about initialization parameters that are currently in effect for a session See Also: " V$PARAMETER " for information about initialization parameters that are currently in effect for a session