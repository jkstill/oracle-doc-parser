---
id: 19c__DBMS_XMLSCHEMA.PURGESCHEMA
name: DBMS_XMLSCHEMA.PURGESCHEMA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA
tags: [dbms_xmlschema]
source_file: DBMS_XMLSCHEMA.html
---

# DBMS_XMLSCHEMA.PURGESCHEMA

This procedure removes the XML schema.

## Syntax

```sql
DBMS_XMLSCHEMA.PURGESCHEMA( 
   schemaid   IN  RAW);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schemaid | RAW) | IN | ID of the schema to be purged |

## Usage Notes

See Also: "XMLSCHEMA Storage and Query: Advanced" chapter of the Oracle XML DB Developer's Guide See Also: "XMLSCHEMA Storage and Query: Advanced" chapter of the Oracle XML DB Developer's Guide Syntax DBMS_XMLSCHEMA.PURGESCHEMA( schemaid IN RAW); Parameters Table 210-11 PURGESCHEMA Procedure Parameters Parameter Description schemaid ID of the schema to be purged Usage Notes The schema should have been originally registered for binary encoding and should have been deleted in the HIDE mode. Once a schema has been deleted in HIDE mode, it continues to exist in the XML DB dictionary and is used for decoding already encoded documents. The user invokes this interface when there are no stored instances encoded with this schema. Once the schema is purged, any space used by that schema will be reclaimed and documents encoded using the schema will raise an error if an attempt is made to decode them. The Schema ID can be obtained from the catalog views.