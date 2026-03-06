---
id: 19c__UTL_SMTP.MAIL
name: UTL_SMTP.MAIL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.MAIL

This subprogram initiate a mail transaction with the server. The destination is a mailbox.

## Syntax

```sql
UTL_SMTP.MAIL (
   c           IN OUT NOCOPY   connection, 
   sender      IN              VARCHAR2, 
   parameters  IN              VARCHAR2 DEFAULT NULL) 
RETURN reply;

UTL_SMTP.MAIL (
   c           IN OUT NOCOPY   connection, 
   sender      IN              VARCHAR2, 
   parameters  IN              VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |
| sender | VARCHAR2 | IN | E-mail address of the user sending the message. |
| parameters | VARCHAR2 | IN | Additional parameters to mail command as defined in Section 6 of [RFC1869]. It must follow the format of "XXX=XXX (XXX=XXX ....)". |

**Returns:** `reply`

## Usage Notes

Syntax UTL_SMTP.MAIL ( c IN OUT NOCOPY connection, sender IN VARCHAR2, parameters IN VARCHAR2 DEFAULT NULL) RETURN reply; UTL_SMTP.MAIL ( c IN OUT NOCOPY connection, sender IN VARCHAR2, parameters IN VARCHAR2 DEFAULT NULL); Parameters Table 276-25 MAIL Function and Procedure Parameters Parameter Description c SMTP connection sender E-mail address of the user sending the message. parameters Additional parameters to mail command as defined in Section 6 of [RFC1869]. It must follow the format of "XXX=XXX (XXX=XXX ....)". Return Values Table 276-26 MAIL Function and Procedure Return Values Return Value Description reply Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types ). In cases where there are multiple replies, the last reply is returned. Usage Notes This command does not send the message; it simply begins its preparation. It must be followed by calls to RCPT and DATA to complete the transaction. The connection to the SMTP server must be open and a HELO or EHLO command must have already been sent. The expected response from the server is a message beginning with status code 250.