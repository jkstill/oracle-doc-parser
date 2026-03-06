---
id: 19c__DBMS_DG.USING
name: DBMS_DG.USING
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DG
tags: [dbms_dg]
source_file: DBMS_DG.html
---

# DBMS_DG.USING

There are conditions detectable by applications running outside of the Oracle database that may warrant the Oracle Data Guard broker to perform a fast-start failover. Because the range of possible conditions is virtually unlimited, it is left to the applications to determine which conditions warrant a fast-start failover.

## Usage Notes

When such conditions occur, the application calls the DBMS_DG . INITIATE_FS_FAILOVER procedure to alert either the primary or fast-start failover target standby database that the application wants a fast-start failover to occur immediately. The database on which the procedure was called then notifies the observer, which immediately initiates a fast-start failover as long as the standby database is in a valid fast-start failover state ("observed" and either "synchronized" or "within lag") to accept a failover.If the configuration is not in a valid fast-start failover state, the INITIATE_FS_FAILOVER subprogram returns an ORA error message (it will not signal an exception) to inform the calling application that a fast-start failover could not be performed. Note: If you are working in a multitenant container database (CDB), then functions within DBMS_DG are only executed at the root level. Ensure you are connected at the root level, not at the individual pluggable database (PDB) level. Note: If you are working in a multitenant container database (CDB), then functions within DBMS_DG are only executed at the root level. Ensure you are connected at the root level, not at the individual pluggable database (PDB) level.