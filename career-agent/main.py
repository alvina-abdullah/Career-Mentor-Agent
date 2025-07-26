import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from agents.run import RunConfig
from roadmap_tool import get_career_roadmap

# 🌍 Load your Gemini API key
load_dotenv()
external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# ⚙️ Define Gemini Model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# 🔧 Configuration
config = RunConfig(
    model=model,
    tracing_disabled=True
)

# 🎯 Agent 1: Career Mentor
Career_agent = Agent(
    name="🧠 Career Mentor Agent",
    instructions="You ask the user about their interests and suggest a suitable career field based on that. Provide a brief explanation for your suggestion."
)

# 🛠️ Agent 2: Skill Roadmap
skill_agent = Agent(
    name="📚 Skill Suggestion Agent",
    instructions="You use the get_career_roadmap tool to share the required skills for the given field. Format the skills as a numbered list for clarity.",
    model=model,
    tools=[get_career_roadmap]
)

# 💼 Agent 3: Job Suggestion
job_agent = Agent(
    name="💼 Job Search Agent",
    instructions="You suggest real-world job roles based on the chosen career field. Include a short description for each job role and format them as a bulleted list.",
    model=model,
)

# ▶️ Main Function
def main():
    print("\n🎓 Welcome to the Career Mentor Agent!\n")
    print("🚀 Let's explore your future together...\n")

    interest = input("💬 What is your field of interest? (e.g., Data Science, AI, Web Dev): ")

    print("\n🔍 Finding the best career path for you...")
    result1 = Runner.run_sync(Career_agent, interest, run_config=config)
    field = result1.final_output.strip()
    print(f"\n🌟 Suggested Career Field: **{field}**")

    print("\n📘 Generating your skill roadmap...")
    result2 = Runner.run_sync(skill_agent, field, run_config=config)
    print(f"\n🛠️ Required Skills:\n{result2.final_output}")

    print("\n🔎 Finding suitable job roles...")
    result3 = Runner.run_sync(job_agent, field, run_config=config)
    print(f"\n💼 Job Opportunities:\n{result3.final_output}")

    print("\n✅ All done! Best of luck for your career ahead! 🌈✨")

# 🚀 Run the Agent System
if __name__ == "__main__":
    main()
