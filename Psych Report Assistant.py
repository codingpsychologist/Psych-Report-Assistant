import os
import pandas as pd
from docxtpl import DocxTemplate
import glob
import PySimpleGUI as sg

# Get the current working directory
cwd = os.getcwd()

# Search for CSV files in the current working directory
csv_files = glob.glob(os.path.join(cwd, '*.csv'))

def generate_word_documents(csv_file_path, docx_template_path, output_folder):
    # Read the CSV file using pandas
    df = pd.read_csv(csv_file_path)

    # Extract specific columns
    selected_columns = df[['FirstName', 'LastName', 'BirthDate', 'Examiner', 'AdministrationDate', 'AgeAtAssessment',
                           'wisc5_vci_ss', 'wisc5_vsi_ss', 'wisc5_fri_ss', 'wisc5_wmi_ss', 'wisc5_psi_ss', 'wisc5_fsiq_ss']]

    # Convert the DataFrame to a list of dictionaries
    data = selected_columns.to_dict('records')

    # Load the Word document template
    doc = DocxTemplate(docx_template_path)

    for row in data:
        # Prepare the context data for rendering
        context = {'data': row}
        # Apply conditional logic
        if str(row['wisc5_fsiq_ss']) == '40':
            context['data']['PR'] = '<0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '41':
            context['data']['PR'] = '<0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '42':
            context['data']['PR'] = '<0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '43':
            context['data']['PR'] = '<0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '44':
            context['data']['PR'] = '<0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '45':
            context['data']['PR'] = '<0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '46':
            context['data']['PR'] = '<0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '47':
            context['data']['PR'] = '<0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '48':
            context['data']['PR'] = '<0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '49':
            context['data']['PR'] = '<0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '50':
            context['data']['PR'] = '<0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '51':
            context['data']['PR'] = '<0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '52':
            context['data']['PR'] = '0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '53':
            context['data']['PR'] = '0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '54':
            context['data']['PR'] = '0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '55':
            context['data']['PR'] = '0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '56':
            context['data']['PR'] = '0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '57':
            context['data']['PR'] = '0.1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '58':
            context['data']['PR'] = '0.2'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '59':
            context['data']['PR'] = '0.3'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '60':
            context['data']['PR'] = '0.4'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '61':
            context['data']['PR'] = '0.5'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '62':
            context['data']['PR'] = '1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '63':
            context['data']['PR'] = '1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '64':
            context['data']['PR'] = '1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '65':
            context['data']['PR'] = '1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '66':
            context['data']['PR'] = '1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '67':
            context['data']['PR'] = '1'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '68':
            context['data']['PR'] = '2'
            context['data']['Classification'] = 'Extremely Low'
        if str(row['wisc5_fsiq_ss']) == '69':
            context['data']['PR'] = '2'
            context['data']['Classification'] = 'Very Low'
        if str(row['wisc5_fsiq_ss']) == '70':
            context['data']['PR'] = '2'
            context['data']['Classification'] = 'Very Low'
        if str(row['wisc5_fsiq_ss']) == '71':
            context['data']['PR'] = '3'
            context['data']['Classification'] = 'Very Low'
        if str(row['wisc5_fsiq_ss']) == '72':
            context['data']['PR'] = '3'
            context['data']['Classification'] = 'Very Low'
        if str(row['wisc5_fsiq_ss']) == '73':
            context['data']['PR'] = '4'
            context['data']['Classification'] = 'Very Low'
        if str(row['wisc5_fsiq_ss']) == '74':
            context['data']['PR'] = '4'
            context['data']['Classification'] = 'Very Low'
        if str(row['wisc5_fsiq_ss']) == '75':
            context['data']['PR'] = '5'
            context['data']['Classification'] = 'Very Low'
        if str(row['wisc5_fsiq_ss']) == '76':
            context['data']['PR'] = '5'
            context['data']['Classification'] = 'Very Low'
        if str(row['wisc5_fsiq_ss']) == '77':
            context['data']['PR'] = '6'
            context['data']['Classification'] = 'Very Low'
        if str(row['wisc5_fsiq_ss']) == '78':
            context['data']['PR'] = '7'
            context['data']['Classification'] = 'Very Low'
        if str(row['wisc5_fsiq_ss']) == '79':
            context['data']['PR'] = '8'
            context['data']['Classification'] = 'Very Low'
        if str(row['wisc5_fsiq_ss']) == '80':
            context['data']['PR'] = '9'
            context['data']['Classification'] = 'Low Average'
        if str(row['wisc5_fsiq_ss']) == '81':
            context['data']['PR'] = '10'
            context['data']['Classification'] = 'Low Average'
        if str(row['wisc5_fsiq_ss']) == '82':
            context['data']['PR'] = '12'
            context['data']['Classification'] = 'Low Average'
        if str(row['wisc5_fsiq_ss']) == '83':
            context['data']['PR'] = '13'
            context['data']['Classification'] = 'Low Average'
        if str(row['wisc5_fsiq_ss']) == '84':
            context['data']['PR'] = '14'
            context['data']['Classification'] = 'Low Average'
        if str(row['wisc5_fsiq_ss']) == '85':
            context['data']['PR'] = '16'
            context['data']['Classification'] = 'Low Average'
        if str(row['wisc5_fsiq_ss']) == '86':
            context['data']['PR'] = '18'
            context['data']['Classification'] = 'Low Average'
        if str(row['wisc5_fsiq_ss']) == '87':
            context['data']['PR'] = '19'
            context['data']['Classification'] = 'Low Average'
        if str(row['wisc5_fsiq_ss']) == '88':
            context['data']['PR'] = '21'
            context['data']['Classification'] = 'Low Average'
        if str(row['wisc5_fsiq_ss']) == '89':
            context['data']['PR'] = '23'
            context['data']['Classification'] = 'Low Average'
        if str(row['wisc5_fsiq_ss']) == '90':
            context['data']['PR'] = '25'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '91':
            context['data']['PR'] = '27'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '92':
            context['data']['PR'] = '30'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '93':
            context['data']['PR'] = '32'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '94':
            context['data']['PR'] = '34'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '95':
            context['data']['PR'] = '37'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '96':
            context['data']['PR'] = '40'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '97':
            context['data']['PR'] = '42'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '98':
            context['data']['PR'] = '45'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '99':
            context['data']['PR'] = '47'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '100':
            context['data']['PR'] = '50'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '101':
            context['data']['PR'] = '53'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '102':
            context['data']['PR'] = '55'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '103':
            context['data']['PR'] = '58'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '104':
            context['data']['PR'] = '61'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '105':
            context['data']['PR'] = '63'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '106':
            context['data']['PR'] = '66'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '107':
            context['data']['PR'] = '68'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '108':
            context['data']['PR'] = '70'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '109':
            context['data']['PR'] = '73'
            context['data']['Classification'] = 'Average'
        if str(row['wisc5_fsiq_ss']) == '110':
            context['data']['PR'] = '75'
            context['data']['Classification'] = 'High Average'
        if str(row['wisc5_fsiq_ss']) == '111':
            context['data']['PR'] = '77'
            context['data']['Classification'] = 'High Average'
        if str(row['wisc5_fsiq_ss']) == '112':
            context['data']['PR'] = '79'
            context['data']['Classification'] = 'High Average'
        if str(row['wisc5_fsiq_ss']) == '113':
            context['data']['PR'] = '81'
            context['data']['Classification'] = 'High Average'
        if str(row['wisc5_fsiq_ss']) == '114':
            context['data']['PR'] = '82'
            context['data']['Classification'] = 'High Average'
        if str(row['wisc5_fsiq_ss']) == '115':
            context['data']['PR'] = '84'
            context['data']['Classification'] = 'High Average'
        if str(row['wisc5_fsiq_ss']) == '116':
            context['data']['PR'] = '86'
            context['data']['Classification'] = 'High Average'
        if str(row['wisc5_fsiq_ss']) == '117':
            context['data']['PR'] = '87'
            context['data']['Classification'] = 'High Average'
        if str(row['wisc5_fsiq_ss']) == '118':
            context['data']['PR'] = '88'
            context['data']['Classification'] = 'High Average'
        if str(row['wisc5_fsiq_ss']) == '119':
            context['data']['PR'] = '90'
            context['data']['Classification'] = 'High Average'
        if str(row['wisc5_fsiq_ss']) == '120':
            context['data']['PR'] = '91'
            context['data']['Classification'] = 'Very High'
        if str(row['wisc5_fsiq_ss']) == '121':
            context['data']['PR'] = '92'
            context['data']['Classification'] = 'Very High'
        if str(row['wisc5_fsiq_ss']) == '122':
            context['data']['PR'] = '93'
            context['data']['Classification'] = 'Very High'
        if str(row['wisc5_fsiq_ss']) == '123':
            context['data']['PR'] = '94'
            context['data']['Classification'] = 'Very High'
        if str(row['wisc5_fsiq_ss']) == '124':
            context['data']['PR'] = '95'
            context['data']['Classification'] = 'Very High'
        if str(row['wisc5_fsiq_ss']) == '125':
            context['data']['PR'] = '95'
            context['data']['Classification'] = 'Very High'
        if str(row['wisc5_fsiq_ss']) == '126':
            context['data']['PR'] = '96'
            context['data']['Classification'] = 'Very High'
        if str(row['wisc5_fsiq_ss']) == '127':
            context['data']['PR'] = '96'
            context['data']['Classification'] = 'Very High'
        if str(row['wisc5_fsiq_ss']) == '128':
            context['data']['PR'] = '97'
            context['data']['Classification'] = 'Very High'
        if str(row['wisc5_fsiq_ss']) == '129':
            context['data']['PR'] = '97'
            context['data']['Classification'] = 'Very High'
        if str(row['wisc5_fsiq_ss']) == '130':
            context['data']['PR'] = '98'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '131':
            context['data']['PR'] = '98'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '132':
            context['data']['PR'] = '98'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '133':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '134':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '135':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '136':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '137':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '138':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '139':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '140':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '141':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '142':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '143':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '144':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '145':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '146':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '147':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '148':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '149':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_fsiq_ss']) == '150':
            context['data']['PR'] = '99'
            context['data']['Classification'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '40':
            context['data']['PR2'] = '<0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '41':
            context['data']['PR2'] = '<0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '42':
            context['data']['PR2'] = '<0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '43':
            context['data']['PR2'] = '<0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '44':
            context['data']['PR2'] = '<0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '45':
            context['data']['PR2'] = '<0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '46':
            context['data']['PR2'] = '<0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '47':
            context['data']['PR2'] = '<0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '48':
            context['data']['PR2'] = '<0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '49':
            context['data']['PR2'] = '<0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '50':
            context['data']['PR2'] = '<0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '51':
            context['data']['PR2'] = '<0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '52':
            context['data']['PR2'] = '0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '53':
            context['data']['PR2'] = '0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '54':
            context['data']['PR2'] = '0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '55':
            context['data']['PR2'] = '0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '56':
            context['data']['PR2'] = '0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '57':
            context['data']['PR2'] = '0.1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '58':
            context['data']['PR2'] = '0.2'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '59':
            context['data']['PR2'] = '0.3'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '60':
            context['data']['PR2'] = '0.4'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '61':
            context['data']['PR2'] = '0.5'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '62':
            context['data']['PR2'] = '1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '63':
            context['data']['PR2'] = '1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '64':
            context['data']['PR2'] = '1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '65':
            context['data']['PR2'] = '1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '66':
            context['data']['PR2'] = '1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '67':
            context['data']['PR2'] = '1'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '68':
            context['data']['PR2'] = '2'
            context['data']['Classification2'] = 'Extremely Low'
        if str(row['wisc5_vci_ss']) == '69':
            context['data']['PR2'] = '2'
            context['data']['Classification2'] = 'Very Low'
        if str(row['wisc5_vci_ss']) == '70':
            context['data']['PR2'] = '2'
            context['data']['Classification2'] = 'Very Low'
        if str(row['wisc5_vci_ss']) == '71':
            context['data']['PR2'] = '3'
            context['data']['Classification2'] = 'Very Low'
        if str(row['wisc5_vci_ss']) == '72':
            context['data']['PR2'] = '3'
            context['data']['Classification2'] = 'Very Low'
        if str(row['wisc5_vci_ss']) == '73':
            context['data']['PR2'] = '4'
            context['data']['Classification2'] = 'Very Low'
        if str(row['wisc5_vci_ss']) == '74':
            context['data']['PR2'] = '4'
            context['data']['Classification2'] = 'Very Low'
        if str(row['wisc5_vci_ss']) == '75':
            context['data']['PR2'] = '5'
            context['data']['Classification2'] = 'Very Low'
        if str(row['wisc5_vci_ss']) == '76':
            context['data']['PR2'] = '5'
            context['data']['Classification2'] = 'Very Low'
        if str(row['wisc5_vci_ss']) == '77':
            context['data']['PR2'] = '6'
            context['data']['Classification2'] = 'Very Low'
        if str(row['wisc5_vci_ss']) == '78':
            context['data']['PR2'] = '7'
            context['data']['Classification2'] = 'Very Low'
        if str(row['wisc5_vci_ss']) == '79':
            context['data']['PR2'] = '8'
            context['data']['Classification2'] = 'Very Low'
        if str(row['wisc5_vci_ss']) == '80':
            context['data']['PR2'] = '9'
            context['data']['Classification2'] = 'Low Average'
        if str(row['wisc5_vci_ss']) == '81':
            context['data']['PR2'] = '10'
            context['data']['Classification2'] = 'Low Average'
        if str(row['wisc5_vci_ss']) == '82':
            context['data']['PR2'] = '12'
            context['data']['Classification2'] = 'Low Average'
        if str(row['wisc5_vci_ss']) == '83':
            context['data']['PR2'] = '13'
            context['data']['Classification2'] = 'Low Average'
        if str(row['wisc5_vci_ss']) == '84':
            context['data']['PR2'] = '14'
            context['data']['Classification2'] = 'Low Average'
        if str(row['wisc5_vci_ss']) == '85':
            context['data']['PR2'] = '16'
            context['data']['Classification2'] = 'Low Average'
        if str(row['wisc5_vci_ss']) == '86':
            context['data']['PR2'] = '18'
            context['data']['Classification2'] = 'Low Average'
        if str(row['wisc5_vci_ss']) == '87':
            context['data']['PR2'] = '19'
            context['data']['Classification2'] = 'Low Average'
        if str(row['wisc5_vci_ss']) == '88':
            context['data']['PR2'] = '21'
            context['data']['Classification2'] = 'Low Average'
        if str(row['wisc5_vci_ss']) == '89':
            context['data']['PR2'] = '23'
            context['data']['Classification2'] = 'Low Average'
        if str(row['wisc5_vci_ss']) == '90':
            context['data']['PR2'] = '25'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '91':
            context['data']['PR2'] = '27'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '92':
            context['data']['PR2'] = '30'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '93':
            context['data']['PR2'] = '32'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '94':
            context['data']['PR2'] = '34'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '95':
            context['data']['PR2'] = '37'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '96':
            context['data']['PR2'] = '40'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '97':
            context['data']['PR2'] = '42'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '98':
            context['data']['PR2'] = '45'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '99':
            context['data']['PR2'] = '47'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '100':
            context['data']['PR2'] = '50'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '101':
            context['data']['PR2'] = '53'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '102':
            context['data']['PR2'] = '55'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '103':
            context['data']['PR2'] = '58'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '104':
            context['data']['PR2'] = '61'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '105':
            context['data']['PR2'] = '63'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '106':
            context['data']['PR2'] = '66'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '107':
            context['data']['PR2'] = '68'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '108':
            context['data']['PR2'] = '70'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '109':
            context['data']['PR2'] = '73'
            context['data']['Classification2'] = 'Average'
        if str(row['wisc5_vci_ss']) == '110':
            context['data']['PR2'] = '75'
            context['data']['Classification2'] = 'High Average'
        if str(row['wisc5_vci_ss']) == '111':
            context['data']['PR2'] = '77'
            context['data']['Classification2'] = 'High Average'
        if str(row['wisc5_vci_ss']) == '112':
            context['data']['PR2'] = '79'
            context['data']['Classification2'] = 'High Average'
        if str(row['wisc5_vci_ss']) == '113':
            context['data']['PR2'] = '81'
            context['data']['Classification2'] = 'High Average'
        if str(row['wisc5_vci_ss']) == '114':
            context['data']['PR2'] = '82'
            context['data']['Classification2'] = 'High Average'
        if str(row['wisc5_vci_ss']) == '115':
            context['data']['PR2'] = '84'
            context['data']['Classification2'] = 'High Average'
        if str(row['wisc5_vci_ss']) == '116':
            context['data']['PR2'] = '86'
            context['data']['Classification2'] = 'High Average'
        if str(row['wisc5_vci_ss']) == '117':
            context['data']['PR2'] = '87'
            context['data']['Classification2'] = 'High Average'
        if str(row['wisc5_vci_ss']) == '118':
            context['data']['PR2'] = '88'
            context['data']['Classification2'] = 'High Average'
        if str(row['wisc5_vci_ss']) == '119':
            context['data']['PR2'] = '90'
            context['data']['Classification2'] = 'High Average'
        if str(row['wisc5_vci_ss']) == '120':
            context['data']['PR2'] = '91'
            context['data']['Classification2'] = 'Very High'
        if str(row['wisc5_vci_ss']) == '121':
            context['data']['PR2'] = '92'
            context['data']['Classification2'] = 'Very High'
        if str(row['wisc5_vci_ss']) == '122':
            context['data']['PR2'] = '93'
            context['data']['Classification2'] = 'Very High'
        if str(row['wisc5_vci_ss']) == '123':
            context['data']['PR2'] = '94'
            context['data']['Classification2'] = 'Very High'
        if str(row['wisc5_vci_ss']) == '124':
            context['data']['PR2'] = '95'
            context['data']['Classification2'] = 'Very High'
        if str(row['wisc5_vci_ss']) == '125':
            context['data']['PR2'] = '95'
            context['data']['Classification2'] = 'Very High'
        if str(row['wisc5_vci_ss']) == '126':
            context['data']['PR2'] = '96'
            context['data']['Classification2'] = 'Very High'
        if str(row['wisc5_vci_ss']) == '127':
            context['data']['PR2'] = '96'
            context['data']['Classification2'] = 'Very High'
        if str(row['wisc5_vci_ss']) == '128':
            context['data']['PR2'] = '97'
            context['data']['Classification2'] = 'Very High'
        if str(row['wisc5_vci_ss']) == '129':
            context['data']['PR2'] = '97'
            context['data']['Classification2'] = 'Very High'
        if str(row['wisc5_vci_ss']) == '130':
            context['data']['PR2'] = '98'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '131':
            context['data']['PR2'] = '98'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '132':
            context['data']['PR2'] = '98'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '133':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '134':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '135':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '136':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '137':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '138':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '139':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '140':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '141':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '142':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '143':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '144':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '145':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '146':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '147':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '148':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '149':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vci_ss']) == '150':
            context['data']['PR2'] = '99'
            context['data']['Classification2'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '40':
            context['data']['PR3'] = '<0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '41':
            context['data']['PR3'] = '<0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '42':
            context['data']['PR3'] = '<0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '43':
            context['data']['PR3'] = '<0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '44':
            context['data']['PR3'] = '<0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '45':
            context['data']['PR3'] = '<0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '46':
            context['data']['PR3'] = '<0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '47':
            context['data']['PR3'] = '<0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '48':
            context['data']['PR3'] = '<0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '49':
            context['data']['PR3'] = '<0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '50':
            context['data']['PR3'] = '<0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '51':
            context['data']['PR3'] = '<0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '52':
            context['data']['PR3'] = '0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '53':
            context['data']['PR3'] = '0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '54':
            context['data']['PR3'] = '0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '55':
            context['data']['PR3'] = '0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '56':
            context['data']['PR3'] = '0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '57':
            context['data']['PR3'] = '0.1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '58':
            context['data']['PR3'] = '0.2'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '59':
            context['data']['PR3'] = '0.3'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '60':
            context['data']['PR3'] = '0.4'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '61':
            context['data']['PR3'] = '0.5'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '62':
            context['data']['PR3'] = '1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '63':
            context['data']['PR3'] = '1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '64':
            context['data']['PR3'] = '1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '65':
            context['data']['PR3'] = '1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '66':
            context['data']['PR3'] = '1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '67':
            context['data']['PR3'] = '1'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '68':
            context['data']['PR3'] = '2'
            context['data']['Classification3'] = 'Extremely Low'
        if str(row['wisc5_vsi_ss']) == '69':
            context['data']['PR3'] = '2'
            context['data']['Classification3'] = 'Very Low'
        if str(row['wisc5_vsi_ss']) == '70':
            context['data']['PR3'] = '2'
            context['data']['Classification3'] = 'Very Low'
        if str(row['wisc5_vsi_ss']) == '71':
            context['data']['PR3'] = '3'
            context['data']['Classification3'] = 'Very Low'
        if str(row['wisc5_vsi_ss']) == '72':
            context['data']['PR3'] = '3'
            context['data']['Classification3'] = 'Very Low'
        if str(row['wisc5_vsi_ss']) == '73':
            context['data']['PR3'] = '4'
            context['data']['Classification3'] = 'Very Low'
        if str(row['wisc5_vsi_ss']) == '74':
            context['data']['PR3'] = '4'
            context['data']['Classification3'] = 'Very Low'
        if str(row['wisc5_vsi_ss']) == '75':
            context['data']['PR3'] = '5'
            context['data']['Classification3'] = 'Very Low'
        if str(row['wisc5_vsi_ss']) == '76':
            context['data']['PR3'] = '5'
            context['data']['Classification3'] = 'Very Low'
        if str(row['wisc5_vsi_ss']) == '77':
            context['data']['PR3'] = '6'
            context['data']['Classification3'] = 'Very Low'
        if str(row['wisc5_vsi_ss']) == '78':
            context['data']['PR3'] = '7'
            context['data']['Classification3'] = 'Very Low'
        if str(row['wisc5_vsi_ss']) == '79':
            context['data']['PR3'] = '8'
            context['data']['Classification3'] = 'Very Low'
        if str(row['wisc5_vsi_ss']) == '80':
            context['data']['PR3'] = '9'
            context['data']['Classification3'] = 'Low Average'
        if str(row['wisc5_vsi_ss']) == '81':
            context['data']['PR3'] = '10'
            context['data']['Classification3'] = 'Low Average'
        if str(row['wisc5_vsi_ss']) == '82':
            context['data']['PR3'] = '12'
            context['data']['Classification3'] = 'Low Average'
        if str(row['wisc5_vsi_ss']) == '83':
            context['data']['PR3'] = '13'
            context['data']['Classification3'] = 'Low Average'
        if str(row['wisc5_vsi_ss']) == '84':
            context['data']['PR3'] = '14'
            context['data']['Classification3'] = 'Low Average'
        if str(row['wisc5_vsi_ss']) == '85':
            context['data']['PR3'] = '16'
            context['data']['Classification3'] = 'Low Average'
        if str(row['wisc5_vsi_ss']) == '86':
            context['data']['PR3'] = '18'
            context['data']['Classification3'] = 'Low Average'
        if str(row['wisc5_vsi_ss']) == '87':
            context['data']['PR3'] = '19'
            context['data']['Classification3'] = 'Low Average'
        if str(row['wisc5_vsi_ss']) == '88':
            context['data']['PR3'] = '21'
            context['data']['Classification3'] = 'Low Average'
        if str(row['wisc5_vsi_ss']) == '89':
            context['data']['PR3'] = '23'
            context['data']['Classification3'] = 'Low Average'
        if str(row['wisc5_vsi_ss']) == '90':
            context['data']['PR3'] = '25'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '91':
            context['data']['PR3'] = '27'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '92':
            context['data']['PR3'] = '30'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '93':
            context['data']['PR3'] = '32'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '94':
            context['data']['PR3'] = '34'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '95':
            context['data']['PR3'] = '37'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '96':
            context['data']['PR3'] = '40'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '97':
            context['data']['PR3'] = '42'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '98':
            context['data']['PR3'] = '45'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '99':
            context['data']['PR3'] = '47'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '100':
            context['data']['PR3'] = '50'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '101':
            context['data']['PR3'] = '53'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '102':
            context['data']['PR3'] = '55'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '103':
            context['data']['PR3'] = '58'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '104':
            context['data']['PR3'] = '61'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '105':
            context['data']['PR3'] = '63'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '106':
            context['data']['PR3'] = '66'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '107':
            context['data']['PR3'] = '68'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '108':
            context['data']['PR3'] = '70'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '109':
            context['data']['PR3'] = '73'
            context['data']['Classification3'] = 'Average'
        if str(row['wisc5_vsi_ss']) == '110':
            context['data']['PR3'] = '75'
            context['data']['Classification3'] = 'High Average'
        if str(row['wisc5_vsi_ss']) == '111':
            context['data']['PR3'] = '77'
            context['data']['Classification3'] = 'High Average'
        if str(row['wisc5_vsi_ss']) == '112':
            context['data']['PR3'] = '79'
            context['data']['Classification3'] = 'High Average'
        if str(row['wisc5_vsi_ss']) == '113':
            context['data']['PR3'] = '81'
            context['data']['Classification3'] = 'High Average'
        if str(row['wisc5_vsi_ss']) == '114':
            context['data']['PR3'] = '82'
            context['data']['Classification3'] = 'High Average'
        if str(row['wisc5_vsi_ss']) == '115':
            context['data']['PR3'] = '84'
            context['data']['Classification3'] = 'High Average'
        if str(row['wisc5_vsi_ss']) == '116':
            context['data']['PR3'] = '86'
            context['data']['Classification3'] = 'High Average'
        if str(row['wisc5_vsi_ss']) == '117':
            context['data']['PR3'] = '87'
            context['data']['Classification3'] = 'High Average'
        if str(row['wisc5_vsi_ss']) == '118':
            context['data']['PR3'] = '88'
            context['data']['Classification3'] = 'High Average'
        if str(row['wisc5_vsi_ss']) == '119':
            context['data']['PR3'] = '90'
            context['data']['Classification3'] = 'High Average'
        if str(row['wisc5_vsi_ss']) == '120':
            context['data']['PR3'] = '91'
            context['data']['Classification3'] = 'Very High'
        if str(row['wisc5_vsi_ss']) == '121':
            context['data']['PR3'] = '92'
            context['data']['Classification3'] = 'Very High'
        if str(row['wisc5_vsi_ss']) == '122':
            context['data']['PR3'] = '93'
            context['data']['Classification3'] = 'Very High'
        if str(row['wisc5_vsi_ss']) == '123':
            context['data']['PR3'] = '94'
            context['data']['Classification3'] = 'Very High'
        if str(row['wisc5_vsi_ss']) == '124':
            context['data']['PR3'] = '95'
            context['data']['Classification3'] = 'Very High'
        if str(row['wisc5_vsi_ss']) == '125':
            context['data']['PR3'] = '95'
            context['data']['Classification3'] = 'Very High'
        if str(row['wisc5_vsi_ss']) == '126':
            context['data']['PR3'] = '96'
            context['data']['Classification3'] = 'Very High'
        if str(row['wisc5_vsi_ss']) == '127':
            context['data']['PR3'] = '96'
            context['data']['Classification3'] = 'Very High'
        if str(row['wisc5_vsi_ss']) == '128':
            context['data']['PR3'] = '97'
            context['data']['Classification3'] = 'Very High'
        if str(row['wisc5_vsi_ss']) == '129':
            context['data']['PR3'] = '97'
            context['data']['Classification3'] = 'Very High'
        if str(row['wisc5_vsi_ss']) == '130':
            context['data']['PR3'] = '98'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '131':
            context['data']['PR3'] = '98'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '132':
            context['data']['PR3'] = '98'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '133':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '134':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '135':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '136':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '137':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '138':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '139':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '140':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '141':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '142':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '143':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '144':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '145':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '146':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '147':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '148':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '149':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_vsi_ss']) == '150':
            context['data']['PR3'] = '99'
            context['data']['Classification3'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '40':
            context['data']['PR4'] = '<0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '41':
            context['data']['PR4'] = '<0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '42':
            context['data']['PR4'] = '<0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '43':
            context['data']['PR4'] = '<0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '44':
            context['data']['PR4'] = '<0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '45':
            context['data']['PR4'] = '<0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '46':
            context['data']['PR4'] = '<0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '47':
            context['data']['PR4'] = '<0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '48':
            context['data']['PR4'] = '<0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '49':
            context['data']['PR4'] = '<0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '50':
            context['data']['PR4'] = '<0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '51':
            context['data']['PR4'] = '<0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '52':
            context['data']['PR4'] = '0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '53':
            context['data']['PR4'] = '0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '54':
            context['data']['PR4'] = '0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '55':
            context['data']['PR4'] = '0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '56':
            context['data']['PR4'] = '0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '57':
            context['data']['PR4'] = '0.1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '58':
            context['data']['PR4'] = '0.2'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '59':
            context['data']['PR4'] = '0.3'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '60':
            context['data']['PR4'] = '0.4'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '61':
            context['data']['PR4'] = '0.5'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '62':
            context['data']['PR4'] = '1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '63':
            context['data']['PR4'] = '1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '64':
            context['data']['PR4'] = '1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '65':
            context['data']['PR4'] = '1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '66':
            context['data']['PR4'] = '1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '67':
            context['data']['PR4'] = '1'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '68':
            context['data']['PR4'] = '2'
            context['data']['Classification4'] = 'Extremely Low'
        if str(row['wisc5_fri_ss']) == '69':
            context['data']['PR4'] = '2'
            context['data']['Classification4'] = 'Very Low'
        if str(row['wisc5_fri_ss']) == '70':
            context['data']['PR4'] = '2'
            context['data']['Classification4'] = 'Very Low'
        if str(row['wisc5_fri_ss']) == '71':
            context['data']['PR4'] = '3'
            context['data']['Classification4'] = 'Very Low'
        if str(row['wisc5_fri_ss']) == '72':
            context['data']['PR4'] = '3'
            context['data']['Classification4'] = 'Very Low'
        if str(row['wisc5_fri_ss']) == '73':
            context['data']['PR4'] = '4'
            context['data']['Classification4'] = 'Very Low'
        if str(row['wisc5_fri_ss']) == '74':
            context['data']['PR4'] = '4'
            context['data']['Classification4'] = 'Very Low'
        if str(row['wisc5_fri_ss']) == '75':
            context['data']['PR4'] = '5'
            context['data']['Classification4'] = 'Very Low'
        if str(row['wisc5_fri_ss']) == '76':
            context['data']['PR4'] = '5'
            context['data']['Classification4'] = 'Very Low'
        if str(row['wisc5_fri_ss']) == '77':
            context['data']['PR4'] = '6'
            context['data']['Classification4'] = 'Very Low'
        if str(row['wisc5_fri_ss']) == '78':
            context['data']['PR4'] = '7'
            context['data']['Classification4'] = 'Very Low'
        if str(row['wisc5_fri_ss']) == '79':
            context['data']['PR4'] = '8'
            context['data']['Classification4'] = 'Very Low'
        if str(row['wisc5_fri_ss']) == '80':
            context['data']['PR4'] = '9'
            context['data']['Classification4'] = 'Low Average'
        if str(row['wisc5_fri_ss']) == '81':
            context['data']['PR4'] = '10'
            context['data']['Classification4'] = 'Low Average'
        if str(row['wisc5_fri_ss']) == '82':
            context['data']['PR4'] = '12'
            context['data']['Classification4'] = 'Low Average'
        if str(row['wisc5_fri_ss']) == '83':
            context['data']['PR4'] = '13'
            context['data']['Classification4'] = 'Low Average'
        if str(row['wisc5_fri_ss']) == '84':
            context['data']['PR4'] = '14'
            context['data']['Classification4'] = 'Low Average'
        if str(row['wisc5_fri_ss']) == '85':
            context['data']['PR4'] = '16'
            context['data']['Classification4'] = 'Low Average'
        if str(row['wisc5_fri_ss']) == '86':
            context['data']['PR4'] = '18'
            context['data']['Classification4'] = 'Low Average'
        if str(row['wisc5_fri_ss']) == '87':
            context['data']['PR4'] = '19'
            context['data']['Classification4'] = 'Low Average'
        if str(row['wisc5_fri_ss']) == '88':
            context['data']['PR4'] = '21'
            context['data']['Classification4'] = 'Low Average'
        if str(row['wisc5_fri_ss']) == '89':
            context['data']['PR4'] = '23'
            context['data']['Classification4'] = 'Low Average'
        if str(row['wisc5_fri_ss']) == '90':
            context['data']['PR4'] = '25'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '91':
            context['data']['PR4'] = '27'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '92':
            context['data']['PR4'] = '30'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '93':
            context['data']['PR4'] = '32'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '94':
            context['data']['PR4'] = '34'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '95':
            context['data']['PR4'] = '37'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '96':
            context['data']['PR4'] = '40'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '97':
            context['data']['PR4'] = '42'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '98':
            context['data']['PR4'] = '45'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '99':
            context['data']['PR4'] = '47'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '100':
            context['data']['PR4'] = '50'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '101':
            context['data']['PR4'] = '53'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '102':
            context['data']['PR4'] = '55'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '103':
            context['data']['PR4'] = '58'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '104':
            context['data']['PR4'] = '61'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '105':
            context['data']['PR4'] = '63'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '106':
            context['data']['PR4'] = '66'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '107':
            context['data']['PR4'] = '68'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '108':
            context['data']['PR4'] = '70'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '109':
            context['data']['PR4'] = '73'
            context['data']['Classification4'] = 'Average'
        if str(row['wisc5_fri_ss']) == '110':
            context['data']['PR4'] = '75'
            context['data']['Classification4'] = 'High Average'
        if str(row['wisc5_fri_ss']) == '111':
            context['data']['PR4'] = '77'
            context['data']['Classification4'] = 'High Average'
        if str(row['wisc5_fri_ss']) == '112':
            context['data']['PR4'] = '79'
            context['data']['Classification4'] = 'High Average'
        if str(row['wisc5_fri_ss']) == '113':
            context['data']['PR4'] = '81'
            context['data']['Classification4'] = 'High Average'
        if str(row['wisc5_fri_ss']) == '114':
            context['data']['PR4'] = '82'
            context['data']['Classification4'] = 'High Average'
        if str(row['wisc5_fri_ss']) == '115':
            context['data']['PR4'] = '84'
            context['data']['Classification4'] = 'High Average'
        if str(row['wisc5_fri_ss']) == '116':
            context['data']['PR4'] = '86'
            context['data']['Classification4'] = 'High Average'
        if str(row['wisc5_fri_ss']) == '117':
            context['data']['PR4'] = '87'
            context['data']['Classification4'] = 'High Average'
        if str(row['wisc5_fri_ss']) == '118':
            context['data']['PR4'] = '88'
            context['data']['Classification4'] = 'High Average'
        if str(row['wisc5_fri_ss']) == '119':
            context['data']['PR4'] = '90'
            context['data']['Classification4'] = 'High Average'
        if str(row['wisc5_fri_ss']) == '120':
            context['data']['PR4'] = '91'
            context['data']['Classification4'] = 'Very High'
        if str(row['wisc5_fri_ss']) == '121':
            context['data']['PR4'] = '92'
            context['data']['Classification4'] = 'Very High'
        if str(row['wisc5_fri_ss']) == '122':
            context['data']['PR4'] = '93'
            context['data']['Classification4'] = 'Very High'
        if str(row['wisc5_fri_ss']) == '123':
            context['data']['PR4'] = '94'
            context['data']['Classification4'] = 'Very High'
        if str(row['wisc5_fri_ss']) == '124':
            context['data']['PR4'] = '95'
            context['data']['Classification4'] = 'Very High'
        if str(row['wisc5_fri_ss']) == '125':
            context['data']['PR4'] = '95'
            context['data']['Classification4'] = 'Very High'
        if str(row['wisc5_fri_ss']) == '126':
            context['data']['PR4'] = '96'
            context['data']['Classification4'] = 'Very High'
        if str(row['wisc5_fri_ss']) == '127':
            context['data']['PR4'] = '96'
            context['data']['Classification4'] = 'Very High'
        if str(row['wisc5_fri_ss']) == '128':
            context['data']['PR4'] = '97'
            context['data']['Classification4'] = 'Very High'
        if str(row['wisc5_fri_ss']) == '129':
            context['data']['PR4'] = '97'
            context['data']['Classification4'] = 'Very High'
        if str(row['wisc5_fri_ss']) == '130':
            context['data']['PR4'] = '98'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '131':
            context['data']['PR4'] = '98'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '132':
            context['data']['PR4'] = '98'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '133':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '134':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '135':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '136':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '137':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '138':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '139':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '140':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '141':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '142':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '143':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '144':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '145':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '146':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '147':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '148':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '149':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_fri_ss']) == '150':
            context['data']['PR4'] = '99'
            context['data']['Classification4'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '40':
            context['data']['PR5'] = '<0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '41':
            context['data']['PR5'] = '<0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '42':
            context['data']['PR5'] = '<0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '43':
            context['data']['PR5'] = '<0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '44':
            context['data']['PR5'] = '<0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '45':
            context['data']['PR5'] = '<0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '46':
            context['data']['PR5'] = '<0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '47':
            context['data']['PR5'] = '<0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '48':
            context['data']['PR5'] = '<0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '49':
            context['data']['PR5'] = '<0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '50':
            context['data']['PR5'] = '<0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '51':
            context['data']['PR5'] = '<0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '52':
            context['data']['PR5'] = '0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '53':
            context['data']['PR5'] = '0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '54':
            context['data']['PR5'] = '0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '55':
            context['data']['PR5'] = '0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '56':
            context['data']['PR5'] = '0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '57':
            context['data']['PR5'] = '0.1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '58':
            context['data']['PR5'] = '0.2'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '59':
            context['data']['PR5'] = '0.3'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '60':
            context['data']['PR5'] = '0.4'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '61':
            context['data']['PR5'] = '0.5'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '62':
            context['data']['PR5'] = '1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '63':
            context['data']['PR5'] = '1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '64':
            context['data']['PR5'] = '1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '65':
            context['data']['PR5'] = '1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '66':
            context['data']['PR5'] = '1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '67':
            context['data']['PR5'] = '1'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '68':
            context['data']['PR5'] = '2'
            context['data']['Classification5'] = 'Extremely Low'
        if str(row['wisc5_wmi_ss']) == '69':
            context['data']['PR5'] = '2'
            context['data']['Classification5'] = 'Very Low'
        if str(row['wisc5_wmi_ss']) == '70':
            context['data']['PR5'] = '2'
            context['data']['Classification5'] = 'Very Low'
        if str(row['wisc5_wmi_ss']) == '71':
            context['data']['PR5'] = '3'
            context['data']['Classification5'] = 'Very Low'
        if str(row['wisc5_wmi_ss']) == '72':
            context['data']['PR5'] = '3'
            context['data']['Classification5'] = 'Very Low'
        if str(row['wisc5_wmi_ss']) == '73':
            context['data']['PR5'] = '4'
            context['data']['Classification5'] = 'Very Low'
        if str(row['wisc5_wmi_ss']) == '74':
            context['data']['PR5'] = '4'
            context['data']['Classification5'] = 'Very Low'
        if str(row['wisc5_wmi_ss']) == '75':
            context['data']['PR5'] = '5'
            context['data']['Classification5'] = 'Very Low'
        if str(row['wisc5_wmi_ss']) == '76':
            context['data']['PR5'] = '5'
            context['data']['Classification5'] = 'Very Low'
        if str(row['wisc5_wmi_ss']) == '77':
            context['data']['PR5'] = '6'
            context['data']['Classification5'] = 'Very Low'
        if str(row['wisc5_wmi_ss']) == '78':
            context['data']['PR5'] = '7'
            context['data']['Classification5'] = 'Very Low'
        if str(row['wisc5_wmi_ss']) == '79':
            context['data']['PR5'] = '8'
            context['data']['Classification5'] = 'Very Low'
        if str(row['wisc5_wmi_ss']) == '80':
            context['data']['PR5'] = '9'
            context['data']['Classification5'] = 'Low Average'
        if str(row['wisc5_wmi_ss']) == '81':
            context['data']['PR5'] = '10'
            context['data']['Classification5'] = 'Low Average'
        if str(row['wisc5_wmi_ss']) == '82':
            context['data']['PR5'] = '12'
            context['data']['Classification5'] = 'Low Average'
        if str(row['wisc5_wmi_ss']) == '83':
            context['data']['PR5'] = '13'
            context['data']['Classification5'] = 'Low Average'
        if str(row['wisc5_wmi_ss']) == '84':
            context['data']['PR5'] = '14'
            context['data']['Classification5'] = 'Low Average'
        if str(row['wisc5_wmi_ss']) == '85':
            context['data']['PR5'] = '16'
            context['data']['Classification5'] = 'Low Average'
        if str(row['wisc5_wmi_ss']) == '86':
            context['data']['PR5'] = '18'
            context['data']['Classification5'] = 'Low Average'
        if str(row['wisc5_wmi_ss']) == '87':
            context['data']['PR5'] = '19'
            context['data']['Classification5'] = 'Low Average'
        if str(row['wisc5_wmi_ss']) == '88':
            context['data']['PR5'] = '21'
            context['data']['Classification5'] = 'Low Average'
        if str(row['wisc5_wmi_ss']) == '89':
            context['data']['PR5'] = '23'
            context['data']['Classification5'] = 'Low Average'
        if str(row['wisc5_wmi_ss']) == '90':
            context['data']['PR5'] = '25'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '91':
            context['data']['PR5'] = '27'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '92':
            context['data']['PR5'] = '30'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '93':
            context['data']['PR5'] = '32'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '94':
            context['data']['PR5'] = '34'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '95':
            context['data']['PR5'] = '37'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '96':
            context['data']['PR5'] = '40'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '97':
            context['data']['PR5'] = '42'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '98':
            context['data']['PR5'] = '45'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '99':
            context['data']['PR5'] = '47'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '100':
            context['data']['PR5'] = '50'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '101':
            context['data']['PR5'] = '53'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '102':
            context['data']['PR5'] = '55'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '103':
            context['data']['PR5'] = '58'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '104':
            context['data']['PR5'] = '61'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '105':
            context['data']['PR5'] = '63'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '106':
            context['data']['PR5'] = '66'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '107':
            context['data']['PR5'] = '68'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '108':
            context['data']['PR5'] = '70'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '109':
            context['data']['PR5'] = '73'
            context['data']['Classification5'] = 'Average'
        if str(row['wisc5_wmi_ss']) == '110':
            context['data']['PR5'] = '75'
            context['data']['Classification5'] = 'High Average'
        if str(row['wisc5_wmi_ss']) == '111':
            context['data']['PR5'] = '77'
            context['data']['Classification5'] = 'High Average'
        if str(row['wisc5_wmi_ss']) == '112':
            context['data']['PR5'] = '79'
            context['data']['Classification5'] = 'High Average'
        if str(row['wisc5_wmi_ss']) == '113':
            context['data']['PR5'] = '81'
            context['data']['Classification5'] = 'High Average'
        if str(row['wisc5_wmi_ss']) == '114':
            context['data']['PR5'] = '82'
            context['data']['Classification5'] = 'High Average'
        if str(row['wisc5_wmi_ss']) == '115':
            context['data']['PR5'] = '84'
            context['data']['Classification5'] = 'High Average'
        if str(row['wisc5_wmi_ss']) == '116':
            context['data']['PR5'] = '86'
            context['data']['Classification5'] = 'High Average'
        if str(row['wisc5_wmi_ss']) == '117':
            context['data']['PR5'] = '87'
            context['data']['Classification5'] = 'High Average'
        if str(row['wisc5_wmi_ss']) == '118':
            context['data']['PR5'] = '88'
            context['data']['Classification5'] = 'High Average'
        if str(row['wisc5_wmi_ss']) == '119':
            context['data']['PR5'] = '90'
            context['data']['Classification5'] = 'High Average'
        if str(row['wisc5_wmi_ss']) == '120':
            context['data']['PR5'] = '91'
            context['data']['Classification5'] = 'Very High'
        if str(row['wisc5_wmi_ss']) == '121':
            context['data']['PR5'] = '92'
            context['data']['Classification5'] = 'Very High'
        if str(row['wisc5_wmi_ss']) == '122':
            context['data']['PR5'] = '93'
            context['data']['Classification5'] = 'Very High'
        if str(row['wisc5_wmi_ss']) == '123':
            context['data']['PR5'] = '94'
            context['data']['Classification5'] = 'Very High'
        if str(row['wisc5_wmi_ss']) == '124':
            context['data']['PR5'] = '95'
            context['data']['Classification5'] = 'Very High'
        if str(row['wisc5_wmi_ss']) == '125':
            context['data']['PR5'] = '95'
            context['data']['Classification5'] = 'Very High'
        if str(row['wisc5_wmi_ss']) == '126':
            context['data']['PR5'] = '96'
            context['data']['Classification5'] = 'Very High'
        if str(row['wisc5_wmi_ss']) == '127':
            context['data']['PR5'] = '96'
            context['data']['Classification5'] = 'Very High'
        if str(row['wisc5_wmi_ss']) == '128':
            context['data']['PR5'] = '97'
            context['data']['Classification5'] = 'Very High'
        if str(row['wisc5_wmi_ss']) == '129':
            context['data']['PR5'] = '97'
            context['data']['Classification5'] = 'Very High'
        if str(row['wisc5_wmi_ss']) == '130':
            context['data']['PR5'] = '98'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '131':
            context['data']['PR5'] = '98'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '132':
            context['data']['PR5'] = '98'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '133':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '134':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '135':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '136':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '137':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '138':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '139':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '140':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '141':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '142':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '143':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '144':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '145':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '146':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '147':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '148':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '149':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_wmi_ss']) == '150':
            context['data']['PR5'] = '99'
            context['data']['Classification5'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '40':
            context['data']['PR6'] = '<0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '41':
            context['data']['PR6'] = '<0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '42':
            context['data']['PR6'] = '<0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '43':
            context['data']['PR6'] = '<0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '44':
            context['data']['PR6'] = '<0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '45':
            context['data']['PR6'] = '<0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '46':
            context['data']['PR6'] = '<0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '47':
            context['data']['PR6'] = '<0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '48':
            context['data']['PR6'] = '<0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '49':
            context['data']['PR6'] = '<0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '50':
            context['data']['PR6'] = '<0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '51':
            context['data']['PR6'] = '<0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '52':
            context['data']['PR6'] = '0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '53':
            context['data']['PR6'] = '0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '54':
            context['data']['PR6'] = '0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '55':
            context['data']['PR6'] = '0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '56':
            context['data']['PR6'] = '0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '57':
            context['data']['PR6'] = '0.1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '58':
            context['data']['PR6'] = '0.2'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '59':
            context['data']['PR6'] = '0.3'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '60':
            context['data']['PR6'] = '0.4'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '61':
            context['data']['PR6'] = '0.5'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '62':
            context['data']['PR6'] = '1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '63':
            context['data']['PR6'] = '1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '64':
            context['data']['PR6'] = '1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '65':
            context['data']['PR6'] = '1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '66':
            context['data']['PR6'] = '1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '67':
            context['data']['PR6'] = '1'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '68':
            context['data']['PR6'] = '2'
            context['data']['Classification6'] = 'Extremely Low'
        if str(row['wisc5_psi_ss']) == '69':
            context['data']['PR6'] = '2'
            context['data']['Classification6'] = 'Very Low'
        if str(row['wisc5_psi_ss']) == '70':
            context['data']['PR6'] = '2'
            context['data']['Classification6'] = 'Very Low'
        if str(row['wisc5_psi_ss']) == '71':
            context['data']['PR6'] = '3'
            context['data']['Classification6'] = 'Very Low'
        if str(row['wisc5_psi_ss']) == '72':
            context['data']['PR6'] = '3'
            context['data']['Classification6'] = 'Very Low'
        if str(row['wisc5_psi_ss']) == '73':
            context['data']['PR6'] = '4'
            context['data']['Classification6'] = 'Very Low'
        if str(row['wisc5_psi_ss']) == '74':
            context['data']['PR6'] = '4'
            context['data']['Classification6'] = 'Very Low'
        if str(row['wisc5_psi_ss']) == '75':
            context['data']['PR6'] = '5'
            context['data']['Classification6'] = 'Very Low'
        if str(row['wisc5_psi_ss']) == '76':
            context['data']['PR6'] = '5'
            context['data']['Classification6'] = 'Very Low'
        if str(row['wisc5_psi_ss']) == '77':
            context['data']['PR6'] = '6'
            context['data']['Classification6'] = 'Very Low'
        if str(row['wisc5_psi_ss']) == '78':
            context['data']['PR6'] = '7'
            context['data']['Classification6'] = 'Very Low'
        if str(row['wisc5_psi_ss']) == '79':
            context['data']['PR6'] = '8'
            context['data']['Classification6'] = 'Very Low'
        if str(row['wisc5_psi_ss']) == '80':
            context['data']['PR6'] = '9'
            context['data']['Classification6'] = 'Low Average'
        if str(row['wisc5_psi_ss']) == '81':
            context['data']['PR6'] = '10'
            context['data']['Classification6'] = 'Low Average'
        if str(row['wisc5_psi_ss']) == '82':
            context['data']['PR6'] = '12'
            context['data']['Classification6'] = 'Low Average'
        if str(row['wisc5_psi_ss']) == '83':
            context['data']['PR6'] = '13'
            context['data']['Classification6'] = 'Low Average'
        if str(row['wisc5_psi_ss']) == '84':
            context['data']['PR6'] = '14'
            context['data']['Classification6'] = 'Low Average'
        if str(row['wisc5_psi_ss']) == '85':
            context['data']['PR6'] = '16'
            context['data']['Classification6'] = 'Low Average'
        if str(row['wisc5_psi_ss']) == '86':
            context['data']['PR6'] = '18'
            context['data']['Classification6'] = 'Low Average'
        if str(row['wisc5_psi_ss']) == '87':
            context['data']['PR6'] = '19'
            context['data']['Classification6'] = 'Low Average'
        if str(row['wisc5_psi_ss']) == '88':
            context['data']['PR6'] = '21'
            context['data']['Classification6'] = 'Low Average'
        if str(row['wisc5_psi_ss']) == '89':
            context['data']['PR6'] = '23'
            context['data']['Classification6'] = 'Low Average'
        if str(row['wisc5_psi_ss']) == '90':
            context['data']['PR6'] = '25'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '91':
            context['data']['PR6'] = '27'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '92':
            context['data']['PR6'] = '30'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '93':
            context['data']['PR6'] = '32'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '94':
            context['data']['PR6'] = '34'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '95':
            context['data']['PR6'] = '37'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '96':
            context['data']['PR6'] = '40'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '97':
            context['data']['PR6'] = '42'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '98':
            context['data']['PR6'] = '45'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '99':
            context['data']['PR6'] = '47'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '100':
            context['data']['PR6'] = '50'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '101':
            context['data']['PR6'] = '53'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '102':
            context['data']['PR6'] = '55'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '103':
            context['data']['PR6'] = '58'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '104':
            context['data']['PR6'] = '61'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '105':
            context['data']['PR6'] = '63'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '106':
            context['data']['PR6'] = '66'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '107':
            context['data']['PR6'] = '68'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '108':
            context['data']['PR6'] = '70'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '109':
            context['data']['PR6'] = '73'
            context['data']['Classification6'] = 'Average'
        if str(row['wisc5_psi_ss']) == '110':
            context['data']['PR6'] = '75'
            context['data']['Classification6'] = 'High Average'
        if str(row['wisc5_psi_ss']) == '111':
            context['data']['PR6'] = '77'
            context['data']['Classification6'] = 'High Average'
        if str(row['wisc5_psi_ss']) == '112':
            context['data']['PR6'] = '79'
            context['data']['Classification6'] = 'High Average'
        if str(row['wisc5_psi_ss']) == '113':
            context['data']['PR6'] = '81'
            context['data']['Classification6'] = 'High Average'
        if str(row['wisc5_psi_ss']) == '114':
            context['data']['PR6'] = '82'
            context['data']['Classification6'] = 'High Average'
        if str(row['wisc5_psi_ss']) == '115':
            context['data']['PR6'] = '84'
            context['data']['Classification6'] = 'High Average'
        if str(row['wisc5_psi_ss']) == '116':
            context['data']['PR6'] = '86'
            context['data']['Classification6'] = 'High Average'
        if str(row['wisc5_psi_ss']) == '117':
            context['data']['PR6'] = '87'
            context['data']['Classification6'] = 'High Average'
        if str(row['wisc5_psi_ss']) == '118':
            context['data']['PR6'] = '88'
            context['data']['Classification6'] = 'High Average'
        if str(row['wisc5_psi_ss']) == '119':
            context['data']['PR6'] = '90'
            context['data']['Classification6'] = 'High Average'
        if str(row['wisc5_psi_ss']) == '120':
            context['data']['PR6'] = '91'
            context['data']['Classification6'] = 'Very High'
        if str(row['wisc5_psi_ss']) == '121':
            context['data']['PR6'] = '92'
            context['data']['Classification6'] = 'Very High'
        if str(row['wisc5_psi_ss']) == '122':
            context['data']['PR6'] = '93'
            context['data']['Classification6'] = 'Very High'
        if str(row['wisc5_psi_ss']) == '123':
            context['data']['PR6'] = '94'
            context['data']['Classification6'] = 'Very High'
        if str(row['wisc5_psi_ss']) == '124':
            context['data']['PR6'] = '95'
            context['data']['Classification6'] = 'Very High'
        if str(row['wisc5_psi_ss']) == '125':
            context['data']['PR6'] = '95'
            context['data']['Classification6'] = 'Very High'
        if str(row['wisc5_psi_ss']) == '126':
            context['data']['PR6'] = '96'
            context['data']['Classification6'] = 'Very High'
        if str(row['wisc5_psi_ss']) == '127':
            context['data']['PR6'] = '96'
            context['data']['Classification6'] = 'Very High'
        if str(row['wisc5_psi_ss']) == '128':
            context['data']['PR6'] = '97'
            context['data']['Classification6'] = 'Very High'
        if str(row['wisc5_psi_ss']) == '129':
            context['data']['PR6'] = '97'
            context['data']['Classification6'] = 'Very High'
        if str(row['wisc5_psi_ss']) == '130':
            context['data']['PR6'] = '98'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '131':
            context['data']['PR6'] = '98'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '132':
            context['data']['PR6'] = '98'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '133':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '134':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '135':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '136':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '137':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '138':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '139':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '140':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '141':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '142':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '143':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '144':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '145':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '146':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '147':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '148':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '149':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'
        if str(row['wisc5_psi_ss']) == '150':
            context['data']['PR6'] = '99'
            context['data']['Classification6'] = 'Extremely High'

        # Render the template with the context data
        doc.render(context)

        # Generate the output file name based on row data
        output_docx_path = os.path.join(output_folder, f"{row['FirstName']}.docx")

        # Save the output Word document
        doc.save(output_docx_path)

    print("Word documents generated successfully.")

# Create the PySimpleGUI layout
layout = [
    [sg.Text('CSV File Path: '), sg.Input(), sg.FileBrowse(key='-CSV-')],
    [sg.Button('Generate Documents')]
]

# Create the PySimpleGUI window
window = sg.Window('Generate Docements', layout, finalize=True)

# Event loop
while True:
    event, values = window.read(timeout=0)
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Generate Documents':
        # Set the file paths and folder
        csv_file_path = values['-CSV-']
        docx_template_path = 'template.docx'
        output_folder = 'Completed WISC-V Reports'

        # Call the function to generate Word documents
        generate_word_documents(csv_file_path, docx_template_path, output_folder)
        sg.Popup('Documents generated successfully!', title='Success')

# Close the window
window.close()

