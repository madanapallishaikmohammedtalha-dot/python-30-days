#Exercise 1
class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        return(f"{self.name} say's woof!")

d1=Dog("Bruno", "Labrador")
print(d1.bark())
d2 =Dog("Max", "Beagle")
print(d2.bark())

#Exercise 2
class Book:
    def __init__(self,title, author, pages):
        self.title=title
        self.author=author
        self.pages=pages
    def summary(self):
        return(f"'{self.title}' by {self.author}, {self.pages} pages")
b1=Book("man","talha","1000")
print(b1.summary())

#Exercise 3
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return(f"Area:{3.14159*self.radius*self.radius}")
    def circumference(self):
        return(f"circumference:{2*3.14159*self.radius}")
c1=Circle(5)
print(c1.area())
print(c1.circumference())

#Exercise 4
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count
    
my_counter = Counter()
my_counter.increment()
my_counter.increment()
my_counter.increment()
print("Count after 3 increments:", my_counter.get_count())
my_counter.reset()
print("Count after reset:", my_counter.get_count())

#Exercise 5
class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        

        if 1900 <= year <= 2026:
            self.year = year
        else:
            print("Invalid year")
            self.year = 0
            
        if 0 <= rating <= 10:
            self.rating = rating
        else:
            print("Invalid rating")
            self.rating = 0

    def info(self):
        return f"{self.title} ({self.year}) — Rating: {self.rating}/10"

movie1 = Movie("Inception", 2010, 8.8)
movie2 = Movie("The Matrix", 1899, 8.7)
print(movie1.info())
print(movie2.info())