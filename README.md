This Code is a for a weather site using openweathermap.org. <br>
You'll need a API key from there to use. <br>
Also Use HTML so be formiliar with that. <br>

Communication contract; I'll send the leaderboard.py file over discord<br>

First create a blank clas to store the leaderboard values inside, I use named the leaderboard so my code looked like: leaderboard = Leaderboard() <br>
An example call of that the place_bet() function could use to call it would be to add a leaderboard.add_winning_bet(bet_amount) which would add whatever the winning bet is to the leaderboard. <br>
Example call: <br>
def place_bet():<br>
    if random.choice([True, False]):<br>
        tokens += bet_amount<br>
        result = "You win!"<br>
        leaderboard.add_winning_bet(bet_amount)<br>
#this would add the bet value to the leaderboard class.<br>
        
#this is the code I changed for the html function to format the leaderboard<br>
Leaderboard Page:<br>
 # <div id="leaderboard" class="page"><br>
  #      <h1>Top 10 Bets</h1><br>
   #     <p>These are the top 10 highest winning bets.</p><br>
   #    <ul id="leaderboard-list"></ul><br>
   #     <button onclick="switchPage('main-menu')">Back to Main Menu</button><br>
  #</div> #you can change any of the text to better fit your project.<br><br>


For the program to request data you must add a leaderboard page requst in the api.py file,
To recieve the leaderbaord add this code to the api.py file<br>
Here's an example code that I used to test the function:<br>
@app.route('/leaderboard', methods=['GET']) #This line creates a new route for the leaderboard page<br>
def leaderboard_page():<br>
    leaderboard.add_winning_bet(50) #example call for testing<br>
    leaderboard.add_winning_bet(200) #example call for testing<br>
    leaderboard.add_winning_bet(500) #example call for testing<br>
    return jsonify({"leaderboard": leaderboard.get_leaderboard()}) #this returns the leaderboard array which is displayed using html<br><br>

UML Diagram:
![{90664A6E-46CB-4254-A975-840A2B438C74}](https://github.com/user-attachments/assets/0cf383a8-93b9-43f3-953a-955435798add)
