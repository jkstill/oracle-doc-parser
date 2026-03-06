---
id: 19c__DBA_CONTAINER_DATA
name: DBA_CONTAINER_DATA
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_CONTAINER_DATA.html
---

# DBA_CONTAINER_DATA

DBA_CONTAINER_DATA displays default (user-level) and object-specific CONTAINER_DATA attributes for container data objects.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USERNAME | VARCHAR2(128) | Name of the user whose attribute is described by this row |
| DEFAULT_ATTR | CHAR2(1) | An indicator of whether the attribute is a default attribute |
| OWNER | VARCHAR2(128) | Name of the object owner if the attribute is object-specific |
| OBJECT_NAME | VARCHAR2(128) | Name of the object if the attribute is object-specific |
| ALL_CONTAINERS | VARCHAR2(1) | An indicator of whether this attribute applies to all containers |
| CONTAINER_NAME | VARCHAR2(128) | Name of a container included in this attribute if it does not apply to all containers |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Objects created with the CONTAINER_DATA clause include CONTAINER_DATA attributes. See Also: For more information about container data objects: " CDB_* Views " " ALL_TABLES " " ALL_VIEWS " " ALL_VIEWS_AE " " V$ Views " " GV$ Views " Oracle Multitenant Administrator's Guide Oracle Database Security Guide See Also: For more information about container data objects: " CDB_* Views " " ALL_TABLES " " ALL_VIEWS " " ALL_VIEWS_AE " " V$ Views " " GV$ Views " Oracle Multitenant Administrator's Guide Oracle Database Security Guide