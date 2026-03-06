---
id: 19c__DBMS_CUBE.EXPORT_XML
name: DBMS_CUBE.EXPORT_XML
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE
tags: [dbms_cube]
source_file: DBMS_CUBE.html
---

# DBMS_CUBE.EXPORT_XML

This procedure writes OLAP metadata to a CLOB.

## Syntax

```sql
DBMS_CUBE.EXPORT_XML
       (object_ids            IN      VARCHAR2,
        out_xml               IN/OUT  CLOB;

DBMS_CUBE.EXPORT_XML
       (object_ids            IN      VARCHAR2,
        options_xml           IN      CLOB,
        out_xml               IN/OUT  CLOB;

DBMS_CUBE.EXPORT_XML
       (object_ids            IN      VARCHAR2,
        options_dirname       IN      VARCHAR2,
        options_filename      IN      VARCHAR2,
        out_xml               IN/OUT  CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_ids | VARCHAR2 | IN | Any of these identifiers. The name of a schema, such as GLOBAL . The fully qualified name of an analytic workspace in the form owner.aw_name .AW , such as GLOBAL.GLOBAL.AW . Cube Dimension Named build process Measure folder You can specify multiple objects by separating the names with commas. Note : When exporting an individual object, be sure to export any objects required to reconstruct it. For example, when exporting a cube, you must also export the dimensions of the cube. |
| options_dirname | VARCHAR2 | IN | The case-sensitive name of a database directory that contains options_filename . |
| options_filename | VARCHAR2 | IN | A file containing an XML document of export options. |
| options_xml | CLOB | IN | A CLOB variable that contains an XML document of export options. Use the CREATE_EXPORT_OPTIONS Procedure to generate this document. |
| out_xml | IN | IN | A CLOB variable that will store the XML document of OLAP metadata for the objects listed in object_ids . |

## Usage Notes

Syntax DBMS_CUBE.EXPORT_XML (object_ids IN VARCHAR2, out_xml IN/OUT CLOB; DBMS_CUBE.EXPORT_XML (object_ids IN VARCHAR2, options_xml IN CLOB, out_xml IN/OUT CLOB; DBMS_CUBE.EXPORT_XML (object_ids IN VARCHAR2, options_dirname IN VARCHAR2, options_filename IN VARCHAR2, out_xml IN/OUT CLOB; Parameters Table 44-10 EXPORT_XML Procedure Parameters Parameter Description object_ids Any of these identifiers. The name of a schema, such as GLOBAL . The fully qualified name of an analytic workspace in the form owner.aw_name .AW , such as GLOBAL.GLOBAL.AW . Cube Dimension Named build process Measure folder You can specify multiple objects by separating the names with commas. Note : When exporting an individual object, be sure to export any objects required to reconstruct it. For example, when exporting a cube, you must also export the dimensions of the cube. options_dirname The case-sensitive name of a database directory that contains options_filename . options_filename A file containing an XML document of export options. options_xml A CLOB variable that contains an XML document of export options. Use the CREATE_EXPORT_OPTIONS Procedure to generate this document. out_xml A CLOB variable that will store the XML document of OLAP metadata for the objects listed in object_ids . Export Options The default settings for the export options are appropriate in many cases, so you can omit the options_xml parameter or the options_dirname and options_filename parameters. However, when upgrading Oracle OLAP 10 g metadata to OLAP 12 c , you must specify an XML document that changes the default settings. This example changes all of the parameters from False to True; set them appropriately for your schema. <?xml version="1.0"?> <Export> <ExportOptions> <Option Name="SuppressNamespace" Value="True"/> <Option Name="SuppressOwner" Value="True"/> <Option Name="PreserveTableOwners" Value="True"/> </ExportOptions> </Export> You can create this XML document manually or by using the CREATE_EXPORT_OPTIONS Procedure . Usage Notes See " DBMS_CUBE - Upgrading 10g Analytic Workspaces " . Example For an example of using EXPORT_XML in an upgrade to the same schema, see " DBMS_CUBE - Upgrading 10g Analytic Workspaces " . The following PL/SQL script copies an OLAP 12 c analytic workspace named GLOBAL12 from the GLOBAL_AW schema to the GLOBAL schema. No upgrade is performed. To upgrade into a different schema, change the example as follows: Call the INITIALIZE_CUBE_UPGRADE procedure. Call the CREATE_EXPORT_OPTIONS procedure with the additional parameter setting SUPPRESS_NAMESPACE=>TRUE . The PL/SQL client must be connected to the database as GLOBAL . The GLOBAL user must have SELECT permissions on GLOBAL_AW.AW$GLOBAL and on all relational data sources. BEGIN -- Create a CLOB for the export options dbms_lob.createtemporary(optionsClob, TRUE); dbms_cube.create_export_options(out_options_xml=>optionsClob, suppress_owner=>TRUE, preserve_table_owners=>TRUE); -- Create a CLOB for the XML template dbms_lob.createtemporary(exportClob, TRUE); -- Export metadata from an analytic workspace to a CLOB dbms_cube.export_xml(object_ids=>'GLOBAL_AW.GLOBAL12.AW', options_xml=>optionsClob, out_xml=>exportClob); -- Import metadata from the CLOB dbms_cube.import_xml(in_xml=>exportClob); -- Load and aggregate the data dbms_cube.build(script=>'GLOBAL.UNITS_CUBE, GLOBAL.PRICE_AND_COST_CUBE'); END; /