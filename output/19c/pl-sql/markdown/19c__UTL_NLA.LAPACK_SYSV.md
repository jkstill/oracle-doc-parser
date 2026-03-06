---
id: 19c__UTL_NLA.LAPACK_SYSV
name: UTL_NLA.LAPACK_SYSV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_SYSV

This procedure computes the solution to a real system of linear equations a * x = b , where a is an n by n symmetric matrix, and x and b are n by nrhs matrices.

## Syntax

```sql
UTL_NLA.LAPACK_SYSV (
   uplo    IN      flag,
   n       IN      POSITIVEN,
   nrhs    IN      POSITIVEN,
   a       IN OUT  UTL_NLA_ARRAY_DBL,
   lda     IN      POSITIVEN,
   ipiv    IN OUT  UTL_NLA_ARRAY_INT,
   b       IN OUT  UTL_NLA_ARRAY_DBL,
   ldb     IN      POSITIVEN,
   info    OUT     INTEGER,
   pack    IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uplo | flag | IN | uplo = 'U' . Upper triangular of A is stored. uplo = 'L' . Lower triangular of A is stored. |
| n | POSITIVEN | IN | The number of linear equations, which is the order of the matrix a. N >= 0 . |
| nrhs | POSITIVEN | IN | The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . |
| a | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n-1) . On entry, the symmetric matrix a . If UPLO = 'U' , the leading n by n upper triangular part of a contains the upper triangular part of the matrix a , and the strictly lower triangular part of a is not referenced. If uplo = 'L' , the leading n by n lower triangular part of a contains the lower triangular part of the matrix a , and the strictly upper triangular part of a is not referenced. On exit, if info = 0, the block diagonal matrix d and the multipliers used to obtain the factor U or L from the factorization A = U*D*U**T or A = L*D*L**T as computed by SSYTRF . |
| lda | POSITIVEN | IN | The leading dimension of the array a . lda >= max(1,n) |
| ipiv | UTL_NLA_ARRAY_INT | IN OUT | INTEGER array , DIMENSION (ldb, nrhs) . Details of the interchanges and the block structure of d , as determined by SSYTRF . If ipiv(k) > 0 , then rows and columns k and ipiv(k) were interchanged, and d(k,k) is a 1 by1 diagonal block. If uplo = 'U' and ipiv(k) = ipiv(k-1) < 0 , then rows and columns k-1 and -ipiv(k) were interchanged and d(k-1:k,k-1:k) is a 2 by 2 diagonal block. If uplo = 'L' and ipiv(k) = ipiv(k+1) < 0, then rows and columns k+1 and -ipiv(k) were interchanged and d(k:k+1,k:k+1) is a 2 by 2 diagonal block. |
| b | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldb, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . |
| ldb | POSITIVEN | IN | The leading dimension of the array b . ldb >= max(1,n) |
| info | INTEGER | OUT | = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i, d(i,i) is exactly zero. The factorization has been completed, but the block diagonal matrix d is exactly singular, so the solution could not be computed. |
| pack | flag | IN | (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major |

## Usage Notes

The diagonal pivoting method is used to factor A as A = U * D * U**T , if UPLO = 'U' or A = L * D * L**T , if UPLO = 'L' where U (or L ) is a product of permutation and unit upper (lower) triangular matrices, and D is symmetric and block diagonal with 1 by 1 and 2 by 2 diagonal blocks. The factored form of A is then used to solve the system of equations A * X = B. See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_SYSV ( uplo IN flag, n IN POSITIVEN, nrhs IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, ipiv IN OUT UTL_NLA_ARRAY_INT, b IN OUT UTL_NLA_ARRAY_DBL, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_SYSV ( uplo IN flag, n IN POSITIVEN, nrhs IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, ipiv IN OUT UTL_NLA_ARRAY_INT, b IN OUT UTL_NLA_ARRAY_FLT, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-60 LAPACK_SYSV Procedure Parameters Parameter Description uplo uplo = 'U' . Upper triangular of A is stored. uplo = 'L' . Lower triangular of A is stored. n The number of linear equations, which is the order of the matrix a. N >= 0 . nrhs The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . a UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n-1) . On entry, the symmetric matrix a . If UPLO = 'U' , the leading n by n upper triangular part of a contains the upper triangular part of the matrix a , and the strictly lower triangular part of a is not referenced. If uplo = 'L' , the leading n by n lower triangular part of a contains the lower triangular part of the matrix a , and the strictly upper triangular part of a is not referenced. On exit, if info = 0, the block diagonal matrix d and the multipliers used to obtain the factor U or L from the factorization A = U*D*U**T or A = L*D*L**T as computed by SSYTRF . lda The leading dimension of the array a . lda >= max(1,n) ipiv INTEGER array , DIMENSION (ldb, nrhs) . Details of the interchanges and the block structure of d , as determined by SSYTRF . If ipiv(k) > 0 , then rows and columns k and ipiv(k) were interchanged, and d(k,k) is a 1 by1 diagonal block. If uplo = 'U' and ipiv(k) = ipiv(k-1) < 0 , then rows and columns k-1 and -ipiv(k) were interchanged and d(k-1:k,k-1:k) is a 2 by 2 diagonal block. If uplo = 'L' and ipiv(k) = ipiv(k+1) < 0, then rows and columns k+1 and -ipiv(k) were interchanged and d(k:k+1,k:k+1) is a 2 by 2 diagonal block. b UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldb, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . ldb The leading dimension of the array b . ldb >= max(1,n) info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i, d(i,i) is exactly zero. The factorization has been completed, but the block diagonal matrix d is exactly singular, so the solution could not be computed. pack (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major