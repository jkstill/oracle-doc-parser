---
id: 19c__V$BH
name: V$BH
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BH.html
---

# V$BH

V$BH displays the status and number of pings for every buffer in the SGA. This is an Oracle Real Application Clusters view.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE# | NUMBER |  |
| BLOCK# | NUMBER |  |
| CLASS# | NUMBER |  |
| STATUS | VARCHAR2(10) |  |
| XNC | NUMBER |  |
| FORCED_READS | NUMBER |  |
| FORCED_WRITES | NUMBER |  |
| LOCK_ELEMENT_ADDR | RAW(4 | 8) |  |
| LOCK_ELEMENT_NAME | NUMBER |  |
| LOCK_ELEMENT_CLASS | NUMBER |  |
| DIRTY | VARCHAR2(1) |  |
| TEMP | VARCHAR2(1) |  |
| PING | VARCHAR2(1) |  |
| STALE | VARCHAR2(1) |  |
| DIRECT | VARCHAR2(1) |  |
| NEW | CHAR(1) |  |
| OBJD | NUMBER |  |
| TS# | NUMBER |  |
| LOBID | NUMBER |  |
| CACHEHINT | NUMBER |  |
| FLASH_CACHE | VARCHAR2(7) |  |
| CELL_FLASH_CACHE | VARCHAR2(7) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content