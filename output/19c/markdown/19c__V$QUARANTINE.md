---
id: 19c__V$QUARANTINE
name: V$QUARANTINE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-QUARANTINE.html
---

# V$QUARANTINE

V$QUARANTINE provides information about quarantined objects.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT | VARCHAR2(64) |  |
| ADDRESS | RAW(8) |  |
| BYTES | NUMBER |  |
| ERROR | VARCHAR2(128) |  |
| TIMESTAMP | TIMESTAMP(6) WITH TIME ZONE |  |
| CON_ID | NUMBER |  |