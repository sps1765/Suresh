import streamlit as st

def calculate_grade(score, max_score):
    percentage = (score / max_score) * 100

    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def main():
    st.title('Simple Grade Calculator')

    st.write('Enter your test scores and the maximum possible score to calculate your grade.')

    score = st.number_input('Enter your score', min_value=0.0, step=0.01)
    max_score = st.number_input('Enter the maximum possible score', min_value=0.0, step=0.01)

    if st.button('Calculate Grade'):
        if score > max_score:
            st.error('Invalid input: Score cannot be greater than the maximum possible score.')
        else:
            grade = calculate_grade(score, max_score)
            st.success(f'Your grade is: {grade}')

if __name__ == "__main__":
    main()

