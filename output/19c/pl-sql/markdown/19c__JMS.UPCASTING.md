---
id: 19c__JMS.UPCASTING
name: JMS.UPCASTING
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: JMS
tags: [jms]
source_file: JMS-Types.html
---

# JMS.UPCASTING

OJMS ADT aq$_jms_message is used to represent a general message, so that different types of messages can reside on the same Oracle Database Advanced Queuing queue. Oracle Database Advanced Queuing supports retrieving and populating of aq$_jms_message by supporting upcasting and downcasting between this ADT and ADTs of specific message types.

## Usage Notes

To read an aq$_jms_message , you must first downcast it to a specific message type according to its message_type field To populate an aq$_jms_message , you must first populate a specific message and upcast it to aq$_jms_message . This avoids copying all member functions of other specific message ADTs to this ADT. It also guarantees that the manipulation of this ADT is consistent with other specific message ADTs.