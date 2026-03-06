---
id: 19c__ALL_SEC_RELEVANT_COLS
name: ALL_SEC_RELEVANT_COLS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SEC_RELEVANT_COLS.html
---

# ALL_SEC_RELEVANT_COLS

ALL_SEC_RELEVANT_COLS describes the security relevant columns of the security policies for the tables and views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_OWNER | VARCHAR2(128) | Owner of the table or view |
| OBJECT_NAME | VARCHAR2(128) | Name of the table or view |
| POLICY_GROUP | VARCHAR2(128) | Name of the policy group |
| POLICY_NAME | VARCHAR2(128) | Name of the policy |
| SEC_REL_COLUMN | VARCHAR2(128) | Name of the security relevant column |
| COLUMN_OPTION | VARCHAR2(8) | Option of the security relevant column: NONE ALL_ROWS |
| COMMON | VARCHAR2(3) | Indicates whether the policy security relevant column is applied and enforced in all application PDBs ( YES ) or only in the local PDB ( NO ) |
| INHERITED | VARCHAR2(3) | Indicates whether the policy security relevant column is inherited from the root ( YES ) or not ( NO ) |

## Usage Notes

Related Views DBA_SEC_RELEVANT_COLS describes the security relevant columns of all security policies in the database. USER_SEC_RELEVANT_COLS describes the security relevant columns of the security policies for the tables and views owned by the current user. This view does not display the OBJECT_OWNER column. See Also: " DBA_SEC_RELEVANT_COLS " " USER_SEC_RELEVANT_COLS " See Also: " DBA_SEC_RELEVANT_COLS " " USER_SEC_RELEVANT_COLS "