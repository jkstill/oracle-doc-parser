---
id: 19c__DBA_OUTLINE_HINTS
name: DBA_OUTLINE_HINTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_OUTLINE_HINTS.html
---

# DBA_OUTLINE_HINTS

DBA_OUTLINE_HINTS describes the set of hints stored in all outlines in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(128) | Name of the outline |
| OWNER | VARCHAR2(128) | Name of the user who created the outline |
| NODE | NUMBER | ID of the query or subquery to which the hint applies. The top-level query is labeled 1 . Subqueries are assigned sequentially numbered labels, starting with 2 . |
| STAGE | NUMBER | Outline hints can be applied at three different stages during the compilation process. This column indicates the stage at which this hint was applied. |
| JOIN_POS | NUMBER | Position of the table in the join order. The value is 0 for all hints except access method hints, which identify a table to which the hint and the join position apply. |
| HINT | CLOB | Text of the hint |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_OUTLINE_HINTS describes the set of hints stored in the outlines owned by the current user. This view does not display the OWNER column. See Also: " USER_OUTLINE_HINTS " See Also: " USER_OUTLINE_HINTS "