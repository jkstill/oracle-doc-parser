---
id: 19c__DBMS_XSTREAM_ADM.RECOVER_OPERATION
name: DBMS_XSTREAM_ADM.RECOVER_OPERATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.RECOVER_OPERATION

This procedure provides options for split and merge operations that stopped because they encountered an errors.

## Syntax

```sql
DBMS_XSTREAM_ADM.RECOVER_OPERATION(
   script_id       IN  RAW,
   operation_mode  IN  VARCHAR2  DEFAULT 'FORWARD');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| script_id | RAW | IN | The operation id of the operation that is being rolled forward, rolled back, or purged. Query the SCRIPT_ID column of the DBA_RECOVERABLE_SCRIPT data dictionary view to determine the operation id. |
| operation_mode | VARCHAR2 | IN | If FORWARD , then the procedure rolls forward the operation. Specify FORWARD to try to complete the operation. If ROLLBACK , then the procedure rolls back all of the actions performed in the operation. If the rollback is successful, then this option also moves the metadata about the operation from the DBA_RECOVERABLE_SCRIPT view to the DBA_RECOVERABLE_SCRIPT_HIST view. The other views retain information about the operation for 30 days. If PURGE , then the procedure moves the metadata about the operation from the DBA_RECOVERABLE_SCRIPT view to the DBA_RECOVERABLE_SCRIPT_HIST view without rolling the operation back. The other views retain information about the operation for 30 days. |

## Usage Notes

This procedure either rolls forward the operation, rolls back the operation, or purges all of the metadata about the operation. Split and merge operations might be run in an XStream Out environment in which multiple outbound servers use the same capture process. This procedure only can perform these actions for split and merge operations using the split_threshold and merge_threshold capture process parameters set to non- NULL values to enable automatic split and merge. Information about the operation is stored in the following data dictionary views when the operation is in process: DBA_RECOVERABLE_SCRIPT DBA_RECOVERABLE_SCRIPT_PARAMS DBA_RECOVERABLE_SCRIPT_BLOCKS DBA_RECOVERABLE_SCRIPT_ERRORS The data dictionary views are populated at the database that contains the capture process. When the operation completes successfully, metadata about the operation is moved from the DBA_RECOVERABLE_SCRIPT view to the DBA_RECOVERABLE_SCRIPT_HIST view. The other views, DBA_RECOVERABLE_SCRIPT_PARAMS , DBA_RECOVERABLE_SCRIPT_BLOCKS , and DBA_RECOVERABLE_SCRIPT_ERRORS , retain information about the operation until it is purged automatically after 30 days. When one of these operations encounters an error and stops, metadata about the operation remains in these views. In this case, you can either roll forward, roll back, or purge the metadata about the operation using the RECOVER_OPERATION procedure. If you choose to roll forward the operation, then correct conditions that caused the errors reported in DBA_RECOVERABLE_SCRIPT_ERRORS before proceeding. Run the RECOVER_OPERATION procedure at the database that contains the capture process. Note: To run the RECOVER_OPERATION procedure, both databases must be Oracle Database 10 g Release 2 or later databases. See Also: " SPLIT_STREAMS Procedure " " MERGE_STREAMS Procedure " " MERGE_STREAMS_JOB Procedure " Note: To run the RECOVER_OPERATION procedure, both databases must be Oracle Database 10 g Release 2 or later databases. See Also: " SPLIT_STREAMS Procedure " " MERGE_STREAMS Procedure " " MERGE_STREAMS_JOB Procedure " Syntax DBMS_XSTREAM_ADM.RECOVER_OPERATION( script_id IN RAW, operation_mode IN VARCHAR2 DEFAULT 'FORWARD'); Parameters Table 217-25 RECOVER_OPERATION Procedure Parameters Parameter Description script_id The operation id of the operation that is being rolled forward, rolled back, or purged. Query the SCRIPT_ID column of the DBA_RECOVERABLE_SCRIPT data dictionary view to determine the operation id. operation_mode If FORWARD , then the procedure rolls forward the operation. Specify FORWARD to try to complete the operation. If ROLLBACK , then the procedure rolls back all of the actions performed in the operation. If the rollback is successful, then this option also moves the metadata about the operation from the DBA_RECOVERABLE_SCRIPT view to the DBA_RECOVERABLE_SCRIPT_HIST view. The other views retain information about the operation for 30 days. If PURGE , then the procedure moves the metadata about the operation from the DBA_RECOVERABLE_SCRIPT view to the DBA_RECOVERABLE_SCRIPT_HIST view without rolling the operation back. The other views retain information about the operation for 30 days.