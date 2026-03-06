---
id: 19c__DBMS_MGD_ID_UTL.VALIDATE_SCHEME
name: DBMS_MGD_ID_UTL.VALIDATE_SCHEME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGD_ID_UTL
tags: [dbms_mgd_id_utl]
source_file: DBMS_MGD_ID_UTL.html
---

# DBMS_MGD_ID_UTL.VALIDATE_SCHEME

This function validates the input tag data translation XML against the Oracle Database tag data translation schema.

## Syntax

```sql
DBMS_MGD_ID_UTL.VALIDATE_SCHEME (
   xml_scheme IN CLOB)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xml_scheme | CLOB) | IN | Scheme to be validated. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_MGD_ID_UTL.VALIDATE_SCHEME ( xml_scheme IN CLOB) RETURN VARCHAR2; Parameters Table 109-19 VALIDATE_SCHEME Function Parameters Parameter Description xml_scheme Scheme to be validated. Usage Notes The return value contains the components names for the specified scheme. Examples See the ADD_SCHEME Procedure or the EPC_TO_ORACLE_SCHEME Function for an example.