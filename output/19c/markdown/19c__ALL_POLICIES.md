---
id: 19c__ALL_POLICIES
name: ALL_POLICIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_POLICIES.html
---

# ALL_POLICIES

DBA_POLICIES describes all Oracle Virtual Private Database (VPD) security policies in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_OWNER | VARCHAR2(128) | Owner of the synonym, table, or view |
| OBJECT_NAME | VARCHAR2(128) | Name of the synonym, table, or view |
| POLICY_GROUP | VARCHAR2(128) | Name of the policy group |
| POLICY_NAME | VARCHAR2(128) | Name of the policy |
| PF_OWNER | VARCHAR2(128) | Owner of the policy function |
| PACKAGE | VARCHAR2(128) | Name of the package containing the policy function |
| FUNCTION | VARCHAR2(128) | Name of the policy function |
| SEL | VARCHAR2(3) | Indicates whether the policy is applied to queries on the object ( YES ) or not ( NO ) |
| INS | VARCHAR2(3) | Indicates whether the policy is applied to INSERT statements on the object ( YES ) or not ( NO ) |
| UPD | VARCHAR2(3) | Indicates whether the policy is applied to UPDATE statements on the object ( YES ) or not ( NO ) |
| DEL | VARCHAR2(3) | Indicates whether the policy is applied to DELETE statements on the object ( YES ) or not ( NO ) |
| IDX | VARCHAR2(3) | Indicates whether the policy is enforced for index maintenance on the object ( YES ) or not ( NO ) |
| CHK_OPTION | VARCHAR2(3) | Indicates whether the check option is enforced for the policy ( YES ) or not ( NO ) |
| ENABLE | VARCHAR2(3) | Indicates whether the policy is enabled ( YES ) or disabled ( NO ) |
| STATIC_POLICY | VARCHAR2(3) | Indicates whether the policy is static ( YES ) or not ( NO ). This column is obsolete because information about static policies is shown in the POLICY_TYPE column. |
| POLICY_TYPE | VARCHAR2(24) | Policy type: STATIC SHARED_STATIC CONTEXT_SENSITIVE SHARED_CONTEXT_SENSITIVE DYNAMIC |
| LONG_PREDICATE | VARCHAR2(3) | Indicates whether the policy function can return a maximum of 32 KB of predicate ( YES ) or not ( NO ). If NO , the default maximum predicate size is 4000 bytes. |
| COMMON | VARCHAR2(3) | Indicates whether the policy is applied and enforced in all application PDBs ( YES ) or only in the local PDB ( NO ) |
| INHERITED | VARCHAR2(3) | Indicates whether the policy is inherited from the root ( YES ) or not ( NO ) |

## Usage Notes

Related Views DBA_POLICIES describes all Oracle Virtual Private Database (VPD) security policies in the database. USER_POLICIES describes all Oracle Virtual Private Database (VPD) security policies associated with objects owned by the current user. This view does not display the OBJECT_OWNER column. See Also: " DBA_POLICIES " " USER_POLICIES " Oracle Database Concepts for an overview of security policies and fine-grained access control Oracle Database Security Guide for more information about security policies The DBMS_RLS package in Oracle Database PL/SQL Packages and Types Reference for information on administering security policies See Also: " DBA_POLICIES " " USER_POLICIES " Oracle Database Concepts for an overview of security policies and fine-grained access control Oracle Database Security Guide for more information about security policies The DBMS_RLS package in Oracle Database PL/SQL Packages and Types Reference for information on administering security policies