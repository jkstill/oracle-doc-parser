---
id: 19c__DBA_PROFILES
name: DBA_PROFILES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_PROFILES.html
---

# DBA_PROFILES

DBA_PROFILES displays all profiles and their limits.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PROFILE | VARCHAR2(128) | Profile name |
| RESOURCE_NAME | VARCHAR2(32) | Resource name |
| RESOURCE_TYPE | VARCHAR2(8) | Indicates whether the resource profile is a KERNEL or a PASSWORD parameter |
| LIMIT | VARCHAR2(128) | Limit placed on this resource for this profile |
| COMMON | VARCHAR2(3) | Indicates whether a given profile is common. Possible values: YES if a profile is common NO if a profile is local (not common) |
| INHERITED | VARCHAR2(3) | Indicates whether the profile definition was inherited from another container ( YES ) or not ( NO ) |
| IMPLICIT | VARCHAR2(3) | Indicates whether this profile was created by an implicit application ( YES ) or not ( NO ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content