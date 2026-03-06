---
id: 19c__DBMS_SPACE_ADMIN.SEGMENT_CORRUPT
name: DBMS_SPACE_ADMIN.SEGMENT_CORRUPT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.SEGMENT_CORRUPT

This procedure marks the segment corrupt or valid so that appropriate error recovery can be performed.

## Syntax

```sql
DBMS_SPACE_ADMIN.SEGMENT_CORRUPT (
   tablespace_name         IN    VARCHAR2,
   header_relative_file    IN    POSITIVE,
   header_block            IN    NUMBER,
   corrupt_option          IN    POSITIVE  DEFAULT SEGMENT_MARK_CORRUPT);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tablespace_name | VARCHAR2 | IN | Name of tablespace in which segment resides |
| header_relative_file | POSITIVE | IN | Relative file number of segment header |
| header_block | NUMBER | IN | Block number of segment header |
| corrupt_option | POSITIVE | IN | SEGMENT_MARK_CORRUPT (default) or SEGMENT_MARK_VALID |

## Usage Notes

It cannot be used on the SYSTEM tablespace. Syntax DBMS_SPACE_ADMIN.SEGMENT_CORRUPT ( tablespace_name IN VARCHAR2, header_relative_file IN POSITIVE, header_block IN NUMBER, corrupt_option IN POSITIVE DEFAULT SEGMENT_MARK_CORRUPT); Parameters Table 159-8 SEGMENT_CORRUPT Procedure Parameters Parameter Description tablespace_name Name of tablespace in which segment resides header_relative_file Relative file number of segment header header_block Block number of segment header corrupt_option SEGMENT_MARK_CORRUPT (default) or SEGMENT_MARK_VALID Usage Noes You can determine the relative file number and block number ( header_relative_file and header_block parameter) of the segment header block by querying DBA_SEGMENTS . Examples The following example marks the segment as corrupt: EXECUTE DBMS_SPACE_ADMIN.SEGMENT_CORRUPT('USERS', 4, 33, DBMS_SPACE_ADMIN.SEGMENT_MARK_CORRUPT); Alternately, the next example marks a corrupt segment valid: EXECUTE DBMS_SPACE_ADMIN.SEGMENT_CORRUPT('USERS', 4, 33, DBMS_SPACE_ADMIN.SEGMENT_MARK_VALID);