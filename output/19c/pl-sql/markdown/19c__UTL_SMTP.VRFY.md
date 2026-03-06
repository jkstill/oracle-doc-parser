---
id: 19c__UTL_SMTP.VRFY
name: UTL_SMTP.VRFY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.VRFY

This function verifies the validity of a destination e-mail address.

## Syntax

```sql
UTL_SMTP.VRFY (
   c          IN OUT NOCOPY connection
   recipient  IN VARCHAR2) 
RETURN reply;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |
| recipient | VARCHAR2) | IN | E-mail address to be verified |

**Returns:** `reply`

## Usage Notes

Syntax UTL_SMTP.VRFY ( c IN OUT NOCOPY connection recipient IN VARCHAR2) RETURN reply; Parameters Table 276-41 VRFY Function Parameters Parameter Description c SMTP connection recipient E-mail address to be verified Return Values Table 276-42 VRFY Function Return Values Return Value Description reply Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types ). In cases where there are multiple replies, the last reply is returned. Usage Notes The server attempts to resolve the destination address recipient. If successful, it returns the recipient's full name and fully qualified mailbox path. The connection to the server must have already been established by means of OPEN_CONNECTION and HELO or EHLO before making this request. Successful verification returns one or more lines beginning with status code 250 or 251.