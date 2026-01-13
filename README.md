**1. Install Visual Studio Code (VS Code)**

Download VS Code from the official site: https://code.visualstudio.com/download.
Follow the installation instructions based on your operating system (Windows, macOS, Linux).
Once installed, open VS Code and set up your preferred extensions for Python development (e.g., Python, Pylance).

**2. Install MongoDB Compass**

Download MongoDB Compass from: https://www.mongodb.com/products/compass.
Install it by following the on-screen instructions.
Use this tool to visually interact with your MongoDB databases.

**3. Install Python**

Download the latest version of Python from: https://www.python.org/downloads/.
Install it, ensuring you check the option to add Python to your system PATH.
Verify the installation by opening a terminal and typing:
python --version

**4. Install Pymongo (Python MongoDB driver)**

Open a terminal or command prompt and run:
pip install pymongo

**Database Information**

1. BrainProject:
This database stores information related to brain-related diseases and conditions, patient medical histories, and relevant treatments.

2. DiabetesProject:
Focused on managing and analyzing diabetic patients’ data, this database includes blood sugar levels, A1C readings, insulin doses, and other relevant health metrics.

3. HeartProject:
This database handles cardiology-related data, including heart rate, ECG readings, cholesterol levels, and patient histories for heart conditions.

4. KidneyProject:
This project focuses on kidney health, including blood tests, creatinine levels, and data regarding kidney diseases and treatments.

5. LungsProject:
This database contains data on lung diseases, including spirometry readings, oxygen levels, and patient histories with respiratory issues.

6. OrthoProject:
This database deals with orthopedic data such as bone density, X-ray records, and patient conditions related to bone health and musculoskeletal disorders.

Code Files Overview
1. hospital.py:
This file contains the main hospital system logic. It coordinates the interaction between different parts of the hospital system, including managing patients, interacting with the database, and handling other hospital functions.

2. menu.py:
This file provides the user interface (UI) for the system. It includes options for navigating through the various functions of the hospital system, like adding new patients, viewing medical records, or updating data.

3. patient.py:
This file handles patient-related operations. It defines the data structure for a patient, methods to retrieve and update patient information, and functions to interface with the databases to store or fetch patient data.
