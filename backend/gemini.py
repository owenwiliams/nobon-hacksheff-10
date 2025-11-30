# 
#   has useful functions for interacting with the ai model.
#  
# summarize a journal into a title
# give prompts to write a journal entry
# suggest a group of milestones for a quest based on title & description <- JSON
# suggest quest description based on title 
# chatbot by athena
# motivational quotes

import os 
from google import genai
from google.genai import types
from typing import List
from dotenv import load_dotenv

# load the api key from .env - private file to be shared
load_dotenv()  
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# the client gets the API key from GEMINI_API_KEY environment variable
client = genai.Client()

# ==============================================================================
# PROMPT GENERATION FUNCTIONS
# ==============================================================================

# passes a journal body to gemini, returns a summarised title based on the body
def summarize_journal_to_title(journal_body: str) -> str:
    instruction = "Summarize the following journal entry into a title which represents the activities of the day, no more than 1 line, including punctuation."
    prompt = f"Journal body{journal_body}"
    return ask_gemini(instruction, prompt)

# based on the journey's title and description, suggest a few possible quests
def suggest_possible_quest_milestones(journey_title: str) -> List:
    instruction = "Based on the following task title and description, suggest 1 possible sub-task to help the user complete this task. Return the sub-task as a string, do not include any other text or formatting. This should be a single sentance, up to 30 words."
    prompt = f"Journey Title: {journey_title}"
    return ask_gemini(instruction, prompt)

# talk to athena
def athena_chatbot(prompt: str) -> str:
    instruction = "You are Athena, the Greek God of wisdom. Your purpose is to provide helpful advice and tips to users to help them on their journey to self-improvement. You speak in a encouraging manner, but not dense and difficult to understand, and stay relevent to the prompt from the user. You should be kind and also encouraging but only when needed. You should avoid being verbose, and do not use complex formatting such as lists or bullet points. Your responses should be also meaningful and relevant, and giving only a few references to ancient greek mythology when appropriate. Your response length should mirror the complexity of the question asked by the user, and advice should feel genuine."
    return ask_athena(instruction, prompt)

# motivational quotes from athena
def motivational_quote() -> str:
    instruction = "You are Athena, the God of Wisdom. You will provide a single brief motivational quote to help the user stay motivated. These quotes should be relevant to self-improvement and personal growth. Each quote should be no more than 1 sentance long."
    prompt = "Provide motivational advice to help the user stay on track with their self-improvement journey."
    return ask_athena(instruction, prompt)

# ==============================================================================
# AI AGENT INTERACTION
# ==============================================================================

# passes a prompt to gemini, returns the response
# this is a generic function that can be used for various purposes
def ask_gemini(instruction: str, prompt: str) -> str:
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=instruction),
    contents=prompt
    )
    return response.text

# passes a prompt to gemini, returns the response
# this is used specifically for the Athena chatbot, and will provide responses as Athena
def ask_athena(instruction: str, prompt: str) -> str:
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction= instruction),
    contents=prompt
    )
    return response.text

# ==============================================================================
# TEST FUNCTIONS
# ==============================================================================

# print(athena_chatbot("How can I stay motivated on my journey to self-improvement? I have no motivation to go to the gym and am struggling to eat healthy."))