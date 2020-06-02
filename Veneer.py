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
    return "{artist}. \"{title}\". {year}, {medium}. {owner_name}, {location}.".format(artist = self.artist, title = self.title, year = self.year, medium = self.medium, owner_name = self.owner.name, location = self.owner.location)

# Our first client wants to list a particular Picasso painting to make more space for her new fascination with Italian Futurism, so let’s see if we can use our data model for this piece:

# The artist is “Picasso, Pablo”.
# The work’s title is “Girl with a Mandolin (Fanny Tellier)”.
# The artwork was created in 1910.
# The medium is “oil on canvas”.
# girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910)
# print(girl_with_mandolin)

# The Marketplace of Artistic Ideas

# In order to buy and sell works of art, we need a marketplace that will maintain the responsibilities of buying, selling, listing, and delisting of those artworks.

class Marketplace():
  def __init__(self):
    self.listings = []

  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  
  def remove_listing(self,expired_listing):
    self.listings.remove(expired_listing)

  def show_listings(self):
    for listing in self.listings:
      print(listing)


veneer = Marketplace()

# print(veneer.show_listings())

# We Need Clients!

class Client():
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  
  def sell_artwork(self, artwork, price):
    if self == artwork.owner:
      New_listing = Listing(artwork, price, artwork.owner)
      veneer.add_listing(New_listing)

  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)

# first client
# Now instantiate our first Client: her name is Edytta Halpirt and she is a collector and not a museum.
edytta = Client("Edytta Halpirt", "Private Collection", False)

# Every purchase requires a buyer and a seller, let’s create a second Client with the following information:

# It’s name is “The MOMA”
# It is located in “New York”
# It is a museum.
moma = Client("The MOMA", "New York", True)

# Updating Our Art Class

# A full citation of a work of art necessarily includes the name of the person/entity whose collection it includes, as well as the location if that place is a museum.
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)

# print(girl_with_mandolin)

# Don't Be Listless
# Now that we have a marketplace to facilitate the buying and selling, let’s create our class to list works of art!
# self.art, the work of art being listed
# self.price, the price of the work
# self.seller an instance of Client.
class Listing():
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller

  def __repr__(self):
    return "{art} : {price}".format(art = self.art, price = self.price)


edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")

veneer.show_listings()

# Buy Low, Sell High
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
# print(veneer.show_listings())



