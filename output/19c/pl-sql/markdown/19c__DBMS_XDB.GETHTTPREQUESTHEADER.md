---
id: 19c__DBMS_XDB.GETHTTPREQUESTHEADER
name: DBMS_XDB.GETHTTPREQUESTHEADER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.GETHTTPREQUESTHEADER

This deprecated function, if called during an HTTP request serviced by XDB, returns the values of the passed header. It is used by routines that implement custom authentication.

## Syntax

```sql
DBMS_XDB.GETHTTPREQUESTHEADER(
    header_name    IN   VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| header_name | VARCHAR2) | IN | Passed header |

**Returns:** `VARCHAR2`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . Note: This procedure is deprecated in Release 12 c . Syntax DBMS_XDB.GETHTTPREQUESTHEADER( header_name IN VARCHAR2) RETURN VARCHAR2; Parameters Table 194-20 GETHTTPREQUESTHEADER Function Parameters Parameter Description header_name Passed header Return Values Returns NULL in case the header is not present in the request, or for AUTHENTICATION , for security reasons.