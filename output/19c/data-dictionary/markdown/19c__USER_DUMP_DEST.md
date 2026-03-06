---
id: 19c__USER_DUMP_DEST
name: USER_DUMP_DEST
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_DUMP_DEST.html
---

# USER_DUMP_DEST

USER_DUMP_DEST specifies the pathname for a directory where the server will write debugging trace files on behalf of a user process.

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: The USER_DUMP_DEST initialization parameter is deprecated. For example, this directory might be set as follows: On MS-DOS: C:\ORACLE\UTRC On UNIX: /oracle/utrc On VMS: DISK$UR3:[ORACLE.UTRC] Note: This parameter is ignored by the diagnosability infrastructure introduced in Oracle Database 11g Release 1 (11.1), which places trace and core files in a location controlled by the DIAGNOSTIC_DEST initialization parameter. See Also: Oracle Database SQL Tuning Guide for more information about the use of trace files Your operating system-specific Oracle documentation for the range of values Note: The USER_DUMP_DEST initialization parameter is deprecated. Note: This parameter is ignored by the diagnosability infrastructure introduced in Oracle Database 11g Release 1 (11.1), which places trace and core files in a location controlled by the DIAGNOSTIC_DEST initialization parameter. See Also: Oracle Database SQL Tuning Guide for more information about the use of trace files Your operating system-specific Oracle documentation for the range of values