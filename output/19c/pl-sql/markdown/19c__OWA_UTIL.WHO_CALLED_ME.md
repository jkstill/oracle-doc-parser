---
id: 19c__OWA_UTIL.WHO_CALLED_ME
name: OWA_UTIL.WHO_CALLED_ME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.WHO_CALLED_ME

This procedure returns information (in the form of output parameters) about the PL/SQL code unit that invoked it.

## Syntax

```sql
OWA_UTIL.WHO_CALLED_ME(
   owner          OUT      VARCHAR2,
   name           OUT      VARCHAR2,
   lineno         OUT      NUMBER,
   caller_t       OUT      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner | VARCHAR2 | OUT | The owner of the program unit. |
| name | VARCHAR2 | OUT | The name of the program unit. This is the name of the package, if the calling program unit is wrapped in a package, or the name of the procedure or function if the calling program unit is a standalone procedure or function. If the calling program unit is part of an anonymous block, this is NULL . |
| lineno | NUMBER | OUT | The line number within the program unit where the call was made. |
| caller_t | VARCHAR2) | OUT | The type of program unit that made the call. The possibilities are: package body, anonymous block, procedure, and function. Procedure and function are only for standalone procedures and functions. |

## Usage Notes

Syntax OWA_UTIL.WHO_CALLED_ME( owner OUT VARCHAR2, name OUT VARCHAR2, lineno OUT NUMBER, caller_t OUT VARCHAR2); Parameters Table 230-15 WHO_CALLED_ME Procedure Parameters Parameter Description owner The owner of the program unit. name The name of the program unit. This is the name of the package, if the calling program unit is wrapped in a package, or the name of the procedure or function if the calling program unit is a standalone procedure or function. If the calling program unit is part of an anonymous block, this is NULL . lineno The line number within the program unit where the call was made. caller_t The type of program unit that made the call. The possibilities are: package body, anonymous block, procedure, and function. Procedure and function are only for standalone procedures and functions.