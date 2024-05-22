from lxml import html

# Load the HTML content
content = '''
<html>
  <head>
    <title>My Web Page</title>
  </head>
  <body>
    <div id="content">
      <h1>My Blog</h1>
      <ul>
        <li class="post"><a href="post1.html">Post 1</a></li>
        <li class="post"><a href="post2.html">Post 2</a></li>
        <li class="post"><a href="post3.html">Post 3</a></li>
      </ul>
    </div>
  </body>
</html>
'''

# Parse the HTML
tree = html.fromstring(content)

# EX1: Links to blog post pages
print("EX1: Links to blog post pages")
links = tree.xpath("//li[@class='post']/a")
for link in links:
    print(link.get('href'))

# Update content for EX2 and EX3
content = '''
<html>
  <head>
    <title>My Web Page</title>
  </head>
  <body>
    <div id="content">
      <h1>My Blog</h1>
      <div class="posts">
        <div class="post">
          <h2><a href="post1.html">Post 1</a></h2>
          <div class="meta">
            <span class="author">John Doe</span>
            <span class="date">2022-05-01</span>
          </div>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
        <div class="post">
          <h2><a href="post2.html">Post 2</a></h2>
          <div class="meta">
            <span class="author">Jane Doe</span>
            <span class="date">2022-05-02</span>
          </div>
          <p>Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
        </div>
        <div class="post">
          <h2><a href="post3.html">Post 3</a></h2>
          <div class="meta">
            <span class="author">John Smith</span>
            <span class="date">2022-05-03</span>
          </div>
          <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        </div>
      </div>
    </div>
  </body>
</html>
'''

# Parse the updated HTML
tree = html.fromstring(content)

# EX2: Titles of blog posts
print("\nEX2: Titles of blog posts")
titles = tree.xpath("//div[@class='post']/h2/a/text()")
for title in titles:
    print(title)

# EX3: Authors of blog posts
print("\nEX3: Authors of blog posts")
authors = tree.xpath("//div[@class='post']//span[@class='author']/text()")
for author in authors:
    print(author)
