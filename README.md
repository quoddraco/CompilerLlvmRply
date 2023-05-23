
### A simple python compiler using the llvm and rply libraries.
    This compiler is a term paper of the 3rd year Information Security at VLSU.
    This project is still under construction.
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
    █░██░██░██░██░██░██░██░██░██░░░░░░░░░░█
    █░██░██░██░██░██░██░██░██░██░░░░░░░░░░█
    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░█░░░░█▀▀▀█░█▀▀█░█▀▀▄░▀█▀░█▄░░█░█▀▀█░░
    ░░█░░░░█░░░█░█▄▄█░█░░█░░█░░█░█░█░█░▄▄░░
    ░░█▄▄█░█▄▄▄█░█░░█░█▄▄▀░▄█▄░█░░▀█░█▄▄█░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

### How to use it:
    git clone
    pip install -r requirements.txt
    python main.py
    
### Simple Example LLVM Code
    ; ModuleID = '<string>'
    source_filename = "<string>"
    target triple = "x86_64-unknown-linux-gnu"

    @fstr1 = internal constant [5 x i8] c"%i \0A\00"

    ; Function Attrs: nofree nounwind
    define void @main() local_unnamed_addr #0 {
    entry:
      %.10 = tail call i32 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([5 x i8], [5 x i8]* @fstr1, i64 0, i64 0), i32 0)
      ret void
    }

    ; Function Attrs: nofree nounwind
    declare i32 @printf(i8* nocapture readonly, ...) local_unnamed_addr #0

    attributes #0 = { nofree nounwind }
### Assembler
      .text
      .file	"<string>"
      .globl	main
      .p2align	4, 0x90
      .type	main,@function
    main:
      movl	$fstr1, %edi
      xorl	%esi, %esi
      xorl	%eax, %eax
      jmp	printf
    .Lfunc_end0:
      .size	main, .Lfunc_end0-main

      .type	fstr1,@object
      .section	.rodata,"a",@progbits
    fstr1:
      .asciz	"%i \n"
      .size	fstr1, 5

      .section	".note.GNU-stack","",@progbits
