SUBROUTINE testfunc(x, y)
    IMPLICIT NONE

    !f2py threadsafe

    INTEGER, INTENT(IN) :: x
    INTEGER, INTENT(OUT) :: y

    y = x + 1

    RETURN

END SUBROUTINE testfunc
