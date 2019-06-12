@echo off

FOR /L %%I IN (1,1,10) do (
	echo When, in disgrace with fortune and men's eyes, > test%%I.txt
	echo I all alone beweep my outcast state, >> test%%I.txt
	echo And trouble deaf heaven with my bootless cries, >> test%%I.txt
	echo And look upon myself and curse my fate, >> test%%I.txt
	echo In the year 1991, when Windows was on the pinnacle came Linux to mankind. >> test%%I.txt
)
pause

