---
id: 19c__DBMS_MGD_ID_UTL.GET_COMPONENTS
name: DBMS_MGD_ID_UTL.GET_COMPONENTS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGD_ID_UTL
tags: [dbms_mgd_id_utl]
source_file: DBMS_MGD_ID_UTL.html
---

# DBMS_MGD_ID_UTL.GET_COMPONENTS

This function returns all relevant separated component names separated by semicolon (;) for the specified scheme.

## Syntax

```sql
DBMS_MGD_ID_UTL.GET_COMPONENTS (
   category_id IN VARCHAR2,
   scheme_name IN VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| category_id | VARCHAR2 | IN | Category ID |
| scheme_name | VARCHAR2) | IN | Name of scheme |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_MGD_ID_UTL.GET_COMPONENTS ( category_id IN VARCHAR2, scheme_name IN VARCHAR2) RETURN VARCHAR2; Parameters Table 109-9 GET_COMPONENTS Function Parameters Parameter Description category_id Category ID scheme_name Name of scheme Usage Notes The return value contains the component names separated by a semicolon (;) for the specified scheme. Examples The following example gets the components: --Contents of get_components.sql DECLARE id mgd_id; getcomps VARCHAR2(1000); getencodings VARCHAR2(1000); getschemenames VARCHAR2(1000); BEGIN DBMS_MGD_ID_UTL.set_java_logging_level(DBMS_MGD_ID_UTL.LOGGING_LEVEL_OFF); DBMS_MGD_ID_UTL.refresh_category(DBMS_MGD_ID_UTL.get_category_id('EPC', NULL)); getcomps := DBMS_MGD_ID_UTL.get_components(1,'SGTIN-64'); dbms_output.put_line('Component names are: ' || getcomps); getencodings := DBMS_MGD_ID_UTL.get_encodings(1,'SGTIN-64'); dbms_output.put_line('Encodings are: ' || getencodings); getschemenames := DBMS_MGD_ID_UTL.get_scheme_names(1); dbms_output.put_line('Scheme names are: ' || getschemenames); END; / SHOW ERRORS; SQL> @get_components.sql . . . Component names are: filter,gtin,companyprefixlength,companyprefix,companyprefixindex,itemref,serial Encodings are: ONS_HOSTNAME,LEGACY,TAG_ENCODING,PURE_IDENTITY,BINARY Scheme names are: GIAI-64,GIAI-96,GID-96,GRAI-64,GRAI-96,SGLN-64,SGLN-96,SGTIN-64,SGTIN-96,SSCC-64 ,SSCC-96,USDOD-64,USDOD-96 PL/SQL procedure successfully completed. . . .