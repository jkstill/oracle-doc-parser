---
id: 19c__UTL_SMTP.CLOSE_DATA
name: UTL_SMTP.CLOSE_DATA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.CLOSE_DATA

This subprogram ends the e-mail message by sending the sequence <CR><LF>.<CR><LF> (a single period at the beginning of a line).

## Syntax

```sql
UTL_SMTP.CLOSE_DATA (
   c     IN OUT NOCOPY connection) 
RETURN reply;

UTL_SMTP.CLOSE_DATA (
   c     IN OUT NOCOPY connection);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |

**Returns:** `reply`

## Usage Notes

Syntax UTL_SMTP.CLOSE_DATA ( c IN OUT NOCOPY connection) RETURN reply; UTL_SMTP.CLOSE_DATA ( c IN OUT NOCOPY connection); Parameters Table 276-11 CLOSE_DATA Function and Procedure Parameters Parameter Description c SMTP connection Return Values Table 276-12 CLOSE_DATA Function and Procedure Return Values Return Value Description reply Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types ). In cases where there are multiple replies, the last reply is returned. Usage Notes The calls to OPEN_DATA , WRITE_DATA , WRITE_RAW_DATA and CLOSE_DATA must be made in the right order. A program calls OPEN_DATA to send the DATA command to the SMTP server. After that, it can call WRITE_DATA or WRITE_RAW_DATA repeatedly to send the actual data. The data is terminated by calling CLOSE_DATA . After OPEN_DATA is called, the only subprograms that can be called are WRITE_DATA , WRITE_RAW_DATA, or CLOSE_DATA . A call to other subprograms results in an INVALID_OPERATION exception being raised. CLOSE_DATA must be called only after OPEN_CONNECTION , HELO or EHLO , MAIL , and RCPT have been called. The connection to the SMTP server must be open and a mail transaction must be active when this routine is called. Note that there is no function form of WRITE_DATA because the SMTP server does not respond until the data-terminator is sent during the call to CLOSE_DATA .