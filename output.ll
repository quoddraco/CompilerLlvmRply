; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"a" = alloca i8
  store i8 3, i8* %"a"
  %".3" = load i8, i8* %"a"
  %"e" = alloca i8
  store i8 6, i8* %"e"
  %".5" = load i8, i8* %"e"
  %".6" = load i8, i8* %"a"
  %".7" = load i8, i8* %"e"
  %".8" = add i8 %".6", %".7"
  %".9" = bitcast [5 x i8]* @"fstr" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i8 %".8")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr" = internal constant [5 x i8] c"%i \0a\00"