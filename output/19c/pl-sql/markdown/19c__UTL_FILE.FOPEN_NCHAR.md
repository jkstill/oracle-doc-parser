---
id: 19c__UTL_FILE.FOPEN_NCHAR
name: UTL_FILE.FOPEN_NCHAR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.FOPEN_NCHAR

This function opens a file in national character set mode for input or output, with the maximum line size specified. With this function, you can read or write a text file in Unicode instead of in the database character set.

## Syntax

```sql
UTL_FILE.FOPEN_NCHAR (
   location     IN VARCHAR2,
   filename     IN VARCHAR2,
   open_mode    IN VARCHAR2,
   max_linesize IN BINARY_INTEGER DEFAULT 1024) 
RETURN FILE_TYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| location | VARCHAR2 | IN | Directory location of file |
| filename | VARCHAR2 | IN | File name (including extension) |
| open_mode | VARCHAR2 | IN | Open mode ( r , w , a , rb , wb , ab ) |
| max_linesize | BINARY_INTEGER | IN | Maximum number of characters for each line, including the newline character, for this file (minimum value 1, maximum value 32767) |

**Returns:** `FILE_TYPE`

## Usage Notes

You can have a maximum of 50 files open simultaneously. Even though the contents of an NVARCHAR2 buffer may be AL16UTF16 or UTF8 (depending on the national character set of the database), the contents of the file are always read and written in UTF8. UTL_FILE converts between UTF8 and AL16UTF16 as necessary. See also FOPEN Function . Syntax UTL_FILE.FOPEN_NCHAR ( location IN VARCHAR2, filename IN VARCHAR2, open_mode IN VARCHAR2, max_linesize IN BINARY_INTEGER DEFAULT 1024) RETURN FILE_TYPE; Parameters Table 263-11 FOPEN_NCHAR Function Parameters Parameter Description location Directory location of file filename File name (including extension) open_mode Open mode ( r , w , a , rb , wb , ab ) max_linesize Maximum number of characters for each line, including the newline character, for this file (minimum value 1, maximum value 32767) Return Values FOPEN_NCHAR returns a file handle, which must be passed to all subsequent procedures that operate on that file. The specific contents of the file handle are private to the UTL_FILE package, and individual components should not be referenced or changed by the UTL_FILE user. Table 263-12 FOPEN_NCHAR Function Return Values Return Description FILE_TYPE Handle to open file Exceptions INVALID_MAXILINESIZE INVALID_MODE INVALID_OPERATION INVALID_PATH