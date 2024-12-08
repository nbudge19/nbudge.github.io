@echo off
@REM 启用延迟变量：在批处理文件中，在需要使用延迟变量的地方使用感叹号（!），而不是百分号（%）。
setlocal enabledelayedexpansion
@REM 取到今天的日期
set today=%date:~8,2%
set month=%date:~5,2%
set year=%date:~0,4%
@REM set year=2024
@REM set today=02
@REM set month=02

@REM 对月份和日进行去0操作；由于0开头的数字会被BAT认为是八进制的数字，所以需要使用set /a进行数值计算
if %month:~0,1%==0 set /a month=%month:~1,1%*1
if %today:~0,1%==0 set /a today=%today:~1,1%*1
@REM echo nowday=%year%-%month%-%today%

@REM 得到昨天的日期
set /A yesterday=%today%-1
@REM 判断昨天是否为月底，如果是则进行月份的调整
if %yesterday% neq 0 call :today1
if %yesterday% equ 0 call :today0
echo %dateago%

@REM pause

@REM 判断日计算结果为非0则直接返回
:today1
@REM 对月份和日进行补0
if %month% lss 10 set month=0%month%
if %yesterday% lss 10 set yesterday=0%yesterday%
@REM 对昨天的日期进行赋值
set dateago=%year%-%month%-%yesterday%
goto :EOF

@REM 判断日计算结果为0则月减；如果月为0则年减
:today0
set /A Oldmonth=%month%-1
@REM 判断每月的天数
for %%m in (1 3 5 7 8 10 12)do (
	if %Oldmonth%==%%m	(
		set yesterday=31
		)
	)
for %%n in (4 6 9 11) do (
	if %Oldmonth%==%%n (
		set yesterday=30
		)
	)
@REM 判断是否为闰年
if %Oldmonth% == 2 (
	set /A div4=%year% %% 4
	set /A div100=%year% %% 100
	set /A div400=%year% %% 400
	@REM echo div4=!div4!
	@REM echo div100=!div100!
	@REM echo div400=!div400!
	if !div4! equ 0 (
		if !div100! neq 0 (
			@REM echo %year% is runnian4
			set yesterday=29
			) else if !div400! equ 0 (
					@REM echo %year% is runnian400
					set yesterday=29
			)else (
				@REM echo %year% not runnian400
				set yesterday=28
			)
		) else (
			@REM echo %year% not runnian4
			set yesterday=28
		)
	)
@REM 当日为0时判断月份，1月的上个月为去年12月，则进行年减
if %Oldmonth% == 0 (
	set /A year=%year%-1
	set Oldmonth=12
	set yesterday=31
	)
@REM 对月份和日进行补0
if %Oldmonth% lss 10 set Oldmonth=0%Oldmonth%
if %yesterday% lss 10 set yesterday=0%yesterday%
@REM 对昨天的日期进行赋值
set dateago=%year%-%Oldmonth%-%yesterday%
goto :EOF




