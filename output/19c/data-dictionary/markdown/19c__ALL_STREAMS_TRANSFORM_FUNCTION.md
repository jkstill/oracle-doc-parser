---
id: 19c__ALL_STREAMS_TRANSFORM_FUNCTION
name: ALL_STREAMS_TRANSFORM_FUNCTION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_STREAMS_TRANSFORM_FUNCTION.html
---

# ALL_STREAMS_TRANSFORM_FUNCTION

ALL_STREAMS_TRANSFORM_FUNCTION displays information about the rule-based transformation functions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RULE_OWNER | VARCHAR2(128) | Owner of the rule associated with the transformation function |
| RULE_NAME | VARCHAR2(128) | Name of the rule associated with the transformation function |
| VALUE_TYPE | VARCHAR2(4000) | Type of the transformation function name. This type must be VARCHAR2 for a rule-based transformation to work properly. |
| TRANSFORM_FUNCTION_NAME | VARCHAR2(4000) | Name of the transformation function (NULL if VALUE_TYPE is not VARCHAR2 ) |
| CUSTOM_TYPE | VARCHAR2(11) | Type of the transformation function: ONE TO ONE - One-to-one transformations ONE TO MANY - One-to-many transformations |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_STREAMS_TRANSFORM_FUNCTION displays information about all rule-based transformation functions in the database. See Also: " DBA_STREAMS_TRANSFORM_FUNCTION " See Also: " DBA_STREAMS_TRANSFORM_FUNCTION "