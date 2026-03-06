---
id: 19c__DBA_HOST_ACLS
name: DBA_HOST_ACLS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HOST_ACLS.html
---

# DBA_HOST_ACLS

DBA_HOST_ACLS describes access control lists assigned to restrict access to network hosts through PL/SQL network utility packages.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| HOST | VARCHAR2(1000) | Network host |
| LOWER_PORT | NUMBER(5) | Lower bound of the port range |
| UPPER_PORT | NUMBER(5) | Upper bound of the port range |
| ACL | VARCHAR2(4000) | The name of the access control list |
| ACLID | RAW(8) | The object ID of the access control list |
| ACL_OWNER | VARCHAR2(128) | The owner of the access control list |