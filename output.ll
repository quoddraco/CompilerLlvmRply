; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"e" = alloca i32
  store i32 6, i32* %"e"
  br label %"w_cond_head"
w_cond_head:
  %".4" = load i32, i32* %"e"
  %".5" = icmp slt i32 %".4", 1000
  br i1 %".5", label %"w_body", label %"w_after"
w_body:
  %".7" = load i32, i32* %"e"
  %".8" = add i32 %".7", 1
  store i32 %".8", i32* %"e"
  %".10" = load i32, i32* %"e"
  %".11" = bitcast [5 x i8]* @"fstr1" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 %".10")
  %".13" = load i32, i32* %"e"
  %".14" = icmp slt i32 %".13", 1000
  br i1 %".14", label %"w_body", label %"w_after"
w_after:
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr1" = internal constant [5 x i8] c"%i \0a\00"