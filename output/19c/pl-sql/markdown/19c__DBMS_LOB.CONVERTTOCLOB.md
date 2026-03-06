---
id: 19c__DBMS_LOB.CONVERTTOCLOB
name: DBMS_LOB.CONVERTTOCLOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.CONVERTTOCLOB

This procedure takes a source BLOB instance, converts the binary data in the source instance to character data using the character set you specify, writes the character data to a destination CLOB or NCLOB instance, and returns the new offsets.

## Syntax

```sql
DBMS_LOB.CONVERTTOCLOB(
   dest_lob       IN OUT NOCOPY  CLOB CHARACTER SET ANY_CS,
   src_blob       IN             BLOB,
   amount         IN             INTEGER,
   dest_offset    IN OUT         INTEGER,
   src_offset     IN OUT         INTEGER, 
   blob_csid      IN             NUMBER,
   lang_context   IN OUT         INTEGER,
   warning        OUT            INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dest_lob | NOCOPY | IN OUT | LOB locator of the destination LOB instance. |
| src_blob | BLOB | IN | LOB locator of the source LOB instance. |
| amount | INTEGER | IN | Number of bytes to convert from the source LOB. If you want to copy the entire BLOB, pass the constant DBMS_LOB . LOBMAXSIZE . If you pass any other value, it must be less than or equal to the size of the BLOB . |
| dest_offset | INTEGER | IN OUT | (IN) Offset in characters in the destination LOB for the start of the write. Specify a value of 1 to start at the beginning of the LOB. (OUT) The new offset in characters after the end of the write. This offset always points to the beginning of the first complete character after the end of the write. |
| src_offset | INTEGER | IN OUT | (IN) Offset in bytes in the source LOB for the start of the read. (OUT) Offset in bytes in the source LOB right after the end of the read. |
| blob_csid | NUMBER | IN | The character set ID of the source data |
| lang_context | INTEGER | IN OUT | ( IN ) Language context, such as shift status, for the current conversion. (OUT) The language context at the time when the current conversion is done. This information is returned so you can use it for subsequent conversions without losing or misinterpreting any source data. For the very first conversion, or if do not care, use the default value of zero. |
| warning | INTEGER) | OUT | Warning message. This parameter indicates when something abnormal happened during the conversion. You are responsible for checking the warning message. Currently, the only possible warning is — inconvertible character. This occurs when the character in the source cannot be properly converted to a character in destination. The default replacement character (for example, '?') is used in place of the inconvertible character. The return value of this error message is defined as the constant warn_inconvertible_char in the DBMS_LOB package. |

## Usage Notes

You can use this interface with any combination of persistent or temporary LOB instances as the source or destination. Syntax DBMS_LOB.CONVERTTOCLOB( dest_lob IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, src_blob IN BLOB, amount IN INTEGER, dest_offset IN OUT INTEGER, src_offset IN OUT INTEGER, blob_csid IN NUMBER, lang_context IN OUT INTEGER, warning OUT INTEGER); Parameters Table 99-19 CONVERTTOCLOB Procedure Parameters Parameter Description dest_lob LOB locator of the destination LOB instance. src_blob LOB locator of the source LOB instance. amount Number of bytes to convert from the source LOB. If you want to copy the entire BLOB, pass the constant DBMS_LOB . LOBMAXSIZE . If you pass any other value, it must be less than or equal to the size of the BLOB . dest_offset (IN) Offset in characters in the destination LOB for the start of the write. Specify a value of 1 to start at the beginning of the LOB. (OUT) The new offset in characters after the end of the write. This offset always points to the beginning of the first complete character after the end of the write. src_offset (IN) Offset in bytes in the source LOB for the start of the read. (OUT) Offset in bytes in the source LOB right after the end of the read. blob_csid The character set ID of the source data lang_context ( IN ) Language context, such as shift status, for the current conversion. (OUT) The language context at the time when the current conversion is done. This information is returned so you can use it for subsequent conversions without losing or misinterpreting any source data. For the very first conversion, or if do not care, use the default value of zero. warning Warning message. This parameter indicates when something abnormal happened during the conversion. You are responsible for checking the warning message. Currently, the only possible warning is — inconvertible character. This occurs when the character in the source cannot be properly converted to a character in destination. The default replacement character (for example, '?') is used in place of the inconvertible character. The return value of this error message is defined as the constant warn_inconvertible_char in the DBMS_LOB package. Usage Notes Preconditions Before calling the CONVERTTOCLOB procedure, the following preconditions must be met: Both the source and destination LOB instances must exist. If the destination LOB is a persistent LOB, the row must be locked before calling the CONVERTTOCLOB procedure. To lock the row, select the LOB using the FOR UPDATE clause of the SELECT statement. Constants and Defaults All parameters are required. You must pass a variable for each OUT or IN OUT parameter. You must pass either a variable or a value for each IN parameter. Table 99-20 gives a summary of typical values for each parameter. The first column lists the parameter, the second column lists the typical value, and the last column describes the result of passing the value. Note that constants are used for some values. These constants are defined in the dbmslob.sql package specification file. Table 99-20 DBMS_LOB.CONVERTTOCLOB Typical Values Parameter Value Description amount LOBMAXSIZE (IN) convert the entire file dest_offset 1 (IN) start from the beginning src_offset 1 (IN) start from the beginning csid DEFAULT_CSID (IN) default CSID , use destination CSID lang_context DEFAULT_LANG_CTX (IN) default language context warning NO_WARNING (OUT) WARN_INCONVERTIBLE_CHAR (OUT) no warning message, success character in source cannot be properly converted General Notes You must specify the desired character set for the source LOB in the blob_csid parameter. You can pass a zero value for blob_csid . When you do so, the database assumes that the desired character set is the same as the destianation LOB character set. You must specify the offsets for both the source and destination LOBs, and the number of characters to copy from the source LOB. The amount and src_offset values are in bytes and the dest_offset is in characters. To convert the entire LOB, you can specify LOBMAXSIZE for the amount parameter. CONVERTTOCLOB gets the source and/or destination LOBs as necessary prior to conversion and write of the data. Exceptions Table 99-21 CONVERTTOCLOB Procedure Exceptions Exception Description VALUE_ERROR Any of the input parameters are NULL or INVALID . INVALID_ARGVAL One or more of the following: - src_offset or dest_offset < 1. - src_offset or dest_offset > LOBMAXSIZE . - amount < 1. - amount > LOBMAXSIZE . See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for more information on using LOBs in application development