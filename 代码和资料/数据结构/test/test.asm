section .data
    helloMessage db "Hello, World!", 0

section .text
    extern GetStdHandle
    extern WriteConsoleA
    extern ExitProcess

    global _start

_start:
    ; 获取stdout的句柄
    mov ecx, -11            ; STD_OUTPUT_HANDLE is -11
    call GetStdHandle
    mov rdi, rax            ; 将句柄保存在rdi中

    ; 写入控制台
    mov rdx, rsp            ; 使用rsp来临时存储pNumberOfBytesWritten
    sub rsp, 8              ; 为pNumberOfBytesWritten预留空间
    mov rsi, helloMessage   ; 要打印的消息
    mov r8d, 13             ; 消息长度
    push 0                  ; bAbortOnError
    push r8                ; nNumberOfCharsToWrite
    push rsi                ; lpBuffer
    push rdi                ; hConsoleOutput
    call WriteConsoleA
    add rsp, 8              ; 恢复rsp

    ; 退出
    mov ecx, 0              ; uExitCode
    call ExitProcess
