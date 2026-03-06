---
id: 19c__DBA_FGA_AUDIT_TRAIL
name: DBA_FGA_AUDIT_TRAIL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
tags: [dba]
source_file: DBA_FGA_AUDIT_TRAIL.html
---

# DBA_FGA_AUDIT_TRAIL

DBA_FGA_AUDIT_TRAIL displays all audit records for fine-grained auditing.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER | Session id of the query |
| TIMESTAMP | DATE | Date and time of the query in the local database session time zone |
| DB_USER | VARCHAR2(128) | Database username who executed the query |
| OS_USER | VARCHAR2(255) | Operating system username who executed the query |
| USERHOST | VARCHAR2(128) | Client host machine name |
| CLIENT_ID | VARCHAR2(128) | Client identifier in each Oracle session |
| ECONTEXT_ID | VARCHAR2(64) | Application execution context identifier |
| EXT_NAME | VARCHAR2(4000) | External name |
| OBJECT_SCHEMA | VARCHAR2(128) | Owner of the table or view |
| OBJECT_NAME | VARCHAR2(128) | Name of the table or view |
| POLICY_NAME | VARCHAR2(128) | Name of the Fine-Grained Auditing Policy |
| SCN | NUMBER | System change number (SCN) of the query |
| SQL_TEXT | NVARCHAR2(2000) | SQL text of the query |
| SQL_BIND | NVARCHAR2(2000) | Bind variable data of the query |
| COMMENT$TEXT | VARCHAR2(4000) | Comments |
| STATEMENT_TYPE | VARCHAR2(7) | Statement type of the query: SELECT INSERT UPDATE DELETE |
| EXTENDED_TIMESTAMP | TIMESTAMP(6) WITH TIME ZONE | Timestamp of the query in UTC (Coordinated Universal Time) time zone |
| PROXY_SESSIONID | NUMBER | Proxy session serial number, if an enterprise user has logged in through the proxy mechanism |
| GLOBAL_UID | VARCHAR2(32) | Global user identifier for the user, if the user has logged in as an enterprise user |
| INSTANCE_NUMBER | NUMBER | Instance number as specified by the INSTANCE_NUMBER initialization parameter |
| OS_PROCESS | VARCHAR2(16) | Operating System process identifier of the Oracle process |
| TRANSACTIONID | RAW(8) | Transaction identifier of the transaction in which the object is accessed or modified |
| STATEMENTID | NUMBER | Numeric ID for each statement run (a statement may cause many actions) |
| ENTRYID | NUMBER | Numeric ID for each audit trail entry in the session |
| OBJ_EDITION_NAME | VARCHAR2(128) | Name of the edition containing the audited object |
| DBID | NUMBER | Database identifier of the audited database |
| RLS_INFO | CLOB | Stores virtual private database (VPD) policy names and predicates separated by delimiter. To format the output into individual rows, use the DBMS_AUDIT_UTIL.DECODE_RLS_INFO_ATRAIL_FGA function. |
| CURRENT_USER | VARCHAR2(128) | Effective user for the statement execution |

## Usage Notes

Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: The SQL_BIND and SQL_TEXT columns are populated only if the policy has been created with the AUDIT_TRAIL parameter set to db , extended . See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_AUDIT_UTIL.DECODE_RLS_INFO_ATRAIL_FGA function. Note: The SQL_BIND and SQL_TEXT columns are populated only if the policy has been created with the AUDIT_TRAIL parameter set to db , extended . See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_AUDIT_UTIL.DECODE_RLS_INFO_ATRAIL_FGA function.