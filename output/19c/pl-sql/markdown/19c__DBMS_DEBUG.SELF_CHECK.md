---
id: 19c__DBMS_DEBUG.SELF_CHECK
name: DBMS_DEBUG.SELF_CHECK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.SELF_CHECK

This procedure performs an internal consistency check. SELF_CHECK also runs a communications test to ensure that the Probe processes are able to communicate.

## Syntax

```sql
DBMS_DEBUG.SELF_CHECK (
   timeout IN binary_integer := 60);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| timeout | binary_integer | IN | The timeout to use for the communication test. Default is 60 seconds. |

## Usage Notes

If SELF_CHECK does not return successfully, then an incorrect version of DBMS_DEBUG was probably installed on this server. The solution is to install the correct version ( pbload . sql loads DBMS_DEBUG and the other relevant packages). Syntax DBMS_DEBUG.SELF_CHECK ( timeout IN binary_integer := 60); Parameters Table 57-41 SELF_CHECK Procedure Parameters Parameter Description timeout The timeout to use for the communication test. Default is 60 seconds. Exceptions Table 57-42 SELF_CHECK Procedure Exceptions Exception Description OER-6516 Probe version is inconsistent pipe_creation_failure Could not create a pipe pipe_send_failure Could not write data to the pipe pipe_receive_failure Could not read data from the pipe pipe_datatype_mismatch Datatype in the pipe was wrong pipe_data_error Data got garbled in the pipe All of these exceptions are fatal. They indicate a serious problem with Probe that prevents it from working correctly.