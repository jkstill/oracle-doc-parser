---
id: 19c__UTL_SMTP.WRITE_RAW_DATA
name: UTL_SMTP.WRITE_RAW_DATA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.WRITE_RAW_DATA

This procedure writes a portion of the e-mail message. A repeat call to WRITE_RAW_DATA appends data to the e-mail message.

## Syntax

```sql
UTL_SMTP.WRITE_RAW_DATA (
   c     IN OUT NOCOPY connection
   data  IN RAW);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |
| data | RAW) | IN | Portion of the text of the message to be sent, including headers, in [RFC822] format |

## Usage Notes

Syntax UTL_SMTP.WRITE_RAW_DATA ( c IN OUT NOCOPY connection data IN RAW); Parameters Table 276-44 WRITE_RAW_DATA Procedure Parameters Parameter Description c SMTP connection data Portion of the text of the message to be sent, including headers, in [RFC822] format Usage Notes The calls to the OPEN_DATA Function and Procedure , WRITE_DATA Procedure , WRITE_RAW_DATA Procedure and CLOSE_DATA Function and Procedure must be made in the correct order. A program calls OPEN_DATA to send the DATA command to the SMTP server. After that, it can call WRITE_DATA or WRITE_RAW_DATA repeatedly to send the actual data. The data is terminated by calling CLOSE_DATA . After OPEN_DATA is called, the only subprograms that can be called are WRITE_DATA , WRITE_RAW_DATA, or CLOSE_DATA . A call to other subprograms results in an INVALID_OPERATION exception being raised. The application must ensure that the contents of the body parameter conform to the MIME(RFC822) specification. The DATA routine terminates the message with a <CR><LF>.<CR><LF> sequence (a single period at the beginning of a line), as required by RFC821. It also translates any sequence of <CR><LF>.<CR><LF> (single period) in the body to <CR><LF>..<CR><LF> (double period). This conversion provides the transparency as described in Section 4.5.2 of RFC821. The OPEN_DATA Function and Procedure , WRITE_DATA Procedure , WRITE_RAW_DATA Procedure and CLOSE_DATA Function and Procedure must be called only after OPEN_CONNECTION Functions , HELO Function and Procedure , or EHLO Function and Procedure , MAIL Function and Procedure , and RCPT Function have been called. The connection to the SMTP server must be open and a mail transaction must be active when this routine is called. Note that there is no function form of the WRITE_DATA Procedure because the SMTP server does not respond until the data-terminator is sent during the call to CLOSE_DATA Function and Procedure .