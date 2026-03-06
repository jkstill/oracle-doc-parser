---
id: 19c__ALL_GOLDENGATE_PRIVILEGES
name: ALL_GOLDENGATE_PRIVILEGES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [all]
source_file: ALL_GOLDENGATE_PRIVILEGES.html
---

# ALL_GOLDENGATE_PRIVILEGES

DBA_GOLDENGATE_PRIVILEGES displays details about Oracle GoldenGate privileges for all users who have been granted Oracle GoldenGate privileges.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USERNAME | VARCHAR2(128) | Name of the user that is granted the privilege |
| PRIVILEGE_TYPE | VARCHAR2(7) | Type of privilege granted: APPLY CAPTURE *: Both APPLY and CAPTURE |
| GRANT_SELECT_PRIVILEGES | VARCHAR2(3) | Shows whether the set of privileges granted to the administrator make the administrator a full privilege administrator or a minimum privilege administrator: YES : The administrator has the SELECT_CATALOG_ROLE role and other privileges, is considered a full privilege administrator, and can manage any Oracle GoldenGate configuration. NO : The administrator is considered a minimum privilege administrator, and can only manage Oracle GoldenGate configurations where the apply_user or capture_user (based on the PRIVILEGE_TYPE column) matches the username. |
| CREATE_TIME | TIMESTAMP(6) | Time at which the privilege was granted |

## Usage Notes

Related Views DBA_GOLDENGATE_PRIVILEGES displays details about Oracle GoldenGate privileges for all users who have been granted Oracle GoldenGate privileges. USER_GOLDENGATE_PRIVILEGES displays details about Oracle GoldenGate privileges. This view does not display the USERNAME column. See Also: " DBA_GOLDENGATE_PRIVILEGES " " USER_GOLDENGATE_PRIVILEGES " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_GOLDENGATE_AUTH package See Also: " DBA_GOLDENGATE_PRIVILEGES " " USER_GOLDENGATE_PRIVILEGES " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_GOLDENGATE_AUTH package