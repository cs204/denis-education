import sm

print("Часть 1.")

class SumTSM(sm.SM):
	def __init__(self):
		self.startState = 0

	def getNextValues(self,state,inp):
		return (state + inp, state + inp)

	def done(self,state):
		return state > 100

#Для проверки раскомментируйте следующие 2 сторки
s = SumTSM()
print(s.transduce(range(20)))

#Правильный вывод
#[0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105]
#--------------------------------------
print("Часть 2. Повторяет SumTSM 4 раза.")
# Создайте автомат fourTimes, который повторяет SumTSM четыре раза и затем завершается.
fourTimes = sm.Repeat(s,4)

#Для проверки раскомментируйте следующию сторку
print(fourTimes.transduce(range(200)))
#-----------------------------------------------
print("Часть 3. Считающий автомат.")

class CountUpTo(sm.SM):
	def __init__(self,num):
		self.startState = 0
		self.endState = num
	def getNextValues(self,state,inp):
		return (state + 1, state + 1)
	def done(self,state):
		return state >= self.endState


#Для проверки раскомментируйте следующие 2 сторки
m = CountUpTo(3)
print(m.run(20))

# правильный вывод
#[1, 2, 3]
#---------------------------------------
print("Часть 4. Несколько считающих машин.")

def makeSequenceCounter(nList):
	smSequence = []
	for num in nList:
		smSequence.append(CountUpTo(num))
	return sm.Sequence(smSequence)

#Для проверки раскомментируйте следующию сторку
print(makeSequenceCounter([2, 5, 3]).run(20))

#правильны вывод [1, 2, 1, 2, 3, 4, 5, 1, 2, 3 ]

