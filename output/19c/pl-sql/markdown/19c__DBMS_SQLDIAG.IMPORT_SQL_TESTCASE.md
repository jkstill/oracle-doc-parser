---
id: 19c__DBMS_SQLDIAG.IMPORT_SQL_TESTCASE
name: DBMS_SQLDIAG.IMPORT_SQL_TESTCASE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.IMPORT_SQL_TESTCASE

This procedure imports a SQL test case into a schema.

## Syntax

```sql
DBMS_SQLDIAG.IMPORT_SQL_TESTCASE (
    directory                IN   VARCHAR2,
    sqlTestCase              IN   CLOB,
    importEnvironment        IN   BOOLEAN   :=  TRUE,
    importMetadata           IN   BOOLEAN   :=  TRUE,
    importData               IN   BOOLEAN   :=  TRUE,
    importPkgbody            IN   BOOLEAN   :=  FALSE,
    importDiagnosis          IN   BOOLEAN   :=  TRUE,
    ignoreStorage            IN   BOOLEAN   :=  TRUE,
    ctrlOptions              IN   VARCHAR2  :=  NULL,
    preserveSchemaMapping    IN   BOOLEAN   :=  FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| directory | VARCHAR2 | IN | Directory containing test case files |
| filename |  |  | Name of a file containing an XML document describing the SQL test case |
| importEnvironment | BOOLEAN | IN | TRUE if the compilation environment should be imported |
| importMetadata | BOOLEAN | IN | TRUE if the definition of the objects referenced in the SQL should be imported |
| importData | BOOLEAN | IN | TRUE if the data of the objects referenced in the SQL should be imported |
| importPkgbody | BOOLEAN | IN | TRUE if the body of the packages referenced in the SQL are imported |
| importDiagnosis | BOOLEAN | IN | TRUE if the diagnostic information associated to the task should be imported |
| ignoreStorage | BOOLEAN | IN | TRUE if the storage attributes should be ignored |
| ctrlOptions | VARCHAR2 | IN | Opaque control parameters, of which only capture is valid for this subprogam. capture - BASIC (default) or WITH_RUNTIME_INFO . This parameter defines the mode of TCB capture. BASIC : runs as Oracle Release 11 g TCB and captures all the information that is captured in that release as well as AWR reports, SQL monitor reports and parameter information. WITH_RUNTIME_INFO : TCB captures runtime information for the SQL, such as dynamic sampling data, list of binds, Dynamic Plan info, along with information captured under BASIC mode. |
| preserveSchemaMapping | BOOLEAN | IN | TRUE if the schema (or schemas) are not re-mapped from the original environment to the test environment (schema mapping in the target database will be identical to the source database). Note that when an import is run with preservesSchemaMapping set to TRUE , if the objects in the schemas exists then the import will overwrite the existing objects. |

## Usage Notes

Syntax This variant requires a source directory and SQL Testcase metadata object (in XML format). DBMS_SQLDIAG.IMPORT_SQL_TESTCASE ( directory IN VARCHAR2, sqlTestCase IN CLOB, importEnvironment IN BOOLEAN := TRUE, importMetadata IN BOOLEAN := TRUE, importData IN BOOLEAN := TRUE, importPkgbody IN BOOLEAN := FALSE, importDiagnosis IN BOOLEAN := TRUE, ignoreStorage IN BOOLEAN := TRUE, ctrlOptions IN VARCHAR2 := NULL, preserveSchemaMapping IN BOOLEAN := FALSE); This variant requires a source directory name of SQL Testcase metadata file. DBMS_SQLDIAG.IMPORT_SQL_TESTCASE ( directory IN VARCHAR2, filename IN VARCHAR2, importEnvironment IN BOOLEAN := TRUE, importMetadata IN BOOLEAN := TRUE, importData IN BOOLEAN := TRUE, importPkgbody IN BOOLEAN := FALSE, importDiagnosis IN BOOLEAN := TRUE, ignoreStorage IN BOOLEAN := TRUE, ctrlOptions IN VARCHAR2 := NULL, preserveSchemaMapping IN BOOLEAN := FALSE); Parameters Table 165-25 IMPORT_SQL_TESTCASE Procedure Parameters Parameter Description directory Directory containing test case files filename Name of a file containing an XML document describing the SQL test case importEnvironment TRUE if the compilation environment should be imported importMetadata TRUE if the definition of the objects referenced in the SQL should be imported importData TRUE if the data of the objects referenced in the SQL should be imported importPkgbody TRUE if the body of the packages referenced in the SQL are imported importDiagnosis TRUE if the diagnostic information associated to the task should be imported ignoreStorage TRUE if the storage attributes should be ignored ctrlOptions Opaque control parameters, of which only capture is valid for this subprogam. capture - BASIC (default) or WITH_RUNTIME_INFO . This parameter defines the mode of TCB capture. BASIC : runs as Oracle Release 11 g TCB and captures all the information that is captured in that release as well as AWR reports, SQL monitor reports and parameter information. WITH_RUNTIME_INFO : TCB captures runtime information for the SQL, such as dynamic sampling data, list of binds, Dynamic Plan info, along with information captured under BASIC mode. preserveSchemaMapping TRUE if the schema (or schemas) are not re-mapped from the original environment to the test environment (schema mapping in the target database will be identical to the source database). Note that when an import is run with preservesSchemaMapping set to TRUE , if the objects in the schemas exists then the import will overwrite the existing objects. Usage Notes A SQL test case generates a set of files needed to help reproduce a SQL failure on a different machine. It contains: a dump file containing schemas objects and statistics ( .dmp ) the explain plan for the statements (in advanced mode) diagnostic information gathered on the offending statement an import script to execute to reload the objects a SQL script to replay system statistics of the source a table of contents file describing the SQL test case metadata. ( xxxxmain.xml ) a README.txt file that explain the usage of the TCB the outlines used by the statement ( ol.xml ) a list of parameters set in the exporting db/env ( prmimp.sql ) a SQL monitor report, if any ( smrpt.html ) an AWR report, if any ( awrrpt.html ) a list of binds used in this statement ( bndlst.xml ) You should not run Test Case Builder (TCB) under user SYS . Instead, use another user who can be granted the DBA privilege The default setting for TCB is that data is not exported. However, in some cases data is required, such as to diagnose an outcome with a result that is not optimal. To export data, call EXPORT_SQL_TESTCASE Procedures with exportData=>TRUE and the data will be imported by default, unless turned OFF by importData=>FALSE . TCB includes PL/SQL package spec by default, but not the PL/SQL package body. However, you may need to have the package body as well, for example, to invoke the PL/SQL functions, or because you have a Virtual Private Database (VPD) function defined in a package. To export a PL/SQL package body, call EXPORT_SQL_TESTCASE Procedures with exportPkgbody=>TRUE . To import a PL/SQL package body, call IMPORT_SQL_TESTCASE Procedures with i mportPkgbody=>TRUE . The capture value used when invoking the EXPORT_SQL_TESTCASE Procedures must be used when calling this procedure.