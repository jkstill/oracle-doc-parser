---
id: 19c__DBMS_PARALLEL_EXECUTE
name: DBMS_PARALLEL_EXECUTE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE

The following examples run on the Human Resources (HR) schema of the Oracle Database Sample Schemas. They requires that the HR schema be created with the JOB SYSTEM privilege.

## Syntax

```sql
DECLARE
  l_sql_stmt VARCHAR2(1000);
  l_try NUMBER;
  l_status NUMBER;
BEGIN
 
  -- Create the TASK
  DBMS_PARALLEL_EXECUTE.CREATE_TASK ('mytask');
 
  -- Chunk the table by ROWID
  DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_ROWID('mytask', 'HR', 'EMPLOYEES', true, 100);
 
  -- Execute the DML in parallel
  l_sql_stmt := 'update EMPLOYEES e 
      SET e.salary = e.salary + 10
      WHERE rowid BETWEEN :start_id AND :end_id';
  DBMS_PARALLEL_EXECUTE.RUN_TASK('mytask', l_sql_stmt, DBMS_SQL.NATIVE,
                                 parallel_level => 10);
 
  -- If there is an error, RESUME it for at most 2 times.
  L_try := 0;
  L_status := DBMS_PARALLEL_EXECUTE.TASK_STATUS('mytask');
  WHILE(l_try < 2 and L_status != DBMS_PARALLEL_EXECUTE.FINISHED) 
  LOOP
    L_try := l_try + 1;
    DBMS_PARALLEL_EXECUTE.RESUME_TASK('mytask');
    L_status := DBMS_PARALLEL_EXECUTE.TASK_STATUS('mytask');
  END LOOP;
 
  -- Done with processing; drop the task
  DBMS_PARALLEL_EXECUTE.DROP_TASK('mytask');
   
END;
/
```

## Usage Notes

This example shows the most common usage of this package. After calling the RUN_TASK Procedure , it checks for errors and reruns in the case of error. DECLARE l_sql_stmt VARCHAR2(1000); l_try NUMBER; l_status NUMBER; BEGIN -- Create the TASK DBMS_PARALLEL_EXECUTE.CREATE_TASK ('mytask'); -- Chunk the table by ROWID DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_ROWID('mytask', 'HR', 'EMPLOYEES', true, 100); -- Execute the DML in parallel l_sql_stmt := 'update EMPLOYEES e SET e.salary = e.salary + 10 WHERE rowid BETWEEN :start_id AND :end_id'; DBMS_PARALLEL_EXECUTE.RUN_TASK('mytask', l_sql_stmt, DBMS_SQL.NATIVE, parallel_level => 10); -- If there is an error, RESUME it for at most 2 times. L_try := 0; L_status := DBMS_PARALLEL_EXECUTE.TASK_STATUS('mytask'); WHILE(l_try < 2 and L_status != DBMS_PARALLEL_EXECUTE.FINISHED) LOOP L_try := l_try + 1; DBMS_PARALLEL_EXECUTE.RESUME_TASK('mytask'); L_status := DBMS_PARALLEL_EXECUTE.TASK_STATUS('mytask'); END LOOP; -- Done with processing; drop the task DBMS_PARALLEL_EXECUTE.DROP_TASK('mytask'); END; / Chunk by User-Provided SQL A user can specify a chunk algorithm by using the CREATE_CHUNKS_BY_SQL Procedure . This example shows that rows with the same manager_id are grouped together and processed in one chunk. DECLARE l_chunk_sql VARCHAR2(1000); l_sql_stmt VARCHAR2(1000); l_try NUMBER; l_status NUMBER; BEGIN -- Create the TASK DBMS_PARALLEL_EXECUTE.CREATE_TASK ('mytask'); -- Chunk the table by MANAGER_ID l_chunk_sql := 'SELECT distinct manager_id, manager_id FROM employees'; DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_SQL('mytask', l_chunk_sql, false); -- Execute the DML in parallel -- the WHERE clause contain a condition on manager_id, which is the chunk -- column. In this case, grouping rows is by manager_id. l_sql_stmt := 'update EMPLOYEES e SET e.salary = e.salary + 10 WHERE manager_id between :start_id and :end_id'; DBMS_PARALLEL_EXECUTE.RUN_TASK('mytask', l_sql_stmt, DBMS_SQL.NATIVE, parallel_level => 10); -- If there is error, RESUME it for at most 2 times. L_try := 0; L_status := DBMS_PARALLEL_EXECUTE.TASK_STATUS('mytask'); WHILE(l_try < 2 and L_status != DBMS_PARALLEL_EXECUTE.FINISHED) Loop L_try := l_try + 1; DBMS_PARALLEL_EXECUTE.RESUME_TASK('mytask'); L_status := DBMS_PARALLEL_EXECUTE.TASK_STATUS('mytask'); END LOOP; -- Done with processing; drop the task DBMS_PARALLEL_EXECUTE.DROP_TASK('mytask'); end; / Executing Chunks in an User-defined Framework You can execute chunks in a self-defined framework without using the RUN_TASK Procedure . This example shows how to use GET_ROWID_CHUNK Procedure , EXECUTE IMMEDIATE , SET_CHUNK_STATUS Procedure to execute the chunks. DECLARE l_sql_stmt varchar2(1000); l_try number; l_status number; l_chunk_id number; l_start_rowid rowid; l_end_rowid rowid; l_any_rows boolean; CURSOR c1 IS SELECT chunk_id FROM user_parallel_execute_chunks WHERE task_name = 'mytask' AND STATUS IN (DBMS_PARALLEL_EXECUTE.PROCESSED_WITH_ERROR, DBMS_PARALLEL_EXECUTE.ASSIGNED); BEGIN -- Create the Objects, task, and chunk by ROWID DBMS_PARALLEL_EXECUTE.CREATE_TASK ('mytask'); DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_ROWID('mytask', 'HR', 'EMPLOYEES', true, 100); l_sql_stmt := 'update EMPLOYEES e SET e.salary = e.salary + 10 WHERE rowid BETWEEN :start_id AND :end_id'; -- Execute the DML in his own framework -- -- Process each chunk and commit. -- After processing one chunk, repeat this process until -- all the chunks are processed. -- <<main_processing>> LOOP -- -- Get a chunk to process; if there is nothing to process, then exit the -- loop; -- DBMS_PARALLEL_EXECUTE.GET_ROWID_CHUNK('mytask', l_chunk_id, l_start_rowid, l_end_rowid, l_any_rows); IF (l_any_rows = false) THEN EXIT; END IF; -- -- The chunk is specified by start_id and end_id. -- Bind the start_id and end_id and then execute it -- -- If no error occured, set the chunk status to PROCESSED. -- -- Catch any exception. If an exception occured, store the error num/msg -- into the chunk table and then continue to process the next chunk. -- BEGIN EXECUTE IMMEDIATE l_sql_stmt using l_start_rowid, l_end_rowid; DBMS_PARALLEL_EXECUTE.SET_CHUNK_STATUS('mytask',l_chunk_id, DBMS_PARALLEL_EXECUTE.PROCESSED); EXCEPTION WHEN OTHERS THEN DBMS_PARALLEL_EXECUTE.SET_CHUNK_STATUS('mytask', l_chunk_id, DBMS_PARALLEL_EXECUTE.PROCESSED_WITH_ERROR, SQLCODE, SQLERRM); END; -- -- Finished processing one chunk; Commit here -- COMMIT; END LOOP;