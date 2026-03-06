---
id: 19c__V$SYSAUX_OCCUPANTS
name: V$SYSAUX_OCCUPANTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dynamic_performance]
source_file: V-SYSAUX_OCCUPANTS.html
---

# V$SYSAUX_OCCUPANTS

V$SYSAUX_OCCUPANTS displays SYSAUX tablespace occupant information.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OCCUPANT_NAME | VARCHAR2(64) |  |
| OCCUPANT_DESC | VARCHAR2(64) |  |
| SCHEMA_NAME | VARCHAR2(64) |  |
| MOVE_PROCEDURE | VARCHAR2(64) |  |
| MOVE_PROCEDURE_DESC | VARCHAR2(64) |  |
| SPACE_USAGE_KBYTES | NUMBER |  |
| CON_ID | NUMBER |  |