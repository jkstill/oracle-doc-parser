---
id: 19c__V$DATABASE_INCARNATION
name: V$DATABASE_INCARNATION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DATABASE_INCARNATION.html
---

# V$DATABASE_INCARNATION

V$DATABASE_INCARNATION displays information about all database incarnations.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INCARNATION# | NUMBER |  |
| RESETLOGS_CHANGE# | NUMBER |  |
| RESETLOGS_TIME | DATE |  |
| PRIOR_RESETLOGS_CHANGE# | NUMBER |  |
| PRIOR_RESETLOGS_TIME | DATE |  |
| STATUS | VARCHAR2(7) |  |
| RESETLOGS_ID | NUMBER |  |
| PRIOR_INCARNATION# | NUMBER |  |
| FLASHBACK_DATABASE_ALLOWED | VARCHAR2(26) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Oracle creates a new incarnation whenever a database is opened with the RESETLOGS option. Records about the current and immediately previous incarnation are also contained in the V$DATABASE view. See Also: " V$DATABASE " See Also: " V$DATABASE "