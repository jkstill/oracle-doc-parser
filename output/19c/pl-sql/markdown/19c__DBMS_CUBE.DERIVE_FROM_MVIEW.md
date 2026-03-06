---
id: 19c__DBMS_CUBE.DERIVE_FROM_MVIEW
name: DBMS_CUBE.DERIVE_FROM_MVIEW
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE
tags: [dbms_cube]
source_file: DBMS_CUBE.html
---

# DBMS_CUBE.DERIVE_FROM_MVIEW

This function generates an XML template that defines a cube with materialized view capabilities, using the information derived from an existing relational materialized view.

## Syntax

```sql
DBMS_CUBE.DERIVE_FROM_MVIEW (
          mvowner        IN  VARCHAR2,
          mvname         IN  VARCHAR2,
          sam_parameters IN  CLOB  DEFAULT NULL)
     RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| mvowner | VARCHAR2 | IN | Owner of the relational materialized view. |
| mvname | VARCHAR2 | IN | Name of the relational materialized view. For restrictions, see " Requirements for the Relational Materialized View " . A single cube materialized view can replace many of the relational materialized views for a table. Choose the materialized view that has the lowest levels of the dimension hierarchies that you want represented in the cube materialized view. |
| sam_parameters | CLOB | IN | Optional list of parameters in the form ' parameter1 = value1 , parameter2 = value2 ,...'. See " SQL Aggregation Management Parameters " . |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_CUBE.DERIVE_FROM_MVIEW ( mvowner IN VARCHAR2, mvname IN VARCHAR2, sam_parameters IN CLOB DEFAULT NULL) RETURN CLOB; Parameters Table 44-8 DERIVE_FROM_MVIEW Function Parameters Parameter Description mvowner Owner of the relational materialized view. mvname Name of the relational materialized view. For restrictions, see " Requirements for the Relational Materialized View " . A single cube materialized view can replace many of the relational materialized views for a table. Choose the materialized view that has the lowest levels of the dimension hierarchies that you want represented in the cube materialized view. sam_parameters Optional list of parameters in the form ' parameter1 = value1 , parameter2 = value2 ,...'. See " SQL Aggregation Management Parameters " . Returns An XML template that defines an analytic workspace containing a cube enabled as a materialized view. Usage Notes To create a cube materialized view from an XML template, use the IMPORT_XML procedure. Then use the REFRESH_MVIEW procedure to refresh the cube materialized view with data. See " Using SQL Aggregation Management " . Examples The following example generates an XML template named sales_cube.xml from the CAL_MONTH_SALES_MV relational materialized view in the SH schema.