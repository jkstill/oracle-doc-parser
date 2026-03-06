---
id: 19c__ALL_OPARGUMENTS
name: ALL_OPARGUMENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_OPARGUMENTS.html
---

# ALL_OPARGUMENTS

ALL_OPARGUMENTS describes arguments for each operator binding accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the operator argument |
| OPERATOR_NAME | VARCHAR2(128) | Name of the operator argument |
| BINDING# | NUMBER | Binding number of the operator argument |
| POSITION | NUMBER | Position of the operator argument (1, 2, 3, ...) |
| ARGUMENT_TYPE | VARCHAR2(61) | Datatype of the operator argument |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_OPARGUMENTS describes arguments of all operator bindings in the database. USER_OPARGUMENTS describes arguments of all operator bindings owned by the current user. See Also: " DBA_OPARGUMENTS " " USER_OPARGUMENTS " See Also: " DBA_OPARGUMENTS " " USER_OPARGUMENTS "