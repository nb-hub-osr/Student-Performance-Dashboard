import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression


# =========================================================
# LOAD DATA
# =========================================================

data = pd.read_csv("students.csv")

# Calculate average marks
data["Average"] = data[["Python", "ML", "OS"]].mean(axis=1)


# =========================================================
# MACHINE LEARNING MODEL
# =========================================================

X = data[["Study_Hours", "Attendance"]]
y = data["Average"]

model = LinearRegression()
model.fit(X, y)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🎓 Student Dashboard")

st.sidebar.write(
    "Analyze student performance and predict average marks."
)

page = st.sidebar.radio(
    "Go to",
    ["Overview", "Student", "Analysis", "Prediction"]
)

st.sidebar.divider()


# Attendance filter
attendance_filter = st.sidebar.slider(
    "Minimum Attendance",
    min_value=0,
    max_value=100,
    value=0
)


# Subject filter
subject = st.sidebar.selectbox(
    "Choose Subject",
    ["All", "Python", "ML", "OS"]
)


# =========================================================
# APPLY ATTENDANCE FILTER
# =========================================================

filtered_data = data[
    data["Attendance"] >= attendance_filter
]


# =========================================================
# OVERVIEW PAGE
# =========================================================

if page == "Overview":

    st.title("🎓 Student Performance Dashboard")

    st.header("📊 Overview")

    # -----------------------------------------------------
    # Check whether students are available
    # -----------------------------------------------------

    if len(filtered_data) == 0:

        st.warning(
            "No students match the selected attendance filter."
        )

    else:

        # -------------------------------------------------
        # Metric cards
        # -------------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Students",
            len(filtered_data)
        )

        col2.metric(
            "Avg Python",
            round(filtered_data["Python"].mean(), 2)
        )

        col3.metric(
            "Avg ML",
            round(filtered_data["ML"].mean(), 2)
        )

        col4.metric(
            "Avg OS",
            round(filtered_data["OS"].mean(), 2)
        )

        st.divider()

        # -------------------------------------------------
        # Student data
        # -------------------------------------------------

        st.subheader("📋 Student Data")

        st.dataframe(
            filtered_data,
            use_container_width=True
        )

        st.divider()

        # -------------------------------------------------
        # Subject chart
        # -------------------------------------------------

        st.subheader("📈 Subject Performance")

        if subject == "All":

            subject_average = filtered_data[
                ["Python", "ML", "OS"]
            ].mean()

            st.bar_chart(subject_average)

        else:

            subject_average = filtered_data[subject].mean()

            st.metric(
                f"Average {subject} Marks",
                round(subject_average, 2)
            )

            st.bar_chart(
                filtered_data.set_index("Name")[subject]
            )


# =========================================================
# STUDENT PAGE
# =========================================================

elif page == "Student":

    st.title("👤 Student Performance")

    # Students matching attendance filter
    student_names = filtered_data["Name"].tolist()

    if len(student_names) == 0:

        st.warning(
            "No students match the selected attendance filter."
        )

    else:

        # -------------------------------------------------
        # Student selector
        # -------------------------------------------------

        student_name = st.selectbox(
            "Choose a student:",
            student_names
        )

        student = data[
            data["Name"] == student_name
        ].iloc[0]

        st.divider()

        st.subheader(
            f"📚 {student_name}"
        )

        # -------------------------------------------------
        # Student marks
        # -------------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Python",
            student["Python"]
        )

        col2.metric(
            "ML",
            student["ML"]
        )

        col3.metric(
            "OS",
            student["OS"]
        )

        col4.metric(
            "Average",
            round(student["Average"], 2)
        )

        st.divider()

        # -------------------------------------------------
        # Attendance and study hours
        # -------------------------------------------------

        col1, col2 = st.columns(2)

        col1.metric(
            "Attendance",
            f"{student['Attendance']}%"
        )

        col2.metric(
            "Study Hours",
            student["Study_Hours"]
        )

        # -------------------------------------------------
        # Attendance status
        # -------------------------------------------------

        if student["Attendance"] < 75:

            st.warning(
                "⚠️ Attendance is below 75%!"
            )

        else:

            st.success(
                "✅ Attendance is satisfactory."
            )

        st.divider()

        # -------------------------------------------------
        # Student performance chart
        # -------------------------------------------------

        st.subheader("📈 Subject Performance")

        marks = {
            "Python": student["Python"],
            "ML": student["ML"],
            "OS": student["OS"]
        }

        st.bar_chart(marks)


# =========================================================
# ANALYSIS PAGE
# =========================================================

elif page == "Analysis":

    st.title("🔎 Student Analysis")

    if len(filtered_data) == 0:

        st.warning(
            "No students match the selected attendance filter."
        )

    else:

        # -------------------------------------------------
        # Student ranking
        # -------------------------------------------------

        st.subheader("🏆 Student Ranking")

        ranked_students = filtered_data.sort_values(
            by="Average",
            ascending=False
        )

        st.dataframe(
            ranked_students[
                ["Name", "Python", "ML", "OS", "Average"]
            ],
            use_container_width=True
        )

        st.divider()

        # -------------------------------------------------
        # Students needing attention
        # -------------------------------------------------

        st.subheader("⚠️ Students Needing Attention")

        at_risk = filtered_data[
            (filtered_data["Attendance"] < 75) |
            (filtered_data["Average"] < 60)
        ]

        if len(at_risk) > 0:

            st.dataframe(
                at_risk[
                    ["Name", "Attendance", "Average"]
                ],
                use_container_width=True
            )

        else:

            st.success(
                "✅ No students currently match the criteria."
            )

        st.divider()

        # -------------------------------------------------
        # Attendance analysis
        # -------------------------------------------------

        st.subheader("📊 Attendance Analysis")

        attendance_average = (
            filtered_data["Attendance"].mean()
        )

        st.metric(
            "Average Attendance",
            f"{attendance_average:.2f}%"
        )

        st.bar_chart(
            filtered_data.set_index("Name")[
                "Attendance"
            ]
        )


# =========================================================
# PREDICTION PAGE
# =========================================================

elif page == "Prediction":

    st.title("🤖 Average Marks Prediction")

    st.write(
        "Enter Study Hours and Attendance "
        "to predict Average Marks."
    )

    st.divider()

    # -----------------------------------------------------
    # User inputs
    # -----------------------------------------------------

    study_hours = st.number_input(
        "📚 Study Hours",
        min_value=0.0,
        max_value=24.0,
        value=5.0
    )

    attendance = st.number_input(
        "📅 Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=90.0
    )

    # -----------------------------------------------------
    # Prediction
    # -----------------------------------------------------

    if st.button("🔮 Predict Average"):

        new_student = [[
            study_hours,
            attendance
        ]]

        prediction = model.predict(
            new_student
        )

        st.success(
            f"Predicted Average: {prediction[0]:.2f}"
        )

        st.info(
            f"Based on {study_hours} study hours "
            f"and {attendance}% attendance."
        )

        st.divider()

        st.subheader("📈 Study Hours vs Average Marks")

        st.scatter_chart(
            data,
            x="Study_Hours",
            y="Average"
)