---
id: 19c__V$LOCKDOWN_RULES
name: V$LOCKDOWN_RULES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-LOCKDOWN_RULES.html
---

# V$LOCKDOWN_RULES

V$LOCKDOWN_RULES displays information about lockdown profile rules that are applicable in the pluggable database (PDB) where this view is queried.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RULE_TYPE | VARCHAR2(128) |  |
| RULE | VARCHAR2(128) |  |
| CLAUSE | VARCHAR2(128) |  |
| CLAUSE_OPTION | VARCHAR2(128) |  |
| STATUS | VARCHAR2(7) |  |
| USERS | VARCHAR2(6) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Security Guide for more information about PDB lockdown profiles See Also: Oracle Database Security Guide for more information about PDB lockdown profiles