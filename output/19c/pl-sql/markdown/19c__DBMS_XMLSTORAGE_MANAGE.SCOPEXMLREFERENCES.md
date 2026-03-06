---
id: 19c__DBMS_XMLSTORAGE_MANAGE.SCOPEXMLREFERENCES
name: DBMS_XMLSTORAGE_MANAGE.SCOPEXMLREFERENCES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORAGE_MANAGE
tags: [dbms_xmlstorage_manage]
source_file: DBMS_XMLSTORAGE_MANAGE.html
---

# DBMS_XMLSTORAGE_MANAGE.SCOPEXMLREFERENCES

This procedure scopes all XML references. Scoped REF types require less storage space and allow more efficient access than unscoped REF types.

## Syntax

```sql
DBMS_XMLSTORAGE_MANAGE.SCOPEXMLREFERENCES;
```

## Usage Notes

Syntax DBMS_XMLSTORAGE_MANAGE.SCOPEXMLREFERENCES; Usage Notes If you have used SETOUTOFLINE Procedure in the DBMS_XMLSTORAGE_MANAGE package to avoid raising '1000 column limit' errors during XML schema registration, you should also use SCOPEXMLREFERENCES Procedure . Using SCOPEXMLREFERENCES after XML schema registration and before loading XML instance data, makes these reference scoped to the out-of-line table only. Note: This procedure is limited to the structured storage model. Note: This procedure is limited to the structured storage model.