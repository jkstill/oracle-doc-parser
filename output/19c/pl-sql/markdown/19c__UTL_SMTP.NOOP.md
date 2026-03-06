---
id: 19c__UTL_SMTP.NOOP
name: UTL_SMTP.NOOP
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.NOOP

This subprogram issues the NULL command.

## Syntax

```sql
UTL_SMTP.NOOP (
   c  IN OUT NOCOPY connection) 
RETURN reply;

UTL_SMTP.NOOP (
   c  IN OUT NOCOPY connection);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |

**Returns:** `reply`

## Usage Notes

Syntax UTL_SMTP.NOOP ( c IN OUT NOCOPY connection) RETURN reply; UTL_SMTP.NOOP ( c IN OUT NOCOPY connection); Parameter Table 276-27 NOOP Function and Procedure Parameters Parameter Description c SMTP connection Return Values Table 276-28 NOOP Function and Procedure Return Values Return Value Description reply Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types ). In cases where there are multiple replies, the last reply is returned. Usage Notes This command has no effect except to elicit a successful reply from the server. It can be issued at any time after the connection to the server has been established with OPEN_CONNECTION . The NOOP command can be used to verify that the server is still connected and is listening properly. This command replies with a single line beginning with status code 250.