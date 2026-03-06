---
id: 19c__UTL_HTTP.SET_WALLET
name: UTL_HTTP.SET_WALLET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.SET_WALLET

This procedure sets the Oracle wallet used for all HTTP requests over Secured Socket Layer (SSL), namely HTTPS.

## Syntax

```sql
UTL_HTTP.SET_WALLET (
   path      IN VARCHAR2,
   password  IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | The directory path that contains the Oracle wallet. The format is file: directory-path . The format of wallet_path on a PC is, for example, f ile:c:\WINNT\Profiles\ username \WALLETS , and in Unix is, for example, file:/home/ username /wallets . When the UTL_HTTP package is executed in the Oracle database server, the wallet is accessed from the database server. Therefore, the wallet path must be accessible from the database server. |
| password | VARCHAR2 | IN | The password needed to open the wallet. If the wallet is auto-login enabled, the password may be omitted and should be set to NULL . See Oracle Database Advanced Security Guide for information about using Oracle Wallet Manager and the ORAPKI utility to create an auto-login wallet. |

## Usage Notes

When the UTL_HTTP package communicates with an HTTP server over SSL, the HTTP server presents its digital certificate, which is signed by a certificate authority, to the UTL_HTTP package for identification purpose. The Oracle wallet contains the list of certificate authorities that are trusted by the user of the UTL_HTTP package. An Oracle wallet is required to make an HTTPS request. See Also: Session Settings and Session Settings Subprograms Oracle Database Security Guide managing fine-grained access See Also: Session Settings and Session Settings Subprograms Oracle Database Security Guide managing fine-grained access Syntax UTL_HTTP.SET_WALLET ( path IN VARCHAR2, password IN VARCHAR2 DEFAULT NULL); Parameters Table 264-58 SET_WALLET Procedure Parameters Parameter Description path The directory path that contains the Oracle wallet. The format is file: directory-path . The format of wallet_path on a PC is, for example, f ile:c:\WINNT\Profiles\ username \WALLETS , and in Unix is, for example, file:/home/ username /wallets . When the UTL_HTTP package is executed in the Oracle database server, the wallet is accessed from the database server. Therefore, the wallet path must be accessible from the database server. password The password needed to open the wallet. If the wallet is auto-login enabled, the password may be omitted and should be set to NULL . See Oracle Database Advanced Security Guide for information about using Oracle Wallet Manager and the ORAPKI utility to create an auto-login wallet. Usage Notes To set up an Oracle wallet, use the Oracle Wallet Manager to create a wallet. In order for the HTTPS request to succeed, the certificate authority that signs the certificate of the remote HTTPS Web server must be a trust point set in the wallet. When a wallet is created, it is populated with a set of well-known certificate authorities as trust points. If the certificate authority that signs the certificate of the remote HTTPS Web server is not among the trust points, or the certificate authority has new root certificates, you should obtain the root certificate of that certificate authority and install it as a trust point in the wallet using Oracle Wallet Manager See Also: Oracle Database Advanced Security Guide for more information on Wallet Manager