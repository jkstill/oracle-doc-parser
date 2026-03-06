---
id: 19c__DBMS_OPTIM_BUNDLE.LISTBUNDLESWITHFCFIXES
name: DBMS_OPTIM_BUNDLE.LISTBUNDLESWITHFCFIXES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OPTIM_BUNDLE
tags: [dbms_optim_bundle]
source_file: dbms_optim_bundle.html
---

# DBMS_OPTIM_BUNDLE.LISTBUNDLESWITHFCFIXES

The DBMS_OPTIM_BUNDLE subprogram, LISTBUNDLESWITHFCFIXES procedure lists the release update names and release update IDs of release updates with fix control fixes.

## Syntax

```sql
DBMS_OPTIM_BUNDLE.LISTBUNDLESWITHFCFIXES ( );
```

## Usage Notes

Syntax DBMS_OPTIM_BUNDLE.LISTBUNDLESWITHFCFIXES ( ); Examples To view the release update names and release update IDs: SQL> set serveroutput on SQL> exec dbms_optim_bundle.listBundlesWithFCFixes; bundleId: 190719, bundleName: 19.4.0.0.190719DBRU bundleId: 191015, bundleName: 19.5.0.0.191015DBRU bundleId: 200414, bundleName: 19.7.0.0.200414DBRU bundleId: 200714, bundleName: 19.8.0.0.200714DBRU bundleId: 201020, bundleName: 19.9.0.0.201020DBRU bundleId: 210119, bundleName: 19.10.0.0.210119DBRU bundleId: 210420, bundleName: 19.11.0.0.210420DBRU bundleId: 210720, bundleName: 19.12.0.0.210720DBRU PL/SQL procedure successfully completed. Exceptions The following exception is raised by the LISTBUNDLESWITHFCFIXES Procedure : ORA-20002 : Internal or other errors