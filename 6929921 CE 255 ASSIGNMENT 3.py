#6929921
#ASANTE BIMPONG EUGENE
#COMPUTER APPLICATION ASSIGNMENT 3


Car =["Volkswagen","Bugatti Chiron","Bugatti Centodieci","Lamborghini Urus","Lamborghini Aventador","McLaren Artura","BMW i8","Toyota Land Cruiser Prado",
      "Ferrari SUV","Toyota Tundra","Porshe Cayenne","Toyota Rav4","Bentley Bentayga","Audi r8",
      "Maserati Ghibli","Jeep Wrangler","Chrysler 300","Dodge Durango","Lexus rx 350","Rolls Royce Ghost",
      "Mercedes Benz E-class","Infiniti QX60","GMC Terrain","Mitsubishi Outlander","Buick Envision","Honda Civic","Buick Encore","Buick Enclave","Rolls Royce Phantom",
      "Lexus lx 570"]
Models=["2010","2015","2018","2019","2020","2022","2023"]
Price=[5550000,720000,890000,970000,1020000,2408000,8705500]
CarModelPrice=[]
print("Welcome to Eugene's Luxirious Car Retail")
order=input("Which car would you like to buy?")
if order in Car:
   model=input("Please enter the model of the car you would like to buy.")
   if model in Models:
     if model=="2010":
      print("The price of the vehicle chosen is GHS",Price[0])
     elif model=="2015":
      print("The price of the vehicle chosen is GHS",Price[1])
     elif model=="2018":
      print("The price of the vehicle chosen is GHS",Price[2])
     elif model=="2019":
      print("The price of the vehicle chosen is GHS",Price[3])     
     elif model=="2020":
      print("The price of the vehicle chosen is GHS",Price[4])
     elif model=="2022":
      print("The price of the vehicle chosen is GHS",Price[5])
     elif model=="2023":
      print("The price of the vehicle chosen is GHS",Price[6])
   else:
     print("This model is not available")
else:
 print("This vehicle is not available")
 
      
    