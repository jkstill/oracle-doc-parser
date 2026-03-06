---
id: 19c__UTL_SMTP.RSET
name: UTL_SMTP.RSET
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.RSET

This subprogram terminates the current mail transaction.

## Syntax

```sql
UTL_SMTP.RSET (
   c  IN OUT NOCOPY connection) 
RETURN reply;

UTL_SMTP.RSET (
   c  IN OUT NOCOPY connection);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |

**Returns:** `reply`

## Usage Notes

Syntax UTL_SMTP.RSET ( c IN OUT NOCOPY connection) RETURN reply; UTL_SMTP.RSET ( c IN OUT NOCOPY connection); Parameters Table 276-37 RSET Function and Procedure Parameters Parameter Description c SMTP connection Return Values Table 276-38 RSET Function and Procedure Return Values Return Value Description reply Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types ). In cases where there are multiple replies, the last reply is returned. Usage Notes This command allows the client to cancel an e-mail message it was in the process of composing. No mail is sent. The client can call RSET at any time after the connection to the SMTP server has been opened by means of OPEN_CONNECTION until DATA or OPEN_DATA is called. Once the e-mail data has been sent, it is too late to prevent the e-mail from being sent. The server responds to RSET with a message beginning with status code 250. Related Functions QUIT Function and Procedure