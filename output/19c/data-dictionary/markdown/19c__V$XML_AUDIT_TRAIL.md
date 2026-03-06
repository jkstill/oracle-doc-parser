---
id: 19c__V$XML_AUDIT_TRAIL
name: V$XML_AUDIT_TRAIL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
tags: [dynamic_performance]
source_file: V-XML_AUDIT_TRAIL.html
---

# V$XML_AUDIT_TRAIL

V$XML_AUDIT_TRAIL shows standard, fine-grained, SYS, and mandatory audit records written in XML format files.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| AUDIT_TYPE | NUMBER |  |
| SESSION_ID | NUMBER |  |
| PROXY_SESSIONID | NUMBER |  |
| STATEMENTID | NUMBER |  |
| ENTRYID | NUMBER |  |
| EXTENDED_TIMESTAMP | TIMESTAMP(6) WITH TIME ZONE |  |
| GLOBAL_UID | VARCHAR2(32) |  |
| DB_USER | VARCHAR2(128) |  |
| CLIENTIDENTIFIER | VARCHAR2(64) |  |
| EXT_NAME | VARCHAR2(1024) |  |
| OS_USER | VARCHAR2(128) |  |
| OS_HOST | VARCHAR2(128) |  |
| OS_PROCESS | VARCHAR2(16) |  |
| TERMINAL | VARCHAR2(30) |  |
| INSTANCE_NUMBER | NUMBER |  |
| OBJECT_SCHEMA | VARCHAR2(128) |  |
| OBJECT_NAME | VARCHAR2(128) |  |
| POLICY_NAME | VARCHAR2(128) |  |
| NEW_OWNER | VARCHAR2(128) |  |
| NEW_NAME | VARCHAR2(128) |  |
| ACTION | NUMBER |  |
| STATEMENT_TYPE | NUMBER |  |
| TRANSACTIONID | RAW(8) |  |
| RETURNCODE | NUMBER |  |
| SCN | NUMBER |  |
| COMMENT_TEXT | VARCHAR2(4000) |  |
| AUTH_PRIVILEGES | VARCHAR2(32) |  |
| GRANTEE | VARCHAR2(128) |  |
| PRIV_USED | NUMBER |  |
| SES_ACTIONS | VARCHAR2(16) |  |
| OS_PRIVILEGE | VARCHAR2(7) |  |
| ECONTEXT_ID | VARCHAR2(64) |  |
| SQL_BIND | VARCHAR2(4000) |  |
| SQL_TEXT | VARCHAR2(4000) |  |
| OBJ_EDITION_NAME | VARCHAR2(128) |  |
| DBID | NUMBER |  |
| RLS_INFO | VARCHAR2(4000) |  |
| CURRENT_USER | VARCHAR2(128) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: The SQL_BIND and SQL_TEXT columns are only populated if the AUDIT_TRAIL initialization parameter is set to xml, extended or if the AUDIT_SYS_OPERATIONS initialization parameter is set to TRUE . See Also: " UNIFIED_AUDIT_TRAIL " " AUDIT_SYS_OPERATIONS " " AUDIT_TRAIL " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_AUDIT_UTIL.DECODE_RLS_INFO_ATRAIL_XML function. Note: The SQL_BIND and SQL_TEXT columns are only populated if the AUDIT_TRAIL initialization parameter is set to xml, extended or if the AUDIT_SYS_OPERATIONS initialization parameter is set to TRUE .