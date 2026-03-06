---
id: 19c__UTL_SMTP.DATA
name: UTL_SMTP.DATA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.DATA

This subprogram specifies the body of an e-mail message.

## Syntax

```sql
UTL_SMTP.DATA (
   c     IN OUT NOCOPY connection
   body  IN  VARCHAR2 CHARACTER SET ANY_CS) 
RETURN reply;

UTL_SMTP.DATA (
   c     IN OUT NOCOPY connection
   body  IN VARCHAR2 CHARACTER SET ANY_CS);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP Connection |
| body | VARCHAR2 | IN | Text of the message to be sent, including headers, in [RFC822] format |

**Returns:** `reply`

## Usage Notes

Syntax UTL_SMTP.DATA ( c IN OUT NOCOPY connection body IN VARCHAR2 CHARACTER SET ANY_CS) RETURN reply; UTL_SMTP.DATA ( c IN OUT NOCOPY connection body IN VARCHAR2 CHARACTER SET ANY_CS); Parameters Table 276-17 DATA Function and Procedure Parameters Parameter Description c SMTP Connection body Text of the message to be sent, including headers, in [RFC822] format Return Values Table 276-18 DATA Function and Procedure Return Values Return Value Description reply Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types ). In cases where there are multiple replies, the last reply is returned. Usage Notes The application must ensure that the contents of the body parameter conform to the MIME(RFC822) specification. The DATA routine terminates the message with a <CR><LF>.<CR><LF> sequence (a single period at the beginning of a line), as required by RFC821. It also translates any sequence of <CR><LF>.<CR><LF> (single period) in body to <CR><LF>..<CR><LF> (double period). This conversion provides the transparency as described in Section 4.5.2 of RFC821. The DATA subprogram must be called only after OPEN_CONNECTION , HELO or EHLO , MAIL and RCPT have been called. The connection to the SMTP server must be open, and a mail transaction must be active when this routine is called. The expected response from the server is a message beginning with status code 250. The 354 response received from the initial DATA command is not returned to the caller.