---
id: 19c__UTL_NLA.LAPACK_GESV
name: UTL_NLA.LAPACK_GESV
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_GESV

This procedure computes the solution to a real system of linear equations a * x = b , where a is an n by n matrix and x and b are n by nrhs matrices.

## Syntax

```sql
a = P * L * U
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n |  |  | The number of linear equations, equivalent to the order of the matrix a . n >= 0 |
| nrhs |  |  | The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . |
| a |  |  | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (lda, n) . On entry, the n by n coefficient matrix a . On exit, the factors L and U from the factorization a = P*L*U ; the unit diagonal elements of L are not stored. |
| lda |  |  | The leading dimension of the array a. lda >= max(1,n) |
| ipiv |  |  | INTEGER array, DIMENSION (n) . The pivot indices that define the permutation matrix P ; row i of the matrix was interchanged with row ipiv(i) . |
| b |  |  | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldb, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . |
| ldb |  |  | The leading dimension of the array b . ldb >= max(1,n) |
| info |  |  | = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , U(i,i) is exactly zero. The factorization has been completed, but the factor U is exactly singular, so the solution could not be computed. |
| pack |  |  | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

The LU decomposition with partial pivoting and row interchanges is used to factor A as a = P * L * U where P is a permutation matrix, L is unit lower triangular, and U is upper triangular. The factored form of a is then used to solve the system of equations a * x = b See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_GESV ( n IN POSITIVEN, nrhs IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, ipiv IN OUT UTL_NLA_ARRAY_INT, b IN OUT UTL_NLA_ARRAY_DBL, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_GESV ( n IN POSITIVEN, nrhs IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, ipiv IN OUT UTL_NLA_ARRAY_INT, b IN OUT UTL_NLA_ARRAY_FLT, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-43 LAPACK_GESV Procedure Parameters Parameter Description n The number of linear equations, equivalent to the order of the matrix a . n >= 0 nrhs The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . a UTL_NLA_ARRAY_FLT / DBL, DIMENSION (lda, n) . On entry, the n by n coefficient matrix a . On exit, the factors L and U from the factorization a = P*L*U ; the unit diagonal elements of L are not stored. lda The leading dimension of the array a. lda >= max(1,n) ipiv INTEGER array, DIMENSION (n) . The pivot indices that define the permutation matrix P ; row i of the matrix was interchanged with row ipiv(i) . b UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldb, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . ldb The leading dimension of the array b . ldb >= max(1,n) info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , U(i,i) is exactly zero. The factorization has been completed, but the factor U is exactly singular, so the solution could not be computed. pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major