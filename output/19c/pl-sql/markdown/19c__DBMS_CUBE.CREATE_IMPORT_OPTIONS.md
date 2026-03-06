---
id: 19c__DBMS_CUBE.CREATE_IMPORT_OPTIONS
name: DBMS_CUBE.CREATE_IMPORT_OPTIONS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE
tags: [dbms_cube]
source_file: DBMS_CUBE.html
---

# DBMS_CUBE.CREATE_IMPORT_OPTIONS

This procedure creates an input XML document that describes processing options for the IMPORT_XML Procedure.

## Syntax

```sql
DBMS_CUBE.CREATE_IMPORT_OPTIONS (
          out_options_xml  IN/OUT  CLOB,
          validate_only    IN      BOOLEAN   DEFAULT FALSE,
          rename_table     IN      VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| out_options_xml | IN | IN | Contains the generated XML document, which can be passed to the options_xml parameter of the IMPORT_XML Procedure . |
| validate_only | BOOLEAN | IN | TRUE causes the IMPORT_XML procedure to validate the metadata described in the input file or the in_xml parameter, without committing the changes to the metadata. |
| rename_table | VARCHAR2 | IN | The name of a table identifying new names for the imported objects, in the form [ schema_name .] table_name . The IMPORT_XML procedure creates objects using the names specified in the table instead of the ones specified in the XML document. See the Usage Notes for the format of the rename table. |

## Usage Notes

Syntax DBMS_CUBE.CREATE_IMPORT_OPTIONS ( out_options_xml IN/OUT CLOB, validate_only IN BOOLEAN DEFAULT FALSE, rename_table IN VARCHAR2 DEFAULT NULL); Parameters Table 44-5 CREATE_IMPORT_OPTIONS Procedure Parameters Parameter Description out_options_xml Contains the generated XML document, which can be passed to the options_xml parameter of the IMPORT_XML Procedure . validate_only TRUE causes the IMPORT_XML procedure to validate the metadata described in the input file or the in_xml parameter, without committing the changes to the metadata. rename_table The name of a table identifying new names for the imported objects, in the form [ schema_name .] table_name . The IMPORT_XML procedure creates objects using the names specified in the table instead of the ones specified in the XML document. See the Usage Notes for the format of the rename table. Usage Notes See the information about using a rename table in DBMS_CUBE - Upgrading 10g Analytic Workspaces . Examples This example specifies validation only and a rename table. For an example of the import CLOB being used in an import, see " IMPORT_XML Procedure " . DECLARE importClob clob; BEGIN dbms_lob.createtemporary(importClob, TRUE); dbms_cube.create_import_options(out_options_xml => importClob, rename_table => 'MY_OBJECT_MAP', validate_only => TRUE); dbms_output.put_line(importClob); END; / It generates the following XML document: <?xml version="1.0"?> <Import> <ImportOptions> <Option Name="ValidateOnly" Value="TRUE"/> <Option Name="RenameTable" Value="MY_OBJECT_MAP"/> </ImportOptions> </Import>