# Lab 6: Composite Data Types – Car Fleet Inventory

This lab introduces you to composite data types in Python — specifically **dictionaries**, **lists**, and **CSV parsing**.

You’ll be working with a file named `car_fleet.csv` to build a **list of dictionaries** that represent vehicles in a fleet. Each row from the CSV file becomes a dictionary that stores properties like `vin`, `make`, `model`, `year`, and more.

---

## What You'll Learn

- How to define a dictionary template (`myVehicle`)  
- How to read data from a `.csv` file using `csv.reader()`  
- How to store each car as a **dictionary** in a list  
- How to **deep copy** template data to avoid reference issues  
- How to loop through and display all vehicle details

---

## Input File: `car_fleet.csv`

Make sure your `car_fleet.csv` file is in the same folder as this script.  
It should contain data in the following format:

## Sample Output  

vin :   
make :   
model : 
year : 0  
range : 0  
topSpeed : 0  
zeroSixty : 0.0  
mileage : 0  
Column names are: vin, make, model, year, range, topSpeed, zeroSixty, mileage  
vin: TMX20122 make: AnyCompany Motors, model:  Coupe, year:  2012, range:  335, topSpeed:  155, zeroSixty:  4.1, mileage:  50000  
vin: TM320163 make: AnyCompany Motors, model:  Sedan, year:  2016, range:  240, topSpeed:  140, zeroSixty:  5.2, mileage:  20000  
vin: TMX20121 make: AnyCompany Motors, model:  SUV, year:  2012, range:  295, topSpeed:  155, zeroSixty:  4.7, mileage:  100000  
vin: TMX20204 make: AnyCompany Motors, model:  Truck, year:  2020, range:  300, topSpeed:  155, zeroSixty:  3.5, mileage:  0  
Processed 5 lines.  
vin : TMX20122  
make : AnyCompany Motors  
model :  Coupe  
year :  2012  
range :  335  
topSpeed :  155  
zeroSixty :  4.1  
mileage :  50000  
vin : TM320163  
make : AnyCompany Motors  
model :  Sedan  
year :  2016  
range :  240  
topSpeed :  140  
zeroSixty :  5.2  
mileage :  20000  
vin : TMX20121  
make : AnyCompany Motors  
model :  SUV  
year :  2012  
range :  295  
topSpeed :  155  
zeroSixty :  4.7  
mileage :  100000  
vin : TMX20204  
make : AnyCompany Motors  
model :  Truck  
year :  2020  
range :  300  
topSpeed :  155  
zeroSixty :  3.5  
mileage :  0
