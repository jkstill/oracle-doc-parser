---
id: 19c__V$DB_TRANSPORTABLE_PLATFORM
name: V$DB_TRANSPORTABLE_PLATFORM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dynamic_performance]
source_file: V-DB_TRANSPORTABLE_PLATFORM.html
---

# V$DB_TRANSPORTABLE_PLATFORM

V$DB_TRANSPORTABLE_PLATFORM displays all platforms to which the database can be transported using the RMAN CONVERT DATABASE command.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PLATFORM_ID | NUMBER |  |
| PLATFORM_NAME | VARCHAR2(101) |  |
| ENDIAN_FORMAT | VARCHAR2(14) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The transportable database feature only supports transports of the same endian platform. Therefore, V$DB_TRANSPORTABLE_PLATFORM displays fewer rows than V$TRANSPORTABLE_PLATFORM . See Also: " V$TRANSPORTABLE_PLATFORM " See Also: " V$TRANSPORTABLE_PLATFORM "