---
id: 19c__DBMS_XSTREAM_ADM.ADD_SUBSET_OUTBOUND_RULES
name: DBMS_XSTREAM_ADM.ADD_SUBSET_OUTBOUND_RULES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.ADD_SUBSET_OUTBOUND_RULES

This procedure adds subset rules to an outbound server configuration. Subset rules instruct the outbound server to stream out a subset of the changes to the specified tables. Outbound servers can stream out a subset of both rows and columns.

## Syntax

```sql
DBMS_XSTREAM_ADM.ADD_SUBSET_OUTBOUND_RULES(
   server_name      IN VARCHAR2,
   table_name       IN VARCHAR2,
   condition        IN VARCHAR2  DEFAULT NULL,
   column_list      IN DBMS_UTILITY.LNAME_ARRAY,
   keep             IN BOOLEAN   DEFAULT TRUE,
   source_database  IN VARCHAR2  DEFAULT NULL);

DBMS_XSTREAM_ADM.ADD_SUBSET_OUTBOUND_RULES(
   server_name      IN VARCHAR2,
   table_name       IN VARCHAR2,
   condition        IN VARCHAR2  DEFAULT NULL,
   column_list      IN VARCHAR2  DEFAULT NULL,
   keep             IN BOOLEAN   DEFAULT TRUE,
   source_database  IN VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| server_name | VARCHAR2 | IN | The name of the outbound server to which rules are being added. Specify an existing outbound server. Do not specify an owner. |
| table_name | VARCHAR2 | IN | The name of the table specified as [ schema_name .] object_name . For example, you can specify hr.employees . If the schema is not specified, then the current user is the default. If the outbound server configuration uses a local capture process, then the table must exist at the local source database. If the outbound server configuration uses a downstream capture process, then the table must exist at both the source database and at the downstream capture database. The specified table cannot have any LOB, LONG , or LONG RAW columns currently or in the future. |
| condition | VARCHAR2 | IN | The subset condition. Specify this condition similar to the way you specify conditions in a WHERE clause in SQL. For example, to specify rows in the hr.employees table where the salary is greater than 4000 and the job_id is SA_MAN , enter the following as the condition: ' salary > 4000 and job_id = ''SA_MAN'' ' If NULL , then the procedure raises an error. Note: The quotation marks in the preceding example are all single quotation marks. |
| column_list | DBMS_UTILITY.LNAME_ARRAY | IN | The list of columns either to include in the outbound server configuration or to exclude from the outbound server configuration. Whether the columns are included or excluded depends on the setting for the keep parameter. The columns can be specified in the following ways: Comma-delimited list of type VARCHAR2 . A PL/SQL associative array of type DBMS_UTILITY.LNAME_ARRAY , where each element is the name of a column. Specify the first column in position 1. The last position must be NULL . To include or exclude all of the columns in a table, specify each column in the table in the list or array. If NULL , then the procedure raises an error. |
| keep | BOOLEAN | IN | If TRUE , then the columns specified in the column_list parameter are kept as part of the outbound server configuration. Therefore, changes to these columns that satisfy the condition in the condition parameter are streamed to the outbound server's client application. If FALSE , then the columns specified in the column_list parameter are excluded from the outbound server configuration. Therefore, changes to these columns are not streamed to the outbound server's client application. See Also: " Usage Notes " |
| source_database | VARCHAR2 | IN | The global name of the container where the specified table_names and schema_names are located. If non- NULL , then a condition is added to the outbound server's rules to filter the LCRs based on the global name of the source database. If NULL , then the procedure does not add a condition regarding the source database to the generated rules. In a CDB, specify the global name of the container to which the rules pertain. The container can be the root or a PDB. For example, mycdb.example.com or hrpdb.example.com . See Oracle Database XStream Guide for more information about setting this parameter in a CDB. If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify DBS1 and the domain is EXAMPLE.COM , then the procedure specifies DBS1.EXAMPLE.COM automatically. |

## Usage Notes

This procedure is overloaded. One column_list parameter is type VARCHAR2 and the other column_list parameter is type DBMS_UTILITY.LNAME_ARRAY . These parameters enable you to enter the list of columns in different ways and are mutually exclusive. Note: This procedure does not add rules to the outbound server's capture process. Note: This procedure does not add rules to the outbound server's capture process. Syntax DBMS_XSTREAM_ADM.ADD_SUBSET_OUTBOUND_RULES( server_name IN VARCHAR2, table_name IN VARCHAR2, condition IN VARCHAR2 DEFAULT NULL, column_list IN DBMS_UTILITY.LNAME_ARRAY, keep IN BOOLEAN DEFAULT TRUE, source_database IN VARCHAR2 DEFAULT NULL); DBMS_XSTREAM_ADM.ADD_SUBSET_OUTBOUND_RULES( server_name IN VARCHAR2, table_name IN VARCHAR2, condition IN VARCHAR2 DEFAULT NULL, column_list IN VARCHAR2 DEFAULT NULL, keep IN BOOLEAN DEFAULT TRUE, source_database IN VARCHAR2 DEFAULT NULL); Parameters Table 217-8 ADD_SUBSET_OUTBOUND_RULES Procedure Parameters Parameter Description server_name The name of the outbound server to which rules are being added. Specify an existing outbound server. Do not specify an owner. table_name The name of the table specified as [ schema_name .] object_name . For example, you can specify hr.employees . If the schema is not specified, then the current user is the default. If the outbound server configuration uses a local capture process, then the table must exist at the local source database. If the outbound server configuration uses a downstream capture process, then the table must exist at both the source database and at the downstream capture database. The specified table cannot have any LOB, LONG , or LONG RAW columns currently or in the future. condition The subset condition. Specify this condition similar to the way you specify conditions in a WHERE clause in SQL. For example, to specify rows in the hr.employees table where the salary is greater than 4000 and the job_id is SA_MAN , enter the following as the condition: ' salary > 4000 and job_id = ''SA_MAN'' ' If NULL , then the procedure raises an error. Note: The quotation marks in the preceding example are all single quotation marks. column_list The list of columns either to include in the outbound server configuration or to exclude from the outbound server configuration. Whether the columns are included or excluded depends on the setting for the keep parameter. The columns can be specified in the following ways: Comma-delimited list of type VARCHAR2 . A PL/SQL associative array of type DBMS_UTILITY.LNAME_ARRAY , where each element is the name of a column. Specify the first column in position 1. The last position must be NULL . To include or exclude all of the columns in a table, specify each column in the table in the list or array. If NULL , then the procedure raises an error. keep If TRUE , then the columns specified in the column_list parameter are kept as part of the outbound server configuration. Therefore, changes to these columns that satisfy the condition in the condition parameter are streamed to the outbound server's client application. If FALSE , then the columns specified in the column_list parameter are excluded from the outbound server configuration. Therefore, changes to these columns are not streamed to the outbound server's client application. See Also: " Usage Notes " source_database The global name of the container where the specified table_names and schema_names are located. If non- NULL , then a condition is added to the outbound server's rules to filter the LCRs based on the global name of the source database. If NULL , then the procedure does not add a condition regarding the source database to the generated rules. In a CDB, specify the global name of the container to which the rules pertain. The container can be the root or a PDB. For example, mycdb.example.com or hrpdb.example.com . See Oracle Database XStream Guide for more information about setting this parameter in a CDB. If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify DBS1 and the domain is EXAMPLE.COM , then the procedure specifies DBS1.EXAMPLE.COM automatically. Usage Notes When the keep parameter is set to TRUE , this procedure creates a keep columns declarative rule-based transformation for the columns listed in column_list . When the keep parameter is set to FALSE , this procedure creates a delete column declarative rule-based transformation for each column listed in column_list .