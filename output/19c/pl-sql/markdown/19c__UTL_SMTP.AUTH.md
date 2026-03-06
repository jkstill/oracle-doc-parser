---
id: 19c__UTL_SMTP.AUTH
name: UTL_SMTP.AUTH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.AUTH

This subprogram sends the AUTH command to authenticate to the SMTP server. The UTL_SMTP package goes through the user's choices of authentication schemes, skips any that is not supported by the SMTP server and uses the first supported.

## Syntax

```sql
UTL_SMTP.AUTH (
   c          IN OUT NOCOPY connection,
   username   IN            VARCHAR2,
   password   IN            VARCHAR2,
   schemes    IN            VARCHAR2 DEFAULT NON_CLEARTEXT_PASSWORD_SCHEMES)
 RETURN reply;

UTL_SMTP.AUTH (
   c          IN OUT NOCOPY connection,
   username   IN            VARCHAR2,
   password   IN            VARCHAR2,
   schemes    IN            VARCHAR2 DEFAULT NON_CLEARTEXT_PASSWORD_SCHEMES);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |
| username | VARCHAR2 | IN | Username |
| password | VARCHAR2 | IN | Password |
| schemes | VARCHAR2 | IN | Space-separated list of authentication schemes UTL_SMTP is allowed to use in the preferred order. See the ALL_SCHEMES and NON_CLEARTEXT_PASSWORD_SCHEMES constants for suggestions. |

**Returns:** `reply`

## Usage Notes

To determine the schemes the SMTP server supports from its EHLO reply, the user must call the EHLO Function and Procedure . Otherwise, UTL_SMTP uses the first scheme in the list. Syntax UTL_SMTP.AUTH ( c IN OUT NOCOPY connection, username IN VARCHAR2, password IN VARCHAR2, schemes IN VARCHAR2 DEFAULT NON_CLEARTEXT_PASSWORD_SCHEMES) RETURN reply; UTL_SMTP.AUTH ( c IN OUT NOCOPY connection, username IN VARCHAR2, password IN VARCHAR2, schemes IN VARCHAR2 DEFAULT NON_CLEARTEXT_PASSWORD_SCHEMES); Parameters Table 276-8 AUTH Function and Procedure Parameters Parameter Description c SMTP connection username Username password Password schemes Space-separated list of authentication schemes UTL_SMTP is allowed to use in the preferred order. See the ALL_SCHEMES and NON_CLEARTEXT_PASSWORD_SCHEMES constants for suggestions. Return Values Table 276-9 AUTH Function and Procedure Function Return Values Return Value Description reply Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types ). In cases where there are multiple replies, the last reply is returned. Usage Notes Currently only PLAIN , LOGIN and CRAM-MD5 authentication schemes are supported by UTL_SMTP . Since the SMTP server may change the authentication schemes it supports after the SMTP connection is secured by SSL/TLS after the STARTTLS command (for example, adding PLAIN and LOGIN ), the caller must call the EHLO Function and Procedure again for UTL_SMTP to update the list after the STARTTLS Function and Procedure is called.