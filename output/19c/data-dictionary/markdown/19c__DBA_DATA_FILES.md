---
id: 19c__DBA_DATA_FILES
name: DBA_DATA_FILES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_DATA_FILES.html
---

# DBA_DATA_FILES

DBA_DATA_FILES describes database files.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE_NAME | VARCHAR2(513) | Name of the database file |
| FILE_ID | NUMBER | Absolute file number of the database file |
| TABLESPACE_NAME | VARCHAR2(30) | Name of the tablespace to which the file belongs |
| BYTES | NUMBER | Size of the file in bytes |
| BLOCKS | NUMBER | Size of the file in Oracle blocks |
| STATUS | VARCHAR2(9) | File status: AVAILABLE or INVALID ( INVALID means that the file number is not in use, for example, a file in a tablespace that was dropped) |
| RELATIVE_FNO | NUMBER | Relative file number |
| AUTOEXTENSIBLE | VARCHAR2(3) | Autoextensible indicator |
| MAXBYTES | NUMBER | Maximum file size in bytes |
| MAXBLOCKS | NUMBER | Maximum file size in blocks |
| INCREMENT_BY | NUMBER | Number of Oracle blocks used as autoextension increment |
| USER_BYTES | NUMBER | The size of the file available for user data. The actual size of the file minus the USER_BYTES value is used to store file related metadata. |
| USER_BLOCKS | NUMBER | Number of blocks which can be used by the data |
| ONLINE_STATUS | VARCHAR2(7) | Online status of the file: SYSOFF SYSTEM OFFLINE ONLINE RECOVER |
| LOST_WRITE_PROTECT | VARCHAR2(7) | Lost write protection status of the file. Possible values: ENABLED : Indicates that lost write data is being collected OFF : Indicates that lost write data is not being collected SUSPEND : Indicates that lost write data is not currently being collected, but it can be enabled at a later date. The lost write data collected when the file was ENABLED remains in the lost write database, but it is not being checked or updated. If lost write protection is enabled for a single data file, it does not have to be enabled for another data file in the same tablespace. If lost write protection is enabled for a tablespace, it is enabled for all data files for that tablespace, including data files added later. You can check the lost write protection status for a tablespace by querying the LOST_WRITE_PROTECT column in the DBA_TABLESPACES view. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: When you query the DBA_DATA_FILES data dictionary view, Oracle must have access to all tablespaces and their data files if the requested information is not already available in the dictionary. If the tablespaces are encrypted, then you must open the Oracle wallet (keystore) before you can query DBA_DATA_FILES . You can use the ADMINISTER KEY MANAGEMENT SET KEYSTORE OPEN statement to open the keystore. Note: When you query the DBA_DATA_FILES data dictionary view, Oracle must have access to all tablespaces and their data files if the requested information is not already available in the dictionary. If the tablespaces are encrypted, then you must open the Oracle wallet (keystore) before you can query DBA_DATA_FILES . You can use the ADMINISTER KEY MANAGEMENT SET KEYSTORE OPEN statement to open the keystore. See Also: Oracle Database Advanced Security Guide for information on opening a software keystore Oracle Database Advanced Security Guide for information on opening a hardware keystore " DBA_TABLESPACES " See Also: Oracle Database Advanced Security Guide for information on opening a software keystore Oracle Database Advanced Security Guide for information on opening a hardware keystore " DBA_TABLESPACES "