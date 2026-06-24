class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer=[]
        for i in range(1,n+1):
            element=""
            if i%3 == 0 and i%5 == 0:
                element+="FizzBuzz"
            elif i%3 == 0:
                element+="Fizz"
            elif i%5 == 0:
                element+="Buzz" 
            else:
                element+=str(i)
            answer.append(element)
        return answer
