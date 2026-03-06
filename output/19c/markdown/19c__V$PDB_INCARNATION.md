---
id: 19c__V$PDB_INCARNATION
name: V$PDB_INCARNATION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-PDB_INCARNATION.html
---

# V$PDB_INCARNATION

Database incarnation number

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DB_INCARNATION# | NUMBER |  |
| PDB_INCARNATION# | NUMBER |  |
| STATUS | VARCHAR2(7) |  |
| INCARNATION_SCN | NUMBER |  |
| INCARNATION_TIME | DATE |  |
| BEGIN_RESETLOGS_SCN | NUMBER |  |
| BEGIN_RESETLOGS_TIME | DATE |  |
| END_RESETLOGS_SCN | NUMBER |  |
| END_RESETLOGS_TIME | DATE |  |
| PRIOR_DB_INCARNATION# | NUMBER |  |
| PRIOR_PDB_INCARNATION# | VARCHAR2(40) |  |
| FLASHBACK_DATABASE_ALLOWED | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |