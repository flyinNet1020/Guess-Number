import random
print ('嗨! 我們來玩猜數字吧！')
start = input('請輸入數字範圍的最小值:')
end = input('請輸入數字範圍的最大值:')
start = int(start)
end = int(end)
r = random.randint(start, end) # Generate a random number
n = 1

while True:
	print('第', n, '次嘗試')
	guess_N = input ('請猜一個數字:')
	guess_N = int(guess_N)
	n += 1
	if r < guess_N:
		print('Oh~你猜錯了，答案比', guess_N, '要小')
	elif r > guess_N:
		print('Oh~你猜錯了，答案比', guess_N, '要大')
	else:
		print('哈！ 你猜對了，恭喜！ 答案就是', guess_N)
		break