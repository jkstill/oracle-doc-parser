---
id: 19c__DBMS_CAPTURE_ADM.INCLUDE_EXTRA_ATTRIBUTE
name: DBMS_CAPTURE_ADM.INCLUDE_EXTRA_ATTRIBUTE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CAPTURE_ADM
tags: [dbms_capture_adm]
source_file: DBMS_CAPTURE_ADM.html
---

# DBMS_CAPTURE_ADM.INCLUDE_EXTRA_ATTRIBUTE

This procedure includes or excludes an extra attribute in logical change records (LCRs) captured by the specified capture process or synchronous capture.

## Syntax

```sql
DBMS_CAPTURE_ADM.INCLUDE_EXTRA_ATTRIBUTE(
   capture_name    IN  VARCHAR2,
   attribute_name  IN  VARCHAR2,
   include         IN  BOOLEAN   DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| capture_name | VARCHAR2 | IN | The name of the capture process or synchronous capture. Specify an existing capture process name or synchronous capture name. Do not specify an owner. |
| attribute_name | VARCHAR2 | IN | The name of the attribute to be included in or excluded from LCRs captured by the capture process or synchronous capture. The following names are valid settings: row_id The rowid of the row changed in a row LCR. This attribute is not included in DDL LCRs, or in row LCRs for index-organized tables. The type is VARCHAR2 . serial# The serial number of the session that performed the change captured in the LCR. The type is NUMBER . session# The identifier of the session that performed the change captured in the LCR. The type is NUMBER . thread# The thread number of the instance in which the change captured in the LCR was performed. Typically, the thread number is relevant only in an Oracle Real Application Clusters (Oracle RAC) environment. The type is NUMBER . tx_name The name of the transaction that includes the LCR. The type is VARCHAR2 . username The name of the user who performed the change captured in the LCR. The type is VARCHAR2 . |
| include | BOOLEAN | IN | If TRUE , then the specified attribute is included in LCRs captured by the capture process or synchronous capture. If FALSE , then the specified attribute is excluded from LCRs captured by the capture process or synchronous capture. |

## Usage Notes

Syntax DBMS_CAPTURE_ADM.INCLUDE_EXTRA_ATTRIBUTE( capture_name IN VARCHAR2, attribute_name IN VARCHAR2, include IN BOOLEAN DEFAULT TRUE); Parameters Table 35-12 INCLUDE_EXTRA_ATTRIBUTE Procedure Parameters Parameter Description capture_name The name of the capture process or synchronous capture. Specify an existing capture process name or synchronous capture name. Do not specify an owner. attribute_name The name of the attribute to be included in or excluded from LCRs captured by the capture process or synchronous capture. The following names are valid settings: row_id The rowid of the row changed in a row LCR. This attribute is not included in DDL LCRs, or in row LCRs for index-organized tables. The type is VARCHAR2 . serial# The serial number of the session that performed the change captured in the LCR. The type is NUMBER . session# The identifier of the session that performed the change captured in the LCR. The type is NUMBER . thread# The thread number of the instance in which the change captured in the LCR was performed. Typically, the thread number is relevant only in an Oracle Real Application Clusters (Oracle RAC) environment. The type is NUMBER . tx_name The name of the transaction that includes the LCR. The type is VARCHAR2 . username The name of the user who performed the change captured in the LCR. The type is VARCHAR2 . include If TRUE , then the specified attribute is included in LCRs captured by the capture process or synchronous capture. If FALSE , then the specified attribute is excluded from LCRs captured by the capture process or synchronous capture. Usage Notes Some information is not captured by a capture process or synchronous capture unless you use this procedure to specify that the information should be captured. If you want to exclude an extra attribute that is being captured by a capture process or synchronous capture, then specify the attribute and specify FALSE for the include parameter.