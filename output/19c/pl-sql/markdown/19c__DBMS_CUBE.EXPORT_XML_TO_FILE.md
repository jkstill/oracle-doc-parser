---
id: 19c__DBMS_CUBE.EXPORT_XML_TO_FILE
name: DBMS_CUBE.EXPORT_XML_TO_FILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE
tags: [dbms_cube]
source_file: DBMS_CUBE.html
---

# DBMS_CUBE.EXPORT_XML_TO_FILE

This procedure exports OLAP metadata to a file. This file can be imported into a new or existing analytic workspace using the IMPORT_XML procedure. In this way, you can create a copy of the analytic workspace in another schema or database.

## Syntax

```sql
DBMS_CUBE.EXPORT_XML_TO_FILE
       (object_ids            IN      VARCHAR2,
        output_dirname        IN      VARCHAR2,
        output_filename       IN      VARCHAR2;

DBMS_CUBE.EXPORT_XML_TO_FILE
       (object_ids            IN      VARCHAR2,
        options_dirname       IN      VARCHAR2,
        options_filename      IN      VARCHAR2,
        output_dirname        IN      VARCHAR2,
        output_filename       IN      VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_ids | VARCHAR2 | IN | Any of these identifiers. The name of a schema, such as GLOBAL . The fully qualified name of an analytic workspace in the form owner.aw_name .AW , such as GLOBAL.GLOBAL.AW . Cube Dimension Named build process Measure folder You can specify multiple objects by separating the names with commas. Note : When exporting an individual object, be sure to export any objects required to reconstruct it. For example, when you export a cube, you must also export the dimensions of the cube. |
| options_dirname | VARCHAR2 | IN | The case-sensitive name of a database directory that contains options_filename . See " Export Options " . |
| options_filename | VARCHAR2 | IN | The name of a file containing an XML document of export options. See " Export Options " . |
| output_dirname | VARCHAR2 | IN | The case-sensitive name of a database directory where output_filename is created. |
| output_filename | VARCHAR2 | IN | The name of the template file created by the procedure. |

## Usage Notes

This procedure can also be used as part of the process for upgrading OLAP standard form metadata contained in an Oracle OLAP 10 g analytic workspace to OLAP 12 c format. Syntax DBMS_CUBE.EXPORT_XML_TO_FILE (object_ids IN VARCHAR2, output_dirname IN VARCHAR2, output_filename IN VARCHAR2; DBMS_CUBE.EXPORT_XML_TO_FILE (object_ids IN VARCHAR2, options_dirname IN VARCHAR2, options_filename IN VARCHAR2, output_dirname IN VARCHAR2, output_filename IN VARCHAR2; Parameters Table 44-11 EXPORT_XML_TO_FILE Procedure Parameters Parameter Description object_ids Any of these identifiers. The name of a schema, such as GLOBAL . The fully qualified name of an analytic workspace in the form owner.aw_name .AW , such as GLOBAL.GLOBAL.AW . Cube Dimension Named build process Measure folder You can specify multiple objects by separating the names with commas. Note : When exporting an individual object, be sure to export any objects required to reconstruct it. For example, when you export a cube, you must also export the dimensions of the cube. options_dirname The case-sensitive name of a database directory that contains options_filename . See " Export Options " . options_filename The name of a file containing an XML document of export options. See " Export Options " . output_dirname The case-sensitive name of a database directory where output_filename is created. output_filename The name of the template file created by the procedure. Export Options The default settings for the export options are appropriate in most cases, and you can omit the options_dirname and options_filename parameters. However, when upgrading Oracle OLAP 10 g metadata to OLAP 12 c , you must specify an XML document that changes the default settings, like the following: <?xml version="2.0"?> <Export> <ExportOptions> <Option Name="SuppressNamespace" Value="True"/> <Option Name="SuppressOwner" Value="True"/> <Option Name="PreserveTableOwners" Value="True"/> </ExportOptions> </Export> You can create this XML document manually or by using the CREATE_EXPORT_OPTIONS Procedure . Usage Notes See " DBMS_CUBE - Upgrading 10g Analytic Workspaces " .