---
id: 19c__UTL_SMTP.COMMAND
name: UTL_SMTP.COMMAND
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.COMMAND

This subprogram performs a generic SMTP command.

## Syntax

```sql
UTL_SMTP.COMMAND (
   c     IN OUT NOCOPY    connection,
   cmd   IN               VARCHAR2,
   arg   IN               VARCHAR2 DEFAULT NULL)
RETURN reply;

UTL_SMTP.COMMAND (
   c     IN OUT NOCOPY    connection,
   cmd   IN               VARCHAR2,
   arg   IN               VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |
| cmd | VARCHAR2 | IN | SMTP command to send to the server |
| arg | VARCHAR2 | IN | Optional argument to the SMTP argument. A space is inserted between cmd and arg . |

**Returns:** `reply`

## Usage Notes

Syntax UTL_SMTP.COMMAND ( c IN OUT NOCOPY connection, cmd IN VARCHAR2, arg IN VARCHAR2 DEFAULT NULL) RETURN reply; UTL_SMTP.COMMAND ( c IN OUT NOCOPY connection, cmd IN VARCHAR2, arg IN VARCHAR2 DEFAULT NULL); Parameters Table 276-13 COMMAND Function and Procedure Parameters Parameter Description c SMTP connection cmd SMTP command to send to the server arg Optional argument to the SMTP argument. A space is inserted between cmd and arg . Return Values Table 276-14 COMMAND Function and Procedure Return Values Return Value Description reply Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types ). In cases where there are multiple replies, the last reply is returned. Usage Notes This function is used to invoke generic SMTP commands. Use COMMAND if only a single reply line is expected. Use COMMAND_REPLIES if multiple reply lines are expected. For COMMAND , if multiple reply lines are returned from the SMTP server, it returns the last reply line only.