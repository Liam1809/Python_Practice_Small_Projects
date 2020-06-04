# Veneer
# Here at Veneer we strive to provide the best marketplace experience to connect vetted art dealers with premium galleries. Create a marketplace for people and organizations to buy and sell pieces of art!

# In this project we’ll be developing classes and objects that represent the various responsibilities of art dealership software.

# Here at Veneer, our main concern is the buying and selling of priceless art works. Let’s start out by building a model for these works of art.
class Art():
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  def __repr__(self):
    return "{artist}. \"{title}\". {year}, {medium}. {owner_name}, {owner_location}.".format(artist = self.artist, title = self.title, year = self.year, medium = self.medium, owner_name = self.owner.name, owner_location = self.owner.location)

class Marketplace():
  def __init__(self):
    self.listings =[]
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  def remove_listing(self, new_listing):
    self.listings.remove(new_listing)
  def show_listings(self):
    for listing in self.listings:
      print(listing)

class Client():
  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum
    if location:
      self.location = location
    else:
      self.location = "Private Collection"
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        art_listing = listing
      if art_listing != None:
        artwork.owner = self
        veneer.remove_listing(art_listing)

class Listing():
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return "\"{art_name} : {price}\"".format(art_name = self.art, price = self.price)

# Let’s see how our Art class looks, create a new work of art. Our first client wants to list a particular Picasso painting to make more space for her new fascination with Italian Futurism, so let’s see if we can use our data model for this piece:

# The artist is “Picasso, Pablo”.
# The work’s title is “Girl with a Mandolin (Fanny Tellier)”.
# The artwork was created in 1910.
# The medium is “oil on canvas”.
# girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910)
# print(girl_with_mandolin)

# Create our main marketplace by instantiating Marketplace and saving it into the variable veneer.
veneer = Marketplace()
# print(veneer.show_listings())

# first Client: her name is Edytta Halpirt and she is a collector and not a museum.
edytta = Client("Edytta Halpirt", None, False)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)
print(girl_with_mandolin)

# second Client: 
# let’s create a second Client with the following information:

# It’s name is “The MOMA”
# It is located in “New York”
# It is a museum.
moma = Client("The MOMA", "New York", True)

edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")
veneer.show_listings()

# the MOMA is very interestd in purchasing girl_with_mandolin
moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)
print(veneer.show_listings())