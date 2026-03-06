---
id: 19c__ALL_MINING_MODEL_XFORMS
name: ALL_MINING_MODEL_XFORMS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_MINING_MODEL_XFORMS.html
---

# ALL_MINING_MODEL_XFORMS

ALL_MINING_MODEL_XFORMS describes the user-specified transformations embedded in all models accessible to the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Name of the model owner |
| MODEL_NAME | VARCHAR2(128) | Name of the model |
| ATTRIBUTE_NAME | VARCHAR2(128) | Name of the attribute used in the transformation |
| ATTRIBUTE_SUBNAME | VARCHAR2(4000) | Subname of the attribute used in the transformation |
| ATTRIBUTE_SPEC | VARCHAR2(4000) | Attribute specification provided to model training |
| EXPRESSION | CLOB | Transformation expression provided to model training |
| REVERSE | VARCHAR2(3) | Indicates whether the specified transformation is a reverse transformation ( YES ) or a forward expression ( NO ) |

## Usage Notes

Related Views DBA_MINING_MODEL_XFORMS describes the user-specified transformations embedded in all models accessible in the system. USER_MINING_MODEL_XFORMS describes the user-specified transformations embedded with the user's own models. This view does not display the OWNER column.