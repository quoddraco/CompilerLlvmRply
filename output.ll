; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"e" = alloca i32
  %".2" = add i32 8, 8
  store i32 %".2", i32* %"e"
  %".4" = load i32, i32* %"e"
  %".5" = bitcast [5 x i8]* @"fstr1" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 %".4")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define void @"zalupa"()
{
entry:
  %"r" = alloca i32
  store i32 10, i32* %"r"
  %"a" = alloca i32
  store i32 1, i32* %"a"
  ret void
}

define void @"penis"()
{
entry:
  %"r" = alloca i32
  store i32 11, i32* %"r"
  ret void
}

@"fstr1" = internal constant [5 x i8] c"%i \0a\00"