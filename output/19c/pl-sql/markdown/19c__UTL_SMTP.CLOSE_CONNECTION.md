---
id: 19c__UTL_SMTP.CLOSE_CONNECTION
name: UTL_SMTP.CLOSE_CONNECTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.CLOSE_CONNECTION

This procedure closes the SMTP connection, causing the current SMTP operation to terminate. Use this procedure only to cancel an e-mail in the middle of the data session.

## Syntax

```sql
UTL_SMTP.CLOSE_CONNECTION (
   c     IN OUT NOCOPY connection);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | SMTP connection |

## Usage Notes

To end the SMTP connection properly, use the QUIT Function and Procedure . Syntax UTL_SMTP.CLOSE_CONNECTION ( c IN OUT NOCOPY connection); Parameters Table 276-10 CLOSE_CONNECTION Procedure Parameters Parameter Description c SMTP connection