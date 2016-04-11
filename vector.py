import math
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(Decimal(x) for x in coordinates)
            self.dimension = len(coordinates)
            self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def __add__(self, v):
        addition = [pair[0] + pair[1] for pair in zip(self.coordinates, v.coordinates)]
        return Vector(addition)
    
    def __sub__(self, v):
        difference = [pair[0] - pair[1] for pair in zip(self.coordinates, v.coordinates)]
        return Vector(difference)
    
    def dot(self, v):
        products = [pair[0] * pair[1] for pair in zip(self.coordinates, v.coordinates)]
        return sum(products)
    
    def times_scalar(self, c):
        scaled_coordinates = [ Decimal(c) * i for i in self.coordinates]
        return Vector(scaled_coordinates)
    
    def magnitude(self):
        accum = 0
        for i in self.coordinates:
            accum += i*i
        return Decimal(math.sqrt(accum))
    
    
    def normalize(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0')/magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
            
    def angle_with(self,v, radians=True):
        try:
            cos_of_angle = self.dot(v)/self.magnitude()/v.magnitude()
            angle_in_rad = math.acos(cos_of_angle)
            if radians:
                result = angle_in_rad
            else:
                result = math.degrees(angle_in_rad)
            return result
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute the angle with the zero vector')
            else:
                raise e

    def is_zero(self, tolerance = 1e-10):
        return self.magnitude() < tolerance
    
    def check_orthogonal(self, v, tolerance = 1e-10):
        return abs(self.dot(v)) <= tolerance

    
    def check_parallel(self, v):
        return self.is_zero() or v.is_zero() or self.angle_with(v) <= 0.0000001
 



print "quiz1"
a1 = Vector([8.218,-9.341])
a2 = Vector([-1.129,2.111]) 
s1 = Vector([7.119,8.215])
s2 = Vector([-8.223,0.878])
scalar1 = 7.41
m1 = Vector([1.671,-1.012,-0.318])

print a1 + a2
print s1 - s2
print m1.times_scalar(scalar1)

print "quiz2"
m1 = Vector([-0.221,7.437])
m2 = Vector([8.813,-1.331,-6.247])
n1 = Vector([5.581,-2.136])
n2 = Vector([1.996,3.108,-4.554])
print m1.magnitude()
print m2.magnitude()
print n1.normalize()
print n2.normalize()


print "quiz3"
m1a = Vector([7.887,4.138])
m1b = Vector([-8.802,6.776])
m2a = Vector([-5.955,-4.904,-1.874])
m2b = Vector([-4.496,-8.755,7.103])
print m1a.dot(m1b)
print m2a.dot(m2b)


ang1a = Vector([3.183,-7.627])
ang1b = Vector([-2.668,5.319])
ang2a = Vector([7.35,0.221,5.188])
ang2b = Vector([2.751,8.259,3.985])
ang3a = Vector([2,2])
ang3b = Vector([4,4])

print ang1a.angle_with(ang1b)
print ang2a.angle_with(ang2b, radians=False)
print ang3a.angle_with(ang3b, radians=True)


print "quiz4"
par_ort_1a = Vector([-7.579,-7.88])
par_ort_1b = Vector([22.737,23.64])
par_ort_2a = Vector([-2.029,9.97,4.172])
par_ort_2b = Vector([-9.231,-6.639,-7.245])
par_ort_3a = Vector([-2.328,-7.284,-1.214])
par_ort_3b = Vector([-1.821,1.072,-2.94])
par_ort_4a = Vector([2.118,4.827])
par_ort_4b = Vector([0,0])

print par_ort_1a.check_parallel(par_ort_1a),   \
      par_ort_1a.check_orthogonal(par_ort_1a), \
      par_ort_1a.angle_with(par_ort_1a, False)

print par_ort_1a.check_parallel(par_ort_2b),   \
      par_ort_1a.check_orthogonal(par_ort_2b), \
      par_ort_1a.angle_with(par_ort_2b, False)

print par_ort_3a.check_parallel(par_ort_3b),   \
      par_ort_3a.check_orthogonal(par_ort_3b), \
      par_ort_3a.angle_with(par_ort_3b, False)

print par_ort_4a.check_parallel(par_ort_4b),   \
      par_ort_4a.check_orthogonal(par_ort_4b), \
      #par_ort_4a.angle_with(par_ort_4b, False)




