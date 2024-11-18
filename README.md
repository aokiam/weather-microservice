This Code is a for a weather site using openweathermap.org. <br>
You'll need a API key from there to use. <br>
Also Use HTML so be formiliar with that. <br>

Communication contract; I'll send the leaderboard.py file over discord

First create a blank clas to store the leaderboard values inside, I use named the leaderboard so my code looked like: leaderboard = Leaderboard() 
An example call of that the place_bet() function could use to call it would be to add a leaderboard.add_winning_bet(bet_amount) which would add whatever the winning bet is to the leaderboard. 
Example call 
def place_bet():
    if random.choice([True, False]):
        tokens += bet_amount
        result = "You win!"
        leaderboard.add_winning_bet(bet_amount)
#this would add the bet value to the leaderboard class.
        
#this is the code I changed for the html function to format the leaderboard
Leaderboard Page 
  <div id="leaderboard" class="page">
        <h1>Top 10 Bets</h1>
        <p>These are the top 10 highest winning bets.</p>
        <ul id="leaderboard-list"></ul>
        <button onclick="switchPage('main-menu')">Back to Main Menu</button>
  </div> #you can change any of the text to better fit your project.


For the program to request data you must add a leaderboard page requst in the api.py file
To recieve the leaderbaord add this code to the api.py file
Here's an example code that I used to test the function:
@app.route('/leaderboard', methods=['GET']) #This line creates a new route for the leaderboard page
def leaderboard_page():
    leaderboard.add_winning_bet(50) #example call for testing
    leaderboard.add_winning_bet(200) #example call for testing
    leaderboard.add_winning_bet(500) #example call for testing
    return jsonify({"leaderboard": leaderboard.get_leaderboard()}) #this returns the leaderboard array which is displayed using html

UML Diagram:
![{90664A6E-46CB-4254-A975-840A2B438C74}](https://github.com/user-attachments/assets/0cf383a8-93b9-43f3-953a-955435798add)
