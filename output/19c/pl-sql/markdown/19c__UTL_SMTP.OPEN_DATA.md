---
id: 19c__UTL_SMTP.OPEN_DATA
name: UTL_SMTP.OPEN_DATA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.OPEN_DATA

This subprogram sends the DATA command after which you can use WRITE_DATA and WRITE_RAW_DATA to write a portion of the e-mail message.

## Syntax

```sql
UTL_SMTP.OPEN_DATA (
   c     IN OUT NOCOPY connection) 
RETURN reply;

UTL_SMTP.OPEN_DATA (
   c     IN OUT NOCOPY connection);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |
| data |  |  | Portion of the text of the message to be sent, including headers, in RFC822 format. |

**Returns:** `reply`

## Usage Notes

Syntax UTL_SMTP.OPEN_DATA ( c IN OUT NOCOPY connection) RETURN reply; UTL_SMTP.OPEN_DATA ( c IN OUT NOCOPY connection); Parameters Table 276-31 OPEN_DATA Function and Procedure Parameters Parameter Description c SMTP connection data Portion of the text of the message to be sent, including headers, in RFC822 format. Return Values Table 276-32 OPEN_DATA Function and Procedure Function Return Values Return Value Description reply Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types ). In cases where there are multiple replies, the last reply is returned. Usage Notes The calls to OPEN_DATA , WRITE_DATA , WRITE_RAW_DATA and CLOSE_DATA must be made in the right order. A program calls OPEN_DATA to send the DATA command to the SMTP server. After that, it can call WRITE_DATA or WRITE_RAW_DATA repeatedly to send the actual data. The data is terminated by calling CLOSE_DATA . After OPEN_DATA is called, the only subprograms that can be called are WRITE_DATA , WRITE_RAW_DATA, or CLOSE_DATA . A call to other subprograms results in an INVALID_OPERATION exception being raised. OPEN_DATA must be called only after OPEN_CONNECTION , HELO or EHLO , MAIL , and RCPT have been called. The connection to the SMTP server must be open and a mail transaction must be active when this routine is called.