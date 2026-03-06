---
id: 19c__V$ASM_ATTRIBUTE
name: V$ASM_ATTRIBUTE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_ATTRIBUTE.html
---

# V$ASM_ATTRIBUTE

V$ASM_ATTRIBUTE displays one row for each attribute defined. In addition to attributes specified by CREATE DISKGROUP and ALTER DISKGROUP statements, the view may show other attributes that are created automatically.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(256) |  |
| VALUE | VARCHAR2(256) |  |
| GROUP_NUMBER | NUMBER |  |
| ATTRIBUTE_INDEX | NUMBER |  |
| ATTRIBUTE_INCARNATION | NUMBER |  |
| READ_ONLY | VARCHAR2(7) |  |
| SYSTEM_CREATED | VARCHAR2(7) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note that attributes are only displayed for disk groups where COMPATIBLE.ASM is set to 11.1 or higher. See Also: Oracle Automatic Storage Management Administrator's Guide for more information about viewing Oracle ASM disk group attributes using this view Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information See Also: Oracle Automatic Storage Management Administrator's Guide for more information about viewing Oracle ASM disk group attributes using this view Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information