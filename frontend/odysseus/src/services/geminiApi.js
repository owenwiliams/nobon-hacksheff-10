import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const generateTitle = async (journalBody) => {
  const response = await axios.post(`${BASE_URL}/ai/generate_title`, {
    prompt: journalBody,
  });
  return response.data;
};

export const suggestQuests = async (journeyTitle) => {
  const response = await axios.post(`${BASE_URL}/ai/suggest_quests`, {
    prompt: journeyTitle,
  });
  return response.data;
};

export const athenaChat = async (prompt) => {
  const response = await axios.post(`${BASE_URL}/ai/athena_chat`, 
    prompt
  );
  return response.data;
};

export const getMotivationalQuote = async () => {
  const response = await axios.get(`${BASE_URL}/ai/motivational_quote`);
  return response.data;
};