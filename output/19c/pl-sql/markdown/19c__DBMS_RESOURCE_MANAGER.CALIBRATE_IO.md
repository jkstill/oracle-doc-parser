---
id: 19c__DBMS_RESOURCE_MANAGER.CALIBRATE_IO
name: DBMS_RESOURCE_MANAGER.CALIBRATE_IO
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.CALIBRATE_IO

This procedure calibrates the I/O capabilities of storage. Calibration status is available from the V$IO_CALIBRATION_STATUS view and results for a successful calibration run are located in DBA_RSRC_IO_CALIBRATE table.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.CALIBRATE_IO (
   num_physical_disks      IN  PLS_INTEGER DEFAULT 1,
   max_latency             IN  PLS_INTEGER DEFAULT 20,
   max_iops                OUT PLS_INTEGER,
   max_mbps                OUT PLS_INTEGER,
   actual_latency          OUT PLS_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| num_physical_disks | PLS_INTEGER | IN | Approximate number of physical disks in the database storage. This parameter is used to determine the initial I/O load for the calibration run. |
| max_latency | PLS_INTEGER | IN | Maximum tolerable latency in milliseconds for database-block-sized IO requests |
| max_iops | PLS_INTEGER | OUT | Maximum number of I/O requests per second that can be sustained. The I/O requests are randomly-distributed, database-block-sized reads. |
| max_mbps | PLS_INTEGER | OUT | Maximum throughput of I/O that can be sustained, expressed in megabytes per second. The I/O requests are randomly-distributed, 1 megabyte reads. |
| actual_latency | PLS_INTEGER) | OUT | Average latency of database-block-sized I/O requests at max_iops rate, expressed in milliseconds |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.CALIBRATE_IO ( num_physical_disks IN PLS_INTEGER DEFAULT 1, max_latency IN PLS_INTEGER DEFAULT 20, max_iops OUT PLS_INTEGER, max_mbps OUT PLS_INTEGER, actual_latency OUT PLS_INTEGER); Parameters Table 142-3 CALIBRATE_IO Procedure Parameters Parameter Description num_physical_disks Approximate number of physical disks in the database storage. This parameter is used to determine the initial I/O load for the calibration run. max_latency Maximum tolerable latency in milliseconds for database-block-sized IO requests max_iops Maximum number of I/O requests per second that can be sustained. The I/O requests are randomly-distributed, database-block-sized reads. max_mbps Maximum throughput of I/O that can be sustained, expressed in megabytes per second. The I/O requests are randomly-distributed, 1 megabyte reads. actual_latency Average latency of database-block-sized I/O requests at max_iops rate, expressed in milliseconds Usage Notes Only users with the SYSDBA privilege can run this procedure. Qualified users must also turn on timed_statistics , and ensure asynch_io is enabled for datafiles. This can be achieved by setting filesystemio_options to either ASYNCH or SETALL . One can also query the asynch_io status by means of the following SQL statement: col name format a50 SELECT name, asynch_io FROM v$datafile f,v$iostat_file i WHERE f.file# = i.file_no AND filetype_name = 'Data File' / Only one calibration can be run at a time. If another calibration is initiated at the same time, it will fail. For an Oracle Real Application Clusters (Oracle RAC) database, the workload is simultaneously generated from all instances. In a multitenant container database (CDB), calibration can only be run from the CDB root ( CDB$ROOT ). Calibration is extremely disruptive to the database performance. It is strongly recommended to run calibration only when database users can tolerate severe deterioration to database performance. For optimal calibration results, no other database workloads should be running. See Also: Oracle Database Performance Tuning Guide for more information about calibration See Also: Oracle Database Performance Tuning Guide for more information about calibration Examples Example of using I/O Calibration procedure SET SERVEROUTPUT ON DECLARE lat NUMBER; iops INTEGER; mbps INTEGER; BEGIN -- DBMS_RESOURCE_MANAGER.CALIBRATE_IO (<DISKS>, <MAX_LATENCY>, iops, mbps, lat); DBMS_RESOURCE_MANAGER.CALIBRATE_IO (2, 10, iops, mbps, lat); end; / View for I/O calibration results SQL> desc V$IO_CALIBRATION_STATUS Name Null? Type ----------------------------------------- -------- ---------------------------- STATUS VARCHAR2(13) CALIBRATION_TIME TIMESTAMP(3) SQL> desc gv$io_calibration_status Name Null? Type ----------------------------------------- -------- ---------------------------- INST_ID NUMBER STATUS VARCHAR2(13) CALIBRATION_TIME TIMESTAMP(3) Column explanation: ------------------- STATUS: IN PROGRESS : Calibration in Progress (Results from previous calibration run displayed, if available) READY : Results ready and available from earlier run NOT AVAILABLE : Calibration results not available. CALIBRATION_TIME: End time of the last calibration run DBA table that stores I/O Calibration results SQL> desc DBA_RSRC_IO_CALIBRATE Name Null? Type ----------------------------------------- -------- ---------------------------- START_TIME TIMESTAMP(6) END_TIME TIMESTAMP(6) MAX_IOPS NUMBER MAX_MBPS NUMBER MAX_PMBPS NUMBER LATENCY NUMBER NUM_PHYSICAL_DISKS NUMBER comment on table DBA_RSRC_IO_CALIBRATE is 'Results of the most recent I/O calibration' / comment on column DBA_RSRC_IO_CALIBRATE.START_TIME is 'start time of the most recent I/O calibration' / comment on column DBA_RSRC_IO_CALIBRATE.END_TIME is 'end time of the most recent I/O calibration' / comment on column DBA_RSRC_IO_CALIBRATE.MAX_IOPS is 'maximum number of data-block read requests that can be sustained per second' / comment on column DBA_RSRC_IO_CALIBRATE.MAX_MBPS is 'maximum megabytes per second of maximum-sized read requests that can be sustained' / comment on column DBA_RSRC_IO_CALIBRATE.MAX_PMBPS is 'maximum megabytes per second of large I/O requests that can be sustained by a single process' / comment on column DBA_RSRC_IO_CALIBRATE.LATENCY is 'latency for data-block read requests' / comment on column DBA_RSRC_IO_CALIBRATE.NUM_PHYSICAL_DISKS is 'number of physical disks in the storage subsystem (as specified by user)' /