---
id: 19c__ALL_CERTIFICATES
name: ALL_CERTIFICATES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CERTIFICATES.html
---

# ALL_CERTIFICATES

ALL_CERTIFICATES displays the certificates accessible to the current user which are used for signature verification for blockchain tables.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CERTIFICATE_ID | RAW(16) | ID for the certificate |
| USER_NAME | VARCHAR2(128) | User who added the certificate |
| DISTINGUISHED_NAME | VARCHAR2(2000) | Uniquely identifies the entity that owns the certificate |
| CERTIFICATE | BLOB | Contents of the certificate |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CERTIFICATES displays all certificates in the database which are used for signature verification for blockchain tables. USER_CERTIFICATES displays the certificates added by the current user which are used for signature verification for blockchain tables. This view does not display the USER_NAME column. Note: This view is available starting with Oracle Database release 19c, version 19.10. See Also: " DBA_CERTIFICATES " " USER_CERTIFICATES " Note: This view is available starting with Oracle Database release 19c, version 19.10. See Also: " DBA_CERTIFICATES " " USER_CERTIFICATES "