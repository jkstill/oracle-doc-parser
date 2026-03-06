---
id: 19c__UTL_SMTP.HELO
name: UTL_SMTP.HELO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.HELO

This subprogram performs the initial handshake with SMTP server using the HELO command.

## Syntax

```sql
UTL_SMTP.HELO (
   c       IN OUT NOCOPY   connection, 
   domain  IN              VARCHAR2) 
RETURN reply;

UTL_SMTP.HELO (
   c       IN OUT NOCOPY   connection, 
   domain  IN              VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |
| domain | VARCHAR2) | IN | Domain name of the local (sending) host. Used for identification purposes. |

**Returns:** `reply`

## Usage Notes

Syntax UTL_SMTP.HELO ( c IN OUT NOCOPY connection, domain IN VARCHAR2) RETURN reply; UTL_SMTP.HELO ( c IN OUT NOCOPY connection, domain IN VARCHAR2); Parameters Table 276-21 HELO Function and Procedure Parameters Parameter Description c SMTP connection domain Domain name of the local (sending) host. Used for identification purposes. Return Values Table 276-22 HELO Function and Procedure Return Values Return Value Description reply Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types ). In cases where there are multiple replies, the last reply is returned. Usage Notes RFC 821 specifies that the client must identify itself to the server after connecting. This routine performs that identification. The connection must have been opened through a call to OPEN_CONNECTION Functions before calling this routine. The expected response from the server is a message beginning with status code 250. Related Functions EHLO Function and Procedure