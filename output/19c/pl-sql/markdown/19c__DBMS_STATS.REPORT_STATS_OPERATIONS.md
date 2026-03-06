---
id: 19c__DBMS_STATS.REPORT_STATS_OPERATIONS
name: DBMS_STATS.REPORT_STATS_OPERATIONS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.REPORT_STATS_OPERATIONS

This function generates a report of all statistics operations that take place between two timestamps which may or may not have been provided.

## Syntax

```sql
DBMS_STATS.REPORT_STATS_OPERATIONS (
   detail_level       VARCHAR2 DEFAULT 'TYPICAL',
   format             VARCHAR2 DEFAULT 'TEXT',
   latestN            NUMBER DEFAULT NULL,
   since              TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   until              TIMESTAMP WITH TIME ZONE DEFAULT NULl,
   auto_only          BOOLEAN DEFAULT FALSE,
   container_ids      DBMS_UTILITY.NUMBER_ARRAY DEFAULT DBMS_STATS.NULL_NUMTAB)
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| detail_level | VARCHAR2 | IN | Detail level for the content of the report BASIC : The report includes - operation ID - operation name - operation target object - start time - end time - completion status (such as: succeeded, failed) TYPICAL : In addition to the information provided at level BASIC , the report includes individual target objects for which statistics are gathered in this operation. Specifically, with regard to operation related details: - total number of target objects - total number of successfully completed objects - total number of failed objects - total number of timed -out objects (applies to only auto statistics gathering) ALL : In addition to the information provided at level TYPICAL , the report includes further information on each target object. Specifically, with regard to operation-related details: - job name (if the operation was run in a job) - session ID - parameter values - additional error details if the operation has failed |
| format | VARCHAR2 | IN | Report format: XML HTML TEXT (Default) |
| latestN | NUMBER | IN | Restricts the report to contain only the latest N operations that took place between the provided time points (since and until). The default value is NULL , meaning that all qualifying operations will be reported. |
| since | TIMESTAMP | IN | The report will include only statistics operations that started after this timestamp. |
| until | TIMESTAMP | IN | The report will include only statistics operations that before after this timestamp. |
| auto_only | BOOLEAN | IN | When TRUE , the report will contain only auto statistics gathering job runs. |
| container_ids | DBMS_UTILITY.NUMBER_ARRAY | IN | A multitenant environment contains one or more pluggable databases (PDBs). container_ids represents a set of PDB IDs so that only statistics operations from the specified PDBs are reported (applies to only multitenant environments). |

**Returns:** `CLOB`

## Usage Notes

It allows the scope of the report to be narrowed down so that report will include only auto statistics gathering runs. Furthermore, in a multitenant environment, users may optionally provide a set of pluggable database (PDB) IDs so that only statistics operations from the specified pluggable databases will be reported. Syntax DBMS_STATS.REPORT_STATS_OPERATIONS ( detail_level VARCHAR2 DEFAULT 'TYPICAL', format VARCHAR2 DEFAULT 'TEXT', latestN NUMBER DEFAULT NULL, since TIMESTAMP WITH TIME ZONE DEFAULT NULL, until TIMESTAMP WITH TIME ZONE DEFAULT NULl, auto_only BOOLEAN DEFAULT FALSE, container_ids DBMS_UTILITY.NUMBER_ARRAY DEFAULT DBMS_STATS.NULL_NUMTAB) RETURN CLOB; Parameters Table 171-107 REPORT_STATS_OPERATIONS Function Parameters Parameter Description detail_level Detail level for the content of the report BASIC : The report includes - operation ID - operation name - operation target object - start time - end time - completion status (such as: succeeded, failed) TYPICAL : In addition to the information provided at level BASIC , the report includes individual target objects for which statistics are gathered in this operation. Specifically, with regard to operation related details: - total number of target objects - total number of successfully completed objects - total number of failed objects - total number of timed -out objects (applies to only auto statistics gathering) ALL : In addition to the information provided at level TYPICAL , the report includes further information on each target object. Specifically, with regard to operation-related details: - job name (if the operation was run in a job) - session ID - parameter values - additional error details if the operation has failed format Report format: XML HTML TEXT (Default) latestN Restricts the report to contain only the latest N operations that took place between the provided time points (since and until). The default value is NULL , meaning that all qualifying operations will be reported. since The report will include only statistics operations that started after this timestamp. until The report will include only statistics operations that before after this timestamp. auto_only When TRUE , the report will contain only auto statistics gathering job runs. container_ids A multitenant environment contains one or more pluggable databases (PDBs). container_ids represents a set of PDB IDs so that only statistics operations from the specified PDBs are reported (applies to only multitenant environments). Usage Notes To invoke this procedure you need the ANALYZE ANY privilege and the ANALYZE ANY DICTIONARY privilege. Examples Note that the type for container_ids input parameter is DBMS_UTILITY.NUMBER_ARRAY which is an associative PL/SQL array collection. Although associative array type allows for more flexible harvals table-like organization of entries, this function treats container_ids as a regular table collection with the first ID located at index 1 and the last id located at index container_ids.count without any empty array slot left between any two IDs. An example for 3 container ids is provided. DECLARE conid_tab DBMS_UTILITY.NUMBER_ARRAY; report clob; BEGIN conid_tab(1) := 124; conid_tab(2) := 63; conid_tab(3) := 98; report := DBMS_STATS.REPORT_STATS_OPERATIONS (container_ids => conid_tab); END;