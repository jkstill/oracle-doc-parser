---
id: 19c__DBMS_XMLSTORAGE_MANAGE.XPATH2TABCOLMAPPING
name: DBMS_XMLSTORAGE_MANAGE.XPATH2TABCOLMAPPING
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORAGE_MANAGE
tags: [dbms_xmlstorage_manage]
source_file: DBMS_XMLSTORAGE_MANAGE.html
---

# DBMS_XMLSTORAGE_MANAGE.XPATH2TABCOLMAPPING

This function maps a path expression (in XPath notation or DOT notations) to the corresponding table name and column name. This is necessary in cases in which the user wants to create an index on this table, or to add a constraint, or to rename a table to make query execution plans more readable.

## Syntax

```sql
DBMS_XMLSTORAGE_MANAGE.XPATH2TABCOLMAPPING (
   owner_name   IN  VARCHAR2 DEFAULT USER, 
   table_name   IN  VARCHAR2,
   column_name  IN  VARCHAR2 DEFAULT NULL,
   xpath        IN  VARCHAR2,
   namespaces   IN  VARCHAR2 DEFAULT NULL)
 RETURN XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner_user |  |  | Owner's name |
| table_name | VARCHAR2 | IN | Name of the base table |
| column_name | VARCHAR2 | IN | Optional name of the XML type column if table_name is not an XMLtype table. If table_name refers to XMLType table then column_name should be NULL. |
| xpath | VARCHAR2 | IN | Path expression in DOT notation or XPath notation (see examples below) |
| namespaces | VARCHAR2 | IN | Optional namespace definitions for path expression |

**Returns:** `XMLTYPE`

## Usage Notes

Syntax DBMS_XMLSTORAGE_MANAGE. XPATH2TABCOLMAPPING ( owner_name IN VARCHAR2 DEFAULT USER, table_name IN VARCHAR2, column_name IN VARCHAR2 DEFAULT NULL, xpath IN VARCHAR2, namespaces IN VARCHAR2 DEFAULT NULL) RETURN XMLTYPE; Parameters Table 213-10 XPATH2TABCOLMAPPING Procedure Parameters Parameter Description owner_user Owner's name table_name Name of the base table column_name Optional name of the XML type column if table_name is not an XMLtype table. If table_name refers to XMLType table then column_name should be NULL. xpath Path expression in DOT notation or XPath notation (see examples below) namespaces Optional namespace definitions for path expression Examples XPath2TablColMapping evaluated on XMLType table with Xpath Notation, namespaces provided SELECT XDB.DBMS_XMLSTORAGE_MANAGE.XPATH2TABCOLMAPPING ( USER, 'XML_TAB', '', '//n1:item/n1:location','''xdbXmark'' as "n1"') FROM DUAL; This produces a result, for example: <Result> <Mapping TableName="SYS_NT12345" ColumnName="location"/> </Result> This allows us to define an index or constraint on table SYS_NT12345 and column location . XPath2TablColMapping evaluated on table not of XMLType but with XMLType column by means of DOT notation SELECT XDB.DBMS_XMLSTORAGE_MANAGE.XPATH2TABCOLMAPPING ( USER,'PurchaseOrderTab','XMLCOL','xmldata.LineItems.LineItem', '') FROM DUAL;