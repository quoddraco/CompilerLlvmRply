; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"t" = alloca i32
  store i32 10, i32* %"t"
  br label %"w_cond_head"
w_cond_head:
  %".4" = load i32, i32* %"t"
  %".5" = icmp slt i32 %".4", 1000
  br i1 %".5", label %"w_body", label %"w_after"
w_body:
  %".7" = load i32, i32* %"t"
  %".8" = call i32 @"rip"(i32 %".7")
  store i32 %".8", i32* %"t"
  %".10" = load i32, i32* %"t"
  %".11" = icmp slt i32 %".10", 1000
  br i1 %".11", label %"w_body", label %"w_after"
w_after:
  %".13" = load i32, i32* %"t"
  %".14" = bitcast [5 x i8]* @"fstr1" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i32 %".13")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define i32 @"rip"(i32 %".1")
{
entry:
  %"t" = alloca i32
  store i32 %".1", i32* %"t"
  %".4" = load i32, i32* %"t"
  %".5" = add i32 %".4", 1
  store i32 %".5", i32* %"t"
  %".7" = load i32, i32* %"t"
  ret i32 %".7"
}

@"fstr1" = internal constant [5 x i8] c"%i \0a\00"