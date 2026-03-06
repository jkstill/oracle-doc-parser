---
id: 19c__ALL_POLICY_ATTRIBUTES
name: ALL_POLICY_ATTRIBUTES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_POLICY_ATTRIBUTES.html
---

# ALL_POLICY_ATTRIBUTES

ALL_POLICY_ATTRIBUTES lists the attribute associations {Namespaces, Attributes} of context-sensitive and shared context-sensitive Oracle Virtual Private Database (VPD) policies for objects accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_OWNER | VARCHAR2(128) | Owner of the synonym, table, or view |
| OBJECT_NAME | VARCHAR2(128) | Name of the synonym, table, or view |
| POLICY_GROUP | VARCHAR2(128) | Name of the policy group |
| POLICY_NAME | VARCHAR2(128) | Name of the policy |
| NAMESPACE | VARCHAR2(128) | Name of the local application context |
| ATTRIBUTE | VARCHAR2(128) | Name of the attribute |
| COMMON | VARCHAR2(3) | Indicates whether the policy attribute is applied and enforced in all application PDBs ( YES ) or only in the local PDB ( NO ) |
| INHERITED | VARCHAR2(3) | Indicates whether the policy attribute is inherited from the root ( YES ) or not ( NO ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_POLICY_ATTRIBUTES lists the attribute associations {Namespaces, Attributes} of all context-sensitive and shared context-sensitive Oracle Virtual Private Database (VPD) policies in the database. USER_POLICY_ATTRIBUTES lists the attribute associations {Namespaces, Attributes} of all context-sensitive and shared-context sensitive Oracle Virtual Private Database (VPD) policies for synonyms, tables, or views owned by the user. See Also: " DBA_POLICY_ATTRIBUTES " " USER_POLICY_ATTRIBUTES " See Also: " DBA_POLICY_ATTRIBUTES " " USER_POLICY_ATTRIBUTES "