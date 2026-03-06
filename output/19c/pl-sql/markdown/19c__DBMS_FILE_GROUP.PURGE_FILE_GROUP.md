---
id: 19c__DBMS_FILE_GROUP.PURGE_FILE_GROUP
name: DBMS_FILE_GROUP.PURGE_FILE_GROUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_GROUP
tags: [dbms_file_group]
source_file: DBMS_FILE_GROUP.html
---

# DBMS_FILE_GROUP.PURGE_FILE_GROUP

This procedure purges a file group using the file group's retention policy.

## Syntax

```sql
DBMS_FILE_GROUP.PURGE_FILE_GROUP(
  file_group_name  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_group_name | VARCHAR2) | IN | The name of the file group, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. If NULL and this procedure is run by SYS user, then the procedure purges all file groups. |

## Usage Notes

A file group's retention policy is determined by its settings for the max_versions , min_versions , and retention_days parameters. The following versions of a file group are removed when a file group is purged: All versions greater than the max_versions setting for the file group when versions are ordered in descending order by creation time. Therefore, the older versions are purged before the newer versions. All versions older than the retention_days setting for the file group unless purging a version would cause the number of versions to drop below the min_versions setting for the file group. A job named SYS.FGR$AUTOPURGE_JOB automatically purges all file groups in a database periodically according to the job's schedule. You can adjust this job's schedule using the DBMS_SCHEDULER package. Alternatively, you can create a job that runs the PURGE_FILE_GROUP procedure periodically. Syntax DBMS_FILE_GROUP.PURGE_FILE_GROUP( file_group_name IN VARCHAR2); Parameter Table 70-13 PURGE_FILE_GROUP Procedure Parameter Parameter Description file_group_name The name of the file group, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. If NULL and this procedure is run by SYS user, then the procedure purges all file groups. Usage Notes If this procedure deletes files on hard disk, then the user who runs the procedure must have WRITE privilege on the directory object that contains the files. Files are deleted when a version is purged and the keep_files parameter is set to N for the version's file group.