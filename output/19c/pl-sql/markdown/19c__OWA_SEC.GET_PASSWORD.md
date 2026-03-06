---
id: 19c__OWA_SEC.GET_PASSWORD
name: OWA_SEC.GET_PASSWORD
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_SEC
tags: [owa_sec]
source_file: OWA_SEC.html
---

# OWA_SEC.GET_PASSWORD

This function returns the password that the user used to log in.

## Syntax

```sql
OWA_SEC.GET_PASSWORD 
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Syntax OWA_SEC.GET_PASSWORD RETURN VARCHAR2; Return Values The password. Usage Notes For security reasons, this function returns a true value only when custom authentication is used. If you call this function when you are not using custom authentication, the function returns an undefined value. Thus, the database passwords are not exposed.