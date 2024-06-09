import time
import lgpio
import tm1637

DIO = 26
CLK = 11
tm = tm1637.TM1637(clk=CLK, dio=DIO)
tm.brightness(2)

def display_digits(input):
	tm.write(input)

def count_check():
	if count[3] == ints[9]:

		if count[2] == ints[9]:
			
			if count[1] == ints[9]:
				count[0] = ints[count[0][0] + 1]
				count[1] = ints[0]
			else:
				count[1] = ints[count[1][0] + 1]
				count[2] = ints[0] 
		
		else:
			count[2] = ints[count[2][0] + 1]
			count[3] = ints[0]
	else:
		count[3] = ints[count[3][0] + 1]


ints = [[0, 0X3F], [1, 0X06], [2, 0X5B], [3, 0X4F], [4, 0X66], [5, 0X6D], [6, 0X7D], [7, 0X07], [8, 0X7F], [9, 0X6F]]

count = [ints[9], ints[9], ints[9], ints[9]]

while True:
	# time.sleep(1)
	print(count)
	if count == [ints[9], ints[9], ints[9], ints[9]]:
		count = [ints[0], ints[0], ints[0], ints[0]] 
		display_digits([count[0][1], count[1][1], count[2][1], count[3][1]])
		continue
	
	count_check()
		
	display_digits([count[0][1], count[1][1], count[2][1], count[3][1]])

