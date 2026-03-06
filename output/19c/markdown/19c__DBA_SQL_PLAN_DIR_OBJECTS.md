---
id: 19c__DBA_SQL_PLAN_DIR_OBJECTS
name: DBA_SQL_PLAN_DIR_OBJECTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_SQL_PLAN_DIR_OBJECTS.html
---

# DBA_SQL_PLAN_DIR_OBJECTS

DBA_SQL_PLAN_DIR_OBJECTS displays the objects created in the SQL plan directive.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DIRECTIVE_ID | NUMBER | The identifier of the SQL plan directive |
| OWNER | VARCHAR2(128) | The username of the owner of the object in the SQL plan directive |
| OBJECT_NAME | VARCHAR2(128) | The name of the object in the SQL plan directive |
| SUBOBJECT_NAME | VARCHAR2(128) | The name of the subobject (for example, column) in the SQL plan directive |
| OBJECT_TYPE | VARCHAR2(6) | The type of the subobject in the SQL plan directive |
| NUM_ROWS | NUMBER | The number of rows in the object when the directive is created |
| NOTES | XMLTYPE | Other notes about the object |

## Usage Notes

See Also: " DBA_SQL_PLAN_DIRECTIVES " Oracle Database SQL Tuning Guide for more information about SQL plan directives See Also: " DBA_SQL_PLAN_DIRECTIVES " Oracle Database SQL Tuning Guide for more information about SQL plan directives