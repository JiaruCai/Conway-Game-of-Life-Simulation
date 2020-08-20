import Conway 
import time
# test_obj = Conway.conway(5,5,False) #set to false so that later can be done by set cell
# print(test_obj.string())
# test_obj.setCell(3,2) #start fom horizontal 
# test_obj.setCell(3,3)
# test_obj.setCell(3,4) 
# print(test_obj.string())
# test_obj.tick() #only apply once conway rule
# print(test_obj.string()) 
# test_obj.tick() #only apply once conway rule
# print(test_obj.string()) 

def runTest(testname, boards):
  train_obj = Conway.conway(0,0, boards[0], True)
  # print(train_obj.string(1, False))
  generation_1_test = Conway.conway(0,0, boards[1], True)
  generation_2_test = Conway.conway(0,0, boards[2], True)
  train_obj.tick()
  if train_obj.string(1, False) == generation_1_test.string(1, False):
    print(testname + " Test 1 Passed")
  else:
    print(testname + " Test 1 Failed")
  train_obj.tick()
  #因为是个obeject oriented program,所以叫方程名即可
  if train_obj.string(1, False) == generation_2_test.string(1, False):
    print(testname + " Test 2 Passed")
  else:
    print(testname + " Test 2 Failed")
  

runTest("Still Lifes BeeHive", [
"""
      ,
  ██  ,
 █  █ ,
  ██  ,
      ,
""",
"""
      ,
  ██  ,
 █  █ ,
  ██  ,
      ,
""",
"""
      ,
  ██  ,
 █  █ ,
  ██  ,
      ,
"""])


runTest("Blinker", [
"""
     ,
     ,
 ███ ,
     ,
     ,
""",
"""
     ,
  █  ,
  █  ,
  █  ,
     ,
""",
"""
     ,
     ,
 ███ ,
     ,
     ,
"""])

runTest("Beacon", [
"""
      ,
 ██   ,
 ██   ,
   ██ ,
   ██ ,
      ,
""",
"""
      ,
 ██   ,
 █    ,
    █ ,
   ██ ,
      ,
""",
"""
      ,
 ██   ,
 ██   ,
   ██ ,
   ██ ,
      ,
"""])



