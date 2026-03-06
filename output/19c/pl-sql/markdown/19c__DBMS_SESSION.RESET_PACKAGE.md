---
id: 19c__DBMS_SESSION.RESET_PACKAGE
name: DBMS_SESSION.RESET_PACKAGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.RESET_PACKAGE

This procedure de-instantiates all packages in this session. It frees the package state.

## Syntax

```sql
DBMS_SESSION.RESET_PACKAGE;
```

## Usage Notes

Note: See " SESSION _TRACE_ENABLE Procedure " . The MODIFY_PACKAGE_STATE interface, introduced in Oracle9i, provides an equivalent of the RESET_PACKAGE capability. It is an efficient, lighter-weight variant for reinitializing the state of all PL/SQL packages in the session. Memory used for caching the execution state is associated with all PL/SQL functions, procedures, and packages that were run in a session. For packages, this collection of memory holds the current values of package variables and controls the cache of cursors opened by the respective PL/SQL programs. A call to RESET_PACKAGE frees the memory associated with each of the previously run PL/SQL programs from the session, and, consequently, clears the current values of any package globals and closes any cached cursors. RESET_PACKAGE can also be used to reliably restart a failed program in a session. If a program containing package variables fails, then it is hard to determine which variables need to be reinitialized. RESET_PACKAGE guarantees that all package variables are reset to their initial values. Note: See " SESSION _TRACE_ENABLE Procedure " . The MODIFY_PACKAGE_STATE interface, introduced in Oracle9i, provides an equivalent of the RESET_PACKAGE capability. It is an efficient, lighter-weight variant for reinitializing the state of all PL/SQL packages in the session. Syntax DBMS_SESSION.RESET_PACKAGE; Usage Notes Because the amount of memory consumed by all executed PL/SQL can become large, you might use RESET_PACKAGE to trim down the session memory footprint at certain points in your database application. However, make sure that resetting package variable values does not affect the application. Also, remember that later execution of programs that have lost their cached memory and cursors will perform slower, because they need to re-create the freed memory and cursors. RESET_PACKAGE does not free the memory, cursors, and package variables immediately when called. Note: RESET_PACKAGE only frees the memory, cursors, and package variables after the PL/SQL call that made the invocation finishes running. For example, PL/SQL procedure P1 calls PL/SQL procedure P2 , and P2 calls RESET_PACKAGE . The RESET_PACKAGE effects do not occur until procedure P1 finishes execution (the PL/SQL call ends).