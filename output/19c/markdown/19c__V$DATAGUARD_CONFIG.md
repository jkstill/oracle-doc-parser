---
id: 19c__V$DATAGUARD_CONFIG
name: V$DATAGUARD_CONFIG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DATAGUARD_CONFIG.html
---

# V$DATAGUARD_CONFIG

V$DATAGUARD_CONFIG displays the unique database names defined with the DB_UNIQUE_NAME and LOG_ARCHIVE_CONFIG initialization parameters, providing a view of the Oracle Data Guard environment from any database in the configuration.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DB_UNIQUE_NAME | VARCHAR2(30) |  |
| PARENT_DBUN | VARCHAR2(30) |  |
| DEST_ROLE | VARCHAR2(17) |  |
| CURRENT_SCN | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

The first row of the view lists the unique database name of the current database that was specified with the DB_UNIQUE_NAME initialization parameter. Additional rows reflect the unique database names of the other databases in the configuration that were specified with the DG_CONFIG keyword of the LOG_ARCHIVE_CONFIG initialization parameter. See Also: " DB_UNIQUE_NAME " " LOG_ARCHIVE_CONFIG " See Also: " DB_UNIQUE_NAME " " LOG_ARCHIVE_CONFIG "