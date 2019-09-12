from flask import Flask, request , redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
 <form id="form" method="POST">
            <label> First Name
                <input name="first_name" type="text"/>
            </label>
                <input type="submit" value="Submit"/>
        </form>
"""

app.route("/")
def index():
    return form

app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' +cgi.escape(first_name) + '</h1>'



time_for="""
    <style>
    .error{{ color:red; }}
    </style>
    <h1>Validate Time</h1>
            <form method="POST">
            <label> Hours (24-hour format)
                <input name="hours" type="text" value="{hours}" />
            </label>
            <p class="error">{hours_error}</p>
            <label> Minutes
                <input name="minutes" type="text" value="{minutes}" />
            </label>
            <p class="error"> {minutes_error}</p>
            <input name="none" type="submit" value="Validate" />
        </form>
"""


#reading the form in a page name validate-time
@app.route('/validate-time')
def display_time_form():
    return time_for.format(hours='', hours_error=' ', minutes ='', minutes_error='')

#function to validate that user entered a number in the form box
def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

#validation function.  First check if it is an integer and then if its 
#within the valid ranges of hours and minutes
@app.route('/validate-time', methods=['POST'])
def validate_time():
    hours= request.form ['hours']
    minutes= request.form['minutes']

    hours_error=''
    minutes_error=''

    if not is_integer(hours):
        hours_error='Not a valid integer '
        hours=''
    else:
        hours=int(hours)
        if hours>23 or hours<0:
            hours_error ='Hour value out of range (0-23)'
            hours=''
    
    if not is_integer(minutes):
        minutes_error='Not a valid integer '
        minutes=''
    else:
        minutes=int(minutes)
        if minutes>59 or minutes<0:
            minutes_error ='Hour value out of range (0-23)'
            minutes=''
    
    if not minutes_error and not hours_error:
        time = str(hours) + ':' + str(minutes)
        return redirect ('/valid-time?time{0}'.format(time))
    else:
        return time_for.format(hours_error=hours_error, minutes_error=minutes_error, hours=hours, minutes=minutes)

@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitted {0}.  Thanks for submitting a valid time</h1>'.format(time)


@app.route("/form-inputs")
def display_form_inputs():
    return """
    <style>
    br {margin-bottom: 20px;}
    </style>
    <form method='POST'>
        <label>type=text
            <input name="user-name" type="text" />
        </label>
        <br>
        <label>type=password
            <input name="user-password" type="password" />
        </label>
        <br>
        <label>type=email
            <input name="user-email" type="email" />
        </label>
        <br>
        <input name="shopping-cart-id" value="0129384" type="hidden" />
        <br>
        <label>Ketchup
            <input type="checkbox" name="cb1" value="first-cb" />
        </label>
        <br>
        <label>Mustard
            <input type="checkbox" name="cb2" value="second-cb" />
        </label>
        <br>
        <label>Small
            <input type="radio" name="coffee-size" value="sm" />
        </label>
        <label>Medium
            <input type="radio" name="coffee-size" value="med" />
        </label>
        <label>Large
            <input type="radio" name="coffee-size" value="lg" />
        </label>
        <br>
        <label>Your life story
            <textarea name="life-story"></textarea>
        </label>
        <br>
        <label>LaunchCode Hub
            <select name="lc-hub">
                <option value="kc">Kansas City</option>
                <option value="mia">Miami</option>
                <option value="ri">Providence</option>
                <option value="sea">Seattle</option>
                <option value="pdx">Portland</option>
            </select>
        </label>
        <br>
        <input type="submit" />
    </form>
    """


@app.route("/form-inputs", methods=['POST'])
def print_form_values():
    resp = ""
    for field in request.form.keys():
        resp += "<b>{key}</b>: {value}<br>".format(key=field, value=request.form[field])

    return resp
    





app.run()