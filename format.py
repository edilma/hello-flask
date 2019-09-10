markup =""" 

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{heading}</h1>
    </body>
</html>
"""

markup =markup.format(title='My Page Title', heading ='Page Heading')
print (markup)