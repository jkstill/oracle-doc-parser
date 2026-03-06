---
id: 19c__DBA_EPG_DAD_AUTHORIZATION
name: DBA_EPG_DAD_AUTHORIZATION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_EPG_DAD_AUTHORIZATION.html
---

# DBA_EPG_DAD_AUTHORIZATION

DBA_EPG_DAD_AUTHORIZATION describes the DADs that are authorized to use different user's privileges.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DAD_NAME | VARCHAR2(64) | Name of DAD |
| USERNAME | VARCHAR2(128) | Name of the user whose privileges the DAD is authorized to use |

## Usage Notes

Related View USER_EPG_DAD_AUTHORIZATION describes the DADs that are authorized to use the user's privileges. This view does not display the USERNAME column. See Also: " USER_EPG_DAD_AUTHORIZATION " See Also: " USER_EPG_DAD_AUTHORIZATION "