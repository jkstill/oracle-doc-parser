---
id: 19c__DBMS_DATA_MINING.IMPORT_MODEL
name: DBMS_DATA_MINING.IMPORT_MODEL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.IMPORT_MODEL

This procedure imports one or more data mining models. The procedure is overloaded. You can call it to import mining models from a dump file set, or you can call it to import a single mining model from a PMML document.

## Syntax

```sql
DBMS_DATA_MINING.IMPORT_MODEL (
      filename          IN  VARCHAR2,
      directory         IN  VARCHAR2,
      model_filter      IN  VARCHAR2 DEFAULT NULL,
      operation         IN  VARCHAR2 DEFAULT NULL,
      remote_link       IN  VARCHAR2 DEFAULT NULL,
      jobname           IN  VARCHAR2 DEFAULT NULL,
      schema_remap      IN  VARCHAR2 DEFAULT NULL,
      tablespace_remap  IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| filename | VARCHAR2 | IN | Name of the dump file set from which the models should be imported. The dump file set must have been created by the EXPORT_MODEL procedure or the expdp export utility of Oracle Data Pump. The dump file set can contain one or more files. (Refer to " EXPORT_MODEL Procedure " for details.) If the dump file set contains multiple files, you can specify ' filename %U' instead of listing them. For example, if your dump file set contains 3 files, archive01.dmp , archive02.dmp , and archive03.dmp , you can import them by specifying 'archive%U' . |
| directory | VARCHAR2 | IN | Name of a pre-defined directory object that specifies where the dump file set is located. Both the exporting and the importing user must have read/write access to the directory object and to the file system directory that it identifies. Note: The target database must have also have read/write access to the file system directory. |
| model_filter | VARCHAR2 | IN | Optional parameter that specifies one or more models to import. If you do not specify a value for model_filter , all models in the dump file set are imported. You can also specify NULL (the default) or 'ALL' to import all models. The value of model_filter can be one or more model names. The following are valid filters. 'mymodel1' 'name IN (''mymodel2'',''mymodel3'')' The first causes IMPORT_MODEL to import a single model named mymodel1 . The second causes IMPORT_MODEL to import two models, mymodel2 and mymodel3 . |
| operation | VARCHAR2 | IN | Optional parameter that specifies whether to import the models or the SQL statements that create the models. By default, the models are imported. You can specify either of the following values for operation : 'IMPORT' — Import the models (Default) 'SQL_FILE' — Write the SQL DDL for creating the models to a text file. The text file is named job_name .sql and is located in the dump set directory. |
| remote_link | VARCHAR2 | IN | Optional parameter that specifies the name of a database link to a remote system. The default value is NULL . A database link is a schema object in a local database that enables access to objects in a remote database. When you specify a value for remote_link , you can import models into the local database from the remote database. The import is fileless; no dump file is involved. The IMP_FULL_DATABASE role is required for importing the remote models. The EXP_FULL_DATABASE privilege, the CREATE DATABASE LINK privilege, and other privileges may also be required. |
| jobname | VARCHAR2 | IN | Optional parameter that specifies the name of the import job. By default, the name has the form username _imp_ nnnn , where nnnn is a number. For example, a job name in the SCOTT schema might be SCOTT_imp_134 . If you specify a job name, it must be unique within the schema. The maximum length of the job name is 30 characters. A log file for the import job, named jobname .log, is created in the same directory as the dump file set. |
| schema_remap | VARCHAR2 | IN | Optional parameter for importing into a different schema. By default, models are exported and imported within the same schema. If the dump file set belongs to a different schema, you must specify a schema mapping in the form export_user : import_user . For example, you would specify 'SCOTT:MARY' to import a model exported by SCOTT into the MARY schema. Note: In some cases, you may need to have the IMP_FULL_DATABASE privilege or the SYS role to import a model from a different schema. |
| tablespace_remap | VARCHAR2 | IN | Optional parameter for importing into a different tablespace. By default, models are exported and imported within the same tablespace. If the dump file set belongs to a different tablespace, you must specify a tablespace mapping in the form export_tablespace : import_tablespace . For example, you would specify 'TBLSPC01:TBLSPC02' to import a model that was exported from tablespace TBLSPC01 into tablespace TBLSPC02 . Note: In some cases, you may need to have the IMP_FULL_DATABASE privilege or the SYS role to import a model from a different tablespace. |
| model_name |  |  | Name for the new model that will be created in the database as a result of an import from PMML The name must be unique within the user's schema. |
| pmmldoc |  |  | The PMML document representing the model to be imported. The PMML document has an XMLTYPE object type. See "XMLTYPE" for details. |
| strict_check |  |  | Whether or not an error occurs when the PMML document contains sections that are not part of core PMML (for example, Output or Targets). Oracle Data Mining supports only core PMML; any non-core features may affect the scoring representation. If the PMML does not strictly conform to core PMML and strict_check is set to TRUE , then IMPORT_MODEL returns an error. If strict_check is FALSE (the default), then the error is suppressed. The model may be imported and scored. |

## Usage Notes

Import from a dump file set You can import mining models from a dump file set that was created by the EXPORT_MODEL Procedure . IMPORT_MODEL and EXPORT_MODEL use Oracle Data Pump technology to export to and import from a dump file set. When Oracle Data Pump is used directly to export/import an entire schema or database, the mining models in the schema or database are included. EXPORT_MODEL and IMPORT_MODEL export/import mining models only. You can import a mining model represented in Predictive Model Markup Language (PMML). The model must be of type RegressionModel , either linear regression or binary logistic regression. PMML is an XML-based standard specified by the Data Mining Group ( https://dmg.org ). Applications that are PMML-compliant can deploy PMML-compliant models that were created by any vendor. Oracle Data Mining supports the core features of PMML 3.1 for regression models. See Also: Oracle Data Mining User's Guide for more information about exporting and importing mining models Oracle Database Utilities for information about Oracle Data Pump https://dmg.org/dmg-faq.html for more information about PMML See Also: Oracle Data Mining User's Guide for more information about exporting and importing mining models Oracle Database Utilities for information about Oracle Data Pump https://dmg.org/dmg-faq.html for more information about PMML Syntax Imports a mining model from a dump file set: DBMS_DATA_MINING.IMPORT_MODEL ( filename IN VARCHAR2, directory IN VARCHAR2, model_filter IN VARCHAR2 DEFAULT NULL, operation IN VARCHAR2 DEFAULT NULL, remote_link IN VARCHAR2 DEFAULT NULL, jobname IN VARCHAR2 DEFAULT NULL, schema_remap IN VARCHAR2 DEFAULT NULL, tablespace_remap IN VARCHAR2 DEFAULT NULL); Imports a mining model from a PMML document: DBMS_DATA_MINING.IMPORT_MODEL ( model_name IN VARCHAR2, pmmldoc IN XMLTYPE strict_check IN BOOLEAN DEFAULT FALSE);