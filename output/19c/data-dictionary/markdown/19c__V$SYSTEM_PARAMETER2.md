---
id: 19c__V$SYSTEM_PARAMETER2
name: V$SYSTEM_PARAMETER2
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dynamic_performance]
source_file: V-SYSTEM_PARAMETER2.html
---

# V$SYSTEM_PARAMETER2

V$SYSTEM_PARAMETER2 displays information about the initialization parameters that are currently in effect for the instance, with each list parameter value appearing as a row in the view. A new session inherits parameter values from the instance-wide values.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NUM | NUMBER |  |
| NAME | VARCHAR2(80) |  |
| TYPE | NUMBER |  |
| VALUE | VARCHAR2(4000) |  |
| DISPLAY_VALUE | VARCHAR2(4000) |  |
| ISDEFAULT | VARCHAR2(6) |  |
| ISSES_MODIFIABLE | VARCHAR2(5) |  |
| ISSYS_MODIFIABLE | VARCHAR2(9) |  |
| ISPDB_MODIFIABLE | VARCHAR2(5) |  |
| ISINSTANCE_MODIFIABLE | VARCHAR2(5) |  |
| ISMODIFIED | VARCHAR2(8) |  |
| ISADJUSTED | VARCHAR2(5) |  |
| ISDEPRECATED | VARCHAR2(5) |  |
| ISBASIC | VARCHAR2(5) |  |
| DESCRIPTION | VARCHAR2(255) |  |
| ORDINAL | NUMBER |  |
| UPDATE_COMMENT | VARCHAR2(255) |  |
| HASH | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Presenting the list parameter values in this format enables you to quickly determine the values for a list parameter. For example, if a parameter value is a, b , then the V$SYSTEM_PARAMETER view does not tell you if the parameter has two values (both a and b ) or one value ( a, b ). V$SYSTEM_PARAMETER2 makes the distinction between the list parameter values clear. See Also: " V$SYSTEM_PARAMETER " See Also: " V$SYSTEM_PARAMETER "