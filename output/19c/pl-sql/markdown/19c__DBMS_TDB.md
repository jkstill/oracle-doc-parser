---
id: 19c__DBMS_TDB
name: DBMS_TDB
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TDB
tags: [dbms_tdb]
source_file: DBMS_TDB.html
---

# DBMS_TDB

The following notes apply to DBMS_TDB .

## Usage Notes

The subprograms in this package are useful both in determining whether the desired cross-platform database conversion is possible, and in checking whether the database is ready for conversion. See Oracle Database Backup and Recovery User's Guide for details on the different uses of these subprograms are used in the conversion process. The subprograms in this package return simple TRUE or FALSE results to indicate whether database transport is possible. Use the subprograms with SERVEROUTPUT ON for informative messages about why transport is not possible.