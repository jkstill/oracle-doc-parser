---
id: 19c__DBMS_OPTIM_BUNDLE.GETBUGSFORBUNDLE
name: DBMS_OPTIM_BUNDLE.GETBUGSFORBUNDLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OPTIM_BUNDLE
tags: [dbms_optim_bundle]
source_file: dbms_optim_bundle.html
---

# DBMS_OPTIM_BUNDLE.GETBUGSFORBUNDLE

The DBMS_OPTIM_BUNDLE subprogram, GETBUGSFORBUNDLE procedure displays execution plan bug fixes applied as part of release updates.

## Syntax

```sql
DBMS_OPTIM_BUNDLE.GETBUGSFORBUNDLE ( 
   bundleid            IN  NUMBER  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| bundleid | NUMBER | IN | The release update ID. If NULL , the execution plan bug fixes from the latest bundle is displayed. If a bundle ID is specified, then the execution plan bug fixes up to the specified bundle is displayed. The default value is NULL . |

## Usage Notes

Syntax DBMS_OPTIM_BUNDLE.GETBUGSFORBUNDLE ( bundleid IN NUMBER DEFAULT NULL); Parameters Table 118-3 GETBUGSFORBUNDLE Procedure Parameters Parameter Description bundleid The release update ID. If NULL , the execution plan bug fixes from the latest bundle is displayed. If a bundle ID is specified, then the execution plan bug fixes up to the specified bundle is displayed. The default value is NULL . Examples To view a listing of the installed but disabled execution plan bug fixes from the most recent release update applied: SQL> set serveroutput on; SQL> execute dbms_optim_bundle.getbugsforbundle; 19.8.0.0.200714DBRU: Bug: 29304314, fix_controls: 29304314 Bug: 29930457, fix_controls: 29930457 The above example lists the installed but disabled execution plan bug fixes from the 19.8.0.0.200714DBRU release. To view a listing of the installed but disabled execution plan bug fixes from release updates up to and including release update 171017: SQL> execute dbms_optim_bundle.getbugsforbundle(171017); Exceptions The following exceptions are raised by the GETBUGSFORBUNDLE Procedure : ORA-20001 : Bad input value ORA-20002 : Internal or other errors