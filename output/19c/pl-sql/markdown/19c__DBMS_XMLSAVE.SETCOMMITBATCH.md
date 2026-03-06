---
id: 19c__DBMS_XMLSAVE.SETCOMMITBATCH
name: DBMS_XMLSAVE.SETCOMMITBATCH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.SETCOMMITBATCH

This procedure sets the commit batch size.

## Syntax

```sql
PROCEDURE setCommitBatch(
   ctxHdl IN ctxType,
   batchSize IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| batchSize | NUMBER) | IN | (IN) |

## Usage Notes

The commit batch size refers to the number or records inserted after which a commit should follow. If batchSize is less than 1 or the session is in "auto-commit" mode, using the XSU does not make any explicit commits. By default, commitBatch is 0 . Syntax PROCEDURE setCommitBatch( ctxHdl IN ctxType, batchSize IN NUMBER); Parameters Table 209-15 SETCOMMITBATCH Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. batchSize (IN) Commit batch size.