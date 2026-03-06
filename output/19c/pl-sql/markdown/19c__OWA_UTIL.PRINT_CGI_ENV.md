---
id: 19c__OWA_UTIL.PRINT_CGI_ENV
name: OWA_UTIL.PRINT_CGI_ENV
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.PRINT_CGI_ENV

This procedure generates all the CGI environment variables and their values made available by the PL/SQL Gateway to the stored procedure.

## Syntax

```sql
OWA_UTIL.PRINT_CGI_ENV;
```

## Usage Notes

Syntax OWA_UTIL.PRINT_CGI_ENV; Examples This procedure generates a list in the following format: cgi_env_var_name = value\n