import streamlit as st

def main():
    st.title('Fragen und Antworten')

    # Fragen und Antwortmöglichkeiten
    questions = [
        {
            'question': 'Was ist die Hauptstadt von Frankreich?',
            'answers': ['Berlin', 'Paris', 'London', 'Rom'],
            'correct_answer': 'Paris'
        },
        {
            'question': 'Welches ist das größte Säugetier?',
            'answers': ['Elefant', 'Wal', 'Giraffe', 'Nashorn'],
            'correct_answer': 'Wal'
        },
        {
            'question': 'Wer hat die Relativitätstheorie entwickelt?',
            'answers': ['Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Stephen Hawking'],
            'correct_answer': 'Albert Einstein'
        },
        {
            'question': 'Was ist die Hauptzutat in Pizza Margherita?',
            'answers': ['Schinken', 'Salami', 'Mozzarella', 'Champignons'],
            'correct_answer': 'Mozzarella'
        }
    ]

    # Schleife über alle Fragen
    for i, q in enumerate(questions):
        st.header(f'Frage {i + 1}: {q["question"]}')
        
        # Schleife über alle Antwortmöglichkeiten
        for answer in q['answers']:
            # Button für jede Antwortmöglichkeit
            if st.button(answer):
                if answer == q['correct_answer']:
                    st.write('Richtig!')
                else:
                    st.write('Falsch.')

# Start der App
if __name__ == '__main__':
    main()
