from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["PROJECT"]

collections = {
    "HeartProject": db["HeartProject"],
    "LungsProject": db["LungsProject"],
    "KidneyProject": db["KidneyProject"],
    "BrainProject": db["BrainProject"],
    "OrthoProject": db["OrthoProject"],
    "DiabetesProject": db["DiabetesProject"],
}

# ---------------- CREATE ---------------- #
def create_patient(collection_name, patient_data):
    collection = collections[collection_name]

    if collection.find_one({"PatientID": patient_data["PatientID"]}):
        return False, "Patient ID already exists"

    collection.insert_one(patient_data)
    return True, "Patient registered successfully"


# ---------------- UPDATE ---------------- #
def update_patient(collection_name, patient_id, update_data):
    collection = collections[collection_name]

    result = collection.update_one(
        {"PatientID": patient_id},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        return False, "Patient ID not found"

    return True, "Patient updated successfully"


# ---------------- DELETE ---------------- #
def delete_patient(patient_id):
    deleted_from = []

    for name, collection in collections.items():
        result = collection.delete_one({"PatientID": patient_id})
        if result.deleted_count > 0:
            deleted_from.append(name)

    if not deleted_from:
        return False, "Patient ID not found"

    return True, f"Patient deleted from {', '.join(deleted_from)}"


# ---------------- SEARCH ---------------- #
def search_patient(patient_id):
    results = []

    for name, collection in collections.items():
        patient = collection.find_one({"PatientID": patient_id}, {"_id": 0})
        if patient:
            results.append({
                "Department": name,
                "Data": patient
            })

    if not results:
        return False, "No patient found"

    return True, results
