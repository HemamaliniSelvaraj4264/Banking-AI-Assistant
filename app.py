import streamlit as st

from services.csv_reader import read_csv
from services.vector_store import create_vector_db
from services.analyzer import analyze_data,category_summary,get_insights
from services.chart import expense_chart
from services.chatbot import ask_ai

st.set_page_config(
    page_title="Banking AI Assistant",
    layout="wide"
)

st.title(" Banking AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

upload_file = st.file_uploader(
    "Upload Bank Statement",
    type="csv"
)

if upload_file:

    data = read_csv(upload_file)

    st.success("CSV Uploaded Successfully!")

    vectordb = create_vector_db(data)
   

    income, expense, savings = analyze_data(data)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Income",f"₹ {income:,}")

    col2.metric("Total Expense", f"₹ {expense:,}")

    col3.metric("Savings", f"₹ {savings:,}")

    st.subheader("Expense by Category")

    summary = category_summary(data)

    chart = expense_chart(summary)

    st.pyplot(chart)

    st.dataframe(summary,width="stretch")

    insight = get_insights(data)

    st.subheader(" Financial Insights")

    st.info(
        f"""
    Highest Expense : {insight['highest_expense']}

    Amount : ₹{insight['highest_amount']}

    Category : {insight['category']}
    """
    )

    st.subheader("Bank Transactions")

    st.dataframe(data,width= "stretch")

    st.divider()

    st.subheader(" Ask AI")

    question = st.text_input(
        "Ask about your bank statement"
    )

    if question:

        with st.spinner("Thinking..."):

            answer = ask_ai(question, data)

            st.session_state.messages.append(
        {"question": question, "answer": answer}
    )

    for chat in st.session_state.messages:

        st.markdown(f" You:{chat['question']}")
        st.markdown(f" AI: {chat['answer']}")
        st.divider()

    st.subheader("Search Transaction")

    search = st.text_input("Search Description")

    if search:

        result = data[
            data["Description"].str.contains(
                search,
                case=False
            )
        ]

        st.dataframe(result, use_container_width=True)
        # st.write(answer)