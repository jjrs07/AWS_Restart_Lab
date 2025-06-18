SELECT 
Name, 
Capital, 
Region, 
SurfaceArea AS "Surface Area",
Population 
from world.country 
WHERE Population > 50000000 
AND Region = "Southern Europe";