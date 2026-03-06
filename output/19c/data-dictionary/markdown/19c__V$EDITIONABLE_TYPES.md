---
id: 19c__V$EDITIONABLE_TYPES
name: V$EDITIONABLE_TYPES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-EDITIONABLE_TYPES.html
---

# V$EDITIONABLE_TYPES

V$EDITIONABLE_TYPES lists all the editionable types based on the current compatibility setting. The SELECT privilege on V$EDITIONABLE_TYPES will be granted to PUBLIC .

## Columns

| Column | Type | Description |
|--------|------|-------------|
| EDITIONABLE_TYPE | VARCHAR2(64) |  |
| TYPE# | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The database compatibility setting will determine the set of editionable types. With compatibility set to 11.2 or 12, this set includes FUNCTION, LIBRARY, PACKAGE, PACKAGE BODY, PROCEDURE, SYNONYM, TRIGGER, TYPE, TYPE BODY, and VIEW. With compatibility set to 12, the set will include these types as well as the SQL TRANSLATION PROFILE. See Also: For more information about edition-based redefinitions, see Oracle Database Development Guide . See Also: For more information about edition-based redefinitions, see Oracle Database Development Guide .