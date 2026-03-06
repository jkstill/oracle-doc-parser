---
id: 19c__DBMS_STATS.REPORT_SINGLE_STATS_OPERATION
name: DBMS_STATS.REPORT_SINGLE_STATS_OPERATION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.REPORT_SINGLE_STATS_OPERATION

This function generates a report for the provided operation optionally in a particular pluggable database (PDB) in a multitenant environment.

## Syntax

```sql
DBMS_STATS.REPORT_SINGLE_STATS_OPERATIONS (
   opid              NUMBER,
   detail_level      VARCHAR2  DEFAULT 'TYPICAL',
   format            VARCHAR2  DEFAULT 'TEXT'
   container_id      NUMBER    DEFAULT NULL)
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| opid | NUMBER | IN | Operation ID |
| detail_level | VARCHAR2 | IN | Detail level for the content of the report BASIC : The report includes - operation ID - operation name - operation target object - start time - end time - completion status (such as: succeeded, failed) TYPICAL : In addition to the information provided at level BASIC , the report includes individual target objects for which statistics are gathered in this operation. Specifically, with regard to operation related details: - total number of target objects - total number of successfully completed objects - total number of failed objects - total number of timed-out objects (applies to only auto statistics gathering) With regard to target objects: - owner and name of each target object - target object type (such as: table, index) - start time - end time - completion status ALL : In addition to the information provided at level TYPICAL , the report includes further information on each target object. Specifically, with regard to operation-related details: - job name - session ID - parameter values - error message if the operation failed With regard to target objects: - job name - batching details - estimated cost - rank in the target list - columns for which histograms were collected - list of collected extended statistics (if any) - reason for including the object in the target list (applies to only automatic statistics gathering operation tasks) - additional error details if the task has failed. Note that several fields (such as job name, estimated task cost) in the report are populated only when an operation is executed concurrently ( CONCURRENT preference is turned on). |
| format | VARCHAR2 | IN | Report format: XML HTML TEXT (Default) |
| container_id | NUMBER | IN | ID of the pluggable database (PDB) on which this operation was performed. Note that in a multitenant environment, operation ID does not uniquely identify an operation. That is, different operations from distinct PDBs may have the same operation ID. Hence, in a multitenant environment, if a PDB ID is not provided, then the report may contain multiple operations. In a typical (non-CDB) database environment, operation ID is unique to each operation. |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_STATS.REPORT_SINGLE_STATS_OPERATIONS ( opid NUMBER, detail_level VARCHAR2 DEFAULT 'TYPICAL', format VARCHAR2 DEFAULT 'TEXT' container_id NUMBER DEFAULT NULL) RETURN CLOB; Parameters Table 171-106 REPORT_SINGLE_STATS_OPERATION Function Parameters Parameter Description opid Operation ID detail_level Detail level for the content of the report BASIC : The report includes - operation ID - operation name - operation target object - start time - end time - completion status (such as: succeeded, failed) TYPICAL : In addition to the information provided at level BASIC , the report includes individual target objects for which statistics are gathered in this operation. Specifically, with regard to operation related details: - total number of target objects - total number of successfully completed objects - total number of failed objects - total number of timed-out objects (applies to only auto statistics gathering) With regard to target objects: - owner and name of each target object - target object type (such as: table, index) - start time - end time - completion status ALL : In addition to the information provided at level TYPICAL , the report includes further information on each target object. Specifically, with regard to operation-related details: - job name - session ID - parameter values - error message if the operation failed With regard to target objects: - job name - batching details - estimated cost - rank in the target list - columns for which histograms were collected - list of collected extended statistics (if any) - reason for including the object in the target list (applies to only automatic statistics gathering operation tasks) - additional error details if the task has failed. Note that several fields (such as job name, estimated task cost) in the report are populated only when an operation is executed concurrently ( CONCURRENT preference is turned on). format Report format: XML HTML TEXT (Default) container_id ID of the pluggable database (PDB) on which this operation was performed. Note that in a multitenant environment, operation ID does not uniquely identify an operation. That is, different operations from distinct PDBs may have the same operation ID. Hence, in a multitenant environment, if a PDB ID is not provided, then the report may contain multiple operations. In a typical (non-CDB) database environment, operation ID is unique to each operation. Usage Notes To invoke this procedure you need the ANALYZE ANY privilege and the ANALYZE ANY DICTIONARY privilege.