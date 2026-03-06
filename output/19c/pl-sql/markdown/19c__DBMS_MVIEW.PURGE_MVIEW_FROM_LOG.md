---
id: 19c__DBMS_MVIEW.PURGE_MVIEW_FROM_LOG
name: DBMS_MVIEW.PURGE_MVIEW_FROM_LOG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MVIEW
tags: [dbms_mview]
source_file: DBMS_MVIEW.html
---

# DBMS_MVIEW.PURGE_MVIEW_FROM_LOG

This procedure is called on the master site or master materialized view site to delete the rows in materialized view refresh related data dictionary tables maintained at the master for the specified materialized view identified by mview_id or the combination of mviewowner , mviewname , and mviewsite .

## Syntax

```sql
DBMS_MVIEW.PURGE_MVIEW_FROM_LOG (
   mview_id       IN   BINARY_INTEGER);

DBMS_MVIEW.PURGE_MVIEW_FROM_LOG (
   mviewowner     IN   VARCHAR2,
   mviewname      IN   VARCHAR2, 
   mviewsite      IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| mview_id | BINARY_INTEGER) | IN | If you want to execute this procedure based on the identification of the target materialized view, specify the materialized view identification using the mview_id parameter. Query the DBA_BASE_TABLE_MVIEWS view at the materialized view log site for a listing of materialized view IDs. Executing this procedure based on the materialized view identification is useful if the target materialized view is not listed in the list of registered materialized views ( DBA_REGISTERED_MVIEWS ). |
| mviewowner | VARCHAR2 | IN | If you do not specify an mview_id , enter the owner of the target materialized view using the mviewowner parameter. Query the DBA_REGISTERED_MVIEWS view at the materialized view log site to view the materialized view owners. |
| mviewname | VARCHAR2 | IN | If you do not specify an mview_id , enter the name of the target materialized view using the mviewname parameter. Query the DBA_REGISTERED_MVIEWS view at the materialized view log site to view the materialized view names. |
| mviewsite | VARCHAR2) | IN | If you do not specify an mview_id , enter the site of the target materialized view using the mviewsite parameter. Query the DBA_REGISTERED_MVIEWS view at the materialized view log site to view the materialized view sites. |

## Usage Notes

If the materialized view specified is the oldest materialized view to have refreshed from any of the master tables or master materialized views, then the materialized view log is also purged. This procedure does not unregister the materialized view. Syntax DBMS_MVIEW.PURGE_MVIEW_FROM_LOG ( mview_id IN BINARY_INTEGER); DBMS_MVIEW.PURGE_MVIEW_FROM_LOG ( mviewowner IN VARCHAR2, mviewname IN VARCHAR2, mviewsite IN VARCHAR2); Note: This procedure is overloaded. The parameter mview_id is mutually exclusive with the three remaining parameters: mviewowner , mviewname , and mviewsite . Note: This procedure is overloaded. The parameter mview_id is mutually exclusive with the three remaining parameters: mviewowner , mviewname , and mviewsite . Parameters Table 113-9 PURGE_MVIEW_FROM_LOG Procedure Parameters Parameter Description mview_id If you want to execute this procedure based on the identification of the target materialized view, specify the materialized view identification using the mview_id parameter. Query the DBA_BASE_TABLE_MVIEWS view at the materialized view log site for a listing of materialized view IDs. Executing this procedure based on the materialized view identification is useful if the target materialized view is not listed in the list of registered materialized views ( DBA_REGISTERED_MVIEWS ). mviewowner If you do not specify an mview_id , enter the owner of the target materialized view using the mviewowner parameter. Query the DBA_REGISTERED_MVIEWS view at the materialized view log site to view the materialized view owners. mviewname If you do not specify an mview_id , enter the name of the target materialized view using the mviewname parameter. Query the DBA_REGISTERED_MVIEWS view at the materialized view log site to view the materialized view names. mviewsite If you do not specify an mview_id , enter the site of the target materialized view using the mviewsite parameter. Query the DBA_REGISTERED_MVIEWS view at the materialized view log site to view the materialized view sites. Usage Notes If there is an error while purging one of the materialized view logs, the successful purge operations of the previous materialized view logs are not rolled back. This is to minimize the size of the materialized view logs. In case of an error, this procedure can be invoked again until all the materialized view logs are purged.