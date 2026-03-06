---
id: 19c__DBMS_XMLSCHEMA.INPLACEEVOLVE
name: DBMS_XMLSCHEMA.INPLACEEVOLVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA
tags: [dbms_xmlschema]
source_file: DBMS_XMLSCHEMA.html
---

# DBMS_XMLSCHEMA.INPLACEEVOLVE

This procedure evolves registered schemas by propagating schema changes to object types and tables.

## Syntax

```sql
DBMS_XMLSCHEMA.INPLACEEVOLVE(
   schemaURL    IN   VARCHAR2, 
   diffXML      IN   XMLType, 
   flags        IN   NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schemaurl | VARCHAR2 | IN | URL of the schema to evolve |
| diffXML | XMLType | IN | Changes to be applied to the schema. This is an XML document conforming to the XDIFF schema and specifies what changes need to be applied and the locations in the schema document where the changes are to be applied. |
| flags | NUMBER) | IN | The following bits may be set in this parameter to control the behavior of this procedure: INPLACE_EVOLVE (value 1, meaning that bit 1 is on) – Perform in-place XML schema evolution: construct a new XML schema and validate it (against the XML schema for XML schemas); construct the DDL statements needed to evolve the instance-document disk structures, execute the DDL statements, and replace the old XML schema with the new. INPLACE_TRACE (value 2, meaning that bit 2 is on) – Perform all steps necessary for in-place evolution, except executing the DDL statements and overwriting the old XML schema with the new, then write both the DDL statements and the new XML schema to a trace file. That is, each of the bits constructs the new XML schema, validates it, and determines the steps needed to evolve the disk structures underlying the instance documents. In addition: Bit INPLACE_EVOLVE carries out those evolution steps and replaces the old XML schema with the new. Bit INPLACE_TRACE saves the evolution steps and the new XML schema in a trace file (it does not carry out the evolution steps) |

## Usage Notes

Syntax DBMS_XMLSCHEMA.INPLACEEVOLVE( schemaURL IN VARCHAR2, diffXML IN XMLType, flags IN NUMBER); Parameters Table 210-10 INPLACEEVOLVE Procedure Parameters Parameter Description schemaurl URL of the schema to evolve diffXML Changes to be applied to the schema. This is an XML document conforming to the XDIFF schema and specifies what changes need to be applied and the locations in the schema document where the changes are to be applied. flags The following bits may be set in this parameter to control the behavior of this procedure: INPLACE_EVOLVE (value 1, meaning that bit 1 is on) – Perform in-place XML schema evolution: construct a new XML schema and validate it (against the XML schema for XML schemas); construct the DDL statements needed to evolve the instance-document disk structures, execute the DDL statements, and replace the old XML schema with the new. INPLACE_TRACE (value 2, meaning that bit 2 is on) – Perform all steps necessary for in-place evolution, except executing the DDL statements and overwriting the old XML schema with the new, then write both the DDL statements and the new XML schema to a trace file. That is, each of the bits constructs the new XML schema, validates it, and determines the steps needed to evolve the disk structures underlying the instance documents. In addition: Bit INPLACE_EVOLVE carries out those evolution steps and replaces the old XML schema with the new. Bit INPLACE_TRACE saves the evolution steps and the new XML schema in a trace file (it does not carry out the evolution steps) Exceptions The procedure raises exceptions in the following cases: An error will be raised for invalid XPATH expressions and for XDIFF documents that do not conform to the xdiff schema. Path expressions that are syntactically correct but result in an invalid node in the schema document will result in an error. If the schema change makes the schema an ill-formed XML document or an invalid XML schema, this will raise an error. Any errors resulting from CREATE TYPE , ALTER TYPE and like commands will generate error messages. Usage Notes Users are required to backup all their data before attempting in-place evolution, as there is no rollback with this operation. A user must register their new XML schema with the database using the REGISTERSCHEMA Procedures and the REGISTERURI Procedure at a schema URL that is different from that of the one to be evolved. If the new schema registers successfully and is usable, only then should the user attempt to evolve the existing schema to the new schema by means of this subprogram. If the registration of the new schema is successful, then the user must delete this schema (and all its dependent objects) before attempting to evolve the schema at the old schema URL.