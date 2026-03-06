---
id: 19c__V$WALLET
name: V$WALLET
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-WALLET.html
---

# V$WALLET

V$WALLET displays metadata of certificates that may be used as a master key for Transparent Data Encryption.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CERT_ID | VARCHAR2(52) |  |
| DN | VARCHAR2(255) |  |
| SERIAL_NUM | VARCHAR2(40) |  |
| ISSUER | VARCHAR2(255) |  |
| KEYSIZE | NUMBER |  |
| STATUS | VARCHAR2(16) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: The use of PKI encryption with Transparent Data Encryption is deprecated. To configure Transparent Data Encryption, use the ADMINISTER KEY MANAGEMENT SQL statement. See Oracle Database Advanced Security Guide for more information. Note: The use of PKI encryption with Transparent Data Encryption is deprecated. To configure Transparent Data Encryption, use the ADMINISTER KEY MANAGEMENT SQL statement. See Oracle Database Advanced Security Guide for more information.