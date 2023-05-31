; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"n" = alloca i32
  store i32 4, i32* %"n"
  %".3" = load i32, i32* %"n"
  %".4" = call i32 @"rip"(i32 %".3")
  store i32 %".4", i32* %"n"
  %".6" = load i32, i32* %"n"
  %".7" = bitcast [5 x i8]* @"fstr1" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".6")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define i32 @"rip"(i32 %".1")
{
entry:
  %"a" = alloca i32
  store i32 %".1", i32* %"a"
  %"r" = alloca i32
  store i32 2, i32* %"r"
  %".5" = load i32, i32* %"r"
  %".6" = load i32, i32* %"a"
  %".7" = mul i32 %".5", %".6"
  store i32 %".7", i32* %"r"
  %".9" = load i32, i32* %"r"
  ret i32 %".9"
}

@"fstr1" = internal constant [5 x i8] c"%i \0a\00"