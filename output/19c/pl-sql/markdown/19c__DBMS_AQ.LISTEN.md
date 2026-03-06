---
id: 19c__DBMS_AQ.LISTEN
name: DBMS_AQ.LISTEN
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQ
tags: [dbms_aq]
source_file: DBMS_AQ.html
---

# DBMS_AQ.LISTEN

This procedure listens on one or more queues on behalf of a list of agents. The address field of the agent indicates the queue the agent wants to monitor. Only local queues are supported as addresses. Protocol is reserved for future use.

## Syntax

```sql
DBMS_AQ.LISTEN (
   agent_list            IN    AQ$_AGENT_LIST_T,
   wait                  IN    BINARY_INTEGER DEFAULT DBMS_AQ.FOREVER, 
   agent                 OUT   SYS.AQ$_AGENT);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| agent_list | AQ$_AGENT_LIST_T | IN | List of agents to listen for |
| wait | BINARY_INTEGER | IN | Time out for the listen call in seconds. By default, the call will block forever. |
| listen_delivery_mode |  |  | The caller specifies whether it is interested in persistent, buffered messages or both types of messages, specifying a delivery mode of DBMS_AQ.PERSISTENT or DBMS_AQ.BUFFERED or DBMS_AQ.PERSISTENT_OR_BUFFERED |
| agent | SYS.AQ$_AGENT) | OUT | Agent with a message available for consumption |
| message_delivery_mode |  |  | Returns the message type along with the queue and consumer for which there is a message |

## Usage Notes

Syntax DBMS_AQ.LISTEN ( agent_list IN AQ$_AGENT_LIST_T, wait IN BINARY_INTEGER DEFAULT DBMS_AQ.FOREVER, agent OUT SYS.AQ$_AGENT); DBMS_AQ.LISTEN ( agent_list IN AQ$_AGENT_LIST_T, wait IN BINARY_INTEGER DEFAULT FOREVER, listen_delivery_mode IN PLS_INTEGER DEFAULT DBMS_AQ.PERSISTENT, agent OUT SYS.AQ$_AGENT, message_delivery_mode OUT PLS_INTEGER); TYPE aq$_agent_list_t IS TABLE of aq$_agent INDEXED BY BINARY_INTEGER; TYPE aq$_agent_list_t IS TABLE of aq$_agent INDEXED BY BINARY_INTEGER; Parameters Table 22-11 LISTEN Procedure Parameters Parameter Description agent_list List of agents to listen for wait Time out for the listen call in seconds. By default, the call will block forever. listen_delivery_mode The caller specifies whether it is interested in persistent, buffered messages or both types of messages, specifying a delivery mode of DBMS_AQ.PERSISTENT or DBMS_AQ.BUFFERED or DBMS_AQ.PERSISTENT_OR_BUFFERED agent Agent with a message available for consumption message_delivery_mode Returns the message type along with the queue and consumer for which there is a message Usage Notes If agent-address is a multiconsumer queue, then agent-name is mandatory. For single-consumer queues, agent-name must not be specified. This procedure takes a list of agents as an argument. You specify the queue to be monitored in the address field of each agent listed. You also must specify the name of the agent when monitoring multiconsumer queues. For single-consumer queues, an agent name must not be specified. Only local queues are supported as addresses. Protocol is reserved for future use. This is a blocking call that returns when there is a message ready for consumption for an agent in the list. If there are messages for more than one agent, only the first agent listed is returned. If there are no messages found when the wait time expires, an error is raised. A successful return from the LISTEN call is only an indication that there is a message for one of the listed agents in one the specified queues. The interested agent must still dequeue the relevant message. Note: You cannot call LISTEN on nonpersistent queues. Note: You cannot call LISTEN on nonpersistent queues.