---
id: 19c__DBMS_LOB.READ
name: DBMS_LOB.READ
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.READ

This procedure reads a piece of a LOB, and returns the specified amount into the buffer parameter, starting from an absolute offset from the beginning of the LOB.

## Syntax

```sql
DBMS_LOB.READ (
   lob_loc   IN             BLOB,
   amount    IN OUT  NOCOPY INTEGER,
   offset    IN             INTEGER,
   buffer    OUT            RAW);

DBMS_LOB.READ (
   lob_loc   IN             CLOB CHARACTER SET ANY_CS,
   amount    IN OUT  NOCOPY INTEGER,
   offset    IN             INTEGER,
   buffer    OUT            VARCHAR2 CHARACTER SET lob_loc%CHARSET); 

DBMS_LOB.READ (
   file_loc   IN             BFILE,
   amount    IN OUT   NOCOPY INTEGER,
   offset    IN              INTEGER,
   buffer    OUT             RAW);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB | IN | Locator for the LOB to be read. For more information, see Operational Notes . |
| file_loc | BFILE | IN | The file locator for the LOB to be examined. |
| amount | NOCOPY | IN OUT | Number of bytes (for BLOBs ) or characters (for CLOBs ) to read, or number that were read. |
| offset | INTEGER | IN | Offset in bytes (for BLOBs ) or characters (for CLOBs ) from the start of the LOB (origin: 1). |
| buffer | RAW) | OUT | Output buffer for the read operation. |

## Usage Notes

The number of bytes or characters actually read is returned in the amount parameter. If the input offset points past the End of LOB, then amount is set to 0, and a NO_DATA_FOUND exception is raised. Syntax DBMS_LOB.READ ( lob_loc IN BLOB, amount IN OUT NOCOPY INTEGER, offset IN INTEGER, buffer OUT RAW); DBMS_LOB.READ ( lob_loc IN CLOB CHARACTER SET ANY_CS, amount IN OUT NOCOPY INTEGER, offset IN INTEGER, buffer OUT VARCHAR2 CHARACTER SET lob_loc%CHARSET); DBMS_LOB.READ ( file_loc IN BFILE, amount IN OUT NOCOPY INTEGER, offset IN INTEGER, buffer OUT RAW); Parameters Table 99-86 READ Procedure Parameters Parameter Description lob_loc Locator for the LOB to be read. For more information, see Operational Notes . file_loc The file locator for the LOB to be examined. amount Number of bytes (for BLOBs ) or characters (for CLOBs ) to read, or number that were read. offset Offset in bytes (for BLOBs ) or characters (for CLOBs ) from the start of the LOB (origin: 1). buffer Output buffer for the read operation. Exceptions Table 99-87 lists exceptions that apply to any LOB instance. Table 99-88 lists exceptions that apply only to BFILE s. Table 99-87 READ Procedure Exceptions Exception Description VALUE_ERROR Any of lob_loc , amount , or offset parameters are NULL . INVALID_ARGVAL Either: - amount < 1 - amount > 32767 bytes (or the character equivalent) - offset < 1 - offset > LOBMAXSIZE - amount is greater, in bytes or characters, than the capacity of buffer . NO_DATA_FOUND End of the LOB is reached, and there are no more bytes or characters to read from the LOB: amount has a value of 0. Table 99-88 READ Procedure Exceptions for BFILEs Exception Description UNOPENED_FILE File is not opened using the input locator. NOEXIST_DIRECTORY Directory does not exist. NOPRIV_DIRECTORY You do not have privileges for the directory. INVALID_DIRECTORY Directory has been invalidated after the file was opened. INVALID_OPERATION File does not exist, or you do not have access privileges on the file. BUFFERING_ENABLED Cannot perform operation with LOB buffering enabled if buffering is enabled on the LOB Usage Notes The form of the VARCHAR2 buffer must match the form of the CLOB parameter. In other words, if the input LOB parameter is of type NCLOB , then the buffer must contain NCHAR data. Conversely, if the input LOB parameter is of type CLOB , then the buffer must contain CHAR data. When calling DBMS_LOB . READ from the client (for example, in a BEGIN / END block from within SQL*Plus), the returned buffer contains data in the client's character set. The database converts the LOB value from the server's character set to the client's character set before it returns the buffer to the user. READ gets the LOB, if necessary, before the read. If the LOB is a DBFS LINK, data is streamed from DBFS, if possible, otherwise an exception is thrown. See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure