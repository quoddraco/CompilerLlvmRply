; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"t" = alloca i32
  store i32 10, i32* %"t"
  %".3" = load i32, i32* %"t"
  %".4" = add i32 %".3", 1
  store i32 %".4", i32* %"t"
  br label %"w_cond_head"
w_cond_head:
  %".7" = load i32, i32* %"t"
  %".8" = icmp slt i32 %".7", 10
  br i1 %".8", label %"w_body", label %"w_after"
w_body:
  %".10" = load i32, i32* %"t"
  %".11" = add i32 %".10", 1
  store i32 %".11", i32* %"t"
  %".13" = load i32, i32* %"t"
  %".14" = icmp slt i32 %".13", 10
  br i1 %".14", label %"w_body", label %"w_after"
w_after:
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define void @"zalupa"()
{
entry:
  %"q" = alloca i32
  store i32 10, i32* %"q"
  br label %"w_cond_head"
w_cond_head:
  %".4" = load i32, i32* %"q"
  %".5" = icmp slt i32 %".4", 20
  br i1 %".5", label %"w_body", label %"w_after"
w_body:
  %".7" = load i32, i32* %"q"
  %".8" = add i32 1, %".7"
  store i32 %".8", i32* %"q"
  %".10" = load i32, i32* %"q"
  %".11" = icmp slt i32 %".10", 20
  br i1 %".11", label %"w_body", label %"w_after"
w_after:
  %"e" = alloca i32
  store i32 10, i32* %"e"
  ret void
}
