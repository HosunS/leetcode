[200~class Solution:
      def maximumSwap(self, num: int) -> int:
          '''
                  iterate through each integer in the number
                          '''
          num = [int(i) for i in str(num)]

          for i in range(len(num) - 1):
              maxNum = max(num[i+1:])

              if num[i] < maxNum:
                  for j in range(len(num)-1 , i , -1):
                      if num[j] == maxNum :
                          break
                  num[i], num[j] = num[j], num[i]
                  break

          return int("".join([str(i) for i in num]))

          


              
