---
id: 19c__DBMS_SPACE_ADMIN.TABLESPACE_VERIFY
name: DBMS_SPACE_ADMIN.TABLESPACE_VERIFY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.TABLESPACE_VERIFY

This procedure verifies that the bitmaps and extent maps for the segments in the tablespace are synchronized.

## Syntax

```sql
DBMS_SPACE_ADMIN.TABLESPACE_VERIFY (
   tablespace_name         IN    VARCHAR2,
   verify_option           IN    POSITIVE DEFAULT TABLESPACE_VERIFY_BITMAP);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tablespace_name | VARCHAR2 | IN | Name of tablespace |
| verify_option | POSITIVE | IN | One option is supported: TABLESPACE_VERIFY_BITMAP |

## Usage Notes

Syntax DBMS_SPACE_ADMIN.TABLESPACE_VERIFY ( tablespace_name IN VARCHAR2, verify_option IN POSITIVE DEFAULT TABLESPACE_VERIFY_BITMAP); Parameters Table 159-20 TABLESPACE_VERIFY Procedure Parameters Parameter Description tablespace_name Name of tablespace verify_option One option is supported: TABLESPACE_VERIFY_BITMAP Examples EXECUTE DBMS_SPACE_ADMIN.TABLESPACE_VERIFY('USERS');