SELECT 
Region, 
Name, 
Population, 
RANK() OVER(partition by Region ORDER BY Population desc) as 'Ranked' 
FROM world.country order by Region, Ranked;