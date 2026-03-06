---
id: 19c__DBMS_XSTREAM_ADM.REMOVE_XSTREAM_CONFIGURATION
name: DBMS_XSTREAM_ADM.REMOVE_XSTREAM_CONFIGURATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.REMOVE_XSTREAM_CONFIGURATION

This procedure removes the XStream configuration at the local database.

## Syntax

```sql
DBMS_XSTREAM_ADM.REMOVE_XSTREAM_CONFIGURATION(
   container IN VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| container | VARCHAR2 | IN | If CURRENT , then the XStream configuration is removed from the current container. CURRENT can be specified while connected to the root or to a PDB in a CDB. If ALL , then the XStream configuration is removed from all of the containers in the CDB. To specify ALL , the procedure must be invoked in the root. If a container name, then the XStream configuration is removed from the specified container. To specify root, use CDB$ROOT while connected to the root. To specify a PDB, the procedure must be invoked in the root. Note: This parameter only applies to a CDB. |

## Usage Notes

Syntax DBMS_XSTREAM_ADM.REMOVE_XSTREAM_CONFIGURATION( container IN VARCHAR2 DEFAULT NULL); Parameters Table 217-28 REMOVE_XSTREAM_CONFIGURATION Procedure Parameters Parameter Description container If CURRENT , then the XStream configuration is removed from the current container. CURRENT can be specified while connected to the root or to a PDB in a CDB. If ALL , then the XStream configuration is removed from all of the containers in the CDB. To specify ALL , the procedure must be invoked in the root. If a container name, then the XStream configuration is removed from the specified container. To specify root, use CDB$ROOT while connected to the root. To specify a PDB, the procedure must be invoked in the root. Note: This parameter only applies to a CDB. Usage Notes Specifically, this procedure performs the following actions at the local database: Drops all capture processes If any tables have been prepared for instantiation, then aborts preparation for instantiation for the table using the ABORT_TABLE_INSTANTIATION procedure in the DBMS_CAPTURE_ADM package If any schemas have been prepared for instantiation, then aborts preparation for instantiation for the schema using the ABORT_SCHEMA_INSTANTIATION procedure in the DBMS_CAPTURE_ADM package If the database has been prepared for instantiation, then aborts preparation for instantiation for the database using the ABORT_GLOBAL_INSTANTIATION procedure in the DBMS_CAPTURE_ADM package Drops propagations that were created using either the DBMS_XSTREAM_ADM package or the DBMS_PROPAGATION_ADM package. Before a propagation is dropped, its propagation job is disabled. Does not drop propagations that were created using the DBMS_AQADM package. Disables all propagation jobs used by propagations Drops all apply processes. If there are apply errors in the error queue for an apply process, then this procedure deletes these apply errors before it drops the apply process. Removes specifications for DDL handlers used by apply processes, but does not delete the PL/SQL procedures used by these handlers Removes specifications for message handlers used by apply processes, but does not delete the PL/SQL procedures used by these handlers Removes specifications for precommit handlers used by apply processes, but does not delete the PL/SQL procedures used by these handlers Removes the instantiation SCN and ignore SCN for each apply object and schema and for the entire database Removes messaging clients Unsets message notification specifications that were set using the SET_MESSAGE_NOTIFICATION procedure in the DBMS_XSTREAM_ADM package Removes specifications for procedure DML handlers and error handlers, but does not delete the PL/SQL procedures used by these handlers Removes update conflict handlers Removes specifications for substitute key columns for apply tables Drops rule sets and rules that were created using the DBMS_XSTREAM_ADM package. Drops unused rule sets that were used by capture processes, propagations, apply processes, and messaging clients, and removes the rules in these rule sets. These rules and rule sets are removed regardless of whether they were created using the DBMS_XSTREAM_ADM package or the DBMS_RULE_ADM package. This procedure stops capture processes and apply processes before it drops them. This procedure does not drop rule sets or rules if they meet both of the following conditions: The rule sets or rules were created using the DBMS_RULE_ADM package. The rule sets or rules were not used by a capture process, propagation, apply process, or messaging client. Note: Running this procedure is dangerous. You should run this procedure only if you are sure you want to remove the entire XStream configuration at a database. If an Oracle Replication configuration exists at the database, then this procedure also removes the entire Oracle Replication configuration. Note: Running this procedure repeatedly does not cause errors. If the procedure fails to complete, then you can run it again. This procedure commits multiple times. Note: Running this procedure is dangerous. You should run this procedure only if you are sure you want to remove the entire XStream configuration at a database. If an Oracle Replication configuration exists at the database, then this procedure also removes the entire Oracle Replication configuration. Note: Running this procedure repeatedly does not cause errors. If the procedure fails to complete, then you can run it again. This procedure commits multiple times.