from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

QUESTIONS = {
    'easy': [
        {
            'question': 'In which year was this song released?',
            'options': ['2019', '2020', '2021'],
            'answer': '2019',
            'spotify_id': '1rgnBhdG2JDFTbYkYRZAku'  # Dance Monkey
        },
        {
            'question': 'Which album is this song from?',
            'options': ['After Hours', 'Starboy', 'Beauty Behind the Madness'],
            'answer': 'After Hours',
            'spotify_id': '0VjIjW4GlUZAMYd2vXMi3b'  # Blinding Lights
        },
        {
            'question': 'How many Grammy awards did this song win?',
            'options': ['4', '2', '0'],
            'answer': '0',
            'spotify_id': '2Fxmhks0bxGSBdJ92vM42m'  # Bad Guy
        },
        {
            'question': 'What position did this song peak at on Billboard Hot 100?',
            'options': ['#1', '#3', '#5'],
            'answer': '#1',
            'spotify_id': '5HCyWlXZPP0y6Gqq8TgA20'  # Stay
        },
        {
            'question': 'Which artist featured in a remix of this song?',
            'options': ['DaBaby', 'Madonna', 'Missy Elliott'],
            'answer': 'DaBaby',
            'spotify_id': '39LLxExYz6ewLAcYrzQQyP'  # Levitating
        },
        {
            'question': 'Where was this song first performed live?',
            'options': ['SNL', 'Grammy Awards', 'BBC Radio'],
            'answer': 'SNL',
            'spotify_id': '6UelLqGlWMcVH1E5c4H7lY'  # Watermelon Sugar
        },
        {
            'question': 'How many weeks was this song #1 on Billboard?',
            'options': ['8 weeks', '11 weeks', '15 weeks'],
            'answer': '8 weeks',
            'spotify_id': '4LRPiXqCikLlN15c3yImP7'  # As It Was
        },
        {
            'question': 'Which TV show featured this song in its finale?',
            'options': ['Euphoria', 'Stranger Things', '13 Reasons Why'],
            'answer': 'Euphoria',
            'spotify_id': '5wANPM4fQCJwkGd4rN57mH'  # drivers license
        },
        {
            'question': 'What color dress did the artist wear in the music video?',
            'options': ['Black', 'Red', 'White'],
            'answer': 'Black',
            'spotify_id': '5QO79kh1waicV47BqGRL3g'  # Save Your Tears
        },
        {
            'question': 'Which award show performance went viral?',
            'options': ['MTV VMAs', 'Billboard Awards', 'Grammy Awards'],
            'answer': 'MTV VMAs',
            'spotify_id': '35mvY5S1H3J2QZyna3TFe0'  # Monster - Nicki Minaj
        }
    ],
    'medium': [
        {
            'question': 'How long did it take to record this song?',
            'options': ['6 hours', '2 days', '1 week'],
            'answer': '6 hours',
            'spotify_id': '3z8h0TU7ReDPLIbEnYhWZb'  # Bohemian Rhapsody
        },
        {
            'question': 'Which guitar was used for the main riff?',
            'options': ['Gibson Les Paul', 'Fender Stratocaster', 'Ibanez RG'],
            'answer': 'Gibson Les Paul',
            'spotify_id': '7o2CTH4ctstm8TNelqjb51'  # Sweet Child O' Mine
        },
        {
            'question': 'In which movie did this song feature prominently?',
            'options': ['The Big Lebowski', 'Forrest Gump', 'Almost Famous'],
            'answer': 'The Big Lebowski',
            'spotify_id': '40riOy7x9W7GXjyGp4pjAv'  # Hotel California
        },
        {
            'question': 'What inspired the lyrics of this song?',
            'options': ['A breakup', 'Political protest', 'Drug addiction'],
            'answer': 'Political protest',
            'spotify_id': '3AhXZa8sUQht0UEdBJgpGc'  # Like a Rolling Stone
        },
        {
            'question': 'How many microphones were used to record the drums?',
            'options': ['2', '4', '8'],
            'answer': '4',
            'spotify_id': '5CQ30WqJwcep0pYcV4AMNc'  # Stairway to Heaven
        },
        {
            'question': 'Which studio was this recorded in?',
            'options': ['Abbey Road', 'Electric Lady', 'Sunset Sound'],
            'answer': 'Abbey Road',
            'spotify_id': '7pKfPomDEeI4TPT6EOYjn9'  # Imagine
        },
        {
            'question': 'What was the original title of this song?',
            'options': ['Funky Music', 'Dance Floor', 'Groove Tonight'],
            'answer': 'Funky Music',
            'spotify_id': 'Z7YzrIafxwkBd4zJRMHPPR'  # Billie Jean
        },
        {
            'question': 'Which synthesizer was used in this recording?',
            'options': ['Moog', 'Roland', 'Yamaha'],
            'answer': 'Moog',
            'spotify_id': '4NsPgRYUdHu2Q5JRNgXYU5'  # Jump - Van Halen
        },
        {
            'question': 'What was the recording budget for this song?',
            'options': ['$15,000', '$50,000', '$100,000'],
            'answer': '$50,000',
            'spotify_id': '7snQQk1zcKl8gZ92AnueZW'  # Born to Run
        },
        {
            'question': 'How many vocal tracks were layered in this recording?',
            'options': ['24', '36', '48'],
            'answer': '36',
            'spotify_id': '6ZFbXIJkuI1dVNWvzJzown'  # A Day in the Life
        }
    ],
    'hard': [
        {
            'question': 'In which key was this piece composed?',
            'options': ['C minor', 'G major', 'D minor'],
            'answer': 'C minor',
            'spotify_id': '1mYGp3HO5IxRdyQyQuLm3W'  # Symphony No. 5
        },
        {
            'question': 'What unusual time signature is this piece written in?',
            'options': ['5/4', '3/4', '7/8'],
            'answer': '5/4',
            'spotify_id': '5UbZ76YAhxHzZO4xG3Q0pS'  # Take Five
        },
        {
            'question': 'Which season was this movement written to represent?',
            'options': ['Spring', 'Summer', 'Winter'],
            'answer': 'Spring',
            'spotify_id': '3h3pOvw6hjOvZxRUseB7h9'  # Four Seasons
        },
        {
            'question': 'What modal scale is predominantly used in this piece?',
            'options': ['Dorian', 'Mixolydian', 'Phrygian'],
            'answer': 'Dorian',
            'spotify_id': '4vLYewWIvqHfUiREPLKTkG'  # Kind of Blue
        },
        {
            'question': 'Which orchestra first performed this piece?',
            'options': ['Vienna', 'Berlin', 'London'],
            'answer': 'Vienna',
            'spotify_id': '14RYXRGcDxRBGYhL5RRbF6'  # Moonlight Sonata
        },
        {
            'question': 'How many movements are in the complete work?',
            'options': ['3', '4', '5'],
            'answer': '4',
            'spotify_id': '2CiT0qAzE2kvS4EZdUQPzF'  # Symphony No. 40
        },
        {
            'question': 'What was the premiere venue for this piece?',
            'options': ['Mariinsky Theatre', 'Bolshoi Theatre', 'Paris Opera'],
            'answer': 'Mariinsky Theatre',
            'spotify_id': '0wsxJPJ4OQK7NggIRmVHgn'  # The Nutcracker
        },
        {
            'question': 'Which instrument family opens this piece?',
            'options': ['Strings', 'Woodwinds', 'Brass'],
            'answer': 'Strings',
            'spotify_id': '2ZwihUZWmqvwRILJcJvXBh'  # Für Elise
        },
        {
            'question': 'What was the composer\'s age when writing this?',
            'options': ['25', '35', '45'],
            'answer': '35',
            'spotify_id': '1BNtFSws7fjbn9aVBPA79j'  # Symphony No. 9
        },
        {
            'question': 'How many variations are in this piece?',
            'options': ['30', '32', '36'],
            'answer': '32',
            'spotify_id': '4Nd5HJn4EExnQkQqtJ0CjW'  # Goldberg Variations
        }
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
                         options=question_data['options'],
                         spotify_id=question_data['spotify_id'])

@app.route('/answer', methods=['POST'])
def handle_answer():
    user_answer = request.form.get('answer', '')
    if user_answer:
        correct_answer = session['questions'][session['current_question_index']]['answer']
        if user_answer == correct_answer:
            session['score'] += 20
    
    session['current_question_index'] += 1
    return next_question()

if __name__ == '__main__':
    app.run(debug=True)