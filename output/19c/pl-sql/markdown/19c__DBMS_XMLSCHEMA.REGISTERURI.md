---
id: 19c__DBMS_XMLSCHEMA.REGISTERURI
name: DBMS_XMLSCHEMA.REGISTERURI
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA
tags: [dbms_xmlschema]
source_file: DBMS_XMLSCHEMA.html
---

# DBMS_XMLSCHEMA.REGISTERURI

This procedure registers an XML Schema specified by a URI name.

## Syntax

```sql
DBMS_XMLSCHEMA.REGISTERURI(
   schemaurl      IN  VARCHAR2,
   schemadocuri   IN  VARCHAR2,
   local          IN  BOOLEAN := TRUE,
   gentypes       IN  BOOLEAN := TRUE,
   genbean        IN  BOOLEAN := FALSE,
   gentables      IN  BOOLEAN := TRUE,
   force          IN  BOOLEAN := FALSE,
   owner          IN  VARCHAR2 := NULL, 
   options          IN  PLS_INTEGER := 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schemaurl | VARCHAR2 | IN | Uniquely identifies the schema document. Can be used inside schemaLocation attribute of XML Schema import element. |
| schemadocuri | VARCHAR2 | IN | Pathname (URI) corresponding to the physical location of the schema document. The URI path could be based on HTTP, FTP, DB or Oracle XML DB protocols. This function constructs a URIType instance using the urifactory , and invokes the REGISTERSCHEMA Procedures . |
| local | BOOLEAN | IN | Determines whether this is a local or global schema. By default, all schemas are registered as local schemas, under /sys/schemas/ <username>/... If a schema is registered as global, it is added under /sys/schemas/PUBLIC/... The user needs write privileges on the directory to register a global schema. |
| gentypes | BOOLEAN | IN | Determines whether the compiler generate object types. By default, TRUE . |
| genbean | BOOLEAN | IN | Determines whether the compiler generate Java beans. By default, FALSE . |
| gentables | BOOLEAN | IN | Determines whether the compiler generate default tables. TRUE by default. |
| force | BOOLEAN | IN | TRUE: schema registration will not raise errors. Instead, it creates an invalid XML schema object in case of any errors. By default, the value of this parameter is FALSE . |
| owner | VARCHAR2 | IN | This parameter specifies the name of the database user owning the XML schema object. By default, the user registering the schema owns the XML schema object. This parameter can be used to register a XML schema to be owned by a different database user. |
| options | PLS_INTEGER | IN | Additional options to specify how the schema should be registered. The various options are represented as bits of an integer and the options parameter should be constructed by doing a BITOR of the desired bits. Possible bits: REGISTER_NODOCID - this will suppress the creation of the DOCID column for out of line tables. This is a storage optimization which might be desirable when we do not need to join back to the document table (for example if we do not care about rewriting certain queries that could be rewritten by making use of the DOCID column) |

## Usage Notes

Note: As of Oracle Database 11g Release 2 (11.2) the genbean parameter is deprecated. Oracle recommends that you do not use this parameter in new applications. Support for this feature is for backward compatibility only. Note: As of Oracle Database 11g Release 2 (11.2) the genbean parameter is deprecated. Oracle recommends that you do not use this parameter in new applications. Support for this feature is for backward compatibility only. Syntax DBMS_XMLSCHEMA.REGISTERURI( schemaurl IN VARCHAR2, schemadocuri IN VARCHAR2, local IN BOOLEAN := TRUE, gentypes IN BOOLEAN := TRUE, genbean IN BOOLEAN := FALSE, gentables IN BOOLEAN := TRUE, force IN BOOLEAN := FALSE, owner IN VARCHAR2 := NULL, options IN PLS_INTEGER := 0); Parameters Table 210-13 REGISTERURI Procedure Parameters Parameter Description schemaurl Uniquely identifies the schema document. Can be used inside schemaLocation attribute of XML Schema import element. schemadocuri Pathname (URI) corresponding to the physical location of the schema document. The URI path could be based on HTTP, FTP, DB or Oracle XML DB protocols. This function constructs a URIType instance using the urifactory , and invokes the REGISTERSCHEMA Procedures . local Determines whether this is a local or global schema. By default, all schemas are registered as local schemas, under /sys/schemas/ <username>/... If a schema is registered as global, it is added under /sys/schemas/PUBLIC/... The user needs write privileges on the directory to register a global schema. gentypes Determines whether the compiler generate object types. By default, TRUE . genbean Determines whether the compiler generate Java beans. By default, FALSE . gentables Determines whether the compiler generate default tables. TRUE by default. force TRUE: schema registration will not raise errors. Instead, it creates an invalid XML schema object in case of any errors. By default, the value of this parameter is FALSE . owner This parameter specifies the name of the database user owning the XML schema object. By default, the user registering the schema owns the XML schema object. This parameter can be used to register a XML schema to be owned by a different database user. options Additional options to specify how the schema should be registered. The various options are represented as bits of an integer and the options parameter should be constructed by doing a BITOR of the desired bits. Possible bits: REGISTER_NODOCID - this will suppress the creation of the DOCID column for out of line tables. This is a storage optimization which might be desirable when we do not need to join back to the document table (for example if we do not care about rewriting certain queries that could be rewritten by making use of the DOCID column)