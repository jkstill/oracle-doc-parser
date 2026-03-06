---
id: 19c__DBMS_XMLSTORAGE_MANAGE.RENAMECOLLECTIONTABLE
name: DBMS_XMLSTORAGE_MANAGE.RENAMECOLLECTIONTABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORAGE_MANAGE
tags: [dbms_xmlstorage_manage]
source_file: DBMS_XMLSTORAGE_MANAGE.html
---

# DBMS_XMLSTORAGE_MANAGE.RENAMECOLLECTIONTABLE

This procedure renames a collection table to the given table name.

## Syntax

```sql
DBMS_XMLSTORAGE_MANAGE.RENAMECOLLECTIONTABLE (
   owner_name             IN VARCHAR2 DEFAULT USER,
   table_name             IN VARCHAR2,
   column_name            IN VARCHAR2 DEFAULT NULL,
   xpath                  IN VARCHAR2,
   collection_table_name  IN VARCHAR2
   namespaces             IN VARCHAR2 default NULL);  // For release 11.2 only
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner_name | VARCHAR2 | IN | The name of the owner |
| table_name | VARCHAR2 | IN | The name of a base table that can be used as the starting point for specifying the collection table |
| column_name | VARCHAR2 | IN | An XMLType column that can be the starting point for specifying the collection table |
| xpath | VARCHAR2 | IN | The XPath expression that specifies the collection table |
| collection_table_name | VARCHAR2 | IN | The name of the collection table |
| namespaces | VARCHAR2 | IN | For Oracle Database 11 g Release 2 (11.2) and higher. The namespaces used in XPath. |

## Usage Notes

An XPath expression specifies the collection table, starting from the XMLtype base table or an XMLType column of the base table. This procedure provides the only way to derive a collection table name from the corresponding collection type name because there is no direct schema annotation for the purpose. Syntax DBMS_XMLSTORAGE_MANAGE.RENAMECOLLECTIONTABLE ( owner_name IN VARCHAR2 DEFAULT USER, table_name IN VARCHAR2, column_name IN VARCHAR2 DEFAULT NULL, xpath IN VARCHAR2, collection_table_name IN VARCHAR2 namespaces IN VARCHAR2 default NULL); // For release 11.2 only Parameters Table 213-9 RENAMECOLLECTIONTABLE Procedure Parameters Parameter Description owner_name The name of the owner table_name The name of a base table that can be used as the starting point for specifying the collection table column_name An XMLType column that can be the starting point for specifying the collection table xpath The XPath expression that specifies the collection table collection_table_name The name of the collection table namespaces For Oracle Database 11 g Release 2 (11.2) and higher. The namespaces used in XPath. Usage Notes Call this procedure after registering the XML schema. The table name serves as a prefix to the index names. Oracle recommends using this function because it makes query execution plans more readable. Report errors that occur while this procedure runs to the user that called the procedure. Note: This procedure is limited to the structured storage model. For Oracle Database 11 g Release 2 (11.2) and higher, only, this function accepts XPath notation as well as DOT notation. If XPath notation is used, a namespaces parameter may also be required. Note: This procedure is limited to the structured storage model.