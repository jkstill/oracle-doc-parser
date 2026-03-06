---
id: 19c__ALL_FILE_GROUP_EXPORT_INFO
name: ALL_FILE_GROUP_EXPORT_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_FILE_GROUP_EXPORT_INFO.html
---

# ALL_FILE_GROUP_EXPORT_INFO

DBA_FILE_GROUP_EXPORT_INFO shows export-related information for each version in the database that has a valid Data Pump dump file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE_GROUP_OWNER | VARCHAR2(128) | Owner of the file group |
| FILE_GROUP_NAME | VARCHAR2(128) | Name of the file group |
| VERSION_NAME | VARCHAR2(128) | User-specified name for the version |
| VERSION | NUMBER | Internal version number |
| EXPORT_VERSION | VARCHAR2(128) | Version of exported objects |
| PLATFORM_NAME | VARCHAR2(101) | Platform on which the export was performed |
| EXPORT_TIME | DATE | Time at which the export job was performed |
| EXPORT_SCN | NUMBER | SCN of the export job |
| SOURCE_GLOBAL_NAME | VARCHAR2(128) | Global name of the exporting database |

## Usage Notes

Related Views DBA_FILE_GROUP_EXPORT_INFO shows export-related information for each version in the database that has a valid Data Pump dump file. USER_FILE_GROUP_EXPORT_INFO shows export-related information for all file groups owned by the current user. This view does not display the FILE_GROUP_OWNER column. See Also: " DBA_FILE_GROUP_EXPORT_INFO " " USER_FILE_GROUP_EXPORT_INFO " See Also: " DBA_FILE_GROUP_EXPORT_INFO " " USER_FILE_GROUP_EXPORT_INFO "