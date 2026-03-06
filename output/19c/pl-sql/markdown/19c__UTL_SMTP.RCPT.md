---
id: 19c__UTL_SMTP.RCPT
name: UTL_SMTP.RCPT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.RCPT

This subprogram specifies the recipient of an e-mail message.

## Syntax

```sql
UTL_SMTP.RCPT (
   c           IN OUT NOCOPY     connection,
   recipient   IN                VARCHAR2,
   parameters  IN                VARCHAR2 DEFAULT NULL)
RETURN reply;

UTL_SMTP.RCPT (
   c           IN OUT NOCOPY     connection,
   recipient   IN                VARCHAR2,
   parameters  IN                VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |
| recipient | VARCHAR2 | IN | E-mail address of the user to which the message is being sent |
| parameters | VARCHAR2 | IN | Additional parameters to RCPT command as defined in Section 6 of [RFC1869]. It must follow the format of "XXX=XXX (XXX=XXX ....)". |

**Returns:** `reply`

## Usage Notes

Syntax UTL_SMTP.RCPT ( c IN OUT NOCOPY connection, recipient IN VARCHAR2, parameters IN VARCHAR2 DEFAULT NULL) RETURN reply; UTL_SMTP.RCPT ( c IN OUT NOCOPY connection, recipient IN VARCHAR2, parameters IN VARCHAR2 DEFAULT NULL); Table 276-35 RCPT Function and Procedure Parameters Parameter Description c SMTP connection recipient E-mail address of the user to which the message is being sent parameters Additional parameters to RCPT command as defined in Section 6 of [RFC1869]. It must follow the format of "XXX=XXX (XXX=XXX ....)". Return Values Table 276-36 RCPT Function and Procedure Function Return Values Return Value Description reply Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types ). In cases where there are multiple replies, the last reply is returned. Usage Notes To send a message to multiple recipients, call this routine multiple times. Each invocation schedules delivery to a single e-mail address. The message transaction must have been begun by a prior call to MAIL , and the connection to the mail server must have been opened and initialized by prior calls to OPEN_CONNECTION and HELO or EHLO respectively. The expected response from the server is a message beginning with status code 250 or 251.