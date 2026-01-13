from tkinter import *
import tkinter.messagebox as msg
from hospital import create_patient, update_patient, delete_patient, search_patient


class Patient:
    def __init__(self, master, mode="register"):
        self.master = master
        self.mode = mode
        self.master.title(f"{mode.capitalize()} Patient")
        self.master.geometry("600x520")
        self.master.config(bg="lightblue")

        Label(
            master,
            text=f"{mode.capitalize()} Patient",
            font=("Helvetica", 16, "bold"),
            bg="lightblue",
            fg="#350d42",
        ).pack(pady=20)

        # Variables
        self.patient_id = StringVar()
        self.name = StringVar()
        self.age = IntVar()
        self.gender = StringVar()
        self.domain = StringVar()
        self.aadhaar = StringVar()
        self.diagnosis = StringVar()
        self.diagnosis_date = StringVar()
        self.symptoms = StringVar()
        self.treatment = StringVar()
        self.family_history = StringVar()

        self.create_widgets()

    # ---------------- UI ---------------- #
    def create_widgets(self):
        frame = Frame(self.master, bg="lightblue")
        frame.pack(padx=20, pady=10)

        Label(frame, text="Patient ID:", bg="lightblue").grid(row=0, column=0, sticky=W)
        Entry(frame, textvariable=self.patient_id).grid(row=0, column=1)

        if self.mode in ["register", "update"]:
            Label(frame, text="Aadhaar No:", bg="lightblue").grid(row=1, column=0, sticky=W)
            Entry(frame, textvariable=self.aadhaar).grid(row=1, column=1)

            Label(frame, text="Name:", bg="lightblue").grid(row=2, column=0, sticky=W)
            Entry(frame, textvariable=self.name).grid(row=2, column=1)

            Label(frame, text="Age:", bg="lightblue").grid(row=3, column=0, sticky=W)
            Entry(frame, textvariable=self.age).grid(row=3, column=1)

            Label(frame, text="Gender:", bg="lightblue").grid(row=4, column=0, sticky=W)
            OptionMenu(frame, self.gender, "Male", "Female", "Other").grid(row=4, column=1)

            Label(frame, text="Domain:", bg="lightblue").grid(row=5, column=0, sticky=W)
            OptionMenu(
                frame,
                self.domain,
                "HeartProject",
                "LungsProject",
                "KidneyProject",
                "BrainProject",
                "OrthoProject",
                "DiabetesProject",
            ).grid(row=5, column=1)

            Label(frame, text="Diagnosis:", bg="lightblue").grid(row=6, column=0, sticky=W)
            Entry(frame, textvariable=self.diagnosis).grid(row=6, column=1)

            Label(frame, text="Diagnosis Date:", bg="lightblue").grid(row=7, column=0, sticky=W)
            Entry(frame, textvariable=self.diagnosis_date).grid(row=7, column=1)

            Label(frame, text="Symptoms:", bg="lightblue").grid(row=8, column=0, sticky=W)
            Entry(frame, textvariable=self.symptoms).grid(row=8, column=1)

            Label(frame, text="Treatment:", bg="lightblue").grid(row=9, column=0, sticky=W)
            Entry(frame, textvariable=self.treatment).grid(row=9, column=1)

            Label(frame, text="Family History:", bg="lightblue").grid(row=10, column=0, sticky=W)
            Entry(frame, textvariable=self.family_history).grid(row=10, column=1)

        # Buttons
        Button(frame, text=self.mode.capitalize(), command=self.perform_action,
               bg="green", fg="white", width=15).grid(row=12, column=0, pady=20)

        Button(frame, text="Clear", command=self.clear_form,
               bg="gray", fg="white", width=15).grid(row=12, column=1)

    # ---------------- LOGIC ---------------- #
    def perform_action(self):
        if self.mode == "register":
            self.register()
        elif self.mode == "update":
            self.update()
        elif self.mode == "search":
            self.search()
        elif self.mode == "delete":
            self.delete()

    def register(self):
        if len(self.aadhaar.get()) != 12:
            msg.showwarning("Error", "Aadhaar must be 12 digits")
            return

        data = {
            "PatientID": self.patient_id.get(),
            "Name": self.name.get(),
            "Age": self.age.get(),
            "Gender": self.gender.get(),
            "AadhaarCard": int(self.aadhaar.get()),
            "Diagnosis": self.diagnosis.get(),
            "DiagnosisDate": self.diagnosis_date.get(),
            "Symptoms": self.symptoms.get(),
            "Treatment": self.treatment.get(),
            "FamilyHistory": self.family_history.get(),
        }

        status, message = create_patient(self.domain.get(), data)
        msg.showinfo("Status", message)
        if status:
            self.clear_form()

    def update(self):
        data = {
            "Name": self.name.get(),
            "Age": self.age.get(),
            "Gender": self.gender.get(),
            "Diagnosis": self.diagnosis.get(),
            "DiagnosisDate": self.diagnosis_date.get(),
            "Symptoms": self.symptoms.get(),
            "Treatment": self.treatment.get(),
            "FamilyHistory": self.family_history.get(),
        }

        status, message = update_patient(self.domain.get(), self.patient_id.get(), data)
        msg.showinfo("Status", message)

    def search(self):
        status, result = search_patient(self.patient_id.get())
        if not status:
            msg.showinfo("Result", result)
            return

        win = Toplevel(self.master)
        win.title("Search Result")
        win.geometry("500x400")

        text = Text(win)
        text.pack(expand=True, fill=BOTH)

        for r in result:
            text.insert(END, f"Department: {r['Department']}\n")
            for k, v in r["Data"].items():
                text.insert(END, f"{k}: {v}\n")
            text.insert(END, "-" * 40 + "\n")

    def delete(self):
        status, message = delete_patient(self.patient_id.get())
        msg.showinfo("Status", message)
        if status:
            self.clear_form()

    def clear_form(self):
        for var in [
            self.patient_id, self.name, self.gender, self.domain,
            self.aadhaar, self.diagnosis, self.diagnosis_date,
            self.symptoms, self.treatment, self.family_history
        ]:
            var.set("")
        self.age.set(0)
