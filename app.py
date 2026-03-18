
from flask import Flask, render_template, request, redirect, url_for
from models import Patient  # Requirement: Import your OOP class

app = Flask(__name__)

# DATA STRUCTURE: Implementing a Queue (First-In, First-Out)
patient_queue = []
total_treated = 0

@app.route('/')
def index():
    # Route 1: Dashboard to view the queue [Requirement: Web UI]
    return render_template('index.html', queue=patient_queue, total=total_treated)

@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    # Route 2: Form to add patients [Requirement: Web UI]
    if request.method == 'POST':
        name = request.form.get('name')
        ailment = request.form.get('ailment')
        
        if name and ailment:
            # Instantiate the Patient Class [Requirement: OOP]
            new_patient = Patient(name, ailment)
            # Add to the end of the list (Queue behavior)
            patient_queue.append(new_patient)
            
        return redirect(url_for('index'))
    return render_template('add_patient.html')

@app.route('/treat')
def treat_patient():
    global total_treated
    if patient_queue:
        # FIFO: Remove the first person who arrived [Requirement: Queue Logic]
        patient_queue.pop(0) 
        total_treated += 1
    return redirect(url_for('index'))

@app.route('/clear')
def clear_queue():
    # NEW FEATURE: Logic to reset the patient queue for Push 11
    global patient_queue, total_treated
    patient_queue = []
    total_treated = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
