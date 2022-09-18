from time import *
import random as rd
def calculate_mistakes(userinput,teststring):
    mismatches = 0
    length = min(len(userinput),len(teststring))
    for i in range(length):
        if userinput[i] != teststring[i]:
            mismatches+=1
    if len(teststring) > len(userinput):
        mismatches += len(teststring)-len(userinput)
    return mismatches

def speed_calculation(start_time,finish_time,userinput):
    total_time = finish_time-start_time
    total_time = round(total_time,2)
    speed = len(userinput)/total_time
    return round(speed,2)

    return 

para1 = "According to the creator Guido Van Rossum, the name of this language was derived from the British comedy series “Monty Python’s Flying Circus”. The comedy was aired on BBC during the 1970s and it gave the creator some form of entertainment during the language development."
para2 = "This one sounds interesting right. Believe it or not, in 2015, Python overtook French to be the most popular language that is taught in primary schools. Statistics revealed that 6 out of 10 parents preferred their children to learn Python instead of French. This just shows that many people appreciated the importance of Python programming."
para3 = "Do you know that Python is one of the official programming languages that are used at Google? The language has been part and parcel of Google thanks to its efficiency and portability. It is an easy language to use even when developing big and complex projects."
# para1 = 'abcde'
# para2 = 'bedfaddd'
# para3 = 'jjjjkdk'
test = [para1,para2,para3]
num = rd.randint(0,2)
teststring = test[num]
print("\n\n\t\t\t\t\t *** Typing speed test ***\n")
print(teststring)
start_time = time()
userinput = input("\n\t\t\t *** please type the given string as fast as possible ***\n\n\t *** Enter *** - ")
finish_time = time()
total_time = speed_calculation(start_time,finish_time,userinput)
print(f"\n\n\t\t\t\t *** words per minute - {round(total_time*60,2)} w/m ***")
print(f"\t\t\t\t *** words per second - {total_time} w/s ***")
mistakes = calculate_mistakes(userinput,teststring)
print(f"\t\t\t\t *** number of mistakes - {mistakes} ***")
print(f"\t\t\t\t *** accuracy - {round((len(teststring)-mistakes)/len(teststring)*100,2)} % ***")