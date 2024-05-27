from lxml import etree

xml_content = '''<bookstore>
  <book category="cooking">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="children">
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
  <book category="web">
    <title lang="en">XQuery Kick Start</title>
    <author>James McGovern</author>
    <author>Per Bothner</author>
    <author>Kurt Cagle</author>
    <author>James Linn</author>
    <author>Vaidyanathan Nagarajan</author>
    <year>2003</year>
    <price>49.99</price>
  </book>
  <book category="web">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>
  <book category="fiction">
    <title lang="en">The Hobbit</title>
    <author>J.R.R. Tolkien</author>
    <year>1937</year>
    <price>22.99</price>
  </book>
  <book category="fiction">
    <title lang="en">The Great Gatsby</title>
    <author>F. Scott Fitzgerald</author>
    <year>1925</year>
    <price>10.99</price>
  </book>
  <book category="cooking">
    <title lang="en">Mastering the Art of French Cooking</title>
    <author>Julia Child</author>
    <author>Louisette Bertholle</author>
    <author>Simone Beck</author>
    <year>1961</year>
    <price>45.00</price>
  </book>
</bookstore>'''

# Parse the XML content
tree = etree.fromstring(xml_content)

# Task 11: Most Expensive Book
max_price = max(tree.xpath("//book/price/text()"), key=float)
most_expensive_books = tree.xpath(f"//book[price={max_price}]/title/text()")
most_expensive_books_with_price = [(title, max_price) for title in most_expensive_books]

# Task 12: Books Sorted by Year
books = tree.xpath("//book")
sorted_books = sorted(books, key=lambda book: int(book.find("year").text))
sorted_titles = [book.find("title").text for book in sorted_books]

# Print results
print("Most Expensive Book:")
for title, price in most_expensive_books_with_price:
    print(f"  - Title: {title}, Price: {price}")

print("\nBooks Sorted by Year:")
for title in sorted_titles:
    print(f"  - {title}")
