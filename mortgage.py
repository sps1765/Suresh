import streamlit as st

def calculate_monthly_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months)
    return monthly_payment

def main():
    st.title('Mortgage Calculator')

    st.write('Enter the details of your mortgage to calculate your monthly payment.')

    principal = st.number_input('Loan Amount ($)', min_value=0.0, step=100.0)
    annual_interest_rate = st.number_input('Annual Interest Rate (%)', min_value=0.0, step=0.01)
    years = st.number_input('Loan Term (Years)', min_value=1, step=1)

    if st.button('Calculate'):
        monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
        st.success(f'Your estimated monthly payment is: ${monthly_payment:.2f}')

if __name__ == "__main__":
    main()
