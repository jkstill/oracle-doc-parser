---
id: 19c__DBMS_SQLDIAG.EXPORT_SQL_TESTCASE_DIR_BY_INC
name: DBMS_SQLDIAG.EXPORT_SQL_TESTCASE_DIR_BY_INC
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.EXPORT_SQL_TESTCASE_DIR_BY_INC

This function generates a SQL test case corresponding to the incident ID passed as an argument. It creates a set of scripts and dump file in the directory passed as an argument.

## Syntax

```sql
DBMS_SQLDIAG.EXPORT_SQL_TESTCASE_DIR_BY_INC (
    incident_id        IN   NUMBER,
    directory          IN   VARCHAR2,
    exportEnvironment  IN   VARCHAR2 := 'TRUE',
    exportMetadata     IN   VARCHAR2 := 'TRUE',
    exportData         IN   VARCHAR2 := 'FALSE',
    samplingPercent    IN   VARCHAR2 := '100', 
    ctrlOptions        IN   VARCHAR2 := NULL
    version            IN   VARCHAR2 := 'COMPATIBLE')
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| incident_id | NUMBER | IN | Incident ID containing the offending SQL. For more information about Incidents, see Oracle Database Performance Tuning Guide . |
| directory | VARCHAR2 | IN | Directory path to the generated files |
| exportEnvironment | VARCHAR2 | IN | TRUE if the compilation environment should be exported |
| exportMetadata | VARCHAR2 | IN | TRUE if the definition of the objects referenced in the SQL should be exported |
| exportData | VARCHAR2 | IN | TRUE if the data of the objects referenced in the SQL should be exported |
| samplingPercent | VARCHAR2 | IN | If is TRUE , specify the sampling percentage to use to create the dump file |
| ctrlOptions | VARCHAR2 | IN | Opaque control parameters. For example, to execute three times, set ctrlOptions with the following string: '<parameter name="mexec_count">3</parameter>' . capture - BASIC (default) or WITH_RUNTIME_INFO . This parameter defines the mode of TCB capture. BASIC : runs as Oracle release 11 g TCB and captures all the information that is captured in that release as well as AWR reports, SQL monitor reports and parameter information. WITH_RUNTIME_INFO : TCB captures runtime information for the SQL, such as dynamic sampling data, list of binds, Dynamic Plan info, along with information captured under BASIC mode. name=mexec_count - Value is any positive number ( N ). This parameter tells TCB to execute the statement for N time and capture runtime info at end of each execution. name=stat_history_since - Value is date. The object statistics history is exported using this parameter. Statistics history after date specified will be exported. |
| version | VARCHAR2 | IN | Version of database objects to be extracted. This option is only valid for EXPORT . Database objects or attributes incompatible with the version will not be extracted. COMPATIBLE - (default) the version of the metadata corresponds to the database compatibility level and the compatibility release level for feature (as given in the V$COMPATIBILITY view). Database compatibility must be set to 9.2 or higher. LATEST - the version of the metadata that specifies the current database version. A specific database version. For example, if '10.0.0' , this cannot be lower than Oracle Database release 10.0.0. |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_SQLDIAG.EXPORT_SQL_TESTCASE_DIR_BY_INC ( incident_id IN NUMBER, directory IN VARCHAR2, exportEnvironment IN VARCHAR2 := 'TRUE', exportMetadata IN VARCHAR2 := 'TRUE', exportData IN VARCHAR2 := 'FALSE', samplingPercent IN VARCHAR2 := '100', ctrlOptions IN VARCHAR2 := NULL version IN VARCHAR2 := 'COMPATIBLE') RETURN BOOLEAN; Parameters Table 165-21 EXPORT_SQL_TESTCASE_DIR_BY_INC Function Parameters Parameter Description incident_id Incident ID containing the offending SQL. For more information about Incidents, see Oracle Database Performance Tuning Guide . directory Directory path to the generated files exportEnvironment TRUE if the compilation environment should be exported exportMetadata TRUE if the definition of the objects referenced in the SQL should be exported exportData TRUE if the data of the objects referenced in the SQL should be exported samplingPercent If is TRUE , specify the sampling percentage to use to create the dump file ctrlOptions Opaque control parameters. For example, to execute three times, set ctrlOptions with the following string: '<parameter name="mexec_count">3</parameter>' . capture - BASIC (default) or WITH_RUNTIME_INFO . This parameter defines the mode of TCB capture. BASIC : runs as Oracle release 11 g TCB and captures all the information that is captured in that release as well as AWR reports, SQL monitor reports and parameter information. WITH_RUNTIME_INFO : TCB captures runtime information for the SQL, such as dynamic sampling data, list of binds, Dynamic Plan info, along with information captured under BASIC mode. name=mexec_count - Value is any positive number ( N ). This parameter tells TCB to execute the statement for N time and capture runtime info at end of each execution. name=stat_history_since - Value is date. The object statistics history is exported using this parameter. Statistics history after date specified will be exported. version Version of database objects to be extracted. This option is only valid for EXPORT . Database objects or attributes incompatible with the version will not be extracted. COMPATIBLE - (default) the version of the metadata corresponds to the database compatibility level and the compatibility release level for feature (as given in the V$COMPATIBILITY view). Database compatibility must be set to 9.2 or higher. LATEST - the version of the metadata that specifies the current database version. A specific database version. For example, if '10.0.0' , this cannot be lower than Oracle Database release 10.0.0.