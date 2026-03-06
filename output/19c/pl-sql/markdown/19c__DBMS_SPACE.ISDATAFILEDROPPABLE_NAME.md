---
id: 19c__DBMS_SPACE.ISDATAFILEDROPPABLE_NAME
name: DBMS_SPACE.ISDATAFILEDROPPABLE_NAME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE
tags: [dbms_space]
source_file: DBMS_SPACE.html
---

# DBMS_SPACE.ISDATAFILEDROPPABLE_NAME

This procedure checks whether a datafile is droppable. This procedure may be called before actually dropping the file.

## Syntax

```sql
DBMS_SPACE.ISDATAFILEDROPPABLE_NAME (
   filename     IN     VARCHAR2, 
   value        OUT    NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| filename | VARCHAR2 | IN | Name of the file |
| value | NUMBER) | OUT | Values: 0 if the file is not droppable, 1 if the file is droppable. |

## Usage Notes

Syntax DBMS_SPACE.ISDATAFILEDROPPABLE_NAME ( filename IN VARCHAR2, value OUT NUMBER); Pragmas pragma restrict_references(free_blocks,WNDS); Parameters Table 158-9 ISDATAFILEDROPPABLE_NAME Procedure Parameters Parameter Description filename Name of the file value Values: 0 if the file is not droppable, 1 if the file is droppable. Examples DECLARE fname VARCHAR2(100); retval NUMBER;BEGIN SELECT file_name INTO fname FROM dba_data_files WHERE file_name like '%empty%';DBMS_SPACE.ISDATAFILEDROPPABLE_NAME(fname, retval);DBMS_OUTPUT.PUT_LINE(retval);END;/