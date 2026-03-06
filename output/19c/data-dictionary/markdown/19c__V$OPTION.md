---
id: 19c__V$OPTION
name: V$OPTION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-OPTION.html
---

# V$OPTION

V$OPTION displays Oracle Database options and features.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PARAMETER | VARCHAR2(64) |  |
| VALUE | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Typically, although not always, options must be separately licensed, whereas features come with the product and are enabled based on the product that is running (for example, Enterprise Edition). Column Datatype Description PARAMETER VARCHAR2(64) Name of the option (or feature) VALUE VARCHAR2(64) Indicates whether the option (or feature) is installed ( TRUE ) or not ( FALSE ) CON_ID NUMBER The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data See Also: Oracle Database Licensing Information User Manual for more information about Oracle Database options and features See Also: Oracle Database Licensing Information User Manual for more information about Oracle Database options and features