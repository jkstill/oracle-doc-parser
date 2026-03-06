---
id: 19c__DBMS_LOB.CLOB2FILE
name: DBMS_LOB.CLOB2FILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.CLOB2FILE

This procedure writes the content of a CLOB into a bfile . This procedure gets called from the deprecated dbms_xslprocessor.clob2file internally.

## Syntax

```sql
DBMS_LOB.CLOB2FILE(
   src_cl      IN  CLOB,
   file_loc    IN  VARCHAR2,
   file_name   IN  VARCHAR2,
   csid        IN  NUMBER   := 0,
   open_mode   IN  VARCHAR2 :='wb');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| src_cl | CLOB | IN | Source CLOB locator to write into a file |
| file_loc | VARCHAR2 | IN | Directory object name where the file is located |
| file_name | VARCHAR2 | IN | File name |
| csid | NUMBER | IN | Character set id of the CLOB locator Must be a valid Oracle id; otherwise returns an error If the value is 0 , then the content of the output file will be in the database character set |
| open_mode | VARCHAR2 | IN | The mode to open the output file in. wb — write byte mode, overwrites the file The default value is wb. |

## Usage Notes

Syntax DBMS_LOB.CLOB2FILE( src_cl IN CLOB, file_loc IN VARCHAR2, file_name IN VARCHAR2, csid IN NUMBER := 0, open_mode IN VARCHAR2 :='wb'); Parameters Table 99-12 CLOB2FILE Procedure Parameters Parameter Description src_cl Source CLOB locator to write into a file file_loc Directory object name where the file is located file_name File name csid Character set id of the CLOB locator Must be a valid Oracle id; otherwise returns an error If the value is 0 , then the content of the output file will be in the database character set open_mode The mode to open the output file in. wb — write byte mode, overwrites the file The default value is wb.