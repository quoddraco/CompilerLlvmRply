; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"t" = alloca i32
  store i32 10, i32* %"t"
  %"e" = alloca i32
  store i32 12, i32* %"e"
  %".4" = load i32, i32* %"t"
  store i32 %".4", i32* %"e"
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define void @"zalupa"()
{
entry:
  %"q" = alloca i32
  store i32 10, i32* %"q"
  %".3" = load i32, i32* %"q"
  ret void
}
