---
id: 19c__UTL_SMTP.QUIT
name: UTL_SMTP.QUIT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.QUIT

This subprogram terminates an SMTP session and disconnects from the server.

## Syntax

```sql
UTL_SMTP.QUIT (
   c  IN OUT NOCOPY connection) 
RETURN reply;

UTL_SMTP.QUIT (
   c  IN OUT NOCOPY connection);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |

**Returns:** `reply`

## Usage Notes

Syntax UTL_SMTP.QUIT ( c IN OUT NOCOPY connection) RETURN reply; UTL_SMTP.QUIT ( c IN OUT NOCOPY connection); Parameter Table 276-33 QUIT Function and Procedure Parameters Parameter Description c SMTP connection Return Values Table 276-34 QUIT Function and Procedure Function Return Values Return Value Description reply Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types ). In cases where there are multiple replies, the last reply is returned. Usage Notes The QUIT command informs the SMTP server of the client's intent to terminate the session. It then closes the connection established by OPEN_CONNECTION which must have been called before executing this command. If a mail transaction is in progress when QUIT is issued, it is canceled in the same manner as RSET. The function form of this command returns a single line beginning with the status code 221 on successful termination. In all cases, the connection to the SMTP server is closed. The fields REMOTE_HOST and REMOTE_PORT of c are reset. Related Functions RSET Function and Procedure