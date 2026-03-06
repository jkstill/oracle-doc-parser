---
id: 19c__V$PARAMETER
name: V$PARAMETER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dynamic_performance]
source_file: V-PARAMETER.html
---

# V$PARAMETER

NUM

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
| ISMODIFIED | VARCHAR2(10) |  |
| ISADJUSTED | VARCHAR2(5) |  |
| ISDEPRECATED | VARCHAR2(5) |  |
| ISBASIC | VARCHAR2(5) |  |
| DESCRIPTION | VARCHAR2(255) |  |
| UPDATE_COMMENT | VARCHAR2(255) |  |
| HASH | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Examples The following query returns the default value for the ALLOW_GLOBAL_DBLINKS initialization parameter: SQL> SELECT name, default_value FROM v$parameter 2 WHERE name = 'allow_global_dblinks'; NAME ----------------------------------------------------------- DEFAULT_VALUE ----------------------------------------------------------- allow_global_dblinks FALSE SQL> The following query shows that the ALLOW_GLOBAL_DBLINKS initialization parameter is not modifiable in a PDB: SQL> SELECT name, ispdb_modifiable FROM v$parameter 2 WHERE name = 'allow_global_dblinks'; NAME ----------------------------------------------------------- ISPDB ----- allow_global_dblinks FALSE SQL> See Also: " V$SYSTEM_PARAMETER " See Also: " V$SYSTEM_PARAMETER "