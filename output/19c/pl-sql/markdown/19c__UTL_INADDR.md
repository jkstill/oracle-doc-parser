---
id: 19c__UTL_INADDR
name: UTL_INADDR
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_INADDR
tags: [utl_inaddr]
source_file: UTL_INADDR.html
---

# UTL_INADDR

This UTL_INADDR example retrieves the local host name and IP address.

## Syntax

```sql
SET serveroutput on
BEGIN
  DBMS_OUTPUT.PUT_LINE(UTL_INADDR.GET_HOST_NAME);  -- get local host name
  DBMS_OUTPUT.PUT_LINE(UTL_INADDR.GET_HOST_ADDRESS);  -- get local IP addr
END;
/
```

## Usage Notes

SET serveroutput on BEGIN DBMS_OUTPUT.PUT_LINE(UTL_INADDR.GET_HOST_NAME); -- get local host name DBMS_OUTPUT.PUT_LINE(UTL_INADDR.GET_HOST_ADDRESS); -- get local IP addr END; /