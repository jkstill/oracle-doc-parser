---
id: 19c__DBMS_MGWADM.STARTUP
name: DBMS_MGWADM.STARTUP
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.STARTUP

This procedure starts the Messaging Gateway agent. It must be called before any propagation activity can take place.

## Syntax

```sql
DBMS_MGWADM.STARTUP(
   instance       IN  BINARY_INTEGER DEFAULT 0,
   force          IN  BINARY_INTEGER DEFAULT DBMS_MGWADM.NO_FORCE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| instance | BINARY_INTEGER | IN | Specifies which instance can run the job queue job used to start the Messaging Gateway agent. If this is zero, then the job can be run by any instance. Caution: This parameter has been deprecated . |
| force | BINARY_INTEGER | IN | If this is DBMS_MGWADM.FORCE , then any positive integer is acceptable as the job instance. If this is DBMS_MGWADM.NO_FORCE (the default), then the specified instance must be running; otherwise the routine raises an exception. Caution: This parameter has been deprecated . |
| agent_name |  |  | Identifies the Messaging Gateway agent. DBMS_MGWADM . DEFAULT_AGENT specifies the default agent. |

## Usage Notes

Syntax DBMS_MGWADM.STARTUP( instance IN BINARY_INTEGER DEFAULT 0, force IN BINARY_INTEGER DEFAULT DBMS_MGWADM.NO_FORCE); DBMS_MGWADM.STARTUP( agent_name IN VARCHAR2); Parameters Table 110-49 STARTUP Procedure Parameters Parameter Description instance Specifies which instance can run the job queue job used to start the Messaging Gateway agent. If this is zero, then the job can be run by any instance. Caution: This parameter has been deprecated . force If this is DBMS_MGWADM.FORCE , then any positive integer is acceptable as the job instance. If this is DBMS_MGWADM.NO_FORCE (the default), then the specified instance must be running; otherwise the routine raises an exception. Caution: This parameter has been deprecated . agent_name Identifies the Messaging Gateway agent. DBMS_MGWADM . DEFAULT_AGENT specifies the default agent. Usage Notes The Messaging Gateway default agent will be started if an agent name is not specified. The force and instance parameters are no longer used and will be ignored. If the instance affinity parameters were being used to start the default agent on a specific instance, the administrator will need to create a database service and then assign that service to the default agent using the DBMS_MGWADM . ALTER_AGENT procedure. The Messaging Gateway agent cannot be started until an agent user has been configured by the DBMS_MGWADM . CREATE_AGENT or DBMS_MGWADM . ALTER_AGENT subprograms.