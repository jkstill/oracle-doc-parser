---
id: 19c__DBMS_METADATA.CONVERT
name: DBMS_METADATA.CONVERT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_METADATA
tags: [dbms_metadata]
source_file: DBMS_METADATA.html
---

# DBMS_METADATA.CONVERT

The DBMS_METADATA.CONVERT functions and procedures transform input XML documents.

## Syntax

```sql
DBMS_METADATA.CONVERT (
   handle   IN NUMBER,
   document IN sys.XMLType)
 RETURN sys.ku$_multi_ddls;

DBMS_METADATA.CONVERT (
  handle   IN NUMBER,
  document IN CLOB)
 RETURN sys.ku$_multi_ddls;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER | IN | The handle returned from OPENW |
| document | sys.XMLType) | IN | The XML document containing object metadata of the type of the OPENW handle |
| result |  |  | The converted document |

**Returns:** `sys.ku$_multi_ddls`

## Usage Notes

The CONVERT functions return creation DDL. The CONVERT procedures return either XML or DDL, depending on the specified transforms. See Also: Subprograms for Submitting XML to the Database See Also: Subprograms for Submitting XML to the Database Syntax The CONVERT functions are as follows: DBMS_METADATA.CONVERT ( handle IN NUMBER, document IN sys.XMLType) RETURN sys.ku$_multi_ddls; DBMS_METADATA.CONVERT ( handle IN NUMBER, document IN CLOB) RETURN sys.ku$_multi_ddls; The CONVERT procedures are as follows: DBMS_METADATA.CONVERT ( handle IN NUMBER, document IN sys.XMLType, result IN OUT NOCOPY CLOB); DBMS_METADATA.CONVERT ( handle IN NUMBER, document IN CLOB, result IN OUT NOCOPY CLOB); Parameters Table 107-7 CONVERT Subprogram Parameters Parameter Description handle The handle returned from OPENW document The XML document containing object metadata of the type of the OPENW handle result The converted document Return Values Either XML or DDL, depending on the specified transforms.