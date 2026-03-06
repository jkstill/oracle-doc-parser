---
id: 19c__ALL_ASSEMBLIES
name: ALL_ASSEMBLIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_ASSEMBLIES.html
---

# ALL_ASSEMBLIES

ALL_ASSEMBLIES provides information about assemblies accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the assembly |
| ASSEMBLY_NAME | VARCHAR2(128) | Name of the assembly |
| FILE_SPEC | VARCHAR2(4000) | Operating system file specification of the assembly |
| SECURITY_LEVEL | VARCHAR2(10) | The maximum security level of the assembly |
| IDENTITY | VARCHAR2(4000) | The identity of the assembly |
| STATUS | VARCHAR2(7) | Status of the assembly |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_ASSEMBLIES provides information about all assemblies in the database. USER_ASSEMBLIES provides information about all assemblies owned by the current user. This view does not display the OWNER column. See Also: " DBA_ASSEMBLIES " " USER_ASSEMBLIES " See Also: " DBA_ASSEMBLIES " " USER_ASSEMBLIES "