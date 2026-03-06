---
id: 19c__MGD_ID.TO_STRING
name: MGD_ID.TO_STRING
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: MGD_ID
tags: [mgd_id]
source_file: MGD_ID-Package-Types.html
---

# MGD_ID.TO_STRING

This function returns the semicolon (;) separated component name value pairs of the MGD_ID object.

## Syntax

```sql
TO_STRING 
 RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Syntax TO_STRING RETURN VARCHAR2; Examples The following example converts the MGD_ID object into a string value: -- Contents of tostring3.sql file call DBMS_MGD_ID_UTL.set_proxy('www-proxy.example.com', '80'); DECLARE id MGD_ID; BEGIN DBMS_MGD_ID_UTL.refresh_category(DBMS_MGD_ID_UTL.get_category_id('EPC', NULL)); dbms_output.put_line('..Testing to_string'); id := mgd_id('EPC', NULL, 'urn:epc:id:gid:0037000.30241.1041970', 'scheme=GID-96'); DBMS_OUTPUT.PUT_LINE('mgd_id object as a string'); DBMS_OUTPUT.PUT_LINE(id.to_string); END; / SHOW ERRORS; call DBMS_MGD_ID_UTL.remove_proxy(); connect / as sysdba; drop user mgduser cascade; SQL> @tostring3.sql . . . ..Testing to_string mgd_id object as a string category_id =1;schemes = GID-96;objectclass = 30241;generalmanager = 0037000;scheme = GID-96;1 = 1;serial = 1041970 PL/SQL procedure successfully completed. . .