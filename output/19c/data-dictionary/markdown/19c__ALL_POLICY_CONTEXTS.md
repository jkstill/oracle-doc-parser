---
id: 19c__ALL_POLICY_CONTEXTS
name: ALL_POLICY_CONTEXTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_POLICY_CONTEXTS.html
---

# ALL_POLICY_CONTEXTS

ALL_POLICY_CONTEXTS describes the driving contexts defined for the synonyms, tables, and views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_OWNER | VARCHAR2(128) | Owner of the synonym, table, or view |
| OBJECT_NAME | VARCHAR2(128) | Name of the synonym, table, or view |
| NAMESPACE | VARCHAR2(128) | Namespace of the driving context |
| ATTRIBUTE | VARCHAR2(128) | Attribute of the driving context |
| COMMON | VARCHAR2(3) | Indicates whether the policy context is applied and enforced in all application PDBs ( YES ) or only in the local PDB ( NO ) |
| INHERITED | VARCHAR2(3) | Indicates whether the policy context is inherited from the root ( YES ) or not ( NO ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_POLICY_CONTEXTS describes all driving contexts in the database. USER_POLICY_CONTEXTS describes the driving contexts defined for the synonyms, tables, and views owned by the current user. This view does not display the OBJECT_OWNER column. See Also: " DBA_POLICY_CONTEXTS " " USER_POLICY_CONTEXTS " See Also: " DBA_POLICY_CONTEXTS " " USER_POLICY_CONTEXTS "