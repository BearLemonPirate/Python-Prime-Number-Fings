#Generates prime numbers with set perameters and gives options for final result
def PrimeNumGenerator():

    #gets settings for generator
    PrimeNumberGenerationMethod = input ("What generation setting would you like?")

    if PrimeNumberGenerationMethod == "1":
        TotalPrimesInput = input("Please input value for total number of primes (between 0 and xxxxx)")
        PrimeNumberGeneratorTotalPrimes()
    
    elif PrimeNumberGenerationMethod == "2":
        lol = 1

    else:
        lol = 1

    #Standard function to generate each prime number
    def GenerateNextPrimeInSequence (PreviousPrime):
        if PreviousPrime == (0 or 1):
            return PreviousPrime
        else:
            TestingNumber = PreviousPrime + 1
            NextPrimeOutput = 0

            while NextPrimeOutput == 0:
                for x in range(2, TestingNumber):

                    #if number can be divided by factor with no remainder, move to next number
                    if TestingNumber%x.is_integer() == True:
                        TestingNumber = TestingNumber + 1
                    else:
                        pass

        

    #func1
    def PrimeNumberGeneratorTotalPrimes (TotalPrimes):
        FuncOutput = [0]
        while FuncOutput < TotalPrimes:
            lol = 1


    #func2
    def PrimeNumberGeneratorWithinRange(MinRange, MaxRange):
        lol = 1