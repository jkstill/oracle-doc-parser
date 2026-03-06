---
id: 19c__DBMS_CAPTURE_ADM.BUILD
name: DBMS_CAPTURE_ADM.BUILD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CAPTURE_ADM
tags: [dbms_capture_adm]
source_file: DBMS_CAPTURE_ADM.html
---

# DBMS_CAPTURE_ADM.BUILD

This procedure extracts the data dictionary of the current database to the redo log and automatically specifies database supplemental logging by running the SQL statement ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;

## Syntax

```sql
DBMS_CAPTURE_ADM.BUILD(
   first_scn OUT NUMBER);

DBMS_CAPTURE_ADM.BUILD;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| first_scn | NUMBER) | OUT | Contains the lowest SCN value corresponding to the data dictionary extracted to the redo log that can be specified as a first SCN for a capture process |

## Usage Notes

This procedure is overloaded. One version of this procedure contains the OUT parameter first_scn , and the other does not. Syntax DBMS_CAPTURE_ADM.BUILD( first_scn OUT NUMBER); DBMS_CAPTURE_ADM.BUILD; Parameters Table 35-8 BUILD Procedure Parameter Parameter Description first_scn Contains the lowest SCN value corresponding to the data dictionary extracted to the redo log that can be specified as a first SCN for a capture process Usage Notes The following usage notes apply to this procedure: You can run this procedure multiple times at a source database. If you plan to capture changes originating at a source database with a capture process, then this procedure must be executed at the source database at least once. When the capture process is started, either at a local source database or at a downstream database, the capture process uses the extracted information in the redo log to create a LogMiner data dictionary. A LogMiner data dictionary is a separate data dictionary used by a capture process to determine the details of a change that it is capturing. The LogMiner data dictionary is necessary because the primary data dictionary of the source database might not be synchronized with the redo data being scanned by a capture process. After executing this procedure, you can query the FIRST_CHANGE# column of the V$ARCHIVED_LOG dynamic performance view where the DICTIONARY_BEGIN column is YES to determine the lowest SCN value for the database that can be specified as a first SCN for a capture process. The first SCN for a capture process is the lowest SCN in the redo log from which the capture process can capture changes.You can specify the first SCN for a capture process when you run the CREATE_CAPTURE or ALTER_CAPTURE procedure in the DBMS_CAPTURE_ADM package. In a CDB, the BUILD procedure must be executed from the root.