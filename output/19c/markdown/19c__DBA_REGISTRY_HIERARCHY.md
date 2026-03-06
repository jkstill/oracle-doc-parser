---
id: 19c__DBA_REGISTRY_HIERARCHY
name: DBA_REGISTRY_HIERARCHY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_REGISTRY_HIERARCHY.html
---

# DBA_REGISTRY_HIERARCHY

DBA_REGISTRY_HIERARCHY displays information about the components loaded into the database, grouped by owner and organized in the component hierarchy.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAMESPACE | VARCHAR2(30) | Component namespace |
| COMP_ID | VARCHAR2(4000) | Component identifier |
| VERSION | VARCHAR2(30) | Component version loaded |
| VERSION_FULL | VARCHAR2(30) | Component full version |
| STATUS | VARCHAR2(11) | Component status: INVALID VALID LOADING LOADED UPGRADING UPGRADED DOWNGRADING DOWNGRADED REMOVING REMOVED |
| MODIFIED | VARCHAR2(20) | Time when the component was last modified |