weather = input("What's the weather like today? (sunny/rainy/cold): ")

if(weather == "sunny"):
    clothing = "Wear a t-shirt and sunglasses."
elif (weather == "rainy"):
    clothig = "Dont forget your umbrella and a scarf."
elif (weather == "cold"):
    clothing = "Make sure to wear a warm coat and a scarf"
else:
    clothing = ("Sorry, I don't have recommendations for this weather.")

print(clothing)

   

