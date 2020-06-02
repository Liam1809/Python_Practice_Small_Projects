# Veneer
# Here at Veneer we strive to provide the best marketplace experience to connect vetted art dealers with premium galleries. Create a marketplace for people and organizations to buy and sell pieces of art!

# In this project we’ll be developing classes and objects that represent the various responsibilities of art dealership software.

# Here at Veneer, our main concern is the buying and selling of priceless art works. Let’s start out by building a model for these works of art.

class Art():
  def __init__(self, artist, title, medium, year):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    
  def __repr__(self):
    return "{artist}. \"{title}\". {year}, {medium}.".format(artist = self.artist, title = self.title, year = self.year, medium = self.medium)

# Our first client wants to list a particular Picasso painting to make more space for her new fascination with Italian Futurism, so let’s see if we can use our data model for this piece:

# The artist is “Picasso, Pablo”.
# The work’s title is “Girl with a Mandolin (Fanny Tellier)”.
# The artwork was created in 1910.
# The medium is “oil on canvas”.
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910)
print(girl_with_mandolin)

# The Marketplace of Artistic Ideas



