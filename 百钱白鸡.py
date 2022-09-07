"""
白钱白鸡
Version: 0.1
Authoer: Taichi
"""

# **百钱百鸡**问题：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100元买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for x in range(21):
  for y in range(34):
    z = 100 - x - y
    if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
      print('公鸡:',x,'母鸡:',y,'小鸡:',z)
