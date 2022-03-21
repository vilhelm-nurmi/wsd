class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def distance_from(punkten, p2):
		return ((((p2.x - punkten.x)**2 + (p2.y - punkten.y)**2))**(1/2))
		
		
class Circle:
	def __init__(self, punkt, r):
		self.center = Point(punkt.x, punkt.y)
		self.radius = r
		
	def is_inside(cirkeln, ko):
		if cirkeln.center.distance_from(ko) < cirkeln.radius:
			return True
		else:
			return False