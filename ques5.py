def convert_temp():
    tf=eval(input("Enter a temperature in Fahrenheit: "))
    def celsius():
        tc = (5 / 9) * (tf - 32)
        return tc
    c=celsius()
    def convert_to_kelvin():
        tc = celsius()
        tk = tc + 273.15
        return tk
    tk=convert_to_kelvin()
    print("The temperature in Fahrenheit is:",tf)
    print("The temperature in celcius is:",c)
    print("The temperature in kelvin is:",tk)



convert_temp()