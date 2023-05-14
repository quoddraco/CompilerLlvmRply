; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"e" = alloca i32
  store i32 6, i32* %"e"
  %".3" = load i32, i32* %"e"
  %".4" = bitcast [5 x i8]* @"fstr1" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %".3")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr1" = internal constant [5 x i8] c"%i \0a\00"
define void @"rip"()
{
entry:
  ret void
}

define void @"sperm"()
{
entry:
  ret void
}
