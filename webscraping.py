from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Webpage</title>
</head>
<body>
    <div id="section-1">
        <h3 data-hello="hi">Hello</h3>
        <img src="https://source.unsplash.com/200x200/?nature,water">
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Porro perferendis consectetur itaque? Repellat facilis sit molestias voluptates impedit, vel in expedita unde accusamus doloribus delectus! Deserunt dolorum ipsum in repudiandae!</p>
    </div>
    <div id="section-2">
        <ul class="items">
            <li class="item"><a href="#">Item 1</a></li>
            <li class="item"><a href="#">Item 2</a></li>
            <li class="item"><a href="#">Item 3</a></li>
            <li class="item"><a href="#">Item 4</a></li>
            <li class="item"><a href="#">Item 5</a></li>
        </ul>
    </div>

</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

# Direct

# print (soup.body)
# print (soup.head)
# print (soup.head.title)

#find()
# el = soup.find('div')

# el = soup.findAll('div')[1]

# el = soup.find(id='section-2')
# el = soup.find(class_='items')
# el = soup.find(attrs={"data-hello": "hi"})

# select 
# el = soup.select('.item')

# get_text()
# el = soup.find(class_='item').get_text()

# for item in soup.select('.item'):
#     print (item.get_text())

# el = soup.body.contents[1].contents[1].next_sibling.next_sibling
# el = soup.body.contents[1].contents[1].find_next_sibling()

# el = soup.find(id='section-2').find_previous_sibling() 

# el = soup.find(class_='item').find_parent()

el = soup.find('h3').find_next_sibling('p')
print(el)

