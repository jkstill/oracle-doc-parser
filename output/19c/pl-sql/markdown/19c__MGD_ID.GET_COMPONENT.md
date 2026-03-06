---
id: 19c__MGD_ID.GET_COMPONENT
name: MGD_ID.GET_COMPONENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: MGD_ID
tags: [mgd_id]
source_file: MGD_ID-Package-Types.html
---

# MGD_ID.GET_COMPONENT

This function returns the value of the specified MGD_ID component.

## Syntax

```sql
GET_COMPONENT (
   component_name  IN  VARCHAR2)
 RETURN VARCHAR2 DETERMINISTIC;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| component_name | VARCHAR2) | IN | Name of component |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax GET_COMPONENT ( component_name IN VARCHAR2) RETURN VARCHAR2 DETERMINISTIC; Parameters Table 289-8 GET_COMPONENT Function Parameter Parameter Description component_name Name of component Usage Notes If the code is an invalid code, meaning its structure is not defined in the metadata table, an error is raised. If the code is valid, but it does not contain the required component, NULL is returned. Examples The following example returns the general manager, object class, and serial number components for this GID-96 identity component: --Contents of get_components.sql file call DBMS_MGD_ID_UTL.set_proxy('www-proxy.example.com', '80'); DECLARE id MGD_ID; BEGIN DBMS_MGD_ID_UTL.set_java_logging_level(DBMS_MGD_ID_UTL.LOGGING_LEVEL_OFF); DBMS_MGD_ID_UTL.refresh_category(DBMS_MGD_ID_UTL.get_category_id('EPC', NULL)); --------------- --PURE_IDENTIT --------------- dbms_output.put_line('..Testing constructor with pure identity'); ---------------------------------------------------------------------- -- PURE_IDENTITY representation can be translated to BINARY and -- TAG_ENCODING ONLY when BOTH scheme and filer are provided. ---------------------------------------------------------------------- id := MGD_ID('EPC', NULL, 'urn:epc:id:sgtin:0037000.030241.1041970', 'scheme=SGTIN-64;filter=3'); dbms_output.put_line(id.to_string); dbms_output.put_line('filter = ' || id.get_component('filter')); dbms_output.put_line('company prefix = ' || id.get_component('companyprefix')); dbms_output.put_line('itemref = ' || id.get_component('itemref')); dbms_output.put_line('serial = ' || id.get_component('serial')); dbms_output.put_line('BINARY format = ' || id.format(NULL, 'BINARY')); dbms_output.put_line('PURE_IDENTITY format = ' || id.format(NULL, 'PURE_IDENTITY')); dbms_output.put_line('TAG_ENCODING format = ' || id.format(NULL, 'TAG_ENCODING')); END; / SHOW ERRORS; call DBMS_MGD_ID_UTL.remove_proxy(); SQL> @get_component.sql . . . ..Testing constructor with pure identity category_id =1;filter = 3;schemes = SGTIN-64;companyprefixlength = 7;companyprefix = 0037000;scheme = SGTIN-64;serial = 1041970;itemref = 030241 filter = 3 company prefix = 0037000 itemref = 030241 serial = 1041970 BINARY format =1001100000000000001000001110110001000010000011111110011000110010 PURE_IDENTITY format = urn:epc:id:sgtin:0037000.030241.1041970 TAG_ENCODING format = urn:epc:tag:sgtin-64:3.0037000.030241.1041970 PL/SQL procedure successfully completed. . . .