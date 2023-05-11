; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"e" = alloca i32
  store i32 6, i32* %"e"
  %"i" = alloca i32
  store i32 4, i32* %"i"
  %".4" = load i32, i32* %"i"
  %".5" = icmp eq i32 %".4", 3
  br i1 %".5", label %"if", label %"else"
if:
  store i32 7, i32* %"e"
  br label %"merge"
else:
  br label %"merge"
merge:
  %".10" = load i32, i32* %"e"
  %".11" = bitcast [5 x i8]* @"fstr1" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 %".10")
  %".13" = load i32, i32* %"i"
  %".14" = bitcast [5 x i8]* @"fstr2" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i32 %".13")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr1" = internal constant [5 x i8] c"%i \0a\00"
@"fstr2" = internal constant [5 x i8] c"%i \0a\00"