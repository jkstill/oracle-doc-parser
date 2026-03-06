---
id: 19c__DBMS_FILE_TRANSFER
name: DBMS_FILE_TRANSFER
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_TRANSFER
tags: [dbms_file_transfer]
source_file: DBMS_FILE_TRANSFER.html
---

# DBMS_FILE_TRANSFER

DBMS_FILE_TRANSFER supports online backup. You should therefore be careful in copying or transferring a file that is being modified by the database because this can result in an inconsistent file, and require recovery. To guarantee consistency, bring files offline when the database is in use.

## Usage Notes

If you want to use DBMS_FILE_TRANSFER for performing backups, note that you are implementing self-managed backups, and should therefore put the files in hot backup mode.