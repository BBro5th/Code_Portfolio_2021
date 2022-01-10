//IF sum < 0 GOTTO END
@sum
D=M
@IF
D;JLT
@ELSE
0;JMP
(IF)
@sum
D=0
M=D
@END
0;JMP
(ELSE)
@sum
M=1
(END)
	@END
	0;JMP
	
// @sum\D=M\@True\D;JLT\@sum\M=1\@sum\M=0\@END\0;JMP\