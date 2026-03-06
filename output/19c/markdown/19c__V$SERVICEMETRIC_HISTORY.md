---
id: 19c__V$SERVICEMETRIC_HISTORY
name: V$SERVICEMETRIC_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-SERVICEMETRIC_HISTORY.html
---

# V$SERVICEMETRIC_HISTORY

Begin timestamp for the interval period

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| INTSIZE_CSEC | NUMBER |  |
| GROUP_ID | NUMBER |  |
| SERVICE_NAME_HASH | NUMBER |  |
| SERVICE_NAME | VARCHAR2(64) |  |
| CTMHASH | NUMBER |  |
| ELAPSEDPERCALL | NUMBER |  |
| CPUPERCALL | NUMBER |  |
| DBTIMEPERCALL | NUMBER |  |
| CALLSPERSEC | NUMBER |  |
| DBTIMEPERSEC | NUMBER |  |
| CON_ID | NUMBER |  |