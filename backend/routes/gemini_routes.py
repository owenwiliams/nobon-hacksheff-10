from fastapi import APIRouter, Depends, HTTPException
from typing import List
import asyncio
from gemini import (
    summarize_journal_to_title,
    suggest_possible_quest_milestones,
    athena_chatbot,
    motivational_quote)
from schema.gemini_schema import ChatRequest

router = APIRouter(prefix="/ai", tags=["ai"])

@router.post("/generate_title", response_model=str)
async def summarize_journal_entry(journal_body: ChatRequest):
    title = summarize_journal_to_title(journal_body.prompt)
    return title


@router.post("/suggest_quests", response_model=List)
async def suggest_quest(journey_title: ChatRequest):
    prompts = [
        f"suggest the FIRST brief quest milestone for this journey: {journey_title.prompt}.",
        f"suggest a MIDDLE stage quest milestone for this journey: {journey_title.prompt}.", 
        f"suggest a FINAL achievement quest milestone for this journey: {journey_title.prompt}."
    ]
    
    # concurrent api calls for speed
    tasks = [asyncio.to_thread(suggest_possible_quest_milestones, prompt) for prompt in prompts]
    results = await asyncio.gather(*tasks)
    return results

@router.post("/athena_chat", response_model=str)
async def athena_chat(request: ChatRequest): 
    response = athena_chatbot(request.prompt)
    return response

@router.get("/motivational_quote", response_model=str)
async def get_motivational_quote():
    quote = motivational_quote()
    return quote

