---
id: 19c__DBMS_XSTREAM_ADM.ENABLE_GG_XSTREAM_FOR_STREAMS
name: DBMS_XSTREAM_ADM.ENABLE_GG_XSTREAM_FOR_STREAMS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.ENABLE_GG_XSTREAM_FOR_STREAMS

This procedure enables XStream optimizations and performance optimizations for Oracle Replication components.

## Syntax

```sql
DBMS_XSTREAM_ADM.ENABLE_GG_XSTREAM_FOR_STREAMS(
   enable IN BOOLEAN  TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| enable | BOOLEAN | IN | If TRUE , then enable XStream performance optimizations for Oracle Replication components. If FALSE , then disable XStream performance optimizations for Oracle Replication components. |

## Usage Notes

This procedure is intended for users of Oracle Replication who want to enable XStream optimizations and optimizations. For example, you can enable the optimizations for an Oracle Replication configuration that uses capture processes and apply processes to replicate changes between Oracle databases. These capabilities and optimizations are enabled automatically for XStream components, such as outbound servers, inbound servers, and capture processes that send changes to outbound servers. It is not necessary to run this procedure for XStream components. When XStream optimizations are enabled, Oracle Replication components can stream ID key LCRs and sequence LCRs. The XStream performance optimizations improve efficiency in various areas, including: LCR processing Handling large transactions DML execution during apply Dependency computation and scheduling Capture process parallelism Syntax DBMS_XSTREAM_ADM.ENABLE_GG_XSTREAM_FOR_STREAMS( enable IN BOOLEAN TRUE); Parameters Table 217-20 ENABLE_GG_XSTREAM_FOR_STREAMS Procedure Parameters Parameter Description enable If TRUE , then enable XStream performance optimizations for Oracle Replication components. If FALSE , then disable XStream performance optimizations for Oracle Replication components. Usage Notes The following usage notes apply to this procedure: When you run this procedure, all capture processes and apply processes are restarted. After you run this procedure, the PURPOSE column in the following views displays XStream Streams : ALL_APPLY DBA_APPLY ALL_CAPTURE DBA_CAPTURE A license for the Oracle GoldenGate product is required to enable XStream performance optimizations for Oracle Replication components. See Also: IS_GG_XSTREAM_FOR_STREAMS Function Oracle Database XStream Guide, Chapter 1, Prerequisites for XStream"