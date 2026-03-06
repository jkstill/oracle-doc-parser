---
id: 19c__DBMS_SPACE_ADMIN.SEGMENT_VERIFY
name: DBMS_SPACE_ADMIN.SEGMENT_VERIFY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.SEGMENT_VERIFY

This procedure checks the consistency of the segment extent map with the tablespace file bitmaps.

## Syntax

```sql
DBMS_SPACE_ADMIN.SEGMENT_VERIFY (
   tablespace_name         IN    VARCHAR2,
   header_relative_file    IN    POSITIVE,
   header_block            IN    NUMBER,
   verify_option           IN    POSITIVE  DEFAULT SEGMENT_VERIFY_EXTENTS);
```

## Usage Notes

Syntax DBMS_SPACE_ADMIN.SEGMENT_VERIFY ( tablespace_name IN VARCHAR2, header_relative_file IN POSITIVE, header_block IN NUMBER, verify_option IN POSITIVE DEFAULT SEGMENT_VERIFY_EXTENTS); Parameters Table 159-11 SEGMENT_VERIFY Procedure Parameters Parameters Description tablespace_name Name of tablespace in which segment resides header_relative_file Relative file number of segment header header_block Block number of segment header verify_option What kind of check to do: SEGMENT_VERIFY_EXTENTS or SEGMENT_VERIFY_EXTENTS_GLOBAL Usage Notes Anomalies are output as block range, bitmap-block, bitmap-block-range, anomaly-information, in the trace file for all block ranges found to have incorrect space representation. The kinds of problems which would be reported are free space not considered free, used space considered free, and the same space considered used by multiple segments. You can determine the relative file number and block number ( header_relative_file and header_block parameter) of the segment header block by querying DBA_SEGMENTS . Examples The following example verifies that the segment with segment header at relative file number 4, block number 33, has its extent maps and bitmaps synchronized. EXECUTE DBMS_SPACE_ADMIN.SEGMENT_VERIFY('USERS', 4, 33, DBMS_SPACE_ADMIN.SEGMENT_VERIFY_EXTENTS);