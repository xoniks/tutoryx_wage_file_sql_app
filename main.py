import streamlit as st 
import pandas as pd 
import os, io


def calculate_wage(hours, rate):

    if hours>40:
        wage = (hours - 40) * 1.5 +  40 * rate

    else:
        wage = hours * rate

    return wage

st.title('Wage calculator')

name = st.text_input('Please enter your name')
hours = st.number_input('Please enter hours', min_value=0)
rate = st.number_input('Please enter rate', min_value=0)


if st.button('Calculate Wage'):

    wage = calculate_wage(hours, rate)

    csv_file = 'wage.csv'
    if not os.path.isfile(csv_file):
        df = pd.DataFrame(columns=['Name',
                                    'Hours',
                                    'Rate',
                                    'Wage'])
        df.to_csv(csv_file, index=False)

    new_entry = pd.DataFrame([[name,hours,rate,wage]],columns=['Name','Hours','Rate','Wage'])
    new_entry.to_csv(csv_file, mode='a',header=False, index=False,  )
    st.success(f'wage {wage:.2f} is added for {name}')

if st.button('Reset CSV file'):
    df = pd.DataFrame(columns=['Name',
                                'Hours',
                                'Rate',
                                'Wage'])
    
    df.to_csv('wage.csv', index=False)
    st.success('CSV file reset')



if os.path.isfile('wage.csv'):
    with open('wage.csv','rb') as f:
        df = pd.read_csv(f)
    st.write('file here')
    towrite = io.BytesIO()
    df.to_csv(towrite, encoding='utf-8', index=False, header=True)
    towrite.seek(0)

    st.download_button(
        label='Download CSV',
        data=towrite,
        file_name='wages.csv',
        mime='text/csv',
    )