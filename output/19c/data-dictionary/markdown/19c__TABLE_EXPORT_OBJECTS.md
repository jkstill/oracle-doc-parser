---
id: 19c__TABLE_EXPORT_OBJECTS
name: TABLE_EXPORT_OBJECTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
source_file: TABLE_EXPORT_OBJECTS.html
---

# TABLE_EXPORT_OBJECTS

TABLE_EXPORT_OBJECTS lists simple path names for some of the object types belonging to a Data Pump schema export, which is invoked using the TABLES parameter on the expdp command.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_PATH | VARCHAR2(200) | Simple path name for the object type |
| COMMENTS | VARCHAR2(2000) | Comment on the object type |
| NAMED | CHAR(1) | Do objects of this type have names? If yes ( Y ), then the name can be specified in the optional name_clause on the EXCLUDE and INCLUDE parameters. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Users of the Data Pump Export and Import utilities can query this view to determine valid values for the EXCLUDE and INCLUDE parameters. See Also: " DATABASE_EXPORT_OBJECTS " " SCHEMA_EXPORT_OBJECTS " Oracle Database Utilities for more information on performing a full Data Pump export using the expdp command See Also: " DATABASE_EXPORT_OBJECTS " " SCHEMA_EXPORT_OBJECTS " Oracle Database Utilities for more information on performing a full Data Pump export using the expdp command