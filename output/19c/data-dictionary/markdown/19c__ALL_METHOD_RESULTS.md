---
id: 19c__ALL_METHOD_RESULTS
name: ALL_METHOD_RESULTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_METHOD_RESULTS.html
---

# ALL_METHOD_RESULTS

ALL_METHOD_RESULTS describes the method results of the object types accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the type |
| TYPE_NAME | VARCHAR2(128) | Name of the type |
| METHOD_NAME | VARCHAR2(128) | Name of the method |
| METHOD_NO | NUMBER | For an overloaded method, a number distinguishing this method from others of the same. Do not confuse this number with the object ID. |
| RESULT_TYPE_MOD | VARCHAR2(7) | Whether this result is a REF to another object |
| RESULT_TYPE_OWNER | VARCHAR2(128) | Owner of the type of the result |
| RESULT_TYPE_NAME | VARCHAR2(128) | Name of the type of the result |
| CHARACTER_SET_NAME | VARCHAR2(44) | Whether the character set or the method is fixed-length character set ( CHAR_CS ) or fixed-length national character set ( NCHAR_CS ), or a particular character set specified by the user |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_METHOD_RESULTS describes the method results of all object types in the database. USER_METHOD_RESULTS describes the method results of the object types owned by the current user. This view does not display the OWNER column. See Also: " DBA_METHOD_RESULTS " " USER_METHOD_RESULTS " See Also: " DBA_METHOD_RESULTS " " USER_METHOD_RESULTS "