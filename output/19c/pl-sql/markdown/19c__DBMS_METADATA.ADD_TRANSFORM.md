---
id: 19c__DBMS_METADATA.ADD_TRANSFORM
name: DBMS_METADATA.ADD_TRANSFORM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_METADATA
tags: [dbms_metadata]
source_file: DBMS_METADATA.html
---

# DBMS_METADATA.ADD_TRANSFORM

The DBMS_METADATA.ADD_TRANSFORM function is used for both retrieval and submission.

## Syntax

```sql
DBMS_METADATA.ADD_TRANSFORM (
   handle       IN NUMBER,
   name         IN VARCHAR2,
   encoding     IN VARCHAR2 DEFAULT NULL,
   object_type  IN VARCHAR2 DEFAULT NULL)
 RETURN NUMBER;
```

**Returns:** `NUMBER`

## Usage Notes

When this procedure is used to retrieve objects, it specifies a transform that FETCH_xxx applies to the XML representation of the retrieved objects. When used to submit objects, it specifies a transform that CONVERT or PUT applies to the XML representation of the submitted objects. It is possible to add more than one transform. See Also: Subprograms for Retrieving Multiple Objects From the Database Subprograms for Submitting XML to the Database " SET_TRANSFORM_PARAM and SET_REMAP_PARAM Procedures " for information about how to modify and customize transform output See Also: Subprograms for Retrieving Multiple Objects From the Database Subprograms for Submitting XML to the Database " SET_TRANSFORM_PARAM and SET_REMAP_PARAM Procedures " for information about how to modify and customize transform output Syntax DBMS_METADATA.ADD_TRANSFORM ( handle IN NUMBER, name IN VARCHAR2, encoding IN VARCHAR2 DEFAULT NULL, object_type IN VARCHAR2 DEFAULT NULL) RETURN NUMBER; Parameters Table 107-4 ADD_TRANSFORM Function Parameters Parameters Description handle The handle returned from OPEN when this transform is used to retrieve objects. Or the handle returned from OPENW when this transform is used in the submission of XML metadata. name The name of the transform. The name can be an internal keyword like DDL to use internally stored stylesheets. If the name contains a colon, it is interpreted as directory_object_name:file_name of a user-supplied Extensible Stylesheet Language Transformation (XSLT) script. Otherwise, name designates a transform implemented by DBMS_METADATA . See Table 107-5 for descriptions of available transforms. encoding The name of the Globalization Support character set in which the stylesheet pointed to by name is encoded. This is only valid if name is a URL. If left NULL and the URL is external to the database, UTF-8 encoding is assumed. If left NULL and the URL is internal to the database (that is, it begins with /oradb/ ), then the encoding is assumed to be the database character set. object_type The definition of this parameter depends upon whether you are retrieving objects or submitting XML metadata. When you use ADD_TRANFORM to retrieve objects, the following definition of object_type applies: Designates the object type to which the transform applies. (Note that this is an object type name, not a path name.) By default the transform applies to the object type of the OPEN handle. When the OPEN handle designates a heterogeneous object type, the following behavior can occur: if object_type is omitted, the transform applies to all object types within the heterogeneous collection if object_type is specified, the transform only applies to that specific object type within the collection If you omit this parameter you can add the DDL transform to all objects in a heterogeneous collection with a single call. If you supply this parameter, you can add a transform for a specific object type. When you use ADD_TRANSFORM in the submission of XML metadata, this parameter is the object type to which the transform applies. By default, it is the object type of the OPENW handle. Because the OPENW handle cannot designate a heterogeneous object type, the caller would normally leave this parameter NULL in the ADD_TRANSFORM calls. The following table describes the transforms available on the ADD_TRANSFORM function. Because new transforms are occasionally added, you might want to query the DBMS_METADATA_TRANSFORMS view to see all valid Oracle-supplied transforms for specific object types. Table 107-5 Transforms Available on ADD_TRANSFORM Function Object Type Transform Name Input Doc Type Output Doc Type Description All DDL XML DDL Convert XML to SQL to create the object All MODIFY XML XML Modify XML document according to transform parameters Subset SXML XML SXML Convert XML to SXML Subset MODIFYSXML SXML SXML Modify SXML document according to transform parameters Subset SXMLDDL SXML DDL Convert SXML to DDL Subset ALTERXML SXML difference document ALTER_XML Generate ALTER_XML from SXML difference document. (See the DBMS_METADATA_DIFF PL/SQL package for more information about SXML difference format.) The following parameters are valid for the ALTERXML transform: XPATH - The XPATH of the object being altered NAME - Name of the object being altered ALTERABLE - Affirms that the object can be altered. If the object cannot be altered, a NOT_ALTERABLE element is inserted whose value indicates the reason. CLAUSE_TYPE - The type of clause (for example, ADD_COLUMN ) COLUMN_ATTRIBUTE - The attribute being modified CONSTRAINT_TYPE - The type of constraint (for example, UNIQUE or PRIMARY ) Subset ALTERDDL ALTER_XML ALTER_DDL Convert ALTER_XML to ALTER_DDL Return Values The opaque handle that is returned is used as input to SET_TRANSFORM_PARAM and SET_REMAP_PARAM . Note that this handle is different from the handle returned by OPEN or OPENW ; it refers to the transform, not the set of objects to be retrieved.