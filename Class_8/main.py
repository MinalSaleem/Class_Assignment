import streamlit as st

class Job:
    def __init__(self, title, company, job_type, location):
        self.title = title
        self.company = company
        self.job_type = job_type
        self.location = location

    def __str__(self):
        return f"{self.title} at {self.company} ({self.job_type}) - {self.location}"

class FullTimeJob(Job):
    def __init__(self, title, company, location):
        super().__init__(title, company, "Full-Time", location)

class PartTimeJob(Job):
    def __init__(self, title, company, location):
        super().__init__(title, company, "Part-Time", location)

class FreelanceJob(Job):
    def __init__(self, title, company, location):
        super().__init__(title, company, "Freelance", location)

class InternshipJob(Job):
    def __init__(self, title, company, location):
        super().__init__(title, company, "Internship", location)


jobs = [
    FullTimeJob("Software Developer", "TechCorp", "New York"),
    PartTimeJob("Data Analyst", "DataWorld", "Remote"),
    FreelanceJob("Graphic Designer", "DesignCo", "San Francisco"),
    FullTimeJob("Web Developer", "WebWorld", "Los Angeles"),
    InternshipJob("Frontend Developer", "StartUp Inc.", "Remote"),
]


if 'user_applied_jobs' not in st.session_state:
    st.session_state.user_applied_jobs = []


st.title("Job Search System")

with st.sidebar:
    st.header("🔍 User Profile")
    name = st.text_input("Enter your name :")
    email = st.text_input("Enter your email :")
    skills = st.multiselect(
        "Select your skills :",
        options=["developer", "data", "design", "frontend", "analysis"],
        default=["developer"]
    )


st.subheader(f"🔎 Recommended Jobs for {name} :")

recommended = [job for job in jobs if any(skill in job.title.lower() for skill in skills)]

if recommended:
    for i, job in enumerate(recommended):
        with st.expander(f"{job.title} at {job.company}"):
            st.write(f"📍 Location: {job.location}")
            st.write(f"🕒 Type: {job.job_type}")
            if st.button(f"Apply for {job.title}", key=f"apply_{i}"):
                if job not in st.session_state.user_applied_jobs:
                    st.session_state.user_applied_jobs.append(job)
                    st.success(f"You applied for {job.title} at {job.company}")
                else:
                    st.warning("You have already applied for this job.")
else:
    st.write("No jobs match your skills.")

st.subheader("📄 Jobs You've Applied For : ")

if st.session_state.user_applied_jobs:
    for job in st.session_state.user_applied_jobs:
        st.write(f"✅ {job}")
else:
    st.info("You haven't applied for any jobs yet.")