---
id: 19c__UTL_NLA.LAPACK_POSV
name: UTL_NLA.LAPACK_POSV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_POSV

This procedure computes the solution to a real system of linear equations a * x = b , where a is an n by n symmetric positive definite matrix and x and b are n by nrhs matrices.

## Syntax

```sql
UTL_NLA.LAPACK_POSV (
   uplo      IN      flag,
   n         IN      POSITIVEN,
   nrhs      IN      POSITIVEN,
   a         IN OUT  UTL_NLA_ARRAY_DBL,
   lda       IN      POSITIVEN,
   b         IN OUT  UTL_NLA_ARRAY_DBL,
   ldb       IN      POSITIVEN,
   info      OUT     INTEGER,
   pack      IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uplo | flag | IN | uplo = 'U'. Upper triangular of A is stored. uplo = 'L' . Lower triangular of A is stored. |
| n | POSITIVEN | IN | The number of linear equations, that is, the order of the matrix a . n >= 0 |
| nrhs | POSITIVEN | IN | The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . |
| a | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (lda, n) . If uplo = 'U' , the leading NRHS n by n upper triangular part of a contains the upper NRHS triangular part of the matrix A, and the strictly lower NRHS triangular part of A is not referenced. If uplo = ' 'L' , then rhs leading n by n lower triangular part of a contains the lower nrhs triangular part of the matrix a, and the strictly upper nrhs triangular part of a is not referenced. On exit, if info = 0, the factor U or L from the Cholesky factorization A = U**T*U or A = L*L**T . |
| lda | POSITIVEN | IN | The leading dimension of the array a. lda >= max (1, n) |
| b | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldb, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . |
| ldb | POSITIVEN | IN | The leading dimension of the array b. ldb >= max(1,n) |
| info | INTEGER | OUT | = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the leading minor of order i of a is not positive definite, so the factorization could not be completed, and the solution has not been computed. |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

The Cholesky decomposition is used to factor A as A = U**T* U if uplo = 'U' or A = L * L**T if UPLO = 'L' where U is an upper triangular matrix and L is a lower triangular matrix. The factored form of A is then used to solve the system of equations A * X = B . See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_POSV ( uplo IN flag, n IN POSITIVEN, nrhs IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, b IN OUT UTL_NLA_ARRAY_DBL, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_POSV ( uplo IN flag, n IN POSITIVEN, nrhs IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, b IN OUT UTL_NLA_ARRAY_FLT, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-48 LAPACK_POSV Procedure Parameters Parameter Description uplo uplo = 'U'. Upper triangular of A is stored. uplo = 'L' . Lower triangular of A is stored. n The number of linear equations, that is, the order of the matrix a . n >= 0 nrhs The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . a UTL_NLA_ARRAY_FLT / DBL, DIMENSION (lda, n) . If uplo = 'U' , the leading NRHS n by n upper triangular part of a contains the upper NRHS triangular part of the matrix A, and the strictly lower NRHS triangular part of A is not referenced. If uplo = ' 'L' , then rhs leading n by n lower triangular part of a contains the lower nrhs triangular part of the matrix a, and the strictly upper nrhs triangular part of a is not referenced. On exit, if info = 0, the factor U or L from the Cholesky factorization A = U**T*U or A = L*L**T . lda The leading dimension of the array a. lda >= max (1, n) b UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldb, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . ldb The leading dimension of the array b. ldb >= max(1,n) info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the leading minor of order i of a is not positive definite, so the factorization could not be completed, and the solution has not been computed. pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major