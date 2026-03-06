---
id: 19c__UTL_NLA.LAPACK_GELS
name: UTL_NLA.LAPACK_GELS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_GELS

This procedure solves overdetermined or underdetermined real linear systems involving an m by n matrix A , or its transpose, using a QR or LQ factorization of A . It is assumed that A has full rank.

## Syntax

```sql
minimize || B - A*X ||
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| trans |  |  | CHARACTER = 'N' : The linear system involves A . CHARACTER = 'T' : The linear system involves A**T . |
| m |  |  | The number of rows of the matrix a. M >= 0 . |
| n |  |  | The number of columns of the matrix a. N >= 0 . |
| nrhs |  |  | The number of right-hand sides, which is the number of columns of the matrix b and x.nrhs >= 0 . |
| a |  |  | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (lda, n) . On entry, the matrix b of right hand side vectors, stored columnwise; b is m by nrhs if TRANS = 'N' , or n by nrhs if trans = 'T' . On exit, if m >= n , a is overwritten by details of its QR factorization as returned by SGEQRF . If m < n , A is overwritten by details of its LQ factorization as returned by SGELQF . |
| lda |  |  | The leading dimension of the array A . lda >= max(1,m) . |
| b |  |  | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldb, nrhs) . On entry, the matrix b of right hand side vectors, stored columnwise. b is m bynrhs if trans = 'n' , or n by nrhs if trans = 'T' . On exit, b is overwritten by the solution vectors, stored columnwise: If trans = 'n' and m >= n , rows 1 to n of b contain the least squares solution vectors; the residual sum of squares for the solution in each column is given by the sum of squares of elements n+1 to m in that column. If trans = 'n' and m < n , rows 1 to n of b contain the minimum norm solution vectors. If trans = 'T' and m >= n , rows 1 to m of b contain the minimum norm solution vectors. If trans = 'T' and m < n , rows 1 to m of b contain the least squares solution vectors; the residual sum of squares for the solution in each column is given by the sum of squares of elements m+1 to n in that column. |
| ldb |  |  | The leading dimension of the array b . ldb >= max(1,m,n) |
| info |  |  | = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value |
| pack |  |  | (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major |

## Usage Notes

The following options are provided: If TRANS = 'N' and m >= n : find the least squares solution of an overdetermined system, that is, solve the least squares problem. minimize || B - A*X || If TRANS = 'N' and m < n : find the minimum norm solution of an underdetermined system A * X = B . If TRANS = 'T' and m >= n : find the minimum norm solution of an undetermined system A**T * X = B . If TRANS = 'T' and m < n : find the least squares solution of an overdetermined system, that is, solve the least squares problem minimize || B - A**T * X || . See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_GELS ( trans IN flag, m IN POSITIVEN, n IN POSITIVEN, nrhs IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, b IN OUT UTL_NLA_ARRAY_DBL, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_GELS ( trans IN flag, m IN POSITIVEN, n IN POSITIVEN, nrhs IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, b IN OUT UTL_NLA_ARRAY_FLT, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-41 LAPACK_GELS Procedure Parameters Parameter Description trans CHARACTER = 'N' : The linear system involves A . CHARACTER = 'T' : The linear system involves A**T . m The number of rows of the matrix a. M >= 0 . n The number of columns of the matrix a. N >= 0 . nrhs The number of right-hand sides, which is the number of columns of the matrix b and x.nrhs >= 0 . a UTL_NLA_ARRAY_FLT / DBL, DIMENSION (lda, n) . On entry, the matrix b of right hand side vectors, stored columnwise; b is m by nrhs if TRANS = 'N' , or n by nrhs if trans = 'T' . On exit, if m >= n , a is overwritten by details of its QR factorization as returned by SGEQRF . If m < n , A is overwritten by details of its LQ factorization as returned by SGELQF . lda The leading dimension of the array A . lda >= max(1,m) . b UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldb, nrhs) . On entry, the matrix b of right hand side vectors, stored columnwise. b is m bynrhs if trans = 'n' , or n by nrhs if trans = 'T' . On exit, b is overwritten by the solution vectors, stored columnwise: If trans = 'n' and m >= n , rows 1 to n of b contain the least squares solution vectors; the residual sum of squares for the solution in each column is given by the sum of squares of elements n+1 to m in that column. If trans = 'n' and m < n , rows 1 to n of b contain the minimum norm solution vectors. If trans = 'T' and m >= n , rows 1 to m of b contain the minimum norm solution vectors. If trans = 'T' and m < n , rows 1 to m of b contain the least squares solution vectors; the residual sum of squares for the solution in each column is given by the sum of squares of elements m+1 to n in that column. ldb The leading dimension of the array b . ldb >= max(1,m,n) info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value pack (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major