---
id: 19c__DBMS_USER_CERTS.ADD_CERTIFICATE
name: DBMS_USER_CERTS.ADD_CERTIFICATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_USER_CERTS
tags: [dbms_user_certs]
source_file: dbms_user_certs.html
---

# DBMS_USER_CERTS.ADD_CERTIFICATE

This procedure can be used by the current user to add an X.509 certificate that is used for signature verification of blockchain tables.

## Syntax

```sql
DBMS_USER_CERTS.ADD_CERTIFICATE(
   x509_cert                 IN  BLOB,
   cert_id                   OUT RAW);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| x509_cert | BLOB | IN | The X.509 certificate used for signature verification of blockchain tables. |
| cert_id | RAW) | OUT | The Global Unique Identifier (GUID) for the certificate. |

## Usage Notes

Syntax DBMS_USER_CERTS.ADD_CERTIFICATE( x509_cert IN BLOB, cert_id OUT RAW); Parameters Table 186-2 ADD_CERTIFICATE Procedure Parameters Parameter Description x509_cert The X.509 certificate used for signature verification of blockchain tables. cert_id The Global Unique Identifier (GUID) for the certificate.