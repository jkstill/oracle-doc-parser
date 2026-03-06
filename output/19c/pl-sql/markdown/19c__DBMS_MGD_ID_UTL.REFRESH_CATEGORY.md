---
id: 19c__DBMS_MGD_ID_UTL.REFRESH_CATEGORY
name: DBMS_MGD_ID_UTL.REFRESH_CATEGORY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGD_ID_UTL
tags: [dbms_mgd_id_utl]
source_file: DBMS_MGD_ID_UTL.html
---

# DBMS_MGD_ID_UTL.REFRESH_CATEGORY

This function refreshes the metadata information on the Java stack for the specified category.

## Syntax

```sql
DBMS_MGD_ID_UTL.REFRESH_CATEGORY (
   category_id  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| category_id | VARCHAR2) | IN | Category ID |

**Returns:** `UNKNOWN`

## Usage Notes

This function must be called before using MGD_ID functions. Syntax DBMS_MGD_ID_UTL.REFRESH_CATEGORY ( category_id IN VARCHAR2); Parameters Table 109-13 REFRESH_CATEGORY Function Parameters Parameter Description category_id Category ID Examples The following example refreshes the metadata information for the EPC category ID. --Contents of tostring3.sql call DBMS_MGD_ID_UTL.set_proxy('www-proxy.example.com', '80'); DECLARE id MGD_ID; BEGIN DBMS_MGD_ID_UTL.set_java_logging_level(DBMS_MGD_ID_UTL.LOGGING_LEVEL_OFF); DBMS_MGD_ID_UTL.refresh_category(DBMS_MGD_ID_UTL.get_category_id('EPC', NULL)); dbms_output.put_line('..Testing to_string'); DBMS_OUTPUT.PUT_LINE('test to_string'); id := mgd_id('EPC', NULL, 'urn:epc:id:gid:0037000.30241.1041970', 'scheme=GID-96'); DBMS_OUTPUT.PUT_LINE('mgd_id object as a string'); DBMS_OUTPUT.PUT_LINE(id.to_string); END; / SHOW ERRORS; call DBMS_MGD_ID_UTL.remove_proxy(); SQL> @tostring3.sql ..Testing to_string test to_string mgd_id object as a string category_id =1;schemes = GID-96;objectclass = 30241;generalmanager = 0037000;scheme = GID-96;1 = 1;serial = 1041970 PL/SQL procedure successfully completed.