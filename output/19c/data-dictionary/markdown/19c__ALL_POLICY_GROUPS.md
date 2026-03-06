---
id: 19c__ALL_POLICY_GROUPS
name: ALL_POLICY_GROUPS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_POLICY_GROUPS.html
---

# ALL_POLICY_GROUPS

ALL_POLICY_GROUPS describes the policy groups defined for the synonyms, tables, and views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_OWNER | VARCHAR2(128) | Owner of the synonym, table, or view |
| OBJECT_NAME | VARCHAR2(128) | Name of the synonym, table, or view |
| POLICY_GROUP | VARCHAR2(128) | Name of the policy group |
| COMMON | VARCHAR2(3) | Indicates whether the policy group is applied and enforced in all application PDBs ( YES ) or only in the local PDB ( NO ) |
| INHERITED | VARCHAR2(3) | Indicates whether the policy group is inherited from the root ( YES ) or not ( NO ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_POLICY_GROUPS describes all policy groups in the database. USER_POLICY_GROUPS describes the policy groups defined for the synonyms, tables, and views owned by the current user. This view does not display the OBJECT_OWNER column. See Also: " DBA_POLICY_GROUPS " " USER_POLICY_GROUPS " See Also: " DBA_POLICY_GROUPS " " USER_POLICY_GROUPS "