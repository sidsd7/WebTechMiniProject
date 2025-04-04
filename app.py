from flask import Flask, render_template, request, session, make_response
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

QUESTIONS = {
    'easy': [
        {'question': 'Who sang "Bohemian Rhapsody"?', 'options': ['Queen', 'The Beatles', 'Led Zeppelin'], 'answer': 'Queen'},
        {'question': 'Which year was "Shape of You" released?', 'options': ['2017', '2015', '2019'], 'answer': '2017'},
        {'question': 'What is Taylor Swift\'s debut album called?', 'options': ['Fearless', 'Taylor Swift', 'Speak Now'], 'answer': 'Taylor Swift'},
        {'question': '"Rolling in the Deep" was sung by?', 'options': ['Adele', 'Beyoncé', 'Rihanna'], 'answer': 'Adele'},
        {'question': '"Uptown Funk" was performed by?', 'options': ['Bruno Mars', 'Justin Timberlake', 'Ed Sheeran'], 'answer': 'Bruno Mars'},
        {'question': '"Thriller" was sung by?', 'options': ['Michael Jackson', 'Prince', 'Madonna'], 'answer': 'Michael Jackson'},
        {'question': '"Uptown Funk" was performed by?', 'options': ['Bruno Mars', 'Justin Timberlake', 'Ed Sheeran'], 'answer': 'Bruno Mars'},
        {'question': '"Love Story" was sung by?', 'options': ['Taylor Swift', 'Selena Gomez', 'Miley Cyrus'], 'answer': 'Taylor Swift'},
        {'question': '"All of Me" was sung by?', 'options': ['John Legend', 'Sam Smith', 'Charlie Puth'], 'answer': 'John Legend'}
             ],
    'medium': [
        {'question': 'Which instrument is featured in "Hotel California"?', 'options': ['Electric Guitar', 'Saxophone', 'Piano'], 'answer': 'Electric Guitar'},
        {'question': 'Before Miley Cyrus, "Wrecking Ball" was offered to which singer?', 'options': ['Alicia Keys', 'Katy Perry', 'Beyonce'], 'answer': 'Beyonce'},
        {'question': 'Who wrote "Sweet Child O\' Mine"?', 'options': ['Guns N\' Roses', 'Aerosmith', 'AC/DC'], 'answer': 'Guns N\' Roses'},
        {'question': 'Which Beatles album was their last recorded together?', 'options': ['Abbey Road', 'Let It Be', 'Help!'], 'answer': 'Abbey Road'},
        {'question': 'What was Elvis Presley\'s first hit?', 'options': ['Heartbreak Hotel', 'Hound Dog', 'Blue Suede Shoes'], 'answer': 'Heartbreak Hotel'},
        {'question': 'Who is known as the "Queen of Pop"?', 'options': ['Madonna', 'Whitney Houston', 'Cher'], 'answer': 'Madonna'},
        {'question': 'Which band performed "Stairway to Heaven"?', 'options': ['Led Zeppelin', 'Pink Floyd', 'The Who'], 'answer': 'Led Zeppelin'},
        {'question': 'What year did The Beatles break up?', 'options': ['1970', '1968', '1972'], 'answer': '1970'},
        {'question': 'Who wrote "Purple Rain"?', 'options': ['Prince', 'Michael Jackson', 'David Bowie'], 'answer': 'Prince'},
        {'question': 'Which band released "Another Brick in the Wall"?', 'options': ['Pink Floyd', 'The Rolling Stones', 'The Who'], 'answer': 'Pink Floyd'}
    ],
    'hard': [
        {'question': 'Which year was "Thriller" released?', 'options': ['1982', '1984', '1986'], 'answer': '1982'},
        {'question': 'Who was the original lead singer of Black Sabbath?', 'options': ['Ozzy Osbourne', 'Ronnie James Dio', 'Ian Gillan'], 'answer': 'Ozzy Osbourne'},
        {'question': 'What was the first music video played on MTV?', 'options': ['Video Killed the Radio Star', 'Bohemian Rhapsody', 'Thriller'], 'answer': 'Video Killed the Radio Star'},
        {'question': 'Which classical composer was deaf?', 'options': ['Beethoven', 'Mozart', 'Bach'], 'answer': 'Beethoven'},
        {'question': 'What was John Lennon\'s last album before his death?', 'options': ['Double Fantasy', 'Mind Games', 'Walls and Bridges'], 'answer': 'Double Fantasy'},
        {'question': 'Who produced Michael Jackson\'s "Thriller" album?', 'options': ['Quincy Jones', 'George Martin', 'Rick Rubin'], 'answer': 'Quincy Jones'},
        {'question': 'Which band\'s original name was "The New Yardbirds"?', 'options': ['Led Zeppelin', 'Deep Purple', 'Black Sabbath'], 'answer': 'Led Zeppelin'},
        {'question': 'What year was the first Grammy Awards ceremony?', 'options': ['1959', '1965', '1950'], 'answer': '1959'},
        {'question': 'Who was known as "The King of Swing"?', 'options': ['Benny Goodman', 'Duke Ellington', 'Glenn Miller'], 'answer': 'Benny Goodman'},
        {'question': 'Which famous guitarist had a custom guitar called "Lucille"?', 'options': ['B.B. King', 'Eric Clapton', 'Jimmy Page'], 'answer': 'B.B. King'}
    ]
}

@app.route('/')
def home():
    if 'high_score' not in session:
        session['high_score'] = 0
    return render_template('home.html')

@app.route('/start', methods=['POST'])
def start_game():
    difficulty = request.form['mode']
    selected_questions = random.sample(QUESTIONS[difficulty], k=5)
    
    for question in selected_questions:
        options = question['options'].copy()
        random.shuffle(options)
        question['options'] = options
    
    session.update({
        'difficulty': difficulty,
        'score': 0,
        'questions': selected_questions,
        'current_question_index': 0
    })
    return next_question()

def next_question():
    if session['current_question_index'] >= len(session['questions']):
        if session['score'] > session['high_score']:
            session['high_score'] = session['score']
        return render_template('results.html',
                             score=session['score'],
                             high_score=session['high_score'])
    
    question_data = session['questions'][session['current_question_index']]
    return render_template('game.html',
                         question_num=session['current_question_index'] + 1,
                         question=question_data['question'],
                         options=question_data['options'])

@app.route('/answer', methods=['POST'])
def handle_answer():
    correct_answer = session['questions'][session['current_question_index']]['answer']
    
    if request.form['answer'] == correct_answer:
        session['score'] += 20  
    
    session['current_question_index'] += 1
    return next_question()

if __name__ == '__main__':
    app.run(debug=True)