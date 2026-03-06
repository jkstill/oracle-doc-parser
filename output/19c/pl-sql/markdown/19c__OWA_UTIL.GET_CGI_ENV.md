---
id: 19c__OWA_UTIL.GET_CGI_ENV
name: OWA_UTIL.GET_CGI_ENV
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.GET_CGI_ENV

This function returns the value of the specified CGI environment variable.

## Syntax

```sql
OWA_UTIL.GET_CGI_ENV(
   param_name       IN      VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| param_name | VARCHAR2) | IN | The name of the CGI environment variable. It is case-insensitive. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax OWA_UTIL.GET_CGI_ENV( param_name IN VARCHAR2) RETURN VARCHAR2; Parameters Table 230-6 GET_CGI_ENV Function Parameters Parameter Description param_name The name of the CGI environment variable. It is case-insensitive. Return Values The value of the specified CGI environment variable. If the variable is not defined, the function returns NULL .