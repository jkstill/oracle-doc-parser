---
id: 19c__DBMS_XMLSAVE.SETBATCHSIZE
name: DBMS_XMLSAVE.SETBATCHSIZE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.SETBATCHSIZE

This procedure changes the batch size used during DML operations.

## Syntax

```sql
PROCEDURE setBatchSize(
   ctxHdl IN ctxType,
   batchSize IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| batchSize | NUMBER) | IN | (IN) |

## Usage Notes

When performing inserts, updates or deletes, it is better to batch the operations so that they get executed in one shot rather than as separate statements. The flip side is that more memory is needed to buffer all the bind values. Note that when batching is used, a commit occurs only after a batch is executed. So if one of the statement inside a batch fails, the whole batch is rolled back. This is a small price to pay considering the performance gain; nevertheless, if this behavior is unacceptable, then set the batch size to 1. Syntax PROCEDURE setBatchSize( ctxHdl IN ctxType, batchSize IN NUMBER); Parameters Table 209-14 SETBATCHSIZE Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. batchSize (IN) Batch size.