---
id: 19c__UTL_SMTP.STARTTLS
name: UTL_SMTP.STARTTLS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.STARTTLS

This subprogram sends the STARTTLS command to secure the SMTP connection using SSL/TLS.

## Syntax

```sql
UTL_SMTP.STARTTLS (
   c            IN OUT NOCOPY  connection,
   secure_host  IN     VARCHAR2 DEFAULT NULL) 
RETURN reply;

UTL_SMTP.STARTTLS (
   c            IN OUT NOCOPY connection,
   secure_host  IN     VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |
| secure_host | VARCHAR2 | IN | The host name to be matched against the common name (CN) of the SMTP server's certificate. It can also be a domain name like "*.example.com" . If NULL , the SMTP host name to connect to will be used. |

**Returns:** `reply`

## Usage Notes

SSL/TLS requires an Oracle wallet which must be specified when the connection was opened by the OPEN_CONNECTION Functions . Syntax UTL_SMTP.STARTTLS ( c IN OUT NOCOPY connection, secure_host IN VARCHAR2 DEFAULT NULL) RETURN reply; UTL_SMTP.STARTTLS ( c IN OUT NOCOPY connection, secure_host IN VARCHAR2 DEFAULT NULL); Parameters Table 276-39 STARTTLS Function and Procedure Parameters Parameter Description c SMTP connection secure_host The host name to be matched against the common name (CN) of the SMTP server's certificate. It can also be a domain name like "*.example.com" . If NULL , the SMTP host name to connect to will be used. Return Values Table 276-40 STARTTLS Function and Procedure Return Values Return Value Description reply SMTP reply Usage Notes The STARTTLS command must only be issued on an unencrypted connection and when the SMTP server indicates the support of the command in the reply of the EHLO command. The wallet to be used for encryption must have been specified when the initial SMTP connection was opened by the OPEN_CONNECTION function.