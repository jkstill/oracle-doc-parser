---
id: 19c__UTL_SMTP.HELP
name: UTL_SMTP.HELP
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.HELP

This function sends the HELP command.

## Syntax

```sql
UTL_SMTP.HELP (
   c         IN OUT NOCOPY   connection, 
   command   IN              VARCHAR2 DEFAULT NULL) 
RETURN replies;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |
| command | VARCHAR2 | IN | Command to get the help message |

**Returns:** `replies`

## Usage Notes

Syntax UTL_SMTP.HELP ( c IN OUT NOCOPY connection, command IN VARCHAR2 DEFAULT NULL) RETURN replies; Parameters Table 276-23 HELP Function Parameters Parameter Description c SMTP connection command Command to get the help message Return Values Table 276-24 HELP Function Return Values Return Value Description replies Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types )