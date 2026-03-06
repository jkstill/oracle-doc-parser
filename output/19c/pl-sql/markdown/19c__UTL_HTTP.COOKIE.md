---
id: 19c__UTL_HTTP.COOKIE
name: UTL_HTTP.COOKIE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.COOKIE

The COOKIE type is the PL/SQL record type that represents an HTTP cookie. The COOKIE_TABLE type is a PL/SQL index-by-table type that represents a collection of HTTP cookies.

## Syntax

```sql
TYPE cookie IS RECORD (
   name  VARCHAR2(256),
   value  VARCHAR2(1024),
   domain  VARCHAR2(256),
   expire  TIMESTAMP WITH TIME ZONE,
   path  VARCHAR2(1024),
   secure  BOOLEAN,
   version  PLS_INTEGER,
   comment  VARCHAR2(1024));

TYPE cookie_table IS TABLE OF cookie INDEX BY binary_integer;
```

## Usage Notes

TYPE cookie IS RECORD ( name VARCHAR2(256), value VARCHAR2(1024), domain VARCHAR2(256), expire TIMESTAMP WITH TIME ZONE, path VARCHAR2(1024), secure BOOLEAN, version PLS_INTEGER, comment VARCHAR2(1024)); TYPE cookie_table IS TABLE OF cookie INDEX BY binary_integer; Fields of COOKIE Record Type Table 264-7 shows the fields for the COOKIE and COOKIE_TABLE record types. PL/SQL programs do not usually examine or change the cookie information stored in the UTL_HTTP package. The cookies are maintained by the package transparently. They are maintained inside the UTL_HTTP package, and they last for the duration of the database session only. PL/SQL applications that require cookies to be maintained beyond the lifetime of a database session can read the cookies using GET_COOKIES, store them persistently in a database table, and re-store the cookies back in the package using ADD_COOKIES in the next database session. All the fields in the cookie record, except for the comment field, must be stored. Do not alter the cookie information, which can result in an application error in the Web server or compromise the security of the PL/SQL and the Web server applications. See " Retrieving and Restoring Cookies " .