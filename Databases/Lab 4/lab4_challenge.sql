SELECT 
SUM(SurfaceArea) as "N. America Surface Area", 
SUM(Population) as "N. America Population" 
FROM world.country WHERE Region = "North America";