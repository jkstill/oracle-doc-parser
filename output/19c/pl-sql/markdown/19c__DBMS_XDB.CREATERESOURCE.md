---
id: 19c__DBMS_XDB.CREATERESOURCE
name: DBMS_XDB.CREATERESOURCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.CREATERESOURCE

The deprecated function creates a new resource. The description of the overload options precede each version of the syntax

## Syntax

```sql
DBMS_XDB.CREATERESOURCE(
     abspath        IN  VARCHAR2,
     datarow        IN  REF SYS.XMLTYPE,
     createfolders  IN  BOOLEAN := FALSE)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource to create. The path name's parent folder must already exist in the hierarchy. In other words, if /foo/bar.txt is passed in, then folder /foo must already exist. |
| data |  |  | String buffer containing new resource's contents. The data is parsed to check if it contains a schema-based XML document, and the contents are stored as schema-based in the schema's default table. Otherwise, it is saved as binary data. |
| datarow | REF | IN | REF to an XMLType row to be used as the contents |
| csid |  |  | Character set id of the document. Must be a valid Oracle ID; otherwise returns an error. If CSID is not specified, or if a zero CSID is specified, then the character set id of the document is determined as follows: From the abspath extension, determine the resource's MIME type. If the MIME type is */xml, then the encoding is detected based on Appendix F of the W3C XML 1.0 Reference at http://www.w3.org/TR/2000/REC-xml-20001006 ; Otherwise, it is defaulted to the database character set. |
| createfolders | BOOLEAN | IN | If TRUE , create the parent folders if they do not exist |
| schemaurl |  |  | For XML data, schema URL data conforms to (default NULL ) |
| elem |  |  | Element name (default NULL ) |

**Returns:** `BOOLEAN`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the CREATERESOURCE Functions . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the CREATERESOURCE Functions . Syntax Given a REF to an existing XMLType row, creates a resource whose contents point to that row. That row should not already exist inside another resource: DBMS_XDB.CREATERESOURCE( abspath IN VARCHAR2, datarow IN REF SYS.XMLTYPE, createfolders IN BOOLEAN := FALSE) RETURN BOOLEAN; Creates a resource with a specified BLOB as its contents, and specifies character set of the source BLOB : DBMS_XDB.CREATERESOURCE( abspath IN VARCHAR2, data IN BLOB, csid IN NUMBER :=0, createfolders IN BOOLEAN := FALSE) RETURN BOOLEAN; Creates a resource with a specified BFILE as its contents, and specifies character set of the source BFILE : DBMS_XDB.CREATERESOURCE ( abspath IN VARCHAR2, data IN BFILE, csid IN NUMBER :=0, createfolders IN BOOLEAN := FALSE) RETURN BOOLEAN; Creates a resource with a specified CLOB as its contents: DBMS_XDB.CREATERESOURCE ( abspath IN VARCHAR2, data IN CLOB, createfolders IN BOOLEAN := FALSE) RETURN BOOLEAN; Given a string, inserts a new resource into the hierarchy with the string as the contents: DBMS_XDB.CREATERESOURCE ( abspath IN VARCHAR2, data IN VARCHAR2, schemaurl IN VARCHAR2 := NULL, elem IN VARCHAR2 := NULL) RETURN BOOLEAN; Given an XMLTYPE and a schema URL, inserts a new resource into the hierarchy with the XMLTYPE as the contents: DBMS_XDB.CREATERESOURCE ( abspath IN VARCHAR2, data IN SYS.XMLTYPE, schemaurl IN VARCHAR2 := NULL, elem IN VARCHAR2 := NULL) RETURN BOOLEAN; Parameters Table 194-10 CREATERESOURCE Function Parameters Parameter Description abspath Absolute path of the resource to create. The path name's parent folder must already exist in the hierarchy. In other words, if /foo/bar.txt is passed in, then folder /foo must already exist. data String buffer containing new resource's contents. The data is parsed to check if it contains a schema-based XML document, and the contents are stored as schema-based in the schema's default table. Otherwise, it is saved as binary data. datarow REF to an XMLType row to be used as the contents csid Character set id of the document. Must be a valid Oracle ID; otherwise returns an error. If CSID is not specified, or if a zero CSID is specified, then the character set id of the document is determined as follows: From the abspath extension, determine the resource's MIME type. If the MIME type is */xml, then the encoding is detected based on Appendix F of the W3C XML 1.0 Reference at http://www.w3.org/TR/2000/REC-xml-20001006 ; Otherwise, it is defaulted to the database character set. createfolders If TRUE , create the parent folders if they do not exist schemaurl For XML data, schema URL data conforms to (default NULL ) elem Element name (default NULL ) Return Values TRUE if operation successful; FALSE , otherwise.