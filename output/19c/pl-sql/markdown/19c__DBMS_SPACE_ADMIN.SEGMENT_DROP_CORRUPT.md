---
id: 19c__DBMS_SPACE_ADMIN.SEGMENT_DROP_CORRUPT
name: DBMS_SPACE_ADMIN.SEGMENT_DROP_CORRUPT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.SEGMENT_DROP_CORRUPT

This procedure drops a segment currently marked corrupt (without reclaiming space).

## Syntax

```sql
DBMS_SPACE_ADMIN.SEGMENT_DROP_CORRUPT (
   tablespace_name         IN    VARCHAR2,
   header_relative_file    IN    POSITIVE,
   header_block            IN    NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tablespace_name | VARCHAR2 | IN | Name of tablespace in which segment resides |
| header_relative_file | POSITIVE | IN | Relative file number of segment header |
| header_block | NUMBER) | IN | Block number of segment header |

## Usage Notes

For this to work, the segment must be marked temporary . To mark a corrupt segment as temporary, issue a DROP command on the segment. Syntax DBMS_SPACE_ADMIN.SEGMENT_DROP_CORRUPT ( tablespace_name IN VARCHAR2, header_relative_file IN POSITIVE, header_block IN NUMBER); Parameters Table 159-9 SEGMENT_DROP_CORRUPT Procedure Parameters Parameter Description tablespace_name Name of tablespace in which segment resides header_relative_file Relative file number of segment header header_block Block number of segment header Usage Notes The space for the segment is not released, and it must be fixed by using the TABLESPACE_FIX_BITMAPS Procedure or the TABLESPACE_REBUILD_BITMAPS Procedure . The procedure cannot be used on the SYSTEM tablespace. You can determine the relative file number and block number ( header_relative_file and header_block parameter) of the segment header block by querying DBA_SEGMENTS . Examples EXECUTE DBMS_SPACE_ADMIN.SEGMENT_DROP_CORRUPT('USERS', 4, 33);