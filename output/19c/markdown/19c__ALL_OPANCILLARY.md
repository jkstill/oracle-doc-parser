---
id: 19c__ALL_OPANCILLARY
name: ALL_OPANCILLARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_OPANCILLARY.html
---

# ALL_OPANCILLARY

ALL_OPANCILLARY describes operators whose bindings are ancillary to other (primary) operators.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the ancillary operator |
| OPERATOR_NAME | VARCHAR2(128) | Name of the ancillary operator |
| BINDING# | NUMBER | Binding number of the ancillary operator |
| PRIMOP_OWNER | VARCHAR2(128) | Owner of the primary operator |
| PRIMOP_NAME | VARCHAR2(128) | Name of the primary operator |
| PRIMOP_BIND# | NUMBER | Binding number of the primary operator |

## Usage Notes

Related Views DBA_OPANCILLARY describes such information about all operators in the database. USER_OPANCILLARY describes such information about operators owned by the current user. See Also: " DBA_OPANCILLARY " " USER_OPANCILLARY " See Also: " DBA_OPANCILLARY " " USER_OPANCILLARY "