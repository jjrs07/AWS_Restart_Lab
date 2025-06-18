SELECT 
Name, 
substring_index(Region, "/", 1) as "Region Name 1",
substring_index(region, "/", -1) as "Region Name 2" 
FROM world.country WHERE Region = "Micronesia/Caribbean";