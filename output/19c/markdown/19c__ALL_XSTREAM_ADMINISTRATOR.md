---
id: 19c__ALL_XSTREAM_ADMINISTRATOR
name: ALL_XSTREAM_ADMINISTRATOR
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_XSTREAM_ADMINISTRATOR.html
---

# ALL_XSTREAM_ADMINISTRATOR

ALL_XSTREAM_ADMINISTRATOR displays information about the current users's granted privileges to be an XStream administrator by procedures in the DBMS_XSTREAM_AUTH package.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USERNAME | VARCHAR2(128) | Name of the user who has been granted privileges to be an XStream administrator |
| PRIVILEGE_TYPE | VARCHAR2(7) | Type of privilege granted: APPLY CAPTURE * - Both APPLY and CAPTURE |
| GRANT_SELECT_PRIVILEGES | VARCHAR2(3) | Shows whether set of privileges granted to the user (grantee) includes the SELECT_CATALOG_ROLE role, which enables the user to manage other XStream servers that belong to other XStream users. Possible values: YES : The administrator has the SELECT_CATALOG_ROLE role and other privileges, is considered a full privilege administrator, and can manage other users' XStream configuration NO : The administrator is considered a minimum privilege administrator, and can only manage XStream configurations where the apply_user or capture_user (based on the PRIVILEGE_TYPE column) matches the username. |
| CREATE_TIME | TIMESTAMP(6) | Time at which the privilege was granted |

## Usage Notes

Related View DBA_XSTREAM_ADMINISTRATOR displays information about the users who have been granted privileges to be XStream administrators by procedures in the DBMS_XSTREAM_AUTH package. See Also: " DBA_XSTREAM_ADMINISTRATOR " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_XSTREAM_AUTH package See Also: " DBA_XSTREAM_ADMINISTRATOR " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_XSTREAM_AUTH package