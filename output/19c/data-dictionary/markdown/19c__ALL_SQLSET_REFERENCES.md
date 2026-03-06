---
id: 19c__ALL_SQLSET_REFERENCES
name: ALL_SQLSET_REFERENCES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [all]
source_file: ALL_SQLSET_REFERENCES.html
---

# ALL_SQLSET_REFERENCES

ALL_SQLSET_REFERENCES describes whether or not the SQL tuning sets accessible to the current user are active.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SQLSET_NAME | VARCHAR2(128) | Name of the SQL tuning set |
| SQLSET_OWNER | VARCHAR2(128) | User name of SQL tuning set owner |
| SQLSET_ID | NUMBER | Identifier of the SQL tuning set |
| ID | NUMBER | Reference identifier |
| OWNER | VARCHAR2(128) | User who registered to use the SQL tuning set |
| DESCRIPTION | VARCHAR2(256) | Description of the usage of the SQL tuning set |
| CREATED | DATE | Date the reference was created |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_SQLSET_REFERENCES describes whether or not all SQL tuning sets in the database are active. A SQL tuning set cannot be dropped if it is referenced. USER_SQLSET_REFERENCES describes whether or not the SQL tuning sets owned by the current user are active. See Also: " DBA_SQLSET_REFERENCES " " USER_SQLSET_REFERENCES " See Also: " DBA_SQLSET_REFERENCES " " USER_SQLSET_REFERENCES "