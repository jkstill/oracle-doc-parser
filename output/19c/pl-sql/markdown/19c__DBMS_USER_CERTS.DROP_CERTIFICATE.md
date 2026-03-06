---
id: 19c__DBMS_USER_CERTS.DROP_CERTIFICATE
name: DBMS_USER_CERTS.DROP_CERTIFICATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_USER_CERTS
tags: [dbms_user_certs]
source_file: dbms_user_certs.html
---

# DBMS_USER_CERTS.DROP_CERTIFICATE

This procedure can be used by the current user to drop a certificate that is used for signature verification of blockchain tables.

## Syntax

```sql
DBMS_USER_CERTS.DROP_CERTIFICATE(
   cert_id                    IN  RAW);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cert_id | RAW) | IN | The Global Unique Identifier (GUID) of the certificate. |

## Usage Notes

Syntax DBMS_USER_CERTS.DROP_CERTIFICATE( cert_id IN RAW); Parameters Table 186-3 DROP_CERTIFICATE Procedure Parameters Parameter Description cert_id The Global Unique Identifier (GUID) of the certificate.