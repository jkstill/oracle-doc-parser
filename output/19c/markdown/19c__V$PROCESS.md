---
id: 19c__V$PROCESS
name: V$PROCESS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-PROCESS.html
---

# V$PROCESS

V$PROCESS displays information about the currently active processes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDR | RAW(4 | 8) |  |
| PID | NUMBER |  |
| SOSID | VARCHAR2(24) |  |
| SPID | VARCHAR2(24) |  |
| STID | VARCHAR2(24) |  |
| EXECUTION_TYPE | VARCHAR2(10) |  |
| PNAME | VARCHAR2(5) |  |
| USERNAME | VARCHAR2(15) |  |
| SERIAL# | NUMBER |  |
| TERMINAL | VARCHAR2(30) |  |
| PROGRAM | VARCHAR2(48) |  |
| TRACEID | VARCHAR2(255) |  |
| TRACEFILE | VARCHAR2(513) |  |
| BACKGROUND | VARCHAR2(1) |  |
| LATCHWAIT | VARCHAR2(16) |  |
| LATCHSPIN | VARCHAR2(16) |  |
| PGA_USED_MEM | NUMBER |  |
| PGA_ALLOC_MEM | NUMBER |  |
| PGA_FREEABLE_MEM | NUMBER |  |
| PGA_MAX_MEM | NUMBER |  |
| NUMA_DEFAULT | NUMBER |  |
| NUMA_CURR | NUMBER |  |
| CPU_USED | NUMBER |  |
| CON_ID | NUMBER |  |