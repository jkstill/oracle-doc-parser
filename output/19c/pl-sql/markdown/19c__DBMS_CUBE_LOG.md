---
id: 19c__DBMS_CUBE_LOG
name: DBMS_CUBE_LOG
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG

The Cube Rejected Records log contains a summary of the loader job and any records that were rejected because they did not meet the expected format.

## Usage Notes

A single row in the source table may have errors in more than one field. Each field generates an error in the log, resulting in multiple rows with the same rowid4 in the SOURCE_ROW column. The default name of the Cube Rejected Records log is CUBE_REJECTED_RECORDS . The following table describes its contents.