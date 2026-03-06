---
id: 19c__DBMS_DST.BEGIN_UPGRADE
name: DBMS_DST.BEGIN_UPGRADE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DST
tags: [dbms_dst]
source_file: DBMS_DST.html
---

# DBMS_DST.BEGIN_UPGRADE

This procedure starts an upgrade window.

## Syntax

```sql
DBMS_DST.BEGIN_UPGRADE (
   new_version                IN  BINARY_INTEGER,
   error_on_overlap_time      IN  BOOLEAN := FALSE,
   error_on_nonexisting_time  IN  BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| new_version | BINARY_INTEGER | IN | New timezone version to which the database is to be upgraded |
| error_on_overlap_time | BOOLEAN | IN | Boolean flag indicating whether to report errors on the 'overlap' time semantic conversion error. The default is FALSE . For more information about boundary cases, see Oracle Database SQL Language Reference . |
| error_on_nonexisting_time | BOOLEAN | IN | Boolean flag indicating whether to report errors on the 'non-existing' time semantic conversion error. The default value is FALSE . |

## Usage Notes

When an upgraded window is started successfully, the TSTZ data in the dictionary tables is upgraded to reflect the new timezone version, and the database property 'DST_UPGRADE_STATE' is set to 'UPGRADE' . Once BEGIN_UPGRADE has been performed successfully, the user must re-start the database. After a successful restart, the database property 'PRIMARY_TT_VERSION' is the new timezone version, and 'SECONDARY_TT_VERSION' is the old timezone version. The procedure operates atomically, and upgrades all or none of the dictionary tables and the database properties. It must be called in the database in OPEN MIGRATE mode. Syntax DBMS_DST.BEGIN_UPGRADE ( new_version IN BINARY_INTEGER, error_on_overlap_time IN BOOLEAN := FALSE, error_on_nonexisting_time IN BOOLEAN := FALSE); Parameters Table 65-4 BEGIN_UPGRADE Procedure Parameters Parameter Description new_version New timezone version to which the database is to be upgraded error_on_overlap_time Boolean flag indicating whether to report errors on the 'overlap' time semantic conversion error. The default is FALSE . For more information about boundary cases, see Oracle Database SQL Language Reference . error_on_nonexisting_time Boolean flag indicating whether to report errors on the 'non-existing' time semantic conversion error. The default value is FALSE .