---
id: 19c__DBMS_STATS.REPORT_GATHER_FIXED_OBJ_STATS
name: DBMS_STATS.REPORT_GATHER_FIXED_OBJ_STATS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.REPORT_GATHER_FIXED_OBJ_STATS

This function runs the GATHER_FIXED_OBJECTS_STATS Procedure in reporting mode.

## Syntax

```sql
DBMS_STATS.REPORT_GATHER_FIXED_OBJ_STATS (
   stattab          IN  VARCHAR2 DEFAULT NULL,
   statid           IN  VARCHAR2 DEFAULT NULL,
   statown          IN  VARCHAR2 DEFAULT NULL, 
   no_invalidate    IN  BOOLEAN  DEFAULT TO_NO_INVALIDATE_TYPE (
                                     GET_PARAM('NO_INVALIDATE')),
   detail_level     IN  VARCHAR2   DEFAULT 'TYPICAL',
   format           IN  VARCHAR2   DEFAULT 'TEXT') 
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stattab | VARCHAR2 | IN | User statistics table identifier describing where to save the current statistics |
| statid | VARCHAR2 | IN | Identifier to associate with these statistics within stattab (optional) |
| statown | VARCHAR2 | IN | Schema containing stattab (if different from current schema) |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| detail_level | VARCHAR2 | IN | Detail level for the content of the report BASIC : The report includes - operation ID - operation name - operation target object - start time - end time - completion status (such as: succeeded, failed) TYPICAL : In addition to the information provided at level BASIC , the report includes individual target objects for which statistics are gathered in this operation. Specifically, with regard to operation related details: - total number of target objects - total number of successfully completed objects - total number of failed objects - total number of timed-out objects (applies to only auto statistics gathering) With regard to target objects: - owner and name of each target object - target object type (such as: table, index) - start time - end time - completion status ALL : In addition to the information provided at level TYPICAL , the report includes further information on each target object. Specifically, with regard to operation-related details: - job name - session ID - parameter values - error message if the operation failed With regard to target objects: - job name - batching details - estimated cost - rank in the target list - columns for which histograms were collected - list of collected extended statistics (if any) - additional error details if the task has failed. Note that several fields (such as job name, estimated task cost) in the report are populated only when an operation is executed concurrently ( CONCURRENT preference is turned on). |
| format | VARCHAR2 | IN | Report format: XML HTML TEXT (Default) |

**Returns:** `CLOB`

## Usage Notes

That is, statistics are not actually collected, but all the objects that will be affected when GATHER_FIXED_OBJ_STATS is invoked are reported. The input set of parameters are exactly the same as in GATHER_FIXED_OBJ_STATS with two extra parameters. Syntax DBMS_STATS.REPORT_GATHER_FIXED_OBJ_STATS ( stattab IN VARCHAR2 DEFAULT NULL, statid IN VARCHAR2 DEFAULT NULL, statown IN VARCHAR2 DEFAULT NULL, no_invalidate IN BOOLEAN DEFAULT TO_NO_INVALIDATE_TYPE ( GET_PARAM('NO_INVALIDATE')), detail_level IN VARCHAR2 DEFAULT 'TYPICAL', format IN VARCHAR2 DEFAULT 'TEXT') RETURN CLOB; Parameters Table 171-103 REPORT_GATHER_FIXED_OBJ_STATS Procedure Parameters Parameter Description stattab User statistics table identifier describing where to save the current statistics statid Identifier to associate with these statistics within stattab (optional) statown Schema containing stattab (if different from current schema) no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . detail_level Detail level for the content of the report BASIC : The report includes - operation ID - operation name - operation target object - start time - end time - completion status (such as: succeeded, failed) TYPICAL : In addition to the information provided at level BASIC , the report includes individual target objects for which statistics are gathered in this operation. Specifically, with regard to operation related details: - total number of target objects - total number of successfully completed objects - total number of failed objects - total number of timed-out objects (applies to only auto statistics gathering) With regard to target objects: - owner and name of each target object - target object type (such as: table, index) - start time - end time - completion status ALL : In addition to the information provided at level TYPICAL , the report includes further information on each target object. Specifically, with regard to operation-related details: - job name - session ID - parameter values - error message if the operation failed With regard to target objects: - job name - batching details - estimated cost - rank in the target list - columns for which histograms were collected - list of collected extended statistics (if any) - additional error details if the task has failed. Note that several fields (such as job name, estimated task cost) in the report are populated only when an operation is executed concurrently ( CONCURRENT preference is turned on). format Report format: XML HTML TEXT (Default) Return Values A CLOB object that contains the report Usage Notes You must have the SYSDBA or ANALYZE ANY DICTIONARY system privilege to execute this procedure.