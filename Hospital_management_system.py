class HospitalManagementSystem():
    def __init__(self):
        self.Patients = []
    
    def add_patient(self,patient_id,name,age,gender,diagnosis):       
        patient = {
            'ID' : patient_id,
            'Name' : name,
            'Age' : age,
            'Gender': gender,
            'Diagnosis' : diagnosis 
        }
        
        self.Patients.append(patient)
        
    def display_all_patients_details(self):
        for patient in self.Patients:
            print(patient)
            
    def search_patient_details_by_ID(self,patient_id):
        for patient in self.Patients:
            if patient['ID'] == patient_id:
                return patient
        return None
    
    def delete_patient_details_by_ID(self,patient_id):
        for patient in self.Patients:
            if patient['ID'] == patient_id:
                self.Patients.remove(patient)
                return True
        return False
    
    def update_patient_details_by_ID(self,patient_id,updated_info):
        for patient in self.Patients:
            if patient['ID'] == patient_id:
                patient.update(updated_info)
                return True
        return False
                
        
hospital = HospitalManagementSystem()
while True:
    print('ADD PATIENT DETAILS         ENTER - 1')
    print('DISPLAY ALL PATIENT DETAILS ENTER - 2')
    print('SEARCH PATIENT DETAILS      ENTER - 3')
    print('DELETE PATIENT DETAILS      ENTER - 4')
    print('UPDATE PATIENT DETAILS      ENTER - 5')
    print('LOGOUT / EXIT PROGRAM       ENTER - 6 ')
    choose_one = input('Enter option 1/2/3/4/5/6: ')
    if '1' == choose_one:
        print('ADD patient details:')
        patient_id = int(input('Enter the ID: '))
        name = input('Enter the name: ')
        age = input('Enter the age: ')
        gender = input('Enter the gender: ')
        diagnosis = input('Enter the diagnosis: ')
        hospital.add_patient(patient_id,name,age,gender,diagnosis)
        hospital.display_all_patients_details()
        
    elif '2' == choose_one:
        print('DISPLAY ALL patient details:')
        hospital.display_all_patients_details()
        
    elif '3' == choose_one:
        print('SEARCH patient details:')
        id_patient = int(input('Enter patient ID: '))
        search_patient = hospital.search_patient_details_by_ID(id_patient)
        if search_patient:
            print(search_patient)
        else:
            print(f'patient ID {id_patient} not found')
            
    elif '4' == choose_one:
        print('DELETE patient details:')
        id_patient = int(input('Enter patient ID: '))
        delete_patient = hospital.delete_patient_details_by_ID(id_patient)
        if delete_patient:
            print(f'patient ID {id_patient} details removed from list')
            hospital.display_all_patients_details()
        else:
            print(f'patient ID {id_patient} not found')
            
    elif '5' == choose_one:
        print('UPDATE patient details:')
        id_patient = int(input('Enter patient ID: '))
        key = input('Enter the key (ID/Name/Age/Gender/Diagnosis): ')
        value = input('Enter the update value: ')
        updated_info = {key : value}
        update_data = hospital.update_patient_details_by_ID(id_patient,updated_info)
        if update_data:
            updated_details = hospital.search_patient_details_by_ID(id_patient)
            print(updated_details)
        else:
            print(f'patient ID {id_patient} not found')
            
    else:
        print('Thankyou! , Visit Again...')
        break

