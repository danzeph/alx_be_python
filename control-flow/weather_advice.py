weather = input("What's the weather like today? (sunny/rainy/cold): ")

clothing = None
if(weather == "sunny"):
    clothing = "Wear a t-shirt and sunglasses."
elif (weather == "rainy"):
    clothig = "Dont forget your umbrella and a scarf."
elif (weather == "cold"):
    clothing = "Make sure to wear a warm coat and a scarf."
else:
    print("Sorry, I don't have recommendations for this weather.")

if clothing is not None:
    print(clothing)

   

