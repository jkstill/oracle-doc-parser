---
id: 19c__ALL_SERVICES
name: ALL_SERVICES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SERVICES.html
---

# ALL_SERVICES

ALL_SERVICES displays all services in the database. The view excludes rows marked for deletion.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SERVICE_ID | NUMBER | Unique ID for the service |
| NAME | VARCHAR2(64) | Name describing the workload |
| NAME_HASH | NUMBER | Hash of the short name for the service |
| NETWORK_NAME | VARCHAR2(512) | Network name used to connect to the service |
| CREATION_DATE | DATE | Date the service was created |
| CREATION_DATE_HASH | NUMBER | Hash of the creation date |
| FAILOVER_METHOD | VARCHAR2(64) | TAF only for compatibility - BASIC or NONE |
| FAILOVER_TYPE | VARCHAR2(64) | For Application Continuity for Java, TRANSACTION . For TAF, SESSION or SELECT . |
| FAILOVER_RETRIES | NUMBER(10) | For Application Continuity and TAF, when reconnecting after a failure, number of attempts to re-connect per incident |
| FAILOVER_DELAY | NUMBER(10) | For Application Continuity and TAF, when reconnecting after a failure, delay between each connection retry (in seconds) |
| MIN_CARDINALITY | NUMBER | Reserved for internal use |
| MAX_CARDINALITY | NUMBER | Reserved for internal use |
| GOAL | VARCHAR2(12) | Runtime Load Balancing Goal being used to create run-time load balancing and connection load balancing advice: NONE SERVICE_TIME - Connections are balanced by response time THROUGHPUT - Connections are balanced by throughput |
| DTP | VARCHAR2(1) | DTP (distributed transaction processing) enforces all sessions for a service at one instance. This is a requirement for XA before 11 g , and is a requirement if resuming and suspending the same XA branch. |
| ENABLED | VARCHAR2(3) | Reserved for internal use |
| AQ_HA_NOTIFICATIONS | VARCHAR2(3) | To enable FAN for OCI connections, set AQ HA Notifications to True . For Oracle Database 12 c , FAN uses ONS (Oracle Notification Service) |
| CLB_GOAL | VARCHAR2(5) | Connection load balancing goal. When using run-time load balancing, GOAL=SERVICE_TIME or THROUGHPUT , set to SHORT . For a session count per service only, use LONG . |
| EDITION | VARCHAR2(128) | A non-NULL value specifies the initial session edition for subsequent database connections that use the service and do not specify an edition. A NULL value has no effect. |
| COMMIT_OUTCOME | VARCHAR2(3) | For Transaction Guard, indicates whether the database service associated with the user session has the COMMIT_OUTCOME service attribute enabled ( YES ) or not ( NO ). This attribute applies on a per session basis and is set at connect time. When COMMIT_OUTCOME = YES : Transaction Guard manages the commit status for all supported transaction types. The outcome of a COMMIT transaction is known. If there is an outage, the application can use DBMS_APP_CONT.GET_LTXID_OUTCOME to return a reliable status for the last in-flight work. A logical transaction ID (LTXID) is set for each user session at login and at each successful commit. See Also: For information about preserving the commit outcome, see Oracle Database Development Guide . For information about logical transaction IDs, see Oracle Database Development Guide . |
| RETENTION_TIMEOUT | NUMBER | For Transaction Guard, when COMMIT_OUTCOME = YES , this value indicates the amount of time (in seconds) that the commit outcome is retained in the database. |
| REPLAY_INITIATION_TIMEOUT | NUMBER | For Application Continuity, indicates a time period (in seconds) after which the request will not be replayed. The time period starts at the first request submission. The default value is 300 seconds, which is 5 minutes. |
| SESSION_STATE_CONSISTENCY | VARCHAR2(128) | Describes how non-transactional is changed during a request. This parameter is considered only if failover_type is set to TRANSACTION for Application Continuity. Examples of session state are NLS settings, optimizer preferences, event settings, PL/SQL global variables, temporary tables, advanced queues, LOBs and result cache. If non-transactional values change after the request starts, the default value of DYNAMIC should be set. Almost all applications should use DYNAMIC mode. If you are unsure, use DYNAMIC mode. |
| GLOBAL_SERVICE | VARCHAR2(3) | Indicates whether the service is global. A global service is managed by Global Data Services (GDS) and can be provided by multiple databases that contain replicated data. Possible values: YES : Indicates the service is global NO : Indicates the service is not global This attribute is set when using GDS. It cannot be set by a user. |
| PDB | VARCHAR2(128) | Name of a PDB associated with a given service. Will contain NULL for a non-CDB or if the service is not associated with a PDB (that is, connecting to a CDB using this service will cause a user to connect to the root.) When managing services for a PDB, use SRVCTL for Oracle RAC and Oracle RAC One Node databases, or connect to that PDB if it is a single instance (not RAC). The PDB attribute shows which PDB has the service. It cannot be set or modified explicitly. |
| SQL_TRANSLATION_PROFILE | VARCHAR2(261) | A non-NULL value specifies the initial SQL translation profile for subsequent database connections that use the service and do not specify a SQL translation profile. A NULL value has no effect. |
| MAX_LAG_TIME | VARCHAR2(128) | The maximum replication lag (in seconds) that is acceptable for a data replica to be used for providing the database service. Can only be specified for global services using the Global Data Services (GDS) interfaces. It is not supported to change this value at local databases. |
| GSM_FLAGS | NUMBER | Flags specific to Global Data Services (GDS). Can only be specified for global services using the GDS interfaces. It is not supported to change these values at local databases. |
| PQ_SVC | VARCHAR2(64) | Name of the associated parallel query rim service |
| STOP_OPTION | VARCHAR2(13) | Stop option for sessions of this service for planned maintenance |
| FAILOVER_RESTORE | VARCHAR2(6) | Indicates whether sessions recover their commonly used session state (like NLS, schema) when they are failed over with TAF |
| DRAIN_TIMEOUT | NUMBER | Number of seconds to wait for sessions to be drained |
| TABLE_FAMILY_ID | NUMBER | Sharded table family ID associated with the service |
| PLACEMENT_POLICY | NUMBER | Placement policy for the service. Possible values: 0 : PDB-NONE 1 : PDB-SINGLETON 2 : PDB-UNIFORM Note: Values other than 0 are applicable only in the ATP-Dedicated Cloud in an Oracle RAC environment. |
| RESET_STATE | VARCHAR2(6) | Reset state for the service. Possible values: LEVEL1 NONE |
| VCSPARE1 | VARCHAR2(1024) | Reserved for internal use |
| NSPARE1 | NUMBER | Reserved for internal use |

## Usage Notes

Related View DBA_SERVICES displays all services in the database. The view excludes rows marked for deletion. See Also: " DBA_SERVICES " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APP_CONT.GET_LTXID_OUTCOME procedure See Also: " DBA_SERVICES " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APP_CONT.GET_LTXID_OUTCOME procedure