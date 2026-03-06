---
id: 19c__DBMS_XMLSTORAGE_MANAGE.INDEXXMLREFERENCES
name: DBMS_XMLSTORAGE_MANAGE.INDEXXMLREFERENCES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORAGE_MANAGE
tags: [dbms_xmlstorage_manage]
source_file: DBMS_XMLSTORAGE_MANAGE.html
---

# DBMS_XMLSTORAGE_MANAGE.INDEXXMLREFERENCES

This procedure creates unique indexes on the REF columns of the given XML type table or the XML type column of a given table.

## Syntax

```sql
DBMS_XMLSTORAGE_MANAGE.INDEXXMLREFERENCES (
   owner_name    IN VARCHAR2 DEFAULT USER, 
   table_name    IN VARCHAR2,
   column_name   IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner_name | VARCHAR2 | IN | The owner's name |
| table_name | VARCHAR2 | IN | The table being indexed |
| column_name | VARCHAR2 | IN | A column name. Not needed for XML type tables. |
| index_name |  |  | The name of the newly created index |

## Usage Notes

If the procedure creates multiple REF columns, it appends _1 , _2 , and so on to their names. Syntax DBMS_XMLSTORAGE_MANAGE.INDEXXMLREFERENCES ( owner_name IN VARCHAR2 DEFAULT USER, table_name IN VARCHAR2, column_name IN VARCHAR2 DEFAULT NULL); Parameters Table 213-6 INDEXXMLREFERENCES Procedure Parameters Parameter Description owner_name The owner's name table_name The table being indexed column_name A column name. Not needed for XML type tables. index_name The name of the newly created index Usage Notes This procedure is only used if the REF s are scoped. See SCOPEXMLREFERENCES Procedure . Indexed REF s lead to better performance when joins between the base table and a child table occur in the query plan. If the base table has a higher selectivity than the child table, there is no need to index the REF s. If the selectivity of the child table is higher than that of the base table and if no indexes are present, then the join of one row in the child table with the base table leads to a full table scan of the base table. INDEXXMLREFERENCES does not index REF s recursively in child tables of a table it is called on. To do this, Oracle recommends calling the procedure from within a loop over the XML_OUT_OF_LINE_TABLES or XML_NESTED_TABLES view. This creates the index names from the current value of a column in the view. Note: This procedure is limited to the structured storage model. Note: This procedure is limited to the structured storage model.