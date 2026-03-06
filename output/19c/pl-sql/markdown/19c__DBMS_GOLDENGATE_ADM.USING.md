---
id: 19c__DBMS_GOLDENGATE_ADM.USING
name: DBMS_GOLDENGATE_ADM.USING
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_GOLDENGATE_ADM
tags: [dbms_goldengate_adm]
source_file: DBMS_GOLDENGATE_ADM.html
---

# DBMS_GOLDENGATE_ADM.USING

This section contains topics which relate to using the DBMS_GOLDENGATE_ADM package.

## Usage Notes

This section contains topics which relate to using the DBMS_GOLDENGATE_ADM package. DBMS_GOLDENGATE_ADM Overview DBMS_GOLDENGATE_ADM Security Model When more than one replica of a table allows changes to the table, a conflict can occur when a change is made to the same row in two different databases at nearly the same time. Oracle GoldenGate replicates changes using row logical change records (LCRs). It detects a conflict by comparing the old values in the row LCR with the current values of the corresponding table row identified by the key columns. If any column value does not match, then there is a conflict. After a conflict is detected, Oracle GoldenGate can resolve the conflict by overwriting values in the row with some values from the row LCR, ignoring the values in the row LCR, or computing a delta to update the row values. XStream inbound servers and outbound servers can be used in an XStream configuration in a multitenant container database (CDB). A CDB is an Oracle database that includes zero, one, or many user-created pluggable databases (PDBs). Note: Using XStream requires purchasing a license for the Oracle GoldenGate product. See Also: Oracle Database XStream Guide Oracle Database Concepts for more information about CDBs and PDBs Note: Using XStream requires purchasing a license for the Oracle GoldenGate product. See Also: Oracle Database XStream Guide Oracle Database Concepts for more information about CDBs and PDBs If subprograms in the package are run from within a stored procedure, then the user who runs the subprograms must be granted EXECUTE privilege on the package directly. It cannot be granted through a role. An Oracle GoldenGate administrator must be configured at each Oracle database in the table’s replication environment, and Oracle GoldenGate must be configured to replicate the table at each Oracle database. You can configure an Oracle GoldenGate administrator using the GRANT_ADMIN_PRIVILEGE procedure in the DBMS_GOLDENGATE_ADM package. See Also: The Oracle GoldenGate documentation for more information about Oracle GoldenGate replication and configuring an Oracle GoldenGate administrator