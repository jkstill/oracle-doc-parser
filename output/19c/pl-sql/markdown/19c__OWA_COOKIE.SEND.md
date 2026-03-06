---
id: 19c__OWA_COOKIE.SEND
name: OWA_COOKIE.SEND
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_COOKIE
tags: [owa_cookie]
source_file: OWA_COOKIE.html
---

# OWA_COOKIE.SEND

This procedure generates a Set-Cookie line, which transmits a cookie to the client.

## Syntax

```sql
OWA_COOKIE.SEND(
   name           in       varchar2,
   value          in       varchar2,
   expires        in       date       DEFAULT NULL,
   path           in       varchar2   DEFAULT NULL,
   domain         in       varchar2   DEFAULT NULL,
   secure         in       varchar2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | varchar2 | in | The name of the cookie. |
| value | varchar2 | in | The value of the cookie. |
| expires | date | in | The date at which the cookie will expire |
| path | varchar2 | in | The value for the path field. |
| domain | varchar2 | in | The value for the domain field. |
| secure | varchar2 | in | If the value of this parameter is not NULL , the "secure" field is added to the line. |

## Usage Notes

This procedure must occur in the context of an HTTP header. Syntax OWA_COOKIE.SEND( name in varchar2, value in varchar2, expires in date DEFAULT NULL, path in varchar2 DEFAULT NULL, domain in varchar2 DEFAULT NULL, secure in varchar2 DEFAULT NULL); Parameters Table 223-5 SEND Procedure Parameters Parameter Description name The name of the cookie. value The value of the cookie. expires The date at which the cookie will expire path The value for the path field. domain The value for the domain field. secure If the value of this parameter is not NULL , the "secure" field is added to the line.