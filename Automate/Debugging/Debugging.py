import traceback

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol needs to single char string")
    if (width < 2) or (height < 2):
        raise Exception("Width and height must be 2 or greater")
    print(symbol * width)
    for i in range(height - 2): 
        print(symbol + (" " * (width - 2)) + symbol)
    print(symbol * width)
    
market_2nd = {"ns": "green", "ew": "red"}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == "green":
           intersection[key] = "yellow"
        elif intersection[key] == "yellow":
            intersection[key] = "red"
        elif intersection[key] == "red":
            intersection[key] = "green"
    assert "red" in intersection.values(), "All lights have to be red"



switchLights(market_2nd)