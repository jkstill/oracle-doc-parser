---
id: 19c__UTL_FILE.FOPEN
name: UTL_FILE.FOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.FOPEN

This function opens a file. You can specify the maximum line size and have a maximum of 50 files open simultaneously.

## Syntax

```sql
UTL_FILE.FOPEN (
   location     IN VARCHAR2,
   filename     IN VARCHAR2,
   open_mode    IN VARCHAR2,
   max_linesize IN BINARY_INTEGER DEFAULT 1024) 
  RETURN FILE_TYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| location | VARCHAR2 | IN | Directory location of file. This string is a directory object name and must be specified in upper case. Read privileges must be granted on this directory object for the UTL_FILE user to run FOPEN . |
| filename | VARCHAR2 | IN | File name, including extension (file type), without directory path. If a directory path is given as a part of the filename, it is ignored by FOPEN . On Unix, the filename cannot end with /. |
| open_mode | VARCHAR2 | IN | Specifies how the file is opened. Modes include: r -- read text w -- write text a -- append text rb -- read byte mode wb -- write byte mode ab -- append byte mode If you try to open a file specifying ' a ' or ' ab ' for open_mode but the file does not exist, the file is created in write mode. |
| max_linesize | BINARY_INTEGER | IN | Maximum number of bytes for each line, including the newline character, for this file (minimum value 1, maximum value 32767). If unspecified, Oracle supplies a default value of 1024. |

**Returns:** `FILE_TYPE`

## Usage Notes

See also FOPEN_NCHAR Function . Syntax UTL_FILE.FOPEN ( location IN VARCHAR2, filename IN VARCHAR2, open_mode IN VARCHAR2, max_linesize IN BINARY_INTEGER DEFAULT 1024) RETURN FILE_TYPE; Parameters Table 263-9 FOPEN Function Parameters Parameter Description location Directory location of file. This string is a directory object name and must be specified in upper case. Read privileges must be granted on this directory object for the UTL_FILE user to run FOPEN . filename File name, including extension (file type), without directory path. If a directory path is given as a part of the filename, it is ignored by FOPEN . On Unix, the filename cannot end with /. open_mode Specifies how the file is opened. Modes include: r -- read text w -- write text a -- append text rb -- read byte mode wb -- write byte mode ab -- append byte mode If you try to open a file specifying ' a ' or ' ab ' for open_mode but the file does not exist, the file is created in write mode. max_linesize Maximum number of bytes for each line, including the newline character, for this file (minimum value 1, maximum value 32767). If unspecified, Oracle supplies a default value of 1024. Return Values FOPEN returns a file handle, which must be passed to all subsequent procedures that operate on that file. The specific contents of the file handle are private to the UTL_FILE package, and individual components should not be referenced or changed by the UTL_FILE user. Table 263-10 FOPEN Function Return Values Return Description FILE_TYPE Handle to open file Exceptions INVALID_MAXILINESIZE INVALID_MODE INVALID_OPERATION INVALID_PATH INVALID_FILENAME