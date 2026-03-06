---
id: 19c__DBMS_MVIEW.REGISTER_MVIEW
name: DBMS_MVIEW.REGISTER_MVIEW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MVIEW
tags: [dbms_mview]
source_file: DBMS_MVIEW.html
---

# DBMS_MVIEW.REGISTER_MVIEW

This procedure enables the administration of individual materialized views. It is invoked at a master site or master materialized view site to register a materialized view.

## Syntax

```sql
DBMS_MVIEW.REGISTER_MVIEW (
   mviewowner  IN   VARCHAR2,
   mviewname   IN   VARCHAR2,
   mviewsite   IN   VARCHAR2,
   mview_id    IN   DATE | BINARY_INTEGER,
   flag        IN   BINARY_INTEGER,
   qry_txt     IN   VARCHAR2,
   rep_type    IN   BINARY_INTEGER := DBMS_MVIEW.REG_UNKNOWN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| mviewowner | VARCHAR2 | IN | Owner of the materialized view. |
| mviewname | VARCHAR2 | IN | Name of the materialized view. |
| mviewsite | VARCHAR2 | IN | Name of the materialized view site for a materialized view registering at an Oracle database version 8.x and higher master site or master materialized view site. This name should not contain any double quotes. |
| mview_id | DATE | IN | The identification number of the materialized view. Specify an Oracle database version 8.x and higher materialized view as a BINARY_INTEGER . Specify an Oracle database version 7 materialized view registering at an Oracle database version 8.x and higher master sites or master materialized view sites as a DATE . |
| flag | BINARY_INTEGER | IN | A constant that describes the properties of the materialized view being registered. Valid constants that can be assigned include the following: DBMS_MVIEW.REG_ROWID_MVIEW for a rowid materialized view DBMS_MVIEW.REG_PRIMARY_KEY_MVIEW for a primary key materialized view DBMS_MVIEW.REG_OBJECT_ID_MVIEW for an object id materialized view DBMS_MVIEW.REG_FAST_REFRESHABLE_MVIEW for a materialized view that can be fast refreshed DBMS_MVIEW.REG_UPDATABLE_MVIEW for a materialized view that is updatable A materialized view can have more than one of these properties. In this case, use the plus sign (+) to specify more than one property. For example, if a primary key materialized view can be fast refreshed, you can enter the following for this parameter: DBMS_MVIEW.REG_PRIMARY_KEY_MVIEW + DBMS_MVIEW.REG_FAST_REFRESHABLE_MVIEW You can determine the properties of a materialized view by querying the ALL_MVIEWS data dictionary view. |
| qry_txt | VARCHAR2 | IN | The first 32,000 bytes of the materialized view definition query. |
| rep_type | BINARY_INTEGER | IN | Version of the materialized view. Valid constants that can be assigned include the following: DBMS_MVIEW.REG_V7_SNAPSHOT if the materialized view is at an Oracle database version 7 site DBMS_MVIEW.REG_V8_SNAPSHOT reg_repapi_snapshot if the materialized view is at an Oracle database version 8.x or higher site DBMS_MVIEW.REG_UNKNOWN (the default) if you do not know whether the materialized view is at an Oracle database version 7 site or an Oracle database version 8.x (or higher) site |

## Usage Notes

Note that, typically, a materialized view is registered automatically during materialized view creation. You should only run this procedure to manually register a materialized view if the automatic registration failed or if the registration information was deleted. Syntax DBMS_MVIEW.REGISTER_MVIEW ( mviewowner IN VARCHAR2, mviewname IN VARCHAR2, mviewsite IN VARCHAR2, mview_id IN DATE | BINARY_INTEGER, flag IN BINARY_INTEGER, qry_txt IN VARCHAR2, rep_type IN BINARY_INTEGER := DBMS_MVIEW.REG_UNKNOWN); Parameters Table 113-13 REGISTER_MVIEW Procedure Parameters Parameter Description mviewowner Owner of the materialized view. mviewname Name of the materialized view. mviewsite Name of the materialized view site for a materialized view registering at an Oracle database version 8.x and higher master site or master materialized view site. This name should not contain any double quotes. mview_id The identification number of the materialized view. Specify an Oracle database version 8.x and higher materialized view as a BINARY_INTEGER . Specify an Oracle database version 7 materialized view registering at an Oracle database version 8.x and higher master sites or master materialized view sites as a DATE . flag A constant that describes the properties of the materialized view being registered. Valid constants that can be assigned include the following: DBMS_MVIEW.REG_ROWID_MVIEW for a rowid materialized view DBMS_MVIEW.REG_PRIMARY_KEY_MVIEW for a primary key materialized view DBMS_MVIEW.REG_OBJECT_ID_MVIEW for an object id materialized view DBMS_MVIEW.REG_FAST_REFRESHABLE_MVIEW for a materialized view that can be fast refreshed DBMS_MVIEW.REG_UPDATABLE_MVIEW for a materialized view that is updatable A materialized view can have more than one of these properties. In this case, use the plus sign (+) to specify more than one property. For example, if a primary key materialized view can be fast refreshed, you can enter the following for this parameter: DBMS_MVIEW.REG_PRIMARY_KEY_MVIEW + DBMS_MVIEW.REG_FAST_REFRESHABLE_MVIEW You can determine the properties of a materialized view by querying the ALL_MVIEWS data dictionary view. qry_txt The first 32,000 bytes of the materialized view definition query. rep_type Version of the materialized view. Valid constants that can be assigned include the following: DBMS_MVIEW.REG_V7_SNAPSHOT if the materialized view is at an Oracle database version 7 site DBMS_MVIEW.REG_V8_SNAPSHOT reg_repapi_snapshot if the materialized view is at an Oracle database version 8.x or higher site DBMS_MVIEW.REG_UNKNOWN (the default) if you do not know whether the materialized view is at an Oracle database version 7 site or an Oracle database version 8.x (or higher) site Usage Notes This procedure is invoked at the master site or master materialized view site by a remote materialized view site using a remote procedure call. If REGISTER_MVIEW is called multiple times with the same mviewowner , mviewname , and mviewsite , then the most recent values for mview_id , flag , and qry_txt are stored. If a query exceeds the maximum VARCHAR2 size, then qry_txt contains the first 32000 characters of the query and the remainder is truncated. When invoked manually, the value of mview_id must be looked up in the materialized view data dictionary views by the person who calls the procedure.