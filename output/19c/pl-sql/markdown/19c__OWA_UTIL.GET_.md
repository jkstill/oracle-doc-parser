---
id: 19c__OWA_UTIL.GET_
name: OWA_UTIL.GET_
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.GET_

This function returns the name of the procedure that is being invoked by the PL/SQL Gateway.

## Syntax

```sql
OWA_UTIL.GET_PROCEDURE
 RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Syntax OWA_UTIL.GET_PROCEDURE RETURN VARCHAR2; Return Values The name of a procedure, including the package name if the procedure is defined in a package.