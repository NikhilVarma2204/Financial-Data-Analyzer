import os
import json
import csv
from crewai import Crew, Agent, Task
from crewai_tools import FileReadTool
from dotenv import load_dotenv
import os
load_dotenv()

class FinancialDataAnalyzer:
    def __init__(self, file_path, company_name, time_span):
        self.file_path = file_path
        self.company_name = company_name
        self.time_span = time_span

        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
        os.environ["OPENAI_API_BASE"] = "https://api.openai.com/v1"
        os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"

        self.output_format = """
                1st month: a
                2nd month: b
                3rd month: c
                4th month: d
                5th month: e
                """

        self.file_tool = FileReadTool(self.file_path)
        self.reader_agent = self.create_reader_agent()
        self.reader_task = self.create_reader_task()

    def create_reader_agent(self):
        return Agent(
            role="Financial Data Analyst",
            goal=f"Analyze financial data for {self.company_name}, identify trends, and provide insights.",
            backstory="You are an experienced financial analyst with expertise in interpreting financial data.",
            tools=[self.file_tool],
            verbose=True,
            allow_delegation=False,
        )

    def create_reader_task(self):
        return Task(
            description=f"Read the extracted financial data and analyze trends for {self.company_name}.",
            agent=self.reader_agent,
            expected_output=f"Predict the price of {self.company_name} for the next {self.time_span} Months in gaps of 1 month. Keep the answer concise and give answer in {self.output_format} format depending on the monts requested by user. Don't give any explanation. Do not use any dates in your answer.",  
        )

    def analyze_data(self):
        crew = Crew(
            agents=[self.reader_agent],
            tasks=[self.reader_task],
            input={'csv_path': self.file_path},
            verbose=True
        )

        result = crew.kickoff()

        task_output = self.reader_task.output
        print(f"Task Description: {task_output.description}")
        print(f"Task Summary: {task_output.summary}")
        print(f"Raw Output: {task_output.raw}")
        if task_output.json_dict:
            print(f"JSON Output: {json.dumps(task_output.json_dict, indent=2)}")
        if task_output.pydantic:
            print(f"Pydantic Output: {task_output.pydantic}")
        return task_output


