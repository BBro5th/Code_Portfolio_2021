@i
M=0
(LOOP)
//am i done?
@i
D=M
@R0
D=D-M
@END
D;JEQ
//Do Stuff in loop
@i
M=M+1
//JUMP TO LOOP
@LOOP
0;JMP

(END)
@END0
0;JMP