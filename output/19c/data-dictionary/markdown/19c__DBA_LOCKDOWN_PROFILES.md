---
id: 19c__DBA_LOCKDOWN_PROFILES
name: DBA_LOCKDOWN_PROFILES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_LOCKDOWN_PROFILES.html
---

# DBA_LOCKDOWN_PROFILES

The script content on this page is for navigation purposes only and does not alter the content in any way.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PROFILE_NAME | VARCHAR2(128) | Name of the lockdown profile |
| RULE_TYPE | VARCHAR2(128) | Rule type. A lockdown profile is used to restrict operations that can be performed by users connected to a given PDB. It provides the ability to add or remove different types of rules like STATEMENT, FEATURES or OPTIONS which will be restricted in the PDB. |
| RULE | VARCHAR2(128) | Rule to be enabled or disabled |
| CLAUSE | VARCHAR2(128) | Clause of the statement |
| CLAUSE_OPTION | VARCHAR2(128) | Option of the clause |
| OPTION_VALUE | VARCHAR2(4000) | Value of the option |
| MIN_VALUE | VARCHAR2(4000) | Minimum value allowed for the option |
| MAX_VALUE | VARCHAR2(4000) | Maximum value allowed for the option |
| LIST | VARCHAR2(4000) | List of allowed values for the option |
| STATUS | VARCHAR2(7) | Status of the lockdown profile: ENABLE DISABLE EMPTY |
| USERS | VARCHAR2(6) | User type. Possible values: COMMON LOCAL ALL |
| EXCEPT_USERS Foot 1 | CLOB | For internal use only |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The PRIVATE_DBAAS , PUBLIC_DBAAS , and SAAS lockdown profiles are empty placeholder profiles for the lockdown profiles of their corresponding deployment type. You can modify and add restrictions to these profiles based on their deployment purpose. For example, if you have a Software as a Service (SAAS) application, you can modify the SAAS lockdown profile and use it. You can also delete and re-create these profiles. See Also: " PDB_LOCKDOWN " Oracle Multitenant Administrator's Guide for an introduction to PDB lockdown profiles Oracle Database SQL Language Reference for more information about creating lockdown profiles Oracle Database SQL Language Reference for more information about dropping lockdown profiles Oracle Database SQL Language Reference for more information about altering lockdown profiles See Also: " PDB_LOCKDOWN " Oracle Multitenant Administrator's Guide for an introduction to PDB lockdown profiles Oracle Database SQL Language Reference for more information about creating lockdown profiles Oracle Database SQL Language Reference for more information about dropping lockdown profiles Oracle Database SQL Language Reference for more information about altering lockdown profiles