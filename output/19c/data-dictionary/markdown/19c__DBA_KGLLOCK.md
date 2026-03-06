---
id: 19c__DBA_KGLLOCK
name: DBA_KGLLOCK
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_KGLLOCK.html
---

# DBA_KGLLOCK

DBA_KGLLOCK lists all the locks and pins held on KGL objects (objects in the Kernel Generic Library cache).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| kgllkuse | RAW(4) | Address of the user session that holds the lock or pin |
| kgllkhdl | RAW(4) | Address of the handle for the KGL object |
| kgllkmod | NUMBER | Current mode of the lock or pin |
| kgllkreq | NUMBER | Mode in which the lock or pin was requested |
| kgllktype | VARCHAR2(4) | Whether this is a lock or a pin |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content