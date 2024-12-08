@echo off
rem 启用延迟变量：在批处理文件中，在需要使用延迟变量的地方使用感叹号（!），而不是百分号（%）。
setlocal enabledelayedexpansion
::取到今天的日期
set today=%date:~8,2%
set month=%date:~5,2%
set year=%date:~0,4%
rem set year=1704
rem set today=01
rem set month=12
::得到昨天的日期
if %month:~0,1%==0 set /a month=%month:~1,1%*1
if %today:~0,1%==0 set /a today=%today:~1,1%*1
rem echo nowday=%year%-%month%-%today%
set /A yesterday=%today%-1
if %yesterday% neq 0 call :today1
if %yesterday% equ 0 call :today0
echo %dateago%

::pause



:today1
if %month% lss 10 set month=0%month%
if %yesterday% lss 10 set yesterday=0%yesterday%
set dateago=%year%-%month%-%yesterday%
goto :EOF
::判断结果日为0则月减；如果月为0则年减
:today0
set /A Oldmonth=%month%-1
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
if %Oldmonth% == 0 (
	set /A year=%year%-1
	set Oldmonth=12
	set yesterday=31
	)
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
if %Oldmonth% lss 10 set Oldmonth=0%Oldmonth%
if %yesterday% lss 10 set yesterday=0%yesterday%
set dateago=%year%-%Oldmonth%-%yesterday%
goto :EOF




