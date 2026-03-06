---
id: 19c__DBMS_SPACE_ADMIN.TABLESPACE_FIX_SEGMENT_STATES
name: DBMS_SPACE_ADMIN.TABLESPACE_FIX_SEGMENT_STATES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.TABLESPACE_FIX_SEGMENT_STATES

This procedure fixes the state of the segments in a tablespace in which migration was aborted.

## Syntax

```sql
DBMS_SPACE_ADMIN.TABLESPACE_FIX_SEGMENT_STATES (
   tablespace_name     IN    VARCHAR);
```

## Usage Notes

During tablespace migration to or from local, the segments are put in a transient state. If migration is aborted, then the segment states are corrected by SMON when event 10906 is set. A database with segments in such a transient state cannot be downgraded. The procedure can be used to fix the state of such segments. Syntax DBMS_SPACE_ADMIN.TABLESPACE_FIX_SEGMENT_STATES ( tablespace_name IN VARCHAR); Parameters Table 159-14 TABLESPACE_FIX_SEGMENT_STATES Procedure Parameters Parameter Name Description tablespace_name Name of the tablespace whose segments must be fixed Usage Notes The tablespace must be kept online and read/write when this procedure is called. Examples EXECUTE DBMS_SPACE_ADMIN.TABLESPACE_FIX_SEGMENT_STATES('TS1')