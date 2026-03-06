---
id: 19c__DBMS_STATS.REPORT_GATHER_AUTO_STATS
name: DBMS_STATS.REPORT_GATHER_AUTO_STATS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.REPORT_GATHER_AUTO_STATS

This function runs the auto statistics gathering job in reporting mode. That is, statistics are not actually collected, but all the objects that will be affected when auto statistics gathering is invoked are reported.

## Syntax

```sql
DBMS_STATS.REPORT_GATHER_AUTO_STATS (
   detail_level      VARCHAR2  DEFAULT 'TYPICAL',
   format            VARCHAR2  DEFAULT 'TEXT')
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| detail_level | VARCHAR2 | IN | Detail level for the content of the report BASIC : The report includes - operation ID - operation name - operation target object - start time - end time - completion status (such as: succeeded, failed) TYPICAL : In addition to the information provided at level BASIC , the report includes individual target objects for which statistics are gathered in this operation. Specifically, with regard to operation related details: - total number of target objects - total number of successfully completed objects - total number of failed objects - total number of timed-out objects (applies to only auto statistics gathering) With regard to target objects: - owner and name of each target object - target object type (such as: table, index) - start time - end time - completion status ALL : In addition to the information provided at level TYPICAL , the report includes further information on each target object. Specifically, with regard to operation-related details: - job name - session ID - parameter values - error message if the operation failed With regard to target objects: - job name - batching details - estimated cost - rank in the target list - columns for which histograms were collected - list of collected extended statistics (if any) - reason for including the object in the target list - additional error details if the task has failed. Note that several fields (such as job name, estimated task cost) in the report are populated only when an operation is executed concurrently ( CONCURRENT preference is turned on). |
| format | VARCHAR2 | IN | Report format: XML HTML TEXT (Default) |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_STATS.REPORT_GATHER_AUTO_STATS ( detail_level VARCHAR2 DEFAULT 'TYPICAL', format VARCHAR2 DEFAULT 'TEXT') RETURN CLOB; Parameters Table 171-100 REPORT_GATHER_AUTO_STATS Function Parameters Parameter Description detail_level Detail level for the content of the report BASIC : The report includes - operation ID - operation name - operation target object - start time - end time - completion status (such as: succeeded, failed) TYPICAL : In addition to the information provided at level BASIC , the report includes individual target objects for which statistics are gathered in this operation. Specifically, with regard to operation related details: - total number of target objects - total number of successfully completed objects - total number of failed objects - total number of timed-out objects (applies to only auto statistics gathering) With regard to target objects: - owner and name of each target object - target object type (such as: table, index) - start time - end time - completion status ALL : In addition to the information provided at level TYPICAL , the report includes further information on each target object. Specifically, with regard to operation-related details: - job name - session ID - parameter values - error message if the operation failed With regard to target objects: - job name - batching details - estimated cost - rank in the target list - columns for which histograms were collected - list of collected extended statistics (if any) - reason for including the object in the target list - additional error details if the task has failed. Note that several fields (such as job name, estimated task cost) in the report are populated only when an operation is executed concurrently ( CONCURRENT preference is turned on). format Report format: XML HTML TEXT (Default) Usage Notes Only user SYS can run the REPORT_GATHER_AUTO_STATS function.