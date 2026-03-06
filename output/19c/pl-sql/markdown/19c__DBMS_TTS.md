---
id: 19c__DBMS_TTS
name: DBMS_TTS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TTS
tags: [dbms_tts]
source_file: DBMS_TTS.html
---

# DBMS_TTS

With respect to transportable tablespaces, disabled and enabled referential integrity constraints are handled differently.

## Usage Notes

A disabled referential integrity constraint does not violate the transportability rules and is dropped during the import phase. An enabled referential integrity constraint violates the transportability rules if it references a table in a tablespace outside the transportable set.