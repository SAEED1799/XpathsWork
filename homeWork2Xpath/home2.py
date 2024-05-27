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

# Define the XPath queries
queries = {
    "1-Extract Titles": "//book/title/text()",
    "2-Extract Authors": "//book/author/text()",
    "3-Books Published After 2004": "//book[year > 2004]/title/text()",
    "4-Books by Category": "//book[@category='web']/title",
    "5-Books with Multiple Authors": "//book[count(author) > 1]/title",
    "6-Books Priced Above $30": "//book[price > 30]/title",
    "7-Titles and Prices of Fiction Books": "//book[@category='fiction']/title | //book[@category='fiction']/price",
    "8-Books with Specific Language": "//book/title[@lang='en']",
    "9-Authors of Cooking Books": "//book[@category='cooking']/author/text()",
    "10-Books Published Between 2000 and 2010": "//book[year >= 2000 and year <= 2010]/title",

}

# Execute each query and print the results
for description, query in queries.items():
    result = tree.xpath(query)
    print(f"{description}:")
    for element in result:
        if isinstance(element, etree._Element):
            print(f"  - {element.text}")
        else:
            print(f"  - {element}")
    print("\n")

