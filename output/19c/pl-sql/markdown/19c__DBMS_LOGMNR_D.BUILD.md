---
id: 19c__DBMS_LOGMNR_D.BUILD
name: DBMS_LOGMNR_D.BUILD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGMNR_D
tags: [dbms_logmnr_d]
source_file: DBMS_LOGMNR_D.html
---

# DBMS_LOGMNR_D.BUILD

This procedure extracts the LogMiner data dictionary to the redo log files.

## Syntax

```sql
DBMS_LOGMNR_D.BUILD (
     dictionary_filename  IN  VARCHAR2,
     dictionary_location  IN  VARCHAR2,
     options              IN  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dictionary_filename | VARCHAR2 | IN | Specifies the name of the LogMiner dictionary file. |
| dictionary_location | VARCHAR2 | IN | Specifies the directory object for the LogMiner dictionary file. |
| options | NUMBER) | IN | Specifies that the LogMiner dictionary is written to the redo log files ( STORE_IN_REDO_LOGS ). |

## Usage Notes

The following considerations apply to a multitenant container database (CDB) environment. In a CDB environment, when you extract to the redo log files, the BUILD procedure must be called from the root database. The LogMiner data dictionary for the entire CDB is extracted to the redo log files. You cannot add or remove PDBs from a CDB while this procedure is running. Note: In previous releases, using a flat file dictionary was one means of mining the redo logs for the changes associated with a specific PDB whose data dictionary was contained within the flat file. This feature is desupported for PDBs in Oracle Database 19c, and desupported in later releases. With Oracle Database 19c and later releases, Oracle recommends that you call DBMS_LOGMNR.START_LOGMNR , and supply the system change number (SCN) or time range that you want to mine. The SCN or time range options of START_LOGMNR are enhanced to support mining of individual PDBs. Note: In previous releases, using a flat file dictionary was one means of mining the redo logs for the changes associated with a specific PDB whose data dictionary was contained within the flat file. This feature is desupported for PDBs in Oracle Database 19c, and desupported in later releases. With Oracle Database 19c and later releases, Oracle recommends that you call DBMS_LOGMNR.START_LOGMNR , and supply the system change number (SCN) or time range that you want to mine. The SCN or time range options of START_LOGMNR are enhanced to support mining of individual PDBs. Syntax DBMS_LOGMNR_D.BUILD ( dictionary_filename IN VARCHAR2, dictionary_location IN VARCHAR2, options IN NUMBER); Parameters Table 103-2 BUILD Procedure Parameters Parameter Description dictionary_filename Specifies the name of the LogMiner dictionary file. dictionary_location Specifies the directory object for the LogMiner dictionary file. options Specifies that the LogMiner dictionary is written to the redo log files ( STORE_IN_REDO_LOGS ). Exceptions Table 103-3 BUILD Procedure Exceptions Exception Description ORA-01302 Dictionary build options are missing or incorrect. This error is returned under the following conditions: If the value of the OPTIONS parameter is not one of the supported values ( STORE_IN_REDO_LOGS ), or is not specified If the STORE_IN_REDO_LOGS option is not specified and neither the dictionary_filename nor the dictionary_location parameter is specified If the STORE_IN_REDO_LOGS option is specified and either the dictionary_filename or the dictionary_location parameter is specified ORA-01308 Initialization parameter UTL_FILE_DIR is not set. Note: In earlier releases, you used the UTL_FILE_DIR initialization parameter to specify a directory location. However, as of Oracle Database 18c, the UTL_FILE_DIR initialization parameter is desupported. It is still supported for backward compatibility, but Oracle recommends that you instead use directory objects. ORA-01336 Specified dictionary file cannot be opened. This error is returned when the dictionary file is read-only. ORA-01308 Dictionary directory is not set. This error is returned under the following conditions: The specified value for the dictionary_location is not a directory object. The specified value for the dictionary_location is a directory object that is defined to be a file path that cannot be accessed.