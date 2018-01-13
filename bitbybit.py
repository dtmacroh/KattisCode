#bitbybit


def main():
	over = False
	loop(over)

def loop(over):
	while not over:
		rounds = int(input())
		array = ["?"]*32
		if rounds ==0:
			over = True
			loop(over)
			break
		for i in range(0, rounds):
			inp = input().split()
			command = inp[0]
			resultBit = int(inp[1])
			if command=="SET":
				array[resultBit] = "1"
			elif command =="CLEAR":
				array[resultBit] = "0"
			elif command == "OR":
				bitCommanded = int(inp[2])
				if array[resultBit] == "1" or array[bitCommanded]=="1":
					array[resultBit] = "1"
				if array[resultBit] == "?" and array[bitCommanded]=="?":
					array[resultBit] = "?"
			elif command == "AND":
				bitCommanded = int(inp[2])
				#print("arrayBitComm {}".format(array[bitCommanded]))
				if array[resultBit] == "1" and array[bitCommanded]=="1":
					array[resultBit] = "1"
				if array[resultBit] == "?" or array[bitCommanded]=="?":
					array[resultBit] = "?"
				
		for i in range(31,-1,-1):
			print(array[i], end='')	
		print()		
			
			

main()
	
	
	
