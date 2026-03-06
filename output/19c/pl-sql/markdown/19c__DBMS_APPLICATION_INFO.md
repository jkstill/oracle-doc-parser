---
id: 19c__DBMS_APPLICATION_INFO
name: DBMS_APPLICATION_INFO
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLICATION_INFO
tags: [dbms_application_info]
source_file: DBMS_APPLICATION_INFO.html
---

# DBMS_APPLICATION_INFO

Your applications should set the name of the module and name of the action automatically each time a user enters that module. The module name could be the name of a form in an Oracle Forms application, or the name of the code segment in an Oracle Precompilers application. The action name should usually be the name or description of the current transaction within a module.

## Usage Notes

If you want to gather your own statistics based on module, you can implement a wrapper around this package by writing a version of this package in another schema that first gathers statistics and then calls the SYS version of the package. The public synonym for DBMS_APPLICATION_INFO can then be changed to point to the DBA's version of the package.