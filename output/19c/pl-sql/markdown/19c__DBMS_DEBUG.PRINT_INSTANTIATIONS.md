---
id: 19c__DBMS_DEBUG.PRINT_INSTANTIATIONS
name: DBMS_DEBUG.PRINT_INSTANTIATIONS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.PRINT_INSTANTIATIONS

This procedure returns a list of the packages that have been instantiated in the current session.

## Syntax

```sql
DBMS_DEBUG.PRINT_INSTANTIATIONS (
   pkgs   IN OUT NOCOPY backtrace_table, 
   flags  IN BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pkgs | NOCOPY | IN OUT | The instantiated packages |
| flags | BINARY_INTEGER) | IN | Bitmask of options: 1 - show specs 2 - show bodies 4 - show local instantiations 8 - show remote instantiations (NYI) 16 - do a fast job. The routine does not test whether debug information exists or whether the libunit is shrink-wrapped. |

## Usage Notes

Syntax DBMS_DEBUG.PRINT_INSTANTIATIONS ( pkgs IN OUT NOCOPY backtrace_table, flags IN BINARY_INTEGER); Parameters Table 57-39 PRINT_INSTANTIATIONS Procedure Parameters Parameter Description pkgs The instantiated packages flags Bitmask of options: 1 - show specs 2 - show bodies 4 - show local instantiations 8 - show remote instantiations (NYI) 16 - do a fast job. The routine does not test whether debug information exists or whether the libunit is shrink-wrapped. Exceptions no_target_program - target session is not currently executing Usage Notes On return, pkgs contains a program_info for each instantiation. The valid fields are: Namespace, Name, Owner, and LibunitType. In addition, Line# contains a bitmask of: 1 - the libunit contains debug info 2 - the libunit is shrink-wrapped