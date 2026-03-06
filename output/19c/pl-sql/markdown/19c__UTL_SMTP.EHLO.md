---
id: 19c__UTL_SMTP.EHLO
name: UTL_SMTP.EHLO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.EHLO

This subprogram performs the initial handshake with SMTP server using the EHLO command.

## Syntax

```sql
UTL_SMTP.EHLO (
   c       IN OUT NOCOPY connection, 
   domain  IN) 
RETURN replies;

UTL_SMTP.EHLO (
   c       IN OUT NOCOPY connection, 
   domain  IN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |
| domain | IN) | IN | Domain name of the local (sending) host. Used for identification purposes. |

**Returns:** `replies`

## Usage Notes

Syntax UTL_SMTP.EHLO ( c IN OUT NOCOPY connection, domain IN) RETURN replies; UTL_SMTP.EHLO ( c IN OUT NOCOPY connection, domain IN); Parameters Table 276-19 EHLO Function and Procedure Parameters Parameter Description c SMTP connection domain Domain name of the local (sending) host. Used for identification purposes. Return Values Table 276-20 EHLO Function and Procedure Return Values Return Value Description replies Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types ). Usage Notes The EHLO interface is identical to HELO except that it allows the server to return more descriptive information about its configuration. [RFC1869] specifies the format of the information returned, which the PL/SQL application can retrieve using the functional form of this call. For compatibility with HELO, each line of text returned by the server begins with status code 250. Related Functions HELO Function and Procedure