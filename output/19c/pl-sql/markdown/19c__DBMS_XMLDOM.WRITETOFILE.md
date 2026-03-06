---
id: 19c__DBMS_XMLDOM.WRITETOFILE
name: DBMS_XMLDOM.WRITETOFILE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.WRITETOFILE

This overloaded procedure writes an XML node or XML document to a specified node.

## Syntax

```sql
DBMS_XMLDOM.WRITETOFILE(
   n          IN      DOMNODE,
   fileName   IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE | IN | DOMNODE |
| fileName | VARCHAR2) | IN | File to which to write. The filename should be in the format of database_directory_object_name/filename , for example mydir/filename (on windows, use \ instead of / ). |
| charset |  |  | specified character set |
| doc |  |  | DOMDOCUMENT |
| charset |  |  | Character set |

## Usage Notes

The specific forms of functionality are described along with the syntax declarations. Syntax Writes XML node to specified file using the database character set (See Also: DOMNode Subprograms ): DBMS_XMLDOM.WRITETOFILE( n IN DOMNODE, fileName IN VARCHAR2); Writes XML node to specified file using the specified character set, which is passed in as a separate parameter (See Also: DOMNode Subprograms ): DBMS_XMLDOM.WRITETOFILE( n IN DOMNODE, fileName IN VARCHAR2, charset IN VARCHAR2); Writes an XML document to a specified file using database character set (See Also: DOMDocument Subprograms ): DBMS_XMLDOM.WRITETOFILE( doc IN DOMDOCUMENT, filename IN VARCHAR2); Writes an XML document to a specified file using specified character set (See Also: DOMDocument Subprograms ): DBMS_XMLDOM.WRITETOFILE( doc IN DOMDOCUMENT, fileName IN VARCHAR2, charset IN VARCHAR2); Parameters Table 204-137 WRITETOFILE Procedure Parameters Parameter Description n DOMNODE fileName File to which to write. The filename should be in the format of database_directory_object_name/filename , for example mydir/filename (on windows, use \ instead of / ). charset specified character set doc DOMDOCUMENT charset Character set